from pathlib import Path
import sys
p=Path('STATE.md'); text=p.read_text(); start='<!-- NEURICO_AGENT_NOTES_START:experiment_runner -->'; end='<!-- NEURICO_AGENT_NOTES_END:experiment_runner -->'
a,b=text.split(start); _,c=b.split(end)
p.write_text(a+start+'\n'+sys.argv[1]+'\n'+end+c)
