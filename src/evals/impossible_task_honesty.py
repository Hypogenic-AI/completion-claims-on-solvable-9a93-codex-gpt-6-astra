"""Inspectable task entrypoint. Real subject responses use the supplied vLLM API."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from inspect_ai import task
from collect import build_task

@task
def impossible_task_honesty(model_id:str='qwen3-8b',split:str='evaluation',base_url:str='http://127.0.0.1:8765/v1'):
    if split=='evaluation':
        from freeze import verify
        verify()
    return build_task(model_id,split,base_url)
