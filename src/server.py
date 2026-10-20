"""Start/stop only this workspace's vLLM process group."""
import os,sys,json,time,signal,subprocess
from pathlib import Path
import requests
from collect import MODELS,main as collect_main

def start(model):
    env=os.environ.copy()
    env['HF_HOME']=str(Path('artifacts/hf').resolve());env['VLLM_CACHE_ROOT']=str(Path('artifacts/vllm_cache').resolve());env['TRITON_CACHE_DIR']=str(Path('artifacts/triton_cache').resolve());env['TORCHINDUCTOR_CACHE_DIR']=str(Path('artifacts/torch_cache').resolve());env['OMP_NUM_THREADS']='8'
    cmd=[sys.executable,'-m','vllm.entrypoints.openai.api_server','--model',str(Path('artifacts/models/'+MODELS[model]).resolve()),'--served-model-name',model,'--port','8765','--host','127.0.0.1','--dtype','bfloat16','--tensor-parallel-size','1','--max-model-len','8192','--max-num-seqs','64','--gpu-memory-utilization','0.80','--enforce-eager','--generation-config','vllm']
    env['XDG_CACHE_HOME']=str(Path('artifacts/cache').resolve());env['CUDA_CACHE_PATH']=str(Path('artifacts/cuda_cache').resolve());env['FLASHINFER_WORKSPACE_BASE']=str(Path('artifacts/flashinfer').resolve())
    gpu=env.get('CUDA_VISIBLE_DEVICES','').split(',')[0]
    wait_start=time.time();free_since=None
    while True:
        free=int(subprocess.check_output(['nvidia-smi','-i',gpu,'--query-gpu=memory.free','--format=csv,noheader,nounits'],text=True).strip())
        if free>67000:
            if free_since is None:free_since=time.time()
            if time.time()-free_since>=30:break
        else:free_since=None
        print(f'Allocated GPU busy: {free} MiB free; waited {time.time()-wait_start:.0f}s',flush=True)
        if time.time()-wait_start>1500:raise RuntimeError('Allocated GPU unavailable after 25 minutes')
        time.sleep(10)
    log=open('logs/server_'+model+'.log','w');p=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,env=env,start_new_session=True)
    Path('results/server_process.json').write_text(json.dumps({'pid':p.pid,'model':model,'cmd':cmd,'started':time.time()}))
    for _ in range(180):
        if p.poll() is not None:
            stop(p);raise RuntimeError(f'Server exited {p.returncode}; see logs/server_{model}.log')
        try:
            r=requests.get('http://127.0.0.1:8765/health',timeout=2)
            if r.ok:return p
        except requests.RequestException:pass
        time.sleep(2)
    stop(p);raise RuntimeError('Server startup timeout')

def stop(p):
    try:os.killpg(p.pid,signal.SIGTERM)
    except ProcessLookupError:pass
    try:p.wait(timeout=30)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid,signal.SIGKILL);p.wait()
    Path('results/server_process.json').unlink(missing_ok=True)

if __name__=='__main__':
    model=sys.argv[1];p=None
    try:
        p=start(model);print('SERVER READY',model,flush=True)
        for split in sys.argv[2:]:
            collect_main(['--model',model,'--split',split])
    finally:
        if p is not None:stop(p)
