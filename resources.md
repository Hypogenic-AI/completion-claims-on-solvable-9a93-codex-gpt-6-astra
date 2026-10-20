# Resources catalog

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
| $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | Shunyu Yao, Noah Shinn, Pedram Razavi et al. | 2024 | `papers/2406.12045_tau_bench.pdf` | State-based database scoring and repeated-run pass^k; retail/airline user simulation |
| AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents | Harsh Trivedi, Tushar Khot, Mareike Hartmann et al. | 2024 | `papers/2407.18901_appworld.pdf` | 750 tasks, 9 apps, 457 APIs and collateral-state checks |
| DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning |  DeepSeek-AI, Daya Guo, Dejian Yang et al. | 2025 | `papers/2501.12948_deepseek_r1.pdf` | RL and distillation model lineage |
| Self-Challenging Language Model Agents | Yifei Zhou, Sergey Levine, Jason E. Weston et al. | 2025 | `papers/2506.01716v1_self_challenging_language_model_agents.pdf` | Code-as-Task generates instructions, verifiers, solution/failure cases; RL evaluated on M3ToolEval and tau-bench |
| BSBench: will your LLM find the largest prime number? | K. O. T. Erziev | 2025 | `papers/2506.04535v1_bsbench_will_your_llm_find_the_largest_prime_number_.pdf` | Impossible/unanswerable question benchmark and dataset mutation |
| MIRAGE-Bench: LLM Agent is Hallucinating and Where to Find Them | Wei-Chen Zhang, Yiyou Sun, Pohao Huang et al. | 2025 | `papers/2507.21017v1_mirage_bench_llm_agent_is_hallucinating_and_where_to_find_them.pdf` | MIRAGE taxonomy: instruction, history and observation unfaithfulness; snapshots and LLM judging |
| ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases | Zi-Qian Zhong, Aditi Raghunathan, Nicholas Carlini | 2025 | `papers/2510.20270_impossiblebench.pdf` | Full review, 25 pages |
| Are Your Agents Upward Deceivers? | Dadi Guo, Qing-Yu Liu, Dong-Rui Liu et al. | 2025 | `papers/2512.04864_are_your_agents_upward_deceivers_.pdf` | Full review, 38 pages |
| FormalJudge: A Neuro-Symbolic Paradigm for Agentic Oversight | Jia-Yi Zhou, Yang Sheng, Hantao Lou et al. | 2026 | `papers/2602.11136v2_formaljudge_a_neuro_symbolic_paradigm_for_agentic_oversight.pdf` | FormalJudge translates requirements into formal checks via Dafny/Z3 |
| SafeRedirect: Defeating Internal Safety Collapse via Task-Completion Redirection in Frontier LLMs | Chao Pan, Yu Wu, Xin Yao | 2026 | `papers/2604.20930v1_saferedirect_defeating_internal_safety_collapse_via_task_completion_re.pdf` | Permission-to-fail/hard-stop mitigation for harmful task-completion pressure |
| Done, But Not Sure: Disentangling World Completion from Self-Termination in Embodied Agents | Ying Chen, Lihuang Fang, Ruien Jiang et al. | 2026 | `papers/2605.08747v4_done_but_not_sure_disentangling_world_completion_from_self_termination.pdf` | VIGIL separates world completion and terminal report in 1,000 embodied episodes across 20 models |
| Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents | Yuan-Dao Cai, Yuzhang Zhu, Li-You Gao et al. | 2026 | `papers/2605.23574_pushbench.pdf` | PushBench tests quantitative persistence and duplicate/false completion using external verifiers |
| Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents | Liang Cheng, Mingsheng Cai, Jiu-Ming Jiang et al. | 2026 | `papers/2605.28532v1_do_agents_know_what_they_can_t_do_evaluating_feasibility_awareness_in_.pdf` | Full review, 14 pages |
| From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents | Laksh Advani | 2026 | `papers/2606.09863v1_from_confident_closing_to_silent_failure_characterizing_false_success_.pdf` | Full review, 18 pages |
| Position: Correct Answer, Wrong Mechanism - When AI Scientists Defend General Claims Their Own Data Contradicts | S. Eulig | 2026 | `papers/2606.23175v1_19.pdf` | 28 Geant4 agent episodes distinguish correct answer from faithful scientific mechanism |
| Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities | E. Lee, Jungpyo Nam, Sunjun Hwang | 2026 | `papers/2607.13596v2_protective_capacity_hallucination_when_large_language_models_claim_non.pdf` | Protective capacity hallucination across eight LLMs and 13,600 sessions |
| Guardrails as Scapegoats: Auditing Unfaithful Safety Refusals in Tool-Augmented LLM Agents | Aarushi Singh | 2026 | `papers/2607.19449v1_guardrails_as_scapegoats_auditing_unfaithful_safety_refusals_in_tool_a.pdf` | Silent tool failures and fabricated safety excuses; four models, 12 stubs, four profiles |
| TRACE: A Self-Evolving Skill Bank for Consistent, Limit-Aware LLM Agents | Wen-Hao Wu, Meng-Hao Zhang, X. Wang et al. | 2026 | `papers/2608.22793_trace.pdf` | TRACE evolves a skill bank from trajectory contrasts on CAR-bench |
| Refusing the Impossible: A Taxonomy and Benchmark for Code Hallucination in Large Language Models | Vishnu Asutosh Dasu, Ashish Kundu, Gang Tan | 2026 | `papers/2609.03267v1_refusing_the_impossible_a_taxonomy_and_benchmark_for_code_hallucinatio.pdf` | 270 impossible code prompts plus 91 solvable controls; 12 models, two-tier judge (reported 82% human agreement) |
| Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return | Arham Sethi, Arsen Kenzhebayev, Saanvi Paturi et al. | 2026 | `papers/2609.14758v1_fabrication_after_tool_failure_tool_augmented_agents_assert_values_the.pdf` | 1,024 enforced failed-tool items; failure signaling and explicit retrieval-status defense |
| The Troy Moment: How LLM Agents Adjudicate the Decision Point Under Impossible Tasks, Claimed Authority, and Peer Information | I. Zhang | 2026 | `papers/2609.15494v3_the_troy_moment_how_llm_agents_adjudicate_the_decision_point_under_imp.pdf` | ImpossibleBench-derived repair tasks vary authority, peers, wording and friction |
| Quantifying Overclaiming Propensity in Frontier LLM Agents | Nolan Smyth, Yorguin-Jose Mantilla-Ramos, Pascal Junior Tikeng Notsawo et al. | 2026 | `papers/2609.20812v3_quantifying_overclaiming_propensity_in_frontier_llm_agents.pdf` | Five feasible file-review scenarios, 12 agents, transcript coverage/planted defects |
| Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models | Jun-Ru Zhu, Shi-Ming Xie, Ai-Me-Lu-Fan Chen et al. | 2026 | `papers/2609.35732v1_failure_transparent_agents_benchmarking_post_failure_reporting_in_tool.pdf` | Full review, 5 pages |
| A Competing-Hazards Systematization of Loss of Control in Autonomous Agents | M. Bouke | 2026 | `papers/2609.38411v1_28.pdf` | Audits 22 incidents/102 safety evaluations using completion/stopping/escape/continuation states |
| Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete Real Tasks | Hao Wang, Ting-Bin Huang | 2026 | `papers/2610.02001v1_mingbird_a_local_first_agent_harness_enabling_small_open_models_to_com.pdf` | Small-model harness study: 4 harnesses x 4 models x 18 tasks and tau2 comparison |
| A Trust Layer for Agent Evaluation | Mohammadreza Sediqin, Shivali Dalmia, Srinivasa Karthikeya Reddy Kovvuri et al. | 2026 | `papers/2610.07274_trust_layer.pdf` | Audits score validity, traced computation, report consistency and repeatability on 108 tasks |
| Agentic Self-Awareness: Aligning Knowing, Acting, and Holding | Qing-Lin Chen, Hiroaki Hayashi, Jia-Xin Zhang et al. | 2026 | `papers/2610.19226v1_agentic_self_awareness_aligning_knowing_acting_and_holding.pdf` | Paired feasible/blocked Terminal-Bench and retail tau2 tasks; separates blocker recognition and warranted deferral |

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
| impossiblebench | https://github.com/safety-research/impossiblebench.git | code/impossiblebench | d4f9a149db2b9cec0fed7bab01d91c07ee10aca2 |
| upward-deception | https://github.com/QingyuLiu/Agentic-Upward-Deception.git | code/upward-deception | b26151c7195111271feba64fb15db6227f25f51b |
| feasigen | https://github.com/LeonChengg/FeasiGen.git | code/feasigen | f5a1a647cda11e4fc2a12ca8e35cb29ba7f0f76c |

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

