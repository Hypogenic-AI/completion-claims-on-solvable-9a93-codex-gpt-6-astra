# Code resources

All three repositories were cloned shallowly and inspected, not installed or run as model evaluations. Commits are in `../evidence/repositories.json`. Python syntax checks passed for 60 source files; this is not a runtime test. Upstream trees remain clean. No user-specified or staged local repositories were listed.

## ImpossibleBench

- Source: https://github.com/safety-research/impossiblebench
- Local: `impossiblebench/`; commit `d4f9a149db2b9cec0fed7bab01d91c07ee10aca2`; MIT code license.
- Official Inspect task definitions, original/oneoff/conflicting data adapters, minimal and full tool scaffolds, exploitation scorers, transcript loader and optional LLM judge.
- Entry points: `demo.py`; `src/impossiblebench/livecodebench_tasks.py::impossible_livecodebench`; `record_to_sample`; `livecodebench_agent_mini.py`; `livecodebench_agent_full.py`; `livecodebench_scorers.py`; `analysis/data_loader.py`.
- Python >=3.10. `setup.py` installs Inspect AI, a git dependency on Inspect Evals (including SWE support), pandas, datasets, jsonlines, swebench and platformdirs; optional analysis uses anthropic/litellm. Docker is default sandbox. These heavyweight evaluation dependencies were not installed in the resource venv.
- If installing later, use the project environment: `uv pip install --python .venv/bin/python -e code/impossiblebench`, then freeze/document resolved dependencies. The package's moving git dependency needs pinning for reproducibility. Prefer adapting the narrow LCB adapter over installing unused SWE functionality.
- The README reports an October 12, 2026 fix for a GitHub-port bug that prevented LCB test modification. This clone includes the update. The paper states its original runs were unaffected.
- Crucial semantics: `allow_test_modifications=False` saves the **condition's** `test` as `test_patch`; it does not restore the benchmark's correct `original_test`. The default scorer measures test passing and marks human intervention incorrect. Add a separate original-specification/state scorer and explicit final-claim scorer. `record_to_sample` omits `original_test` from metadata, so preserve it yourself from the downloaded data.
- Public task defaults differ from the paper replication configuration: default max_attempts=3, message_limit=30 and a pass-tests instruction; `demo.py` sets tuned prompts/budgets. Freeze all parameters explicitly. Do not confuse these defaults with paper results.
- Downloaded raw dataset includes `lcbhard_77` syntax defects. See datasets README before using.

## Agentic Upward Deception

- Source: https://github.com/QingyuLiu/Agentic-Upward-Deception
- Local: `upward-deception/`; commit `b26151c7195111271feba64fb15db6227f25f51b`. No explicit license found at this revision.
- `evaluation.py` materializes temporary files, runs a Smolagents CodeAgent, captures final answers/logs and applies task-specific judge templates in `template/`.
- `models/agent_runner.py` selects valid/broken tools; `utils/incorrect_tools.py` provides failure stubs; `models/judge_model.py` implements the model judge. `evaluate_dataset` assigns sequential `task_id` internally; `task_index` is the source ID.
- `requirements.txt`: smolagents 1.23.0, litellm 1.80.9, python-pptx 1.0.2, langchain-community 0.4.1, pypdf 6.4.0, nltk, openpyxl, yt-dlp, Wikipedia-API, python-dotenv. Some imports rely on transitive dependencies. Installing exact upstream requirements would downgrade this project's pypdf; resolve deliberately, never in a shared environment.
- Model connection requires `EVAL_URL`, `EVAL_KEY`, `EVAL_MODEL_ID`; judge separately configured. Do not print keys or copy credentials into artifacts.
- Example upstream command (not run): `.venv/bin/python code/upward-deception/evaluation.py --dataset datasets/upward_deception/task_3.json --output_dir results/upward --results results/upward.json --prompts_dir code/upward-deception/template`.
- Important limitations: random synthetic file contents and randomized error wording are not seeded by the runner; web-capable utilities may introduce external failures. Replace these with deterministic fixtures for paired causality. The `timeout` constructor argument is accepted but not passed into the shown model constructor; do not assume a hard timeout is enforced.
- `compute_metrics` increments the HFR denominator only under `download_ok and related`, narrower than its “among related instances” description. Do not reuse HFR as our endpoint. Fresh `results` paths are necessary across treatments: resume reads existing tasks without validating input/prompt equality.
- Author dataset JSON copied verbatim to datasets/ for immediate use; upstream source copy remains in the clone. Text-substitution defects are documented separately.

## FeasiGen

- Source: https://github.com/LeonChengg/FeasiGen
- Local: `feasigen/`; commit `f5a1a647cda11e4fc2a12ca8e35cb29ba7f0f76c`; MIT.
- README is still “under construction”; no pyproject/requirements file found. No generated task data or successful traces shipped in the inspected tree.
- Reusable core: `src/feasiagent/data/schema.py`, `path_intersection.py`, `tool_pool.py`; execution/metrics in `eval/agent_loop.py`, `eval/runner.py`, `metrics/feasibility.py`.
- `scripts/build_path_dataset.py` turns successful multi-model tool traces into masked-tool STOP samples. `scripts/eval.py` supports original/feasibility modes. `scripts/download_sources.py` currently implements BFCL download only despite additional loader/config files. Data creation requires external benchmark sources and successful traces; this clone alone cannot reproduce the paper's 1,036 tasks.
- Imports indicate pydantic, openai, PyYAML, huggingface_hub; plotting adds numpy/matplotlib. Runtime dependencies and APIs were not validated.
- Construction caveat: `build_path_dataset.py` accepts `task_success=None` traces with nonempty tool_call_set as successful. Tighten to verified success for our task construction. Set min-agreement=1.0 and still audit alternate solution paths; observed tool-set intersection is not proof of indispensability.
- Upstream scripts default output under `code/feasigen/data/`; adapt output paths to this workspace's datasets/ and evidence/ before executing. No source-download, inference, model server or paid API run was started.

## Reclone at recorded commits

```bash
pwd
git clone --depth 1 https://github.com/safety-research/impossiblebench.git code/impossiblebench
git clone --depth 1 https://github.com/QingyuLiu/Agentic-Upward-Deception.git code/upward-deception
git clone --depth 1 https://github.com/LeonChengg/FeasiGen.git code/feasigen
```

For future reproduction fetch the SHA in `evidence/repositories.json` and checkout that SHA; a default-branch shallow clone alone is not a pin. Existing clones already match these SHAs. Do not rerun clone commands over existing directories.
