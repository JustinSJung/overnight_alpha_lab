# Learned-Rule Daily Candidate Report - 2026-08-18

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

- Total candidate rows: **34**
- Rows with active learned-rule adjustment: **0**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 20 |
| general_review | 7 |
| positive_candidate | 4 |
| watchlist_candidate | 3 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 095270 | 웨이브일렉트로 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 009410 | 태영건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 363280 | 티와이홀딩스 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 950220 | 네오이뮨텍 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 0009K0 | 에임드바이오 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 196450 | 코아시아씨엠 | spin_off | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 003470 | 유안타증권 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 033310 | 엠투엔 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 001740 | SK네트웍스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 003470 | 유안타증권 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000950 | 전방 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000950 | 전방 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 001740 | SK네트웍스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 033540 | 파라텍 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 294090 | 이오플로우 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 142760 | 모아라이프플러스 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 089230 | THE E&M | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 038880 | 아이에이 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 038880 | 아이에이 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 038880 | 아이에이 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 062970 | 한국첨단소재 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 062970 | 한국첨단소재 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 340810 | 시선AI | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 069920 | 엑시온그룹 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 069920 | 엑시온그룹 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 340810 | 시선AI | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 340810 | 시선AI | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 418620 | E8 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 340810 | 시선AI | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
