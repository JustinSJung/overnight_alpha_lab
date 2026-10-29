# Training-Only Model Selection Research

RESEARCH_ONLY. Model family is selected inside training; all external scores remain historical development evidence.

## Selection and Timing

Selected family: extra_trees
Fixed families and fixed unweighted ensemble are compared on three purged expanding folds using date-equal raw Brier. No calibration/test scores choose the family.
The matched shallow-HGB anchor uses exactly the same newer train/calibration rows. Do not compare absolute AUC changes to an older differently timed model as a family effect.
The shared return point is an absolute-error conditional-median proxy, not an expected mean. Empirical residual ranges have no coverage guarantee under regime change and dependent outcomes.

| Family | Training-only OOF date Brier |
|---|---:|
| linear | 0.244497 |
| hgb_shallow | 0.243599 |
| hgb_medium | 0.243497 |
| extra_trees | 0.243384 |
| fixed_mean | 0.243478 |
| Past fold-training constant | 0.244928 |

The minimum training-CV score is selection-optimistic, not an independent final validation.

## External Historical Comparison

| Period | Role | Rows | Dates | Pooled AUC | Daily AUC | Date Brier | Known constant Brier | Empirical band coverage | Band width |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| development_audit | anchor | 52002 | 62 | 0.5492850227382226 | 0.5340134197494568 | 0.249874 | 0.250352 | 90.85% | 34.03% |
| development_audit | selected | 52002 | 62 | 0.55328668039751 | 0.5367614551401109 | 0.249627 | 0.250352 | 90.85% | 34.03% |
| short_recent_tail | anchor | 5853 | 7 | 0.5348034318622553 | 0.5141118802862802 | 0.203540 | 0.206523 | 90.66% | 34.03% |
| short_recent_tail | selected | 5853 | 7 | 0.5313025210084035 | 0.510167324231652 | 0.203395 | 0.206523 | 90.66% | 34.03% |

## Fixed Policy

| Period | Role | Cases | Dates | Date-equal success | All-date five-session net proxy | Block lower 95% |
|---|---|---:|---:|---:|---:|---:|
| development_audit | anchor | 0 | 0 | None | 0.0 | 0.0 |
| development_audit | selected | 11 | 8 | 0.6875 | 0.017393780450277868 | -0.00036789379561033385 |
| short_recent_tail | anchor | 0 | 0 | None | 0.0 | None |
| short_recent_tail | selected | 1 | 1 | 0.0 | -0.003750830564784059 | None |

The 60% probability / 0.3% median-proxy policy is unchanged. No-selection dates are zero exposure proxies. These are overlapping close-to-close research outcomes, not executable/compounded strategy returns.

## Paired Selected Minus Matched Anchor

| Period | Date Brier difference | 95% five-session-block interval |
|---|---:|---|
| development_audit | -0.000247 | [-0.0009781958523989787, 0.00028869474604763284] |
| short_recent_tail | -0.000145 | [None, None] |

Primary development screen: False
Reasons: paired_probability_improvement_not_established, weak_cross_sectional_discrimination, insufficient_fixed_policy_cases_or_dates, positive_policy_net_proxy_not_established
Production recommendation gate: False. Original forward ledgers, public model and candidate pool unchanged.

## Fit-Time Audit

Fit as-of: 2026-06-30
Partitions: {'train': {'rows': 616595, 'dates': 744, 'start': '2023-02-01', 'end': '2026-02-20', 'latest_label': '2026-02-27'}, 'calibration': {'rows': 64704, 'dates': 77, 'start': '2026-03-03', 'end': '2026-06-23', 'latest_label': '2026-06-30'}}
Common-cohort excluded rows: 0
Residual bounds use calibration outcomes only. No external test score/label is in the as-of bundle.
The July-September interval has already been inspected in prior research; October is a short diagnostic tail, not adequate new evidence or a selection period.
Current-universe and retrospectively adjusted-price limitations remain.

Protocol SHA256: 50d172aa507471a3fe6f345a89bacf289f44ea733efae879e9426a1193561935
Artifacts (ignored): /Users/justin/Desktop/overnight_alpha_lab/data/models/price_forecaster_selected/runs/20261021T054357Z_4e5d1a7e
