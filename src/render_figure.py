"""Render the frozen statistics with export-safe labels; does not recompute them."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from analyze import MODELS
pairs=[('unsupported_done','solvable'),('unsupported_done','impossible'),('supported_done','solvable'),('correct_blocked','impossible'),('parse_failure','solvable'),('parse_failure','impossible')]
labels=['Unsupported DONE\nsolvable','Unsupported DONE\nimpossible','Correct completion\nsolvable','Correct BLOCKED\nimpossible','Parse failure\nsolvable','Parse failure\nimpossible']
fig,axs=plt.subplots(1,2,figsize=(11,4.5))
for ax,model in zip(axs,MODELS):
    s=json.loads((Path('results/analysis')/(model+'.json')).read_text())
    v=[s['metrics'][m][c] for m,c in pairs];y=[a['mean'] for a in v]
    ax.bar(range(6),y,yerr=[[b-a['ci95'][0] for a,b in zip(v,y)],[a['ci95'][1]-b for a,b in zip(v,y)]],capsize=3,color=['#a64b3b','#a64b3b','#41795c','#41795c','#697b9b','#697b9b'])
    ax.set_xticks(range(6),labels,rotation=55,ha='right',fontsize=8);ax.set_ylim(0,1.05);ax.set_title(model,fontsize=11);ax.set_ylabel('Probability (95% bootstrap CI)')
fig.suptitle('200 paired base items per checkpoint; three seeds per condition',fontsize=10)
fig.tight_layout();fig.savefig('figures/outcomes.png',dpi=180,bbox_inches='tight');plt.close(fig)
