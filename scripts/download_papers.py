"""Recreate the validated paper archive from its recorded primary-source URLs."""
from pathlib import Path
import requests,json,hashlib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];assert Path.cwd()==ROOT and (ROOT/'.git').exists()
rows=json.loads(Path('evidence/papers_manifest.json').read_text())
for row in rows:
    path=Path(row['file']);expected=row.get('sha256')
    if path.exists() and (not expected or hashlib.sha256(path.read_bytes()).hexdigest()==expected):continue
    url=row.get('download_url') or 'https://arxiv.org/pdf/'+row['arxiv_id']
    r=requests.get(url,timeout=90);r.raise_for_status();assert r.content.startswith(b'%PDF')
    if expected and hashlib.sha256(r.content).hexdigest()!=expected:
        raise ValueError(f'Upstream bytes changed for {path}; inspect version rather than silently accepting.')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(r.content);PdfReader(path)
print(f'{len(rows)} PDFs available and checked against recorded hashes when present.')
