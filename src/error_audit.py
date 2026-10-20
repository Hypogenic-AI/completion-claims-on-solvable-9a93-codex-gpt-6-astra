"""Post-hoc descriptive audit of protocol exposure; not a hypothesis-selection step."""
import json
from pathlib import Path
from analyze import MODELS,estimate

def main():
    result={'posthoc':True,'purpose':'Distinguish failing to act in the scaffold from reacting to an observed environment barrier.','models':{}}
    for model in MODELS:
        rows=[json.loads(p.read_text()) for p in (Path('results/transcripts/evaluation')/model).glob('*.json')]
        summary={}
        for cond in ['solvable','impossible']:
            r=[x for x in rows if x['condition']==cond]
            for name,predicate in [('executed_any_tool',lambda x:any('observation' in t for t in x['turns'])),('saw_blocker_error',lambda x:any(t.get('observation',{}).get('error') in ['RECORD_NOT_FOUND','PERMISSION_DENIED'] for t in x['turns']))]:
                by={}
                for x in r:by.setdefault(x['id'],[]).append(int(predicate(x)))
                value=estimate([sum(v)/len(v) for v in by.values() if len(v)==3]);value.update(events=sum(predicate(x) for x in r),observed_episodes=len(r));summary[cond+'/'+name]=value
        result['models'][model]=summary
    Path('results/error_audit.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
