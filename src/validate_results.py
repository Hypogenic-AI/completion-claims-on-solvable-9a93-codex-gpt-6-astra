"""Validate exact transcript replay, planned pairing, hashes and reported outcomes."""
import json,hashlib,subprocess,sys
from pathlib import Path
from protocol import World,parse,score
from freeze import verify
from analyze import MODELS,METRICS

def main():
    frozen=verify()
    from tokenizers import Tokenizer
    canonical=Tokenizer.from_file('artifacts/models/DeepSeek-R1-Distill-Llama-8B/tokenizer.json')
    for model in frozen['models'].values():
        for name,info in model['weights'].items():
            p=Path(model['local_path'])/name
            h=hashlib.sha256()
            with p.open('rb') as stream:
                while chunk:=stream.read(8*1024*1024):h.update(chunk)
            assert h.hexdigest()==info['sha256'],p
    items={i['id']:i for i in json.loads(Path('datasets/custom/items.json').read_text())};fail=[];counts={};max_context=0;max_turns=0;first=None;last=None
    for split in ['development','evaluation']:
        for model in MODELS:
            rows=[]
            for p in sorted((Path('results/transcripts')/split/model).glob('*.json')):
                r=json.loads(p.read_text());i=items[r['id']];w=World(i,r['condition']);rows.append(r)
                if first is None or r['started']<first:first=r['started']
                if last is None or r['finished']>last:last=r['finished']
                terminal=None;perror=None;trunc=False
                for t in r['turns']:
                    if model.startswith('deepseek'):
                        assert canonical.decode(t['generated_token_ids'],skip_special_tokens=True)==t['raw'],p
                        decoded_prompt=canonical.decode(t['prompt_token_ids'],skip_special_tokens=False)
                        assert r['messages'][0]['content'] in decoded_prompt,p
                        assert r['messages'][2*(t['turn']-1)]['content'] in decoded_prompt,p
                    max_context=max(max_context,t['prompt_tokens']+(t.get('usage') or {}).get('completion_tokens',0))
                    assert t['prompt_tokens']+1024<=8192
                    pp=parse(t['raw'],model.startswith('deepseek'),t['finish_reason']=='length')
                    assert pp['final']==t['final'] and pp['reasoning']==t['reasoning'] and pp['error']==t['parse_error'],p
                    if 'action' in t:
                        assert pp['action']==t['action'],p
                        obs=w.step(t['action']);assert obs==t['observation'],p
                    if pp['action'] is not None and pp['action']['action'] in ['DONE','BLOCKED','REFUSE']:terminal=pp['action']
                assert w.records==r['final_records'] and w.mutations==r['mutations'] and w.attempts==r['attempts'],p
                assert terminal==r['terminal'],p
                old=r['outcome'];new=score(w,terminal,old['parse_error'],old['truncated'],old['infra_error'],old['action_limit'])
                assert new==old,p
                if r['condition']=='impossible':assert not old['state_success'] and not old['supported_done'],p
                max_turns=max(max_turns,len(r['turns']));assert len(r['turns'])<=6,p
            keys={(r['id'],r['condition'],r['seed']) for r in rows};assert len(keys)==len(rows)
            counts[split+'/'+model]=len(rows)
    for model in MODELS:
        summary=json.loads(Path('results/analysis/'+model+'.json').read_text());record=json.loads(Path('results/safety/custom:impossible-task-honesty-v1__'+model+'.json').read_text())
        assert record['schema']=='neurico-safety-result/v1' and record['judge'] is None
        assert record['n']==counts['evaluation/'+model]==summary['observed_episodes']
        if record['status']=='success':assert record['n']==1200 and summary['collected_complete']
        for metric in METRICS:
            for cond in ['solvable','impossible']:
                v=summary['metrics'][metric][cond];assert v['planned_episodes']==600 and v['planned_n']==200
                assert record['metrics'][cond+'/'+metric]==v['mean']
    fixture=json.loads(Path('results/fixtures/checks.json').read_text());assert fixture['passed']==fixture['n']==80
    assert json.loads(Path('results/fixtures/parser_checks.json').read_text())['passed']==13
    assert Path('REPORT.md').exists() and Path('README.md').exists()
    # Repeat analysis on existing actual transcripts; do not rerun any subject.
    targets=list(Path('results/analysis').glob('*.json'))+[Path('results/item_level_paired.json')]
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in targets}
    subprocess.run([sys.executable,'src/analyze.py'],check=True,stdout=subprocess.PIPE)
    after={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in targets};assert before==after,'Analysis rerun changed outputs'
    subprocess.run([sys.executable,'src/render_figure.py'],check=True)
    result={'validation_pass':True,'collection_complete':all(counts['evaluation/'+m]==1200 for m in MODELS),'counts':counts,'all_transcripts_replayed':True,'max_rendered_context_tokens_including_generation':max_context,'max_actions':max_turns,'fixture_agreement':80,'parser_edge_cases':13,'analysis_repeat_identical':True,'frozen_hashes_verified':True,'weight_hashes_verified':True,'first_subject_timestamp':first,'last_subject_timestamp':last,'failures':fail}
    Path('results/final_validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
