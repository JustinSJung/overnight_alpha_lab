# Learned-Rule Daily Candidate Report - 2026-09-07

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

- Total candidate rows: **446**
- Rows with active learned-rule adjustment: **446**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| general_review | 221 |
| risk_or_avoid_review | 194 |
| watchlist_candidate | 22 |
| volatile_watchlist | 9 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 098070 | 한텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 336260 | 두산퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 079810 | APS이노베이션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 011560 | 세보엠이씨 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 336260 | 두산퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 108230 | 톱텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 002020 | 코오롱 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 003070 | 코오롱글로벌 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 294630 | 서남 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 302430 | 이노메트리 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 336260 | 두산퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 336260 | 두산퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 336260 | 두산퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 006260 | LS | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 092870 | 엑시콘 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 036190 | 금화피에스시 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 083640 | 인콘 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 376270 | HEM파마 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 083640 | 인콘 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 083640 | 인콘 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 336260 | 두산퓨얼셀 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 083640 | 인콘 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 284 | 23.94% |
| 039200 | 오스코텍 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |
| 011090 | 에넥스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |
| 011090 | 에넥스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |
| 011090 | 에넥스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |
| 002820 | SUN&L | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |
| 048410 | 현대바이오 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |
| 011090 | 에넥스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |
| 011090 | 에넥스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 44 | 59.09% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
