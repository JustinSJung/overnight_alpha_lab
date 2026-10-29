# Learned-Rule Daily Candidate Report - 2026-10-19

## Purpose

This report applies learned event-rule score adjustments to the daily candidate scoring formula.

The current v4 score formula is:

```text
base_event_score
+ market_adjusted_score_adjustment
+ trading_volume_score_adjustment
+ learned_event_score_adjustment
= final_learned_rule_score
```

This report is for research and portfolio demonstration purposes only. It is not investment advice.

## Summary

- Total candidate rows: **1913**
- Rows with active learned-rule adjustment: **1887**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 1690 |
| general_review | 203 |
| watchlist_candidate | 20 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 025560 | 미래산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 025560 | 미래산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 089790 | 제이티 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 189330 | 씨이랩 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 215090 | 솔디펜스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 028100 | 동아지질 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 047040 | 대우건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 0203K0 | 송우인포텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 004800 | 효성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 000640 | 동아제약 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 222420 | 쎄노텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 475230 | 엔알비 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 215090 | 솔디펜스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 215090 | 솔디펜스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 215090 | 솔디펜스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 019660 | 글로본 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 348350 | 위드텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 025560 | 미래산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 025560 | 미래산업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 865 | 30.29% |
| 148780 | 비큐AI | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 267 | 53.56% |
| 363250 | 진시스템 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 469480 | IBKS제24호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 469480 | IBKS제24호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 007680 | 대원 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 498390 | 한화플러스제5호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 498390 | 한화플러스제5호스팩 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 007680 | 대원 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 263700 | 케어랩스 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 316 | 18.99% |
| 004890 | 동일산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1442 | 34.74% |
| 004890 | 동일산업 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 1442 | 34.74% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
