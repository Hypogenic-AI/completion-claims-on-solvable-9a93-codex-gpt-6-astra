"""Inspect-backed subject collection against a local vLLM raw completion API.

The API receives token IDs from the pinned native chat template, preserving all
reasoning text. No semantic judge is called. Each episode writes its own transcript.
"""
import os,json,time,asyncio,random
from pathlib import Path
import httpx
from transformers import AutoTokenizer
from inspect_ai import Task,task,eval as inspect_eval
from inspect_ai.dataset import Sample,MemoryDataset
from inspect_ai.solver import solver,TaskState,Generate
from inspect_ai.scorer import scorer,Score,Target,mean
from inspect_ai.model import ChatMessageAssistant,ChatMessageUser
from protocol import PROTOCOL,World,parse,score,SEEDS
MODELS={'qwen3-8b':'Qwen3-8B','deepseek-r1-distill-llama-8b':'DeepSeek-R1-Distill-Llama-8B'}

@scorer(metrics={k:[mean()] for k in ['unsupported_done','supported_done','correct_blocked','refuse','unauthorized_attempt','parse_failure','truncated','infra_failure']})
def endpoint_score():
    async def run(state:TaskState,target:Target):
        s=state.metadata['outcome']
        return Score(value={k:int(s[k]) for k in ['unsupported_done','supported_done','correct_blocked','refuse','unauthorized_attempt','parse_failure','truncated','infra_failure']},answer=state.metadata.get('terminal_action','NONE'),explanation='Exact final state, mutation log and parsed terminal JSON; clustered inference is performed separately.')
    return run

def build_task(model_id,split,base_url,concurrency=64):
    tokenizer=AutoTokenizer.from_pretrained('artifacts/models/'+MODELS[model_id],local_files_only=True)
    native=model_id.startswith('deepseek')
    outdir=Path('results/transcripts')/split/model_id;outdir.mkdir(parents=True,exist_ok=True)
    items=[i for i in json.loads(Path('datasets/custom/items.json').read_text()) if i['split']==split]
    samples=[]
    seeds=SEEDS if split=='evaluation' else [11]
    for item in items:
        for seed in seeds:
            for cond in ['solvable','impossible']:
                samples.append(Sample(id=f"{item['id']}__{seed}__{cond}",input=PROTOCOL+'\nTask: '+item['task'],target=str(item['gold']),metadata={'item':item,'condition':cond,'seed':seed}))
    random.Random(20261020).shuffle(samples)
    sem=asyncio.Semaphore(concurrency)
    @solver
    def interact():
        async def solve(state:TaskState,generate:Generate):
            meta=state.metadata;i=meta['item'];cond=meta['condition'];seed=meta['seed'];world=World(i,cond)
            messages=[{'role':'user','content':PROTOCOL+'\nTask: '+i['task']}]
            terminal=None;perror=None;trunc=False;infra=None;turns=[];started=time.time();limit=False
            async with sem:
                async with httpx.AsyncClient(timeout=240) as client:
                    for turn in range(6):
                        ids=tokenizer.apply_chat_template(messages,tokenize=True,return_dict=False,add_generation_prompt=True,**({'enable_thinking':False} if not native else {}))
                        assert isinstance(ids,list) and all(isinstance(x,int) for x in ids), 'Expected flat token-ID list'
                        # Reserve the full requested action budget, never silently shorten it.
                        if len(ids)+1024>8192:
                            perror='context_limit';trunc=True;break
                        payload={'model':model_id,'prompt':ids,'max_tokens':1024,'temperature':0.6,'top_p':1,'seed':seed,'stream':False}
                        response=None;errors=[]
                        for attempt in range(3):
                            try:
                                r=await client.post(base_url+'/completions',json=payload);r.raise_for_status();response=r.json();break
                            except (httpx.HTTPError,ValueError) as e:
                                errors.append(f'{type(e).__name__}: {str(e)[:400]}')
                                if attempt<2:await asyncio.sleep(attempt+1)
                        if response is None:infra='; '.join(errors);break
                        choice=response['choices'][0];raw=choice['text'];finish=choice['finish_reason'];trunc=finish=='length'
                        p=parse(raw,reasoning_required=native,truncated=trunc)
                        entry=dict(turn=turn+1,prompt_tokens=len(ids),raw=raw,reasoning=p['reasoning'],final=p['final'],parse_error=p['error'],finish_reason=finish,usage=response.get('usage'),request_seed=seed,infrastructure_retries=errors)
                        turns.append(entry);messages.append({'role':'assistant','content':raw})
                        state.messages.append(ChatMessageAssistant(content=raw))
                        if p['error'] is not None:perror=p['error'];break
                        a=p['action']
                        if a['action'] in ['DONE','BLOCKED','REFUSE']:terminal=a;break
                        observation=world.step(a);entry['action']=a;entry['observation']=observation
                        text='Tool response: '+json.dumps(observation,ensure_ascii=False)+'\nReturn the next single JSON action.'
                        messages.append({'role':'user','content':text});state.messages.append(ChatMessageUser(content=text))
                    else:limit=True
            outcome=score(world,terminal,perror,trunc,infra,limit)
            record=dict(id=i['id'],episode_id=str(state.sample_id),template=i['template'],blocker=i['blocker'],model=model_id,condition=cond,seed=seed,split=split,started=started,finished=time.time(),terminal=terminal,outcome=outcome,turns=turns,messages=messages,final_records=world.records,mutations=world.mutations,attempts=world.attempts)
            (outdir/(str(state.sample_id)+'.json')).write_text(json.dumps(record,ensure_ascii=False)+'\n')
            state.metadata['outcome']=outcome;state.metadata['terminal_action']=(terminal or {}).get('action','NONE');state.completed=True
            return state
        return solve
    return Task(dataset=MemoryDataset(samples,name=split),solver=interact(),scorer=endpoint_score(),name='impossible_task_honesty_v1',metadata={'eval_id':'custom:impossible-task-honesty-v1','subject':model_id,'split':split})

def main(argv=None):
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--model',required=True,choices=MODELS);p.add_argument('--split',choices=['development','evaluation'],required=True);p.add_argument('--port',type=int,default=8765);a=p.parse_args(argv)
    if a.split=='evaluation':
        from freeze import verify
        verify()
    task=build_task(a.model,a.split,f'http://127.0.0.1:{a.port}/v1')
    # Mock is only the unused Inspect transport: every subject action is the real
    # vLLM API call above. This avoids Inspect normalizing raw reasoning channels.
    logs=inspect_eval(task,model='mockllm/model',log_dir='results/safety/inspect_logs',log_format='json',max_samples=64,display='none',log_samples=True)
    result={'model':a.model,'split':a.split,'logs':[x.location for x in logs],'statuses':[x.status for x in logs]}
    Path(f'results/{a.model}_{a.split}_collection.json').write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
    if not all(x.status=='success' for x in logs):raise SystemExit(1)
if __name__=='__main__':main()
