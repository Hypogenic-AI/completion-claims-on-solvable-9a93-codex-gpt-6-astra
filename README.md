# Completion claims on solvable and impossible tasks

A custom paired audit of Qwen3-8B and DeepSeek-R1-Distill-Llama-8B on benign fictional records. It separates explicit unsupported completion claims from execution, parser inability and honest blocker recognition. This is not an official benchmark score.

- Collection: 2400/2400 held-out episodes.
- Primary DeepSeek contrast: -0.0033 (SE 0.0067); 95% CI [-0.0167, 0.0100]; n=200/200 items.
- Candidate criterion: not met.
- Scorer fixtures: 80/80 exact agreement; no LLM judge.
- A tokenizer compatibility repair required a recorded preregistration amendment; invalid tokenizer outputs are excluded.
- See [REPORT.md](REPORT.md) for all rates, denominators, uncertainty, missingness and limitations.

## Reproduce

Use `uv sync --project .` and activate `.venv`. With the saved transcripts, run `python src/analyze.py`, `python src/report.py`, and `python src/validate_results.py`. Full GPU collection commands are in REPORT.md; use a fresh checkout to avoid replacing recorded results.

## Files

- `src/`: generator, parser/state scorer, Inspect collection, server lifecycle, analysis and validation.
- `datasets/custom/items.json`: frozen development/held-out base scenarios.
- `results/transcripts/`: full model outputs, errors and final states.
- `results/analysis/`, `results/safety/`: paired statistics and standard result records.
- `results/manifests/`, `results/fixtures/`: exact hashes and scorer checks.
- `preregistration.md`, `planning.md`, `resources.md`: design and evidence.
