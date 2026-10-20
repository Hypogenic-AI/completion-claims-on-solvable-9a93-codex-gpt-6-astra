"""Final resource audit. Does not claim model evaluation or write completion marker."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
assert Path.cwd()==ROOT and (ROOT/'.git').exists()
assert Path(sys.prefix).resolve()==(ROOT/'.venv').resolve()
required=['papers/README.md','datasets/README.md','datasets/.gitignore','code/README.md','literature_review.md','resources.md','planning.md','STATE.md','pyproject.toml','uv.lock','evidence/reading_log.md','evidence/dataset_validation.json','evidence/development_validation.json']
for f in required:assert Path(f).is_file() and Path(f).stat().st_size>0,f
papers=json.loads(Path('evidence/papers_manifest.json').read_text())
assert len(papers)==len(list(Path('papers').glob('*.pdf')))==27
assert len({p['arxiv_id'].split('v')[0] for p in papers})==27
for p in papers:
 f=Path(p['file']);assert hashlib.sha256(f.read_bytes()).hexdigest()==p['sha256'],str(f)
 assert len(PdfReader(f).pages)==p['pages']>0
 assert f.name in Path('papers/README.md').read_text()
chunks=list(Path('papers/pages').glob('*.pdf'))
for f in chunks:assert len(PdfReader(f).pages)>0
raw=json.loads(Path('evidence/dataset_download_manifest.json').read_text())
for r in raw:
 f=Path(r['path']);assert len(f.read_bytes())==r['bytes']
 assert hashlib.sha256(f.read_bytes()).hexdigest()==r['sha256']
 assert subprocess.run(['git','check-ignore','-q',str(f)]).returncode==0,str(f)
for f in Path('datasets/samples').glob('*'):
 assert f.stat().st_size<100_000
 assert subprocess.run(['git','check-ignore','-q',str(f)]).returncode==1,str(f)
 json.loads(f.read_text())
assert subprocess.run(['git','check-ignore','-q','datasets/development_twins/pairs.jsonl']).returncode==0
repos=json.loads(Path('evidence/repositories.json').read_text())
for r in repos:
 assert subprocess.check_output(['git','-C',r['path'],'rev-parse','HEAD'],text=True).strip()==r['sha']
 assert not subprocess.check_output(['git','-C',r['path'],'status','--porcelain'],text=True).strip()
validation=json.loads(Path('evidence/dataset_validation.json').read_text())
assert validation['lcb']['paired_base_ids']==103
assert not validation['lcb']['pairing_issues']
assert validation['upward']['total']==200
assert sum(validation['upward'][f'task_{i}.json']['instruction_task_index_artifacts'] for i in range(1,6))==48
dev=json.loads(Path('evidence/development_validation.json').read_text());assert dev['pairs']==30 and dev['episodes']==60
assert hashlib.sha256(Path('datasets/development_twins/pairs.jsonl').read_bytes()).hexdigest()==dev['sha256']
assert all(a['goal_reachable']==(a['condition']=='solvable') for a in dev['audit'])
code=json.loads(Path('evidence/code_validation.json').read_text());assert all(not r['syntax_errors'] for r in code)
state=Path('STATE.md').read_text()
for marker in ['<!-- NEURICO_AGENT_NOTES_START:resource_finder -->','<!-- NEURICO_AGENT_NOTES_END:resource_finder -->']:assert state.count(marker)==1
# Check relative file links from core documents. External URLs deliberately not re-downloaded.
import re
links=[]
for doc in ['papers/README.md','literature_review.md','resources.md']:
 for target in re.findall(r'\]\(([^)]+)\)',Path(doc).read_text()):
  if '://' in target or target.startswith('#'):continue
  path=Path(doc).parent/target.split('#')[0];assert path.exists(),(doc,target);links.append(str(path))
report={'status':'passed','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'papers_unique':27,'paper_chunks_validated':len(chunks),'downloaded_datasets':2,'raw_dataset_files':len(raw),'lcb_base_tasks':103,'lcb_syntax_clean_pairs':102,'upward_tasks':200,'synthetic_development_pairs':30,'synthetic_development_templates':3,'repositories':3,'python_source_files_syntax_checked':sum(r['python_files'] for r in code),'full_reading_pages':100,'required_files':required,'relative_file_links_checked':len(links),'data_hashes_match':True,'paper_hashes_match':True,'raw_data_git_ignored':True,'samples_git_visible_under_100kb':True,'repo_commits_match_and_trees_clean':True,'isolated_venv':str(Path(sys.prefix)),'model_inference_performed':False,'hypothesis_tested':False,'limitations':['lcbhard_77 malformed impossible tests; independent semantic QC still required','48 Upward Deception instruction text artifacts; no solvable twins','Development set has only three templates; cannot support confirmatory claims','Official evaluation runtimes not installed/executed','HCRC withdrawn; coding DriftBench PDF unresolved','FeasiGen generated data and FTA artifact download unavailable']}
Path('evidence/final_validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
