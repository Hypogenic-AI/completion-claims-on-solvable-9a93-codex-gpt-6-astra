"""Resolve paper-finder's relevance>=2 results and download public PDFs."""
import requests,json,concurrent.futures,re,time
from pathlib import Path
from pypdf import PdfReader
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
assert Path.cwd()==root and (root/'.git').exists()
p=max(Path('paper_search_results').glob('*.jsonl'),key=lambda p:p.stat().st_size)
rows=[json.loads(l) for l in p.read_text().splitlines()]
rows=[dict(p,search_index=i) for i,p in enumerate(rows) if p['relevance']>=2]
def fetch(p):
 try:
  url=p['url']; ident='CorpusId:'+url.rsplit(':',1)[-1] if 'CorpusId:' in url else url.rsplit('/',1)[-1]
  r=requests.get('https://api.semanticscholar.org/graph/v1/paper/'+ident,params={'fields':'title,authors,year,externalIds,openAccessPdf,url,abstract'},timeout=30)
  if r.ok:
   meta=r.json();p['metadata']=meta;aid=meta.get('externalIds',{}).get('ArXiv');pdf=(meta.get('openAccessPdf') or {}).get('url')
  else:aid=None;pdf=None;p['s2_status']=r.status_code
  if not aid:
   q='ti:"'+p['title'].split(':')[0].replace('"','')+'"'
   r=requests.get('https://export.arxiv.org/api/query',params={'search_query':q,'max_results':3},timeout=40)
   ns={'a':'http://www.w3.org/2005/Atom'}
   for e in ET.fromstring(r.text).findall('a:entry',ns):
    title=e.findtext('a:title',namespaces=ns).strip();norm=lambda t:re.sub(r'[^a-z0-9]','',t.lower())
    if norm(title)==norm(p['title']):
     aid=e.findtext('a:id',namespaces=ns).rsplit('/',1)[-1];p['arxiv_summary']=e.findtext('a:summary',namespaces=ns);p['published']=e.findtext('a:published',namespaces=ns);break
  p['arxiv_id']=aid
  urls=([f'https://arxiv.org/pdf/{aid}'] if aid else [])+([pdf] if pdf else [])
  for u in urls:
   try:
    r=requests.get(u,timeout=60);r.raise_for_status()
    if not r.content.startswith(b'%PDF'):continue
    name=(aid or 'paper')+'_'+re.sub('[^a-z0-9]+','_',p['title'].lower())[:70]+'.pdf'
    path=Path('papers')/name;path.write_bytes(r.content);p.update(file=str(path),pages=len(PdfReader(path).pages),download_url=u,status='downloaded');break
   except Exception as e:p['download_error']=str(e)
  if 'file' not in p:p['status']='unavailable'
 except Exception as e:p.update(status='error',error=str(e))
 print(p['search_index'],p['status'],p.get('arxiv_id'),p['title'],flush=True);return p
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:out=list(ex.map(fetch,rows))
Path('evidence/literature_downloads.json').write_text(json.dumps(out,indent=2))
