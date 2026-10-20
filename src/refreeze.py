"""Preserve preregistration amendments only before held-out inference begins."""
from pathlib import Path
import json,datetime
from freeze import FILES,digest

def main():
    assert not list(Path('results/transcripts/evaluation').glob('*/*.json')), 'Cannot amend after held-out inference'
    path=Path('results/manifests/frozen.json');old=json.loads(path.read_text());archive=Path('results/manifests')/('frozen_'+old['created'].replace(':','-')+'.json')
    archive.write_text(path.read_text())
    old_hashes=dict(old['sha256']);paths=set(old_hashes)|set(FILES)
    old['sha256']={p:digest(p) for p in sorted(paths)}
    old['supersedes']=str(archive);old['amendment']='Pre-evaluation infrastructure amendment: explicit flat token IDs for Transformers 5 serialization; collection reuses imports in server parent. No subject response or held-out outcome exists.'
    old['changed_files']=[p for p,h in old['sha256'].items() if old_hashes.get(p)!=h];old['created']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    path.write_text(json.dumps(old,indent=2)+'\n');print('Refrozen',old['created'],old['changed_files'])
if __name__=='__main__':main()
