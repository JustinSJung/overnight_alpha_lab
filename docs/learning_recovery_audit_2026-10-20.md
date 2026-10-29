# Learning recovery audit - 2026-10-20

Source: origin/main at 51e4efa9337f6ffb84c09695c8438f19ba7f364e.
Local experimental branch: fix/avoid-lr-model (23bc20c before this audit).

## Current operating state

The October 20 Pipeline run (39351468461) and Pages deployment
(39355392536) completed successfully. The live dashboard reports an October 20
update; the October 8 screenshot is an older output.

| Metric | Value |
|---|---:|
| Unique predictions | 29,191 |
| Evaluated predictions | 13,306 |
| Overall directional accuracy | 48.32% |
| Wilson lower bound shown as reliability | 47.5 / 100 |
| Buy evaluated predictions | 1,826 |
| Buy directional accuracy | 41.57% |
| Buy mean next-close return | -0.2920% |
| Avoid evaluated predictions | 11,480 |
| Avoid directional accuracy | 49.40% |
| Avoid mean underlying next-close return | -0.0411% |

The Wilson lower bound converges toward observed accuracy as the sample grows.
Additional observations alone cannot turn a roughly 48% hit rate into a 65%
reliability score. The published number is a statistical lower bound on a mixed
directional hit rate, not a calibrated probability for the next recommendation.

## Confirmed diagnostic defect and correction

The October 20 price signal diagnostics reported 318,560 evaluated rows, while
the public dashboard reported 13,306 independent evaluated predictions. The
diagnostics loaded all historical evaluation snapshots without deduplicating
them, then ranked repeated snapshots as if they were independent candidates.

The diagnostics now use src/evaluation/metrics.py::dedupe_evaluations before
counting outcomes or assigning daily ranks. The same shared result normalizer
is used as in the dashboard. Candidate snapshots are also deduplicated before
ranking. Pending candidates still occupy their daily rank slots.

Regression tests verify that repeated snapshots do not increase evaluated
counts or move additional candidates into daily Top 10 buckets, and that
latest resolved snapshots and normalized result strings are handled correctly.

## Existing AVOID model: later-period validation

The local logistic model was trained on September 30. It is diagnostic only
and is absent from origin/main: it does not update production ranking or the
public reliability score. Production price candidate scoring still uses fixed
v2 weights; learned price-candidate rule reports do not train those weights.

The fixed local model was evaluated on October signal dates strictly after
September 30. Features were recovered from the earliest available candidate
snapshot per stable prediction identity. Predictions were retained only when
that snapshot existed on or before the signal date. Latest deduplicated
evaluation outcomes and stored initial direction were used as labels.
No coefficients or thresholds were fitted using this later period.

| Later-period AVOID metric | Value |
|---|---:|
| Eligible evaluated predictions | 4,284 |
| Distinct signal dates | 10 |
| Eligible pool accuracy | 53.15% |
| Fixed-model ROC AUC | 0.5813 |
| Daily model Top 10%: count / accuracy | 431 / 54.76% |
| Daily model Top 20%: count / accuracy | 861 / 54.36% |
| Daily model Top 30%: count / accuracy | 1,289 / 55.55% |

Daily percentage buckets use ceil(day_count * fraction) separately for each
signal date, then aggregate outcomes. They contain the same eligible feature
population as the baseline, rather than a different historical population.
Avoid accuracy counts falling underlying prices as successful; underlying
returns in the first table are not short-trade returns or trading P&L.

This is limited evidence from ten dates, not proof of a durable selection edge.
Correlated stocks on the same date are not independent experiments. Keep this
model experimental and evaluate additional future dates before promotion.
Buy-side quality needs its own time-separated investigation; an avoid-only
model cannot resolve the buy hit rate of 41.57%.

## Scope

The correction changes diagnostic aggregation. It does not modify candidate
generation, scoring weights, trade/order behavior, or the reliability formula.
No production deployment or branch merge was performed during this audit.
