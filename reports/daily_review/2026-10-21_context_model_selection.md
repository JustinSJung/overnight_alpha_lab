# OHLCV + Market Context Model Selection

RESEARCH_ONLY. No production promotion. All external periods are previously inspected historical development data.

## Training-Only Selection

Chosen input: ohlcv_19
Chosen family: extra_trees
Three purged expanding folds select the input/family. Calibration and external scores do not choose them.
Market inputs describe the observed current universe, not KOSPI/KOSDAQ or an investable index.

| Input | Family | Training-only date Brier |
|---|---|---:|
| ohlcv_19 | linear | 0.244497 |
| ohlcv_19 | hgb_shallow | 0.243599 |
| ohlcv_19 | hgb_medium | 0.243497 |
| ohlcv_19 | extra_trees | 0.243384 |
| ohlcv_19 | fixed_mean | 0.243478 |
| ohlcv_market_29 | linear | 0.246144 |
| ohlcv_market_29 | hgb_shallow | 0.249620 |
| ohlcv_market_29 | hgb_medium | 0.251818 |
| ohlcv_market_29 | extra_trees | 0.247128 |
| ohlcv_market_29 | fixed_mean | 0.247060 |

## Identical-Row Historical Evaluation

| Period | Input | Rows | Dates | AUC | Daily AUC | Date Brier | Constant Brier | Policy cases | Policy dates |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| development_audit | ohlcv_19 | 52002 | 62 | 0.55328668039751 | 0.5367614551401109 | 0.249627 | 0.250352 | 11 | 8 |
| development_audit | ohlcv_market_29 | 52002 | 62 | 0.5364282332404648 | 0.5170612715415077 | 0.252745 | 0.250352 | 63 | 4 |
| short_recent_tail | ohlcv_19 | 5853 | 7 | 0.5313025210084035 | 0.510167324231652 | 0.203395 | 0.206523 | 1 | 1 |
| short_recent_tail | ohlcv_market_29 | 5853 | 7 | 0.5842187224540166 | 0.44851546673736 | 0.184580 | 0.206523 | 0 | 0 |

## Context Minus OHLCV

| Period | Date Brier difference | 95% five-date-block interval |
|---|---:|---|
| development_audit | 0.003118 | [-0.00979387048337137, 0.012760592483103949] |
| short_recent_tail | -0.018816 | [None, None] |

## Fixed Policy and Empirical Range

| Period | Input | All-date net return proxy | Block lower 95% | Range coverage | Range width |
|---|---|---:|---:|---:|---:|
| development_audit | ohlcv_19 | 0.017393780450277868 | -0.00036789379561033385 | 90.85% | 34.03% |
| development_audit | ohlcv_market_29 | 0.010245924707035555 | -0.0022015565080081216 | 90.99% | 35.04% |
| short_recent_tail | ohlcv_19 | -0.003750830564784059 | None | 90.66% | 34.03% |
| short_recent_tail | ohlcv_market_29 | 0.0 | None | 93.55% | 35.04% |

Fixed policy remains p >= 0.60 AND median return proxy > 0.003. No-selection days are zero exposure.
Overlapping close-to-close outcomes are not executable strategy or compounded returns. Empirical ranges have no coverage guarantee.

Development screen: False
Reasons: paired_probability_improvement_not_established, does_not_beat_known_constant_probability, weak_cross_sectional_discrimination, insufficient_fixed_policy_cases_or_dates, positive_policy_net_proxy_not_established, context_not_selected_inside_training
Recommendation gate: False, including when the training-selected input is OHLCV only.

## Audit

Fit as-of: 2026-06-30
Partitions: {'train': {'rows': 616595, 'dates': 744, 'start': '2023-02-01', 'end': '2026-02-20', 'latest_label': '2026-02-27'}, 'calibration': {'rows': 64704, 'dates': 77, 'start': '2026-03-03', 'end': '2026-06-23', 'latest_label': '2026-06-30'}}
Common finite-29-feature cohort exclusions: 0
Both arms use the same rows, label definition, dates, weights and calibration method.
Each regressor uses its own feature set; it is a conditional-median proxy, not an expected mean.
Current-universe, adjustment and repeated historical research limitations remain. No independent prospective result is claimed.
Protocol SHA256: 9c9c3e5c07149d86c38e3f09e08599a9f9dc1d9325985e70eb10ab66d28acf2f
Ignored artifacts: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_forecaster_context_selected/runs/20261021T055001Z_6b053112
