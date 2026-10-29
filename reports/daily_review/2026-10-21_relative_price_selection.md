# Relative Price Selection Research

RESEARCH_ONLY. Retrospective development experiment, not a new untouched test or a buy recommendation.

## Meaning and Coverage

Relative probability means beating the equal-weight input-eligible candidate universe over five quote sessions. It is NOT the chance of a profitable purchase and the universe is NOT KOSPI/KOSDAQ.
The reference includes the candidate itself. Identical assumed costs cancel in relative comparisons; absolute net proxies still subtract 0.3%.
Eligibility uses signal-close inputs only. Entire dates with missing constituent outcomes are excluded, never just unresolved stocks. This complete-date filter and the current-universe/retrospectively adjusted-history selection bias remain limitations.
Evaluation coverage: 166/166 dates; 141304 rows.
All portfolio rates/returns below give each signal date equal weight. Top20 is primary; Top10 is secondary. Ranking has no probability cutoff and is NOT an activated recommendation policy.

## Selection Results

| Group | Dates | Cases | Absolute success | Beats universe | Five-session net proxy | Excess vs universe |
|---|---:|---:|---:|---:|---:|---:|
| pool | 166 | 141304 | 42.000% | 41.048% | -0.456% | 0.000% |
| relative_top20 | 166 | 3320 | 41.295% | 42.952% | -0.646% | -0.190% |
| absolute_top20 | 166 | 3320 | 42.410% | 41.536% | -0.636% | -0.179% |
| momentum_top20 | 166 | 3320 | 40.994% | 41.717% | 0.331% | 0.787% |
| relative_top10 | 166 | 1660 | 40.964% | 43.675% | -0.761% | -0.305% |
| absolute_top10 | 166 | 1660 | 41.687% | 41.325% | -0.824% | -0.367% |
| momentum_top10 | 166 | 1660 | 41.084% | 42.108% | 0.941% | 1.398% |
| random_top20 | 166 | 3320 | 41.991% | 41.069% | -0.433% | 0.024% |
| random_top10 | 166 | 1660 | 41.877% | 41.033% | -0.458% | -0.001% |

Random is the mean of 100 pre-fixed, independent deterministic random selections (not the best seed). Portfolio outcomes overlap in time; they are not compounded or executable next-open P&L.

## Primary Top20 Paired Comparisons

| Reference | Relative model minus reference return | Simultaneous family-95% interval |
|---|---:|---|
| pool | -0.190% | [-1.160%, 0.739%] |
| absolute_top20 | -0.010% | [-0.803%, 0.728%] |
| momentum_top20 | -0.977% | [-3.638%, 1.388%] |
| random_top20 | -0.213% | [-1.168%, 0.709%] |

Paired circular blocks of five observed signal dates; 5,000 resamples, seed 42. Four comparisons use Bonferroni-adjusted intervals. These are approximate development diagnostics after earlier inspection of the same dates, not new independent evidence.
Top20 absolute net-proxy interval: {'mean': -0.00645946893721741, 'lower': -0.020733187390754287, 'upper': 0.006930477219442654}
Development screen passed: False
Screen reasons: no_clear_advantage_vs_pool, no_clear_advantage_vs_absolute_top20, no_clear_advantage_vs_momentum_top20, no_clear_advantage_vs_random_top20, absolute_net_proxy_lower_bound_not_positive
Production recommendation gate: False (prospective validation is always required).

## Probability Diagnostics

| Model | Date Brier | Known past-constant Brier | Mean daily AUC | Sigmoid slope |
|---|---:|---:|---:|---:|
| relative | 0.241868 | 0.242015 | 0.5190165364942597 | 1.136067 |
| absolute_control | 0.244258 | 0.243851 | 0.5211655879174214 | 0.767534 |

The two Brier scores concern different targets; do not compare their numeric levels to claim one model is more reliable. Relative and absolute classifiers share inputs, dates, sample weights and fixed model settings.

## Monthly Primary Results

| Month | Dates | Relative Top20 excess | Absolute-control Top20 excess | Momentum Top20 excess | Random Top20 excess | Relative Top20 net proxy |
|---|---:|---:|---:|---:|---:|---:|
| 2025-10 | 10 | 0.028% | -0.420% | 0.494% | 0.045% | -0.906% |
| 2025-11 | 20 | -0.122% | 0.212% | -2.797% | -0.039% | -0.071% |
| 2025-12 | 21 | -2.406% | -1.392% | 5.449% | 0.021% | -2.289% |
| 2026-01 | 21 | 0.702% | 2.811% | -0.859% | -0.017% | 2.797% |
| 2026-02 | 17 | -2.769% | -4.270% | 0.255% | -0.039% | -4.212% |
| 2026-03 | 21 | 0.472% | -0.764% | 4.727% | 0.079% | 1.338% |
| 2026-04 | 22 | -0.757% | 0.058% | -0.639% | 0.038% | 1.628% |
| 2026-05 | 18 | 1.451% | -0.094% | 0.864% | 0.035% | -4.218% |
| 2026-06 | 16 | 2.133% | 1.838% | -1.237% | 0.106% | -1.487% |

## Temporal Audit

Fit as-of: 2025-10-17

| Partition | Rows | Dates | Signal start | Signal end | Latest cross-sectional label |
|---|---:|---:|---|---|---|
| train | 398764 | 490 | 2023-02-01 | 2025-02-05 | 2025-02-12 |
| calibration | 137002 | 160 | 2025-02-13 | 2025-10-10 | 2025-10-17 |
| test | 141304 | 166 | 2025-10-20 | 2026-06-23 | 2026-06-30 |

No future test outcomes/scores are attached to the serialized as-of model. Experimental relative bundles have a separate schema and cannot replace an absolute forecast bundle.
No candidate generation, legacy evaluation, dashboard, default model, frozen forward ledger, or deployment was changed.

Protocol SHA256: 658701b6db02c5158ae36ec91fd222d270e7de198e5c71d322a70e8c639899b6
Dataset SHA256: b719c4a35e8b90ce7f4c9409263c9473275aadc313871738cc227126c8dd1007
Artifacts (ignored by Git): /Users/justin/Desktop/overnight_alpha_lab/data/models/price_relative_selection/20261021T043216Z_abe350aa
