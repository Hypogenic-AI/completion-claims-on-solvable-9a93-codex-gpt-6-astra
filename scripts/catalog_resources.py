from pathlib import Path
import json,hashlib,collections,csv
ROOT=Path(__file__).resolve().parents[1];assert Path.cwd()==ROOT
papers=json.loads(Path('evidence/papers_manifest.json').read_text())
notes={
'2406.12045':'State-based database scoring and repeated-run pass^k; retail/airline user simulation. Background: evaluator pattern, not a direct false-DONE experiment.',
'2407.18901':'750 tasks, 9 apps, 457 APIs and collateral-state checks. Background: authoritative world-state evaluation; full environment pruned for implementation cost.',
'2501.12948':'RL and distillation model lineage. Background only; target-model behavior must be measured separately. Official pinned model card also archived.',
'2506.01716':'Code-as-Task generates instructions, verifiers, solution/failure cases; RL evaluated on M3ToolEval and tau-bench. Abstract screen: useful data-quality pattern, training out of scope.',
'2506.04535':'Impossible/unanswerable question benchmark and dataset mutation. Abstract screen: lacks mutable final-state task execution; implementation pruned.',
'2507.21017':'MIRAGE taxonomy: instruction, history and observation unfaithfulness; snapshots and LLM judging. Abstract screen: classification context, not a paired completion endpoint.',
'2510.20270':'Full review, 25 pages. 103 LCB and 349 SWE tasks per variant; exploitation measured through mutated tests. Official code/data staged; stronger independent oracle needed.',
'2512.04864':'Full review, 38 pages. 200 tasks, 11 models, GPT-5 judge; broken tools, missing data and fabricated artifacts. Closest released constrained-task source; no solvable twins.',
'2602.11136':'FormalJudge translates requirements into formal checks via Dafny/Z3. Abstract screen: judge-method context; specification translation remains a source of error; formal stack not required for simple state predicates.',
'2604.20930':'Permission-to-fail/hard-stop mitigation for harmful task-completion pressure. Abstract screen: domain and incentives differ from benign task hypothesis; no implementation.',
'2605.08747':'VIGIL separates world completion and terminal report in 1,000 embodied episodes across 20 models. Abstract screen: useful outcome taxonomy; robotics implementation pruned.',
'2605.23574':'PushBench tests quantitative persistence and duplicate/false completion using external verifiers. Abstract screen: long-horizon/count confound; verifier ideas retained only.',
'2605.28532':'Full review, 14 pages. 1,036 critical-tool-masked tasks, 283-item human audit, false-continuation metric. Code staged; no generated data shipped in current tree.',
'2606.09863':'Full review, 18 pages. False success in tau2/AppWorld, domain-sensitive lightweight detectors vs five LLM judges. Supports separate claims/state and conditional denominators.',
'2606.23175':'28 Geant4 agent episodes distinguish correct answer from faithful scientific mechanism. Abstract screen: small domain-specific evidence; does not test impossible twins.',
'2607.13596':'Protective capacity hallucination across eight LLMs and 13,600 sessions. Abstract screen: role/capability boundaries matter, but vulnerable-user settings are outside benign primary suite.',
'2607.19449':'Silent tool failures and fabricated safety excuses; four models, 12 stubs, four profiles. Abstract screen: do not conflate tool errors, fabrication and safety refusal; broad outcome differs from DONE.',
'2608.22793':'TRACE evolves a skill bank from trajectory contrasts on CAR-bench. Abstract screen; recovered via author website. Reliability and limit-awareness context, optimization outside scope.',
'2609.03267':'270 impossible code prompts plus 91 solvable controls; 12 models, two-tier judge (reported 82% human agreement). Abstract screen: paired controls useful; code plausibility is distinct from completed state.',
'2609.14758':'1,024 enforced failed-tool items; failure signaling and explicit retrieval-status defense. Abstract screen: retrieval-value honesty broader than completed state; supports fixed-trace diagnostic.',
'2609.15494':'ImpossibleBench-derived repair tasks vary authority, peers, wording and friction. Abstract screen: extra pressure interventions pruned to retain a clean impossibility contrast.',
'2609.20812':'Five feasible file-review scenarios, 12 agents, transcript coverage/planted defects. Abstract plus selected methods: explicit overclaim differs from omission; long-review direction pruned.',
'2609.35732':'Full review, 5 pages. 100 fixed-failure scenarios, 3 policies, 6 models, 3,600 responses. Reporting isolation useful; no successful controls or released artifact link.',
'2609.38411':'Audits 22 incidents/102 safety evaluations using completion/stopping/escape/continuation states. Abstract screen: retain budget exhaustion separately; incident association is not causal evidence.',
'2610.02001':'Small-model harness study: 4 harnesses x 4 models x 18 tasks and tau2 comparison. Abstract screen: harness sensitivity and limited single-machine evidence, not target-model confirmation.',
'2610.07274':'Audits score validity, traced computation, report consistency and repeatability on 108 tasks. Abstract screen: independent evidence layers; not a paired task-impossibility experiment.',
'2610.19226':'Paired feasible/blocked Terminal-Bench and retail tau2 tasks; separates blocker recognition and warranted deferral. Abstract/targeted screen: supports direction 1; harness-search transfer limits reported.',
}
for p in papers:
 f=Path(p['file']);p['sha256']=hashlib.sha256(f.read_bytes()).hexdigest();p['bytes']=f.stat().st_size
 aid=p['arxiv_id'].split('v')[0];p['review_note']=notes[aid]
 if not p.get('download_url'):p['download_url']='https://arxiv.org/pdf/'+p['arxiv_id']
