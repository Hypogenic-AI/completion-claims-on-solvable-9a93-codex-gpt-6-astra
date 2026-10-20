"""Hash immutable design, exact model revisions and native template bytes."""
from pathlib import Path
import json,hashlib,datetime,importlib.metadata,subprocess,os
FILES=['src/protocol.py','src/prepare.py','src/collect.py','src/server.py','src/analyze.py','src/freeze.py','src/validate_protocol.py','src/evals/impossible_task_honesty.py','preregistration.md','datasets/custom/items.json','results/fixtures/labelled.json','pyproject.toml','uv.lock']

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def verify():
    frozen=json.loads(Path('results/manifests/frozen.json').read_text())
    bad=[p for p,h in frozen['sha256'].items() if digest(p)!=h]
    assert not bad,f'Frozen files changed: {bad}'
    return frozen

def main():
    if Path('results/manifests/frozen.json').exists():verify();print('Existing freeze verified');return
    models={};files=list(FILES)
    for name,repo in [('Qwen3-8B','Qwen/Qwen3-8B'),('DeepSeek-R1-Distill-Llama-8B','deepseek-ai/DeepSeek-R1-Distill-Llama-8B')]:
        meta=json.loads(Path('evidence/'+name+'_metadata.json').read_text());path=Path('artifacts/models')/name
        for p in path.iterdir():
            if p.suffix in ['.json','.jinja','.model']:files.append(str(p))
        models[repo]={'revision':meta['sha'],'local_path':str(path),'weights':{p.name:{'bytes':p.stat().st_size,'sha256':digest(p)} for p in path.glob('*.safetensors')}}
    versions={p:importlib.metadata.version(p) for p in ['vllm','torch','transformers','inspect-ai','inspect-evals','numpy','scipy','httpx']}
    frozen=dict(created=datetime.datetime.now(datetime.timezone.utc).isoformat(),eval_id='custom:impossible-task-honesty-v1',sha256={p:digest(p) for p in sorted(set(files))},models=models,versions=versions,cuda_visible_devices=os.environ.get('CUDA_VISIBLE_DEVICES'),hardware=subprocess.check_output(['nvidia-smi','--query-gpu=name,memory.total,memory.free','--format=csv'],text=True),generation={'temperature':.6,'top_p':1,'seeds':[11,22,33],'max_tokens':1024,'actions':6,'max_context':8192,'dtype':'bfloat16','tp':1,'batch_concurrency':64},planned_episodes=2400)
    Path('results/manifests/frozen.json').write_text(json.dumps(frozen,indent=2)+'\n');print('Frozen',frozen['created'])
if __name__=='__main__':main()
