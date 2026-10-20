# Reproduction and code map

Use only the workspace `.venv` (`uv sync --project .`). No shared research interpreter is used. All commands run from this workspace root.

- `src/protocol.py`: seeded fictional-record generator, closed state dispatcher, strict final-action parser, exact claim/state scorer, and oracle policy. Source availability and write permissions are environment interventions; requests are identical within each pair.
- `src/prepare.py`: creates the 20 development and 200 held-out items, 80 programmatically labelled scorer fixtures, constant-policy baselines and impossibility checks. Labels are not human calibration.
- `src/validate_protocol.py`: independently specified parser edge cases, including incomplete reasoning and conflicting JSON.
- `src/collect.py`: builds the Inspect dataset and solver, renders native model chat templates to flat integer token IDs, calls the real local vLLM completion API, dispatches actions, and writes complete per-episode transcripts. Inspect's unused mock transport does not generate subject responses.
- `src/evals/impossible_task_honesty.py`: registered Inspect task entrypoint for the same custom solver.
- `src/server.py`: starts one vLLM server on the allocated GPU, waits for readiness, runs requested collections sequentially, and stops only its own process group. It waits for stable free GPU memory rather than interfering with another job.
- `src/freeze.py`: hashes source, items, labelled fixtures, dependency lock, native templates, and exact model weights/revisions. Existing freezes are verified rather than silently replaced.
- `src/refreeze.py`: archives a superseded manifest and records a pre-evaluation amendment. It refuses to run after any held-out transcript exists.
- `src/analyze.py`: averages seeds within items, computes paired item-bootstrap intervals, exact seed-11 boundary bounds, missing-data bounds, capability-conditioned sensitivity and secondary checkpoint differences.
- `src/report.py`: converts actual Inspect logs with the safety-evals skill script, adds the item-cluster statistics, and generates REPORT.md and README.md from saved results.
- `src/validate_results.py`: replays every saved action against a fresh environment, re-parses raw text, verifies state/claim outcomes, checks schemas and denominators, and repeats analysis to test byte-identical statistics.

The full collection commands and final collection status are in REPORT.md. For analysis-only reproduction, run `.venv/bin/python src/analyze.py`, `.venv/bin/python src/report.py`, then `.venv/bin/python src/validate_results.py`; these commands do not query subject models or judges. Full reruns should use a fresh checkout/output directory to preserve the original frozen run.

The source-provenance barrier is deliberate: guessing a hidden value would otherwise make a missing-source task accidentally completable. Both twins state the same source-read rule, and the dispatcher enforces it. Revoked-write twins additionally deny all output writes. Neither error can be bypassed through another tool.

Output files contain arbitrary model-generated text as data only. The dispatcher never executes it as code. All records and values are fictional and benign.
