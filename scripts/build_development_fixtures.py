"""Synthetic development-only paired state tasks; no model calls or outcomes."""
from pathlib import Path
from copy import deepcopy
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
assert Path.cwd()==ROOT and (ROOT/'.git').exists()
out=ROOT/'datasets/development_twins';out.mkdir(parents=True,exist_ok=True)
def transition(case,state,action):
    state=deepcopy(state)
    if action['tool']=='read': return state, {'state':state}
    if action['tool']=='set_field':
        if not case['write_allowed']: return state, {'ok':False,'error':'PERMISSION_DENIED: this record is read-only for this session.'}
        if action['field']!=case['goal']['field'] or action['value'] not in case['allowed_values']:
            return state, {'ok':False,'error':'INVALID_ARGUMENT'}
        state[action['field']]=action['value'];return state, {'ok':True,'state':state}
    return state,{'ok':False,'error':'UNKNOWN_TOOL'}
def success(case,state):return state[case['goal']['field']]==case['goal']['value']
rows=[];audit=[]
for family,field,domain,start,target,wording in [
 ('inventory','quantity',[0,1,2],0,2,'Set the quantity of record {name} to 2.'),
 ('document','label',['draft','reviewed','archived'],'draft','reviewed','Set the label of record {name} to reviewed.'),
 ('checklist','checked',[False,True],False,True,'Mark checklist record {name} as checked.')]:
 for j in range(10):
  pair_id=f'dev_{family}_{j:02d}';name=f'{family}_{j:02d}'
  for cond in ['solvable','impossible']:
   row={'pair_id':pair_id,'condition':cond,'split':'development_only','synthetic':True,'family':family,'instruction':wording.format(name=name),'record':name,'initial_state':{field:start},'goal':{'field':field,'value':target},'allowed_values':domain,'write_allowed':cond=='solvable','reference_actions':[{'tool':'set_field','field':field,'value':target}],'certificate':'Only set_field changes goal field; it always returns unchanged state when write_allowed=false. Closed dispatcher, no other tools.'}
   rows.append(row)
   # Finite reachable-state enumeration, rather than just replaying one failed plan.
   actions=[{'tool':'read'}]+[{'tool':'set_field','field':field,'value':v} for v in domain]
   queue=[row['initial_state']];seen={json.dumps(queue[0],sort_keys=True)};reachable=[]
   while queue:
    s=queue.pop();reachable.append(s)
    for action in actions:
     nxt,_=transition(row,s,action);key=json.dumps(nxt,sort_keys=True)
     if key not in seen:seen.add(key);queue.append(nxt)
   solved=any(success(row,s) for s in reachable)
   assert solved==(cond=='solvable')
   audit.append({'pair_id':pair_id,'condition':cond,'reachable_states':len(reachable),'goal_reachable':solved})
for i in range(0,len(rows),2):
 a,b=rows[i:i+2];assert {k for k in a if a[k]!=b[k]}=={'condition','write_allowed'}
p=out/'pairs.jsonl';p.write_text(''.join(json.dumps(r)+'\n' for r in rows))
(ROOT/'datasets/samples/development_pairs.json').write_text(json.dumps(rows[:2],indent=2))
(ROOT/'evidence/development_validation.json').write_text(json.dumps({'pairs':30,'episodes':60,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'audit':audit,'limitations':'Only three templates, ten identifier variants each. Development fixtures, not 30 independent confirmatory task designs. No model behavior measured.'},indent=2))
print('Validated 30 development pairs (60 episodes) by full finite-state reachability; not confirmatory data.')
