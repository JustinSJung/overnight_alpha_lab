# OHLCV Information Learning Experiment

RESEARCH_ONLY. New historical inputs, not a confidence-score adjustment or deployment.

Both arms share the original absolute five-session >0.3% target, rows, purged fitting dates, date weights, fixed HGB settings and 60%/0.3% policy.
Extra features use only same-close or trailing OHLCV. Volume times adjusted close is a liquidity proxy, not actual traded value. Inactive zero-volume bars contribute neutral gap/range, never an invented future quote.
The later chronological audit was predeclared as primary. It is historical development evidence, not claimed an untouched final test. Current-universe, adjustment and survivorship limitations remain.

| Period | Model | Rows | Dates | Pooled AUC | Mean daily AUC | Date Brier | Past constant Brier |
|---|---|---:|---:|---:|---:|---:|---:|
| earlier_development | baseline | 141304 | 166 | 0.5158240678501571 | 0.5215895417685417 | 0.244220 | 0.243851 |
| earlier_development | enriched | 141304 | 166 | 0.5284780384103298 | 0.5336722301138831 | 0.244036 | 0.243851 |
| later_chronological_audit | baseline | 52002 | 62 | 0.543055923488925 | 0.5243732241278157 | 0.245680 | 0.247899 |
| later_chronological_audit | enriched | 52002 | 62 | 0.5530950825299037 | 0.5344885725666823 | 0.244968 | 0.247899 |

## Fixed Policy (Date-Equal)

| Period | Model | Selected rows | Selected dates | Date-equal success | All-date five-session net proxy | Block lower 95% |
|---|---|---:|---:|---:|---:|---:|
| earlier_development | baseline | 1044 | 104 | 47.250% | -0.098% | -1.497% |
| earlier_development | enriched | 1468 | 139 | 45.367% | 1.204% | -1.366% |
| later_chronological_audit | baseline | 156 | 39 | 53.573% | -0.453% | -4.688% |
| later_chronological_audit | enriched | 377 | 56 | 51.410% | 1.761% | -2.926% |

Zero-selection dates are zero exposure proxies, not failed predictions. Overlapping close-to-close return proxies are not executable or compounded strategy returns.

## Paired Enriched Minus Baseline Date Brier

| Period | Difference | Five-session-block 95% interval |
|---|---:|---|
| earlier_development | -0.000184 | [-0.0005390005930546949, 0.00018998821219854943] |
| later_chronological_audit | -0.000711 | [-0.0014596413989841608, -8.784657082439e-06] |

Negative differences favor enriched inputs. Paired circular blocks: 5,000 resamples, seed 42; approximate development diagnostics, not independent guarantees.

Primary development screen: False
Reasons: weak_cross_sectional_discrimination, positive_policy_net_proxy_not_established
Production promotion: False. Separate actual future validation is still required even if development passes.

## Fit-Time Audit

Fit as-of: 2025-10-17
Train: {'rows': 398764, 'dates': 490, 'start': '2023-02-01', 'end': '2025-02-05', 'latest_label': '2025-02-12'}
Calibration: {'rows': 137002, 'dates': 160, 'start': '2025-02-13', 'end': '2025-10-10', 'latest_label': '2025-10-17'}
Common-cohort excluded rows: 0
Model bundles contain only fitting-period metadata, no later outcomes or scores.

Dataset SHA256: 5c80f09881bf52d08d05a88f8b0af903bc1671c7d4a7e63ab7ac948b5d19dac2
Protocol SHA256: 97622765b3c70a26753bf8ac49fb29864b79ed58d33ff1ddb2bfea2b0d0c14bf
Artifacts (ignored): /Users/justin/Desktop/overnight_alpha_lab/data/models/price_forecaster_ohlcv/20261021T051534Z_3b0bbeb4

No scoring formula, candidate pool, deployed/default model, or original forward ledger was changed.
