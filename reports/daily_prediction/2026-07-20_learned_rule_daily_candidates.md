# Learned-Rule Daily Candidate Report - 2026-07-20

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

- Total candidate rows: **39**
- Rows with active learned-rule adjustment: **0**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 24 |
| positive_candidate | 6 |
| watchlist_candidate | 6 |
| general_review | 3 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065420 | 에스아이리소스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 431190 | 케이쓰리아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 389680 | 유디엠텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 065420 | 에스아이리소스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 065420 | 에스아이리소스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 065420 | 에스아이리소스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 290560 | 파라택시스이더리움 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 290560 | 파라택시스이더리움 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 144510 | 지씨셀 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 290560 | 파라택시스이더리움 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 290560 | 파라택시스이더리움 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 290560 | 파라택시스이더리움 | merger | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 078350 | 한양디지텍 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 033310 | 엠투엔 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 055550 | 신한지주 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 018700 | 졸스 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 018700 | 졸스 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 224060 | 더코디 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 018700 | 졸스 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 018700 | 졸스 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 018700 | 졸스 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 018700 | 졸스 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 065420 | 에스아이리소스 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 354200 | 엔젠바이오 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 065420 | 에스아이리소스 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 065420 | 에스아이리소스 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 255220 | SG | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 290720 | 푸드나무 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 354200 | 엔젠바이오 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 018700 | 졸스 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
