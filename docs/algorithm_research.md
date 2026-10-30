# Offline Algorithm Research / 알고리즘 연구실

## Scope

This is a separate research layer, not a new high-confidence production model.
It synthesizes small numerical feature programs, trains established scikit-learn
estimators, compares them on matched purged chronological development folds,
and remembers results before selecting the next parent program.

The user chose **no paid API calls**. There is no LLM connection, free-form Python
generation, autonomous general reasoning, LLM fine-tuning or promise that this
system gets smarter merely with time. Memory guides bounded numerical program
search; measured development progress is not proof of future accuracy or novelty.

## Research Loop

1. Reuse completed, checksum-verified KIS history; do not make new API requests.
2. Validate the fixed policy, implementation hashes and full research memory.
3. Reserve the snapshot and trial before computing any score.
4. Propose a numerical program from scratch or mutate a ranked previous program.
5. Fit/calibrate on earlier mature outcomes; compare on three later 20-session
   development periods against the same-period HGB control and past constant.
6. Record both successes and failures. Reuse the memory in the next cycle.

The original 19 completed-price features remain available to every model. New
programs can add at most four outputs from eight bounded numerical operations.
They can combine features nonlinearly; this is more than choosing a model name
or learning rate, but it is not unrestricted architecture or loss-function search.
The current proposal engine does not read natural-language papers or invent
natural-language hypotheses. A validated program JSON can be imported later.

## Data and Evaluation

The next-open to fifth-session-close target, 0.3% assumed cost, 60% probability
threshold and five-per-day monitoring cap are unchanged. All input-eligible
stocks remain in each development period. Missing outcomes are counted, not
removed before selection or replaced with successful stocks. No-outcome dates
remain in comparisons if their five-session outcome window has elapsed.

Training uses 252 signal sessions, calibration 60, with label-availability purging
at each boundary. Each candidate has its own training/calibration fit; its control
has exactly the same dates and rows. Date-equal Brier error is the development
search objective. Selected success/return summaries are conditional diagnostics,
not a backtested executable portfolio. The matched control is a research HGB,
not an assertion that the current production model has been beaten.

All historical periods have been reused for research. They are **development
data**, not an untouched final holdout. Selecting the best of many scores can
overfit these periods. No confidence interval from this adaptive search is used
to claim high confidence. A promising candidate needs a separately reviewed
prospective registration and search/multiple-comparison accounting. It is NOT
added to the existing registered eight-family competition or its evidence budget.

## Safety and Budgets

- Numerical programs are interpreted as JSON data; no `eval`, `exec`, imports,
  attribute access, arbitrary Python, file access or network operations exist in
  their language. This is not an OS sandbox for running untrusted Python.
- Worker processes receive no inherited KIS, LLM, GitHub or other API secrets.
  They execute trusted repository code only, with two numerical threads,
  a 300-second wall timeout, 240-second CPU budget and 6 GiB Linux address-space
  limit. These limits may stop an experiment rather than lowering evaluation rules.
- Two trials per completed-price snapshot, 120 trials total. Failed, timed-out
  and reserved-but-interrupted attempts consume the budget. Rerunning a snapshot
  never creates fresh trials or silently retries failures.
- Each proposal is recorded before evaluation. Small hash-linked events plus a
  separate head anchor detect corruption, missing events and truncated tails.
  Git preserves published records. These are not externally attested timestamps
  or protection against a person deliberately rewriting the whole Git history.
- Source or input revisions require review; do not delete memory to reset results.
- No production estimator, existing goal file, confidence formula, original
  prediction, recommendation flag, candidate pool or order endpoint is changed.

## Operation

```bash
bash scripts/price_model.sh research-algorithms --data-root data/ml_history/kis_updated_20261028
bash scripts/price_model.sh research-algorithms context
bash scripts/price_model.sh research-algorithms --data-root PATH --proposal program.json
```

Without `--data-root`, the latest completed snapshot from the disposable ML Beta
cache is used. If no snapshot exists, the system reports waiting for data; it
does not fabricate results or fetch data using hidden credentials.

The Algorithm Research workflow follows successful main-branch ML Beta runs.
It checks out trusted latest main, reads the existing price cache, runs the fixed
tests and research, and publishes only small event JSON, a status/report and HTML.
It does not save research estimators to the ML Beta cache. Research failure does
not block the already completed production refresh; failed publication retains
the experiment originals in a 90-day artifact for careful recovery.

The public dashboard separates completed evaluations, execution errors,
interrupted attempts and development-screen passes. A completed evaluation is
not a successful algorithm: a worse-than-control result is retained too. It explicitly
states that the LLM is disconnected and research is not applied to production.
Full development details remain in `reports/daily_review/algorithm_research_report.md`
and the research memory. The dashboard does not raise its reliability score to
reflect the number of experiments or the best historical result.

Connecting an LLM later requires an explicit model/provider and cost budget,
an approved restricted proposal interface and reviewed protocol migration.
It must not be treated as already enabled by this offline implementation.