## Experiment-runner additions (October 20, 2026)

The user-specific protocol supersedes the resource-phase coding and fixed-trace directions. `datasets/custom/items.json` contains 20 development and 200 held-out base scenarios over the four requested templates. `src/protocol.py` implements source-read provenance, permanent permission barriers and exact claim/state scoring. Both requested model revisions were downloaded into the workspace, with hashes in `results/manifests/frozen.json`; neither exact checkpoint appeared in the live OpenRouter catalog snapshot `evidence/openrouter_catalog.json`. Inference uses the isolated project environment and allocated GPU only.

Supplied safety-KB design/gap snapshots are copied into `evidence/impossible-task-snapshot.md` and `evidence/anthropic-gaps-snapshot.md`. These are design context, not official benchmark scores. The implementation uses real local vLLM inference and deterministic scoring with no LLM judge. Scorer fixtures, baseline results, raw transcripts and final analysis are under `results/`; final collection status and findings are in `REPORT.md`. Initial GPU contention and the startup failure are preserved in `logs/server_qwen3-8b_startup_failure.log`.

Final execution outcome: 2400 valid held-out episodes collected. An incompatible Transformers 5.19.0 interpretation of the DeepSeek tokenizer required a documented repair using the pinned Rust tokenizer.json; 212 invalid saved episodes are preserved separately and excluded. See preregistration_amendment.md, REPORT.md, and results/final_validation.json for the precise scope and checks. No candidate is supported.