papers.sort(key=lambda x:x['arxiv_id'])
Path('evidence/papers_manifest.json').write_text(json.dumps(papers,indent=2))
t='# Downloaded papers\n\n27 unique papers, downloaded from primary public sources and PDF-parsed. Five full chunked reviews (100 pages total); all other downloaded papers are explicitly screened at abstract/selected-section depth. Full page-by-page notes: `../evidence/reading_log.md`. Raw bibliographic metadata and SHA-256: `../evidence/papers_manifest.json`.\n\nRecreate PDFs from the workspace root: `.venv/bin/python scripts/download_papers.py`. Split with `.venv/bin/python .codex/skills/paper-finder/scripts/pdf_chunker.py papers/FILE.pdf --pages-per-chunk 3`. PDFs and chunk files remain local, excluded from git; index/manifests/scripts are retained.\n\n'
for i,p in enumerate(papers,1):
 t+=f"## {i}. {p['title']}\n\n- Authors: {p.get('authors','')}\n- Year: {p.get('year','')}; arXiv: {p['arxiv_id']}; {p['pages']} pages.\n- Local PDF: [{Path(p['file']).name}]({Path(p['file']).name}).\n- {p['review_note']}\n\n"
t+='## Search exclusions and access gaps\n\nPaper-finder returned 164 candidates (25 rated >=2; 139 peripheral score-1 records retained as metadata but not downloaded). Of the 25, 23 PDFs were recovered, HCRC was verified author-withdrawn (arXiv 2607.04562) and excluded, and the coding DriftBench paper could not be resolved despite Semantic Scholar/arXiv retries. Do not substitute the unrelated database DriftBench paper. Four additional unique primary papers were acquired manually. No HCRC result is used as evidence. TRACE was recovered from its author website. See evidence/literature_downloads.json, literature_retry.json and final_access_attempts.json.\n'
Path('papers/README.md').write_text(t)
# Search screening log (title/relevance decisions, not a claim of full review for all 164).
p=max(Path('paper_search_results').glob('*.jsonl'),key=lambda x:x.stat().st_size)
search=[json.loads(l) for l in p.read_text().splitlines()]
resolved={r['search_index']:r for r in json.loads(Path('evidence/literature_downloads.json').read_text())}
with Path('evidence/screening.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['index','title','service_relevance','decision','reason'])
 for i,r in enumerate(search):
  d=resolved.get(i)
  if d:w.writerow([i,r['title'],r['relevance'],d['status'],d.get('exclusion_reason','Core or supporting abstract review; see paper catalog for depth')])
  else:w.writerow([i,r['title'],r['relevance'],'title_screen_excluded','Peripheral score-1 candidate; preserve metadata, no additional implementation direction'])
repos=json.loads(Path('evidence/repositories.json').read_text())
t='''# Resources catalog

Prepared on October 20, 2026 for **Completion claims on solvable and impossible tasks**. Resource gathering is complete; the hypothesis has not been tested. Read `planning.md` before implementing the three retained directions.

## Inventory

- **27 unique PDF papers**, including five complete chunked readings (100 pages).
- **2 downloaded official datasets**: 103 base coding tasks in three splits (309 rows) and 200 constrained tool tasks.
- **1 generated development fixture**: 30 pairs / 60 records, only three templates; not confirmatory data.
- **3 pinned official code repositories**; source inspection and Python syntax checks only.
- Fresh project `.venv`, `pyproject.toml`, `uv.lock`. No model weights, inference results, external judge calls or model server.

## Papers

| Title | Authors | Year | Local file | Use |
|---|---|---|---|---|
'''
for p in papers:
 authors=', '.join(p.get('authors','').split(', ')[:3])+(' et al.' if len(p.get('authors','').split(', '))>3 else '')
 t+=f"| {p['title']} | {authors} | {p.get('year','')} | `{p['file']}` | {p['review_note'].split('.')[0]} |\n"
t+='''
The concise synthesis is `literature_review.md`; per-paper notes are `papers/README.md`; full chunk notes are `evidence/reading_log.md`. Primary URLs, versions, page counts, bytes and SHA-256 hashes are in `evidence/papers_manifest.json`. `scripts/download_papers.py` recreates the archive and rejects unexpected byte changes.

## Datasets

| Resource | Source / revision | Local size | Location | Intended use |
|---|---|---|---|---|
| Impossible-LiveCodeBench | HF fjzzq2002/impossible_livecodebench / 98650ffc3f28a01b261669b6d19fcd7773823710 | 103 x 3 rows; 875,550 bytes | datasets/impossible_livecodebench/ | Paired coding replication, after semantic validation and exclusion/repair of lcbhard_77 |
| Agentic Upward Deception | Author GitHub / b26151c7195111271feba64fb15db6227f25f51b | 200 rows; 212,142 bytes | datasets/upward_deception/ | Broken-tool task patterns and versioned neutral-domain adaptation |
| Development twins (generated) | scripts/build_development_fixtures.py | 30 pairs / 60 rows, three templates | datasets/development_twins/ | Dispatcher, exact-state scorer and final-channel parsing development only |

Download commands, licenses/uncertainties, schemas and sample records are in `datasets/README.md`. `scripts/download_datasets.py` uses pinned official URLs. `scripts/validate_datasets.py` checks schemas, IDs, alignment, missingness and syntax. Dataset bytes are excluded from git, small examples remain tracked under `datasets/samples/`.

**Validation limits:** `lcbhard_77` has malformed impossible tests; use a paired base-ID exclusion, leaving 102 syntax-clean pairs, before any model outcomes. No source gold solutions exist in this LCB release, and parsing is not semantic proof. Forty-eight Upward Deception prompts contain substitution artifacts; missing source content is intentional in several task types. These data are usable for preparation/adaptation, not immediately a clean confirmatory benchmark. The generated fixture has exhaustive finite-state reachability validation but deliberately lacks task diversity.

## Repositories

| Name | Source | Local path | Pinned commit |
|---|---|---|---|
'''
for r in repos:t+=f"| {r['name']} | {r['url']} | {r['path']} | {r['sha']} |\n"
t+='''
See `code/README.md` for installation requirements, key entry points, examples marked unrun, and scorer/runtime caveats. Sixty Python files pass AST parsing; all three clones are clean. Heavy evaluation dependencies were not installed. Important findings: ImpossibleBench's protected `test_patch` is still the treatment test, not `original_test`; its metric is exploitation, not false DONE. Upward Deception's HFR denominator is narrower than its docstring, resume does not validate changed inputs, and failure messages include randomness. FeasiGen ships construction code rather than the generated corpus, and its builder accepts some traces with unknown success. Address these before adapting.

## Model resource

Canonical target: `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`, pinned HF revision `6a6f4aa4197940add57724a7707d069478df56b1`. `evidence/hf_model.json`, `model_card.md`, `model_config.json` and `tokenizer_config.json` preserve metadata and template. Official metadata lists 8,030,261,248 parameters and about 16.1 GB of weight storage. Weight files were intentionally not downloaded in this resource phase. The exact checkpoint, dtype and serving protocol must be verified by the runner; native tool execution has not been tested. The card recommends user-role instructions, no system prompt, temperature .5–.7, and repeated evaluations. Upstream Llama licensing also applies per the card.

## Search, limitations and handoff

Paper-finder was tried first and succeeded after adding httpx. Its 164 records were screened, with 25 higher-ranked candidates attempted; 23 obtained plus four manual unique papers. HCRC was verified withdrawn and excluded; the coding DriftBench remained unresolved after retries. The author website recovered TRACE. No claim is made to an exhaustive literature review. Raw logs: `paper_search_results/`, `evidence/arxiv_search.json`, `screening.tsv`, and access-attempt JSONs. Browser search returned empty results, so direct arXiv/GitHub/HF primary-source APIs were used. `rg` was unavailable; Python/find were used locally.

The HF unofficial paired dataset was gated, so the official source was used. FeasiGen's inspected release has no generated tasks; FTA promises data but gives no public link in its PDF. AppWorld/tau2 full runtime downloads and SWE-bench implementation were pruned on feasibility grounds. No staged local resources or explicit user repositories were listed. Broad background papers do not expand the three-direction budget.

The main empirical gap is a controlled, powered paired experiment on the specified distilled 8B checkpoint. Treat endpoint choice carefully: unconditional unsupported-DONE probability and false-claim probability conditional on failure answer different questions. Existing studies use broader metrics, different models, different denominators or uncontrolled settings. No reviewed result establishes the requested >=.10 difference.

## Runner starting sequence

1. Read STATE.md, literature_review.md and planning.md; keep its three-direction ranking unless new evidence invalidates it.
2. `uv sync --project .`; run the dataset validation scripts. Add serving/Inspect dependencies only to this environment.
3. Build a closed dispatcher around the development fixture; implement exact final-state and terminal-DONE scoring, with parser/timeout controls. Confirm solvable capability and prohibit bypass routes.
4. Curate a separate diverse confirmatory set with reference solutions and impossibility certificates; freeze prompts, budgets, generation settings, pair IDs and sample size. The 30 development pairs must not be used as confirmatory samples.
5. Run target-model twins in fresh states/contexts, randomizing order. Report paired estimates/95% CIs, per-condition state success and claims, truncation/errors, and template-cluster sensitivity. Optional fixed-trace and coding checks remain within the retained directions.
6. Save raw transcripts/state snapshots and neurico-safety-result/v1 records following safety-evals. Mark any finding candidate, not confirmed. Use azure-models if an OpenAI-family semantic judge becomes necessary; the primary endpoint needs no model judge.

Completion evidence is recorded in `evidence/final_validation.json`; the marker `.resource_finder_complete` is written only after artifact validation. No experiment outcome is implied by that marker.
'''
Path('resources.md').write_text(t)
print('Catalogs generated:',len(papers),'papers;',len(repos),'repos')
