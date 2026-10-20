"""Download the two fixed subject revisions into this workspace only."""
import os
from pathlib import Path
os.environ['HF_HOME']=str(Path('artifacts/hf').resolve())
import json,concurrent.futures
from huggingface_hub import snapshot_download

def get(name):
    metadata=json.loads(Path('evidence/'+name.split('/')[-1]+'_metadata.json').read_text())
    path=snapshot_download(name,revision=metadata['sha'],local_dir='artifacts/models/'+name.split('/')[-1],allow_patterns=['*.json','*.safetensors','*.model','*.jinja','*.txt'],max_workers=8)
    print(name,path,flush=True)
with concurrent.futures.ThreadPoolExecutor(2) as ex:
    list(ex.map(get,['Qwen/Qwen3-8B','deepseek-ai/DeepSeek-R1-Distill-Llama-8B']))
