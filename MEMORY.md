# Memory

Condensed reference of standing decisions in the price-candidate evaluation
pipeline. See `DEVELOPMENT_LOG.md` for the narrative/dates. Update this file
in place when a decision changes; don't let it grow into a chronological log
(that's what `DEVELOPMENT_LOG.md` is for).

## Dedup key: candidate-level, no `evaluation_date`

**What**: `evaluation_integrity_audit.py` and `v2_performance_monitor.py`
independently reported "v2 evaluated cases" that differed by up to 6.5x
(~13,345 vs ~1,606) on the same underlying data.

**Why**: `evaluation_integrity_audit.py` computed a correct candidate-level
dedup key (`candidate_id`, else
`stock_code+signal_date+prediction_date+score_version`) but only used it to
report a duplicate-count diagnostic -- it never actually deduplicated the
frame before computing performance metrics. `v2_performance_monitor.py` did
dedupe, but its key also included `evaluation_date`, so a candidate
re-evaluated on a later calendar day (e.g. once t3/t5 returns became
available) counted as a second "unique" row instead of collapsing into the
first.

**Fixed**: Both scripts now use the same key via
`src/evaluation/metrics.py::candidate_key_series()` /
`dedupe_evaluations()`. `evaluation_date` is excluded from the identity key
and used only as a sort column (oldest first, `keep="last"`) so the most
complete evaluation snapshot per candidate wins.

**Agreed number** (2026-08-11 snapshot, grows daily): **1,606** v2-scored
evaluated cases, reported identically by both scripts.

## Success rate must be reported by direction (buy vs avoid), not blended

**What**: Every success-rate metric on the dashboard, diagnostics page, and
in `v2_performance_monitor.py` / `evaluation_integrity_audit.py` was a single
number blending two populations that behave oppositely.

**Why it matters**: `candidate_direction` ("buy" for BUY_CANDIDATE/WATCHLIST,
"avoid" for AVOID, from `expected_positive()`) splits the pool roughly
11% buy / 89% avoid by volume, and buy-type candidates meaningfully
outperform avoid-type on the same underlying data (v2, 2026-08-11 snapshot:
buy 58.29% vs avoid 38.48%). A blended rate mostly reflects the avoid-type
majority and hides the buy-type signal.

**Convention going forward**: Report buy and avoid separately wherever a
success rate is shown. The blended rate may still be shown as a labeled
"reference / all" metric, never as the only number. Direction is computed
via `src/evaluation/metrics.py::direction_series()` /
`direction_success_summary()`, backed by the `candidate_direction` column
saved at evaluation time (falls back to a row-wise recompute for older CSVs
that predate the column).

## Top10/20/50/100 rank buckets: rank the full candidate pool, not evaluated-only

**What**: Even after the dedup fix above, the two scripts' Top-N success
rates diverged sharply on identical data (Top50: 46.29% vs 58.21%, a 12pp
gap).

**Why**: `evaluation_integrity_audit.py` ranked candidates only within the
subset that already had a resolved success/failure outcome for the day.
`v2_performance_monitor.py` ranked the full candidate pool issued that day
(pending + evaluated + skipped), then filtered the resulting Top-N slot
occupants down to whichever had since resolved.

**Decision**: Standardized on the full-pool approach
(`src/evaluation/metrics.py::assign_daily_rank()` /
`rank_bucket_rows()`). Reasoning: ranking only within already-evaluated rows
introduces a survivorship bias -- which candidates happen to have resolved
fastest is not independent of the outcome, and evaluated-only ranking
silently lets a still-pending top scorer get crowded out of a Top-N slot by
a lower-ranked candidate that simply resolved sooner. Full-pool ranking
reflects what you would have actually picked at signal time, before any
outcome was known; the success rate is then reported only over whichever
Top-N members have since resolved (still-pending ones are excluded from the
rate, not from the ranking).

Both scripts now report byte-identical Top10/20/50/100 success rates
(2026-08-11 snapshot: 59.81% / 58.39% / 58.21% / 49.20%).

## Verification environment

Local `.venv` is Python 3.9 and cannot run this codebase (needs 3.10+ for
`X | None` type hints). For quick iteration, a scratch venv with Python 3.13
+ `pandas==2.3.3` (matching `requirements.txt`'s pin) works. Before merging
anything that touches the report-generation scripts, re-verify in a
`python:3.11-slim` Docker container with `pip install -r requirements.txt`
run verbatim -- this matches `pipeline.yml`'s `actions/setup-python@v5`
step exactly and has caught nothing different from the scratch venv so far,
but is the closer match to CI.

## Latest full-pipeline CI verification

- Workflow: `pipeline.yml`, triggered manually via `gh workflow run` after
  merging `fix/shared-evaluation-utils` to confirm the real GitHub Actions
  environment (not just local Docker) succeeds end-to-end.
- Run: https://github.com/JustinSJung/overnight_alpha_lab/actions/runs/31461831275
  -- **success**, Python 3.11.15 (matches `pipeline.yml`'s pin), all 25
  pipeline steps including the 5 scripts touched by this work
  (`evaluation_integrity_audit.py`, `price_candidate_rule_learner.py`,
  `directional_penalty_diagnostics.py`, `v2_performance_monitor.py`,
  `dashboard_generator.py`) completed without error, and the workflow's
  own commit-and-push step landed cleanly on `main` as commit `9bb06d9`.
- With that run's fresh 2026-08-11 data, `evaluation_integrity_audit.py`
  and `v2_performance_monitor.py` report identical Top10/20/50/100 success
  rates: 58.12% / 56.21% / 54.18% / 48.06% (grows/shifts daily as more
  candidates get evaluated -- the 2026-08-11 snapshot numbers earlier in
  this file, 59.81/58.39/58.21/49.20, are from a few hours earlier the same
  day, before this CI run added ~4,200 new evaluation rows).
