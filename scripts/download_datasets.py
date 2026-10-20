"""Download pinned official resources without executing their code."""
from pathlib import Path
import concurrent.futures,hashlib,json,requests
ROOT=Path(__file__).resolve().parents[1]
assert Path.cwd()==ROOT and (ROOT/'.git').exists()
LCB_REV='98650ffc3f28a01b261669b6d19fcd7773823710'
UP_REV='b26151c7195111271feba64fb15db6227f25f51b'
JOBS=[(f'https://huggingface.co/datasets/fjzzq2002/impossible_livecodebench/resolve/{LCB_REV}/data/{s}-00000-of-00001.parquet',f'datasets/impossible_livecodebench/{s}.parquet') for s in ['original','oneoff','conflicting']]
JOBS += [(f'https://raw.githubusercontent.com/QingyuLiu/Agentic-Upward-Deception/{UP_REV}/dataset/task_{i}.json',f'datasets/upward_deception/task_{i}.json') for i in range(1,6)]
def fetch(job):
 url,dest=job;p=Path(dest);p.parent.mkdir(parents=True,exist_ok=True)
 r=requests.get(url,timeout=90);r.raise_for_status();p.write_bytes(r.content)
 return {'path':dest,'url':url,'bytes':len(r.content),'sha256':hashlib.sha256(r.content).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:rows=list(ex.map(fetch,JOBS))
Path('evidence/dataset_download_manifest.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
