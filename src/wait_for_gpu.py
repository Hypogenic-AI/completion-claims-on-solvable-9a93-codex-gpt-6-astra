"""Read-only preflight wait: avoid racing another job's checkpoint transition."""
import os,time,subprocess,datetime
free_since=None;start=time.time()
while True:
    free=int(subprocess.check_output(['nvidia-smi','-i',os.environ['CUDA_VISIBLE_DEVICES'].split(',')[0],'--query-gpu=memory.free','--format=csv,noheader,nounits'],text=True).strip())
    if free>67000:
        if free_since is None:free_since=time.time()
        if time.time()-free_since>=90:break
    else:free_since=None
    print(datetime.datetime.now(datetime.timezone.utc).isoformat(), 'free_MiB',free,'stable_s',round(time.time()-free_since) if free_since else 0,flush=True)
    if time.time()-start>600:raise SystemExit('GPU not stably available within ten minutes')
    time.sleep(10)
print('GPU preflight passed',flush=True)
