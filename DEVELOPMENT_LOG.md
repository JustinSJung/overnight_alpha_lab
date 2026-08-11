# Development Log

Running log of notable engineering changes to the price-candidate evaluation
and reporting layer. See `MEMORY.md` for a condensed reference of standing
decisions; this file is the chronological narrative.

## 2026-08-11 — Directional reporting, dedup unification, shared evaluation utils

Three related data-quality issues were found and fixed in the price-candidate
evaluation reporting pipeline, across four branches (`feature/directional-reporting`,
`fix/unify-dedup`, `fix/shared-evaluation-utils`, all merged to `main`).

### 1. Buy/avoid directional reporting

The dashboard, diagnostics page, `v2_performance_monitor.py`, and
`evaluation_integrity_audit.py` only ever reported one blended success rate
per candidate pool. Splitting by `expected_positive()` (BUY_CANDIDATE/WATCHLIST
vs AVOID) showed the two behave very differently: buy-type candidates
(11% of volume) outperform avoid-type candidates (89% of volume) by a wide
margin, and that signal was being averaged away. Added `candidate_direction`
to the evaluation schema and buy/avoid breakdowns everywhere the blended rate
was shown; the blended number is kept as a labeled reference metric, not
removed. Added `directional_penalty_diagnostics.py` (penalty bucket x
momentum tertile x direction cross tabs) as a new daily pipeline step.

### 2. Dedup key mismatch inflated v2 evaluated-case counts up to 6.5x

`evaluation_integrity_audit.py` computed a correct candidate-level dedup key
but never applied it before computing performance metrics (only used it for
duplicate-count diagnostics). `v2_performance_monitor.py` did dedupe, but its
key included `evaluation_date`, so the same candidate re-evaluated on a later
calendar day (once t3/t5 returns became available) was kept as a separate
row instead of being collapsed. Result: the two scripts reported ~13,345 vs
~1,606 "v2 evaluated cases" for the same underlying data. Fixed by having
both use the same candidate-level key (`candidate_id`, else
`stock_code+signal_date+prediction_date+score_version`, `evaluation_date`
excluded from the key and used only to pick the latest row via sort order).
Both scripts now report exactly 1,606.

### 3. Top10/20/50/100 rank buckets used two different candidate pools

Even after the dedup fix, Top50 success rate was 46.29% in
`evaluation_integrity_audit.py` vs 58.21% in `v2_performance_monitor.py` on
the same data. Root cause: `evaluation_integrity_audit.py` ranked only within
already-evaluated candidates for the day; `v2_performance_monitor.py` ranked
the full candidate pool for the day (pending + evaluated + skipped) and only
filtered to evaluated rows afterward. Ranking within evaluated-only rows is a
survivorship bias -- it silently drops still-pending top scorers from
competing for a Top-N slot, which lets lower-ranked but already-resolved
candidates take their place. Decided to standardize on the full-pool
approach (reflects what you would have actually picked at signal time).
Both scripts now report byte-identical Top10/20/50/100 success rates.

### Refactor: src/evaluation/metrics.py as the shared source of truth

All three fixes above were, at root, the same handful of functions
(`candidate_key_series`, `dedupe_evaluations`, `success_series`,
`direction_series`, `assign_daily_rank`, rank-bucket assignment) having
drifted into 4-5 slightly different local reimplementations across
`price_candidate_rule_learner.py`, `dashboard_generator.py`,
`evaluation_integrity_audit.py`, `v2_performance_monitor.py`, and
`directional_penalty_diagnostics.py`. Consolidated all of them into
`src/evaluation/metrics.py` and had all five scripts import from there,
deleting the local copies. Verified via full before/after run of all five
scripts that this was behavior-preserving except for the two intentional
fixes above (dedup key, rank pool).

### Verification

- Local dev venv is Python 3.9, which can't run this codebase's `X | None`
  type-hint syntax (needs 3.10+). Used a scratch venv (Python 3.13 +
  `pandas==2.3.3`, matching `requirements.txt`'s pin) for iterative
  development, then re-verified all 5 scripts end-to-end in a
  `python:3.11-slim` Docker container with `pip install -r requirements.txt`
  exactly as `pipeline.yml` does, before merging to `main`. All 5 exited 0
  with numbers matching the scratch-venv runs.
- Also manually triggered the real `pipeline.yml` GitHub Actions workflow
  (`workflow_dispatch`) post-merge to confirm the full daily pipeline still
  succeeds end-to-end with these changes live: **success**
  (run [31461831275](https://github.com/JustinSJung/overnight_alpha_lab/actions/runs/31461831275),
  Python 3.11.15, all 25 steps green, auto-committed as `9bb06d9`). See
  `MEMORY.md` for the post-run number cross-check.

v2 scoring weights and penalty formulas were not touched in any of this
work; no v4/v5 ranker or ML model was introduced.
