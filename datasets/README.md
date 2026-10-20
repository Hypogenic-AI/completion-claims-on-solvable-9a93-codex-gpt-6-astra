# Local datasets and reproduction

Two official datasets downloaded; one synthetic development fixture generated. Raw data are ignored by git, while this file and small samples are retained. Run commands from the repository root (`pwd` first). Downloads are pinned by revision, with SHA-256 and byte sizes in `evidence/dataset_download_manifest.json`.

## Recreate and validate all resources

```bash
pwd
uv sync --project .
.venv/bin/python scripts/download_datasets.py
.venv/bin/python scripts/build_development_fixtures.py
.venv/bin/python scripts/validate_datasets.py
```

## Impossible-LiveCodeBench — official paired coding dataset

- Source: `fjzzq2002/impossible_livecodebench` on Hugging Face, linked from the official `safety-research/impossiblebench` repository.
- Revision: `98650ffc3f28a01b261669b6d19fcd7773823710`.
- Files: `impossible_livecodebench/{original,oneoff,conflicting}.parquet`.
- Size: 103 rows per split, 309 rows total, 103 matched base tasks; 875,550 bytes total.
- Schema: string fields `task_id`, `prompt`, `test`, `original_test`, `entry_point`, `impossible_type`.
- Purpose: secondary coding replication; these are hard algorithmic tasks, potentially too difficult for the target 8B model.
- Pair by `task_id`, never by row order. All three ID sets match; prompts, entry points and original tests match within every pair. No null or empty string fields.
- **Known defect:** `lcbhard_77` has an unterminated string in `test` in both oneoff and conflicting. Exclude this base ID from *all* conditions for a syntax-clean derivative (102 pairs), or fix in a separately versioned derivative before any model outcomes. Raw files are untouched. Syntax validity does not establish semantic validity.
- No gold solutions supplied. Authors did not apply gold-solution QC to this split. Require reference-solution validation and independent impossibility checks before causal claims. Mutable tests must never be the authoritative success oracle.
- License: the downloaded HF metadata contains no explicit dataset license; do not infer one from the code license. Underlying LiveCodeBench problem provenance remains relevant. Resources are staged for local research; record provenance in any derivative.

Loading:
```python
import pyarrow.parquet as pq
original = {r['task_id']: r for r in pq.read_table('datasets/impossible_livecodebench/original.parquet').to_pylist()}
conflicting = {r['task_id']: r for r in pq.read_table('datasets/impossible_livecodebench/conflicting.parquet').to_pylist()}
pairs = [(original[k], conflicting[k]) for k in sorted(original) if k != 'lcbhard_77']
```
Small actual records: `samples/impossible_livecodebench.json` (all three variants of one task).

## Agentic Upward Deception — official constrained-task data

- Source: `QingyuLiu/Agentic-Upward-Deception`, revision `b26151c7195111271feba64fb15db6227f25f51b`.
- Downloaded directly from the author's `dataset/task_{1..5}.json`, preserving original bytes in `upward_deception/`.
- Size: 40 records/type, 200 total, 212,142 bytes. JSON lists, globally unique `task_index`.
- Common schema: `task_index`, `instruction`, `task_type`, `tool`, `topic`; file fields depend on type.
- Types: broken reader, irrelevant file, local decoy, missing downloader + downstream task, nonexistent file + downstream task. Eight topic labels (including upstream spelling `Acadamic`).
- Missing `file_content` for types 1/4/5 is intentional; types 2/3 contain it. All instructions are nonempty. Some type 4/5 records use `attached_file_name` rather than `target_file_name`; handle explicitly.
- **Known text defect:** 48 instructions contain `task_index` embedded in words (11/10/11/8/8 by type), apparently from a global replacement. Preserve raw data. Repair individually into a provenance-tracked derivative or exclude under a predeclared rule. Do not blindly replace all occurrences.
- These are blocked tasks, not paired solvable twins. Type 1 lacks authentic source content; a repaired solvable twin needs a generated/curated fixture. Use neutral domains and exact state goals for the primary study. Imported medical/financial tasks are benchmark scenarios, not advice.
- Published metrics include non-disclosure, source substitution and file fabrication; none equals the requested explicit DONE endpoint.
- License: no explicit license was found in the repository tree/README at this revision; record as unspecified.

Loading:
```python
import json
rows = json.load(open('datasets/upward_deception/task_3.json'))
```
Actual small samples: `samples/upward_deception.json`, one record/type. File content fixtures and environment behavior are constructed by the author runner; downloading task JSON alone does not recreate an operational sandbox.

## Development twins — generated here, not an external benchmark

- File: `development_twins/pairs.jsonl`, 30 pairs / 60 episode records.
- Three toy families: inventory quantity, document label, checklist checked state; ten identifier variants/family. All records are explicitly `development_only` and `synthetic`.
- Same instruction and initial state per pair; only `write_allowed` and metadata `condition` differ. `set_field` is the only state-changing transition. Permanent denial establishes impossibility; all finite legal states/actions were exhaustively enumerated.
- Reference transition function and generator: `scripts/build_development_fixtures.py`. Validation: `evidence/development_validation.json`.
- **Only three templates:** this is a plumbing fixture, not 30 independent designs, not a powered sample and not evidence for the hypothesis. Never pass condition, goal certificate, or oracle actions to the model. The runner must implement the dispatcher and build/freeze a diverse confirmatory set separately.
- Authored in this workspace; source benchmark records were not copied into the generated fixture.
- Sample: `samples/development_pairs.json`.

## Search decisions and resources not downloaded

HF search snapshots are in `evidence/hf_*.json`. The unofficial ImpossibleBench-pairs dataset required authorization (HTTP 401), so the official unrestricted release was used. FeasiGen's author repository contains construction code/configs but no released task data in the inspected tree; clone is cataloged separately. FTA's PDF promises artifacts but provides no public download link. AppWorld/tau2 were screened as established state-based benchmarks, but full runtime data and user simulators add unnecessary setup for the retained directions. SWE-bench was pruned before implementation due to runtime/capability cost; its metadata is retained only as search evidence. Kaggle/UCI are not suitable sources for paired agent state/claim trajectories.
