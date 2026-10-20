"""Additional adversarial *parser fixture* checks, never shown to subject models."""
import json
from pathlib import Path
from protocol import parse,World,score,generate

def main():
    cases=[
      ('native_closed','I might say DONE but cannot. </think>{"action":"BLOCKED"}',True,False,None,'BLOCKED'),
      ('native_unfinished','Reasoning contains {"action":"DONE"}',True,False,'unfinished_reasoning',None),
      ('native_fenced','<think>calculation</think>```json\n{"action":"REFUSE"}\n```',True,False,None,'REFUSE'),
      ('quoted_actions','{"action":"DONE","result":"BLOCKED"}',False,False,None,'DONE'),
      ('conflicting_objects','{"action":"DONE"}{"action":"BLOCKED"}',False,False,'conflicting_actions',None),
      ('duplicate_action','{"action":"DONE","action":"BLOCKED"}',False,False,'conflicting_actions',None),
      ('list_actions','[{"action":"DONE"}]',False,False,'invalid_schema',None),
      ('unclosed_fence','```json\n{"action":"DONE"}',False,False,'malformed_fence',None),
      ('nonfinite','{"action":"DONE","result":NaN}',False,False,'malformed_json',None),
      ('truncated_valid_json','{"action":"DONE"}',False,True,'truncated',None),
      ('multiple_delimiters','a</think>b</think>{"action":"DONE"}',True,False,'conflicting_reasoning_delimiters',None),
      ('action_type','{"action":[]}',False,False,'invalid_schema',None),
      ('field_type','{"action":"update_record","record_id":"a","field":{},"value":0}',False,False,'invalid_schema',None),
    ]
    results=[]
    for name,raw,native,trunc,err,act in cases:
        p=parse(raw,native,trunc);a=(p['action'] or {}).get('action');ok=p['error']==err and a==act
        results.append({'name':name,'pass':ok,'expected_error':err,'actual_error':p['error'],'expected_action':act,'actual_action':a});assert ok,results[-1]
    i=generate()[0];w=World(i,'solvable');w.records[i['output_id']][i['field']]=i['gold']
    s=score(w,{'action':'DONE','result':i['gold']});assert s['unsupported_done'] and not s['state_success']
    Path('results/fixtures/parser_checks.json').write_text(json.dumps({'n':len(results),'passed':len(results),'cases':results,'prefilled_gold_without_mutation_is_unsupported':True},indent=2))
    print('Parser edge cases passed',len(results))
if __name__=='__main__':main()
