from pathlib import Path
import ast,collections,hashlib,json
import pyarrow.parquet as pq
ROOT=Path(__file__).resolve().parents[1];assert Path.cwd()==ROOT
splits={s:pq.read_table(f'datasets/impossible_livecodebench/{s}.parquet').to_pylist() for s in ['original','oneoff','conflicting']}
report={'lcb':{},'upward':{}};maps={}
for s,rows in splits.items():
 ids=[r['task_id'] for r in rows];assert len(ids)==len(set(ids))
 maps[s]={r['task_id']:r for r in rows}
 syntax=[]
 for r in rows:
  for field in ['prompt','test','original_test']:
   try:ast.parse(r[field])
   except SyntaxError as e:syntax.append({'id':r['task_id'],'field':field,'error':str(e)})
 report['lcb'][s]={'rows':len(rows),'columns':list(rows[0]),'nulls':{k:sum(r.get(k) is None for r in rows) for k in rows[0]},'empty_strings':{k:sum(r.get(k)=='' for r in rows) for k in rows[0]},'unique_ids':len(set(ids)),'syntax_errors':syntax}
assert set(maps['original'])==set(maps['oneoff'])==set(maps['conflicting'])
issues=[]
for tid,o in maps['original'].items():
 for s in ['oneoff','conflicting']:
  r=maps[s][tid]
  for field in ['prompt','entry_point','original_test']:
   if o[field]!=r[field]:issues.append({'id':tid,'split':s,'mismatch':field})
  if r['test']==o['test']:issues.append({'id':tid,'split':s,'mismatch':'unchanged_test'})
report['lcb']['pairing_issues']=issues
report['lcb']['paired_base_ids']=len(maps['original'])
report['lcb']['reference_solutions_present']=False
report['lcb']['warning']='Parsing and ID checks do not prove solvability, specification consistency or impossibility; independent gold solutions/invariants needed before confirmatory use.'
(Path('datasets/samples/impossible_livecodebench.json')).write_text(json.dumps({s:rows[:1] for s,rows in splits.items()},indent=2))
all_rows=[]
for p in sorted(Path('datasets/upward_deception').glob('*.json')):
 rows=json.loads(p.read_text());all_rows+=rows
 ids=[r['task_index'] for r in rows]
 report['upward'][p.name]={'rows':len(rows),'unique_ids':len(set(ids)),'columns':sorted(set().union(*(r.keys() for r in rows))),'empty_instruction':sum(not r.get('instruction') for r in rows),'missing_or_empty_file_content':sum(not r.get('file_content') for r in rows),'instruction_task_index_artifacts':sum('task_index' in r['instruction'] for r in rows),'topics':dict(collections.Counter(r.get('topic') for r in rows))}
(Path('datasets/samples/upward_deception.json')).write_text(json.dumps([json.loads(p.read_text())[0] for p in sorted(Path('datasets/upward_deception').glob('*.json'))],indent=2))
report['upward']['total']=len(all_rows)
report['upward']['global_duplicate_task_indices']=len(all_rows)-len(set(r['task_index'] for r in all_rows))
report['upward']['warning']='Raw author data preserved. Some instructions contain accidental task_index substitutions inside words; clean only in a separately versioned derivative. No solvable twins. Missing file_content is intentional in broken-reader/download tasks.'
Path('evidence/dataset_validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
