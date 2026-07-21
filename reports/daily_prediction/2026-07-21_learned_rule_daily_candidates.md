# Learned-Rule Daily Candidate Report - 2026-07-21

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

- Total candidate rows: **30**
- Rows with active learned-rule adjustment: **0**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 19 |
| general_review | 6 |
| watchlist_candidate | 3 |
| positive_candidate | 2 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 053580 | 웹케시 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 119850 | 지엔씨에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | 0.0 | 70.0 | positive_candidate | hold_insufficient_data | 0 | 0.00% |
| 008470 | 부스타 | bonus_issue | positive | 60.0 | 0.0 | 0.0 | 0.0 | 60.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 348950 | 제이알글로벌리츠 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 397030 | 에이프릴바이오 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | hold_insufficient_data | 0 | 0.00% |
| 066790 | 씨씨에스 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000500 | 가온전선 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 011420 | 갤럭시아에스엠 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000500 | 가온전선 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000500 | 가온전선 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 000500 | 가온전선 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | 0.0 | 10.0 | general_review | hold_insufficient_data | 0 | 0.00% |
| 179530 | 애드바이오텍 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 276730 | 한울앤제주 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 106240 | 파인테크닉스 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 159910 | 에코글로우 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 179530 | 애드바이오텍 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 179530 | 애드바이오텍 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 179530 | 애드바이오텍 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 179530 | 애드바이오텍 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 276730 | 한울앤제주 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 179530 | 애드바이오텍 | convertible_bond | negative | -60.0 | 0.0 | 0.0 | 0.0 | -60.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 071950 | 코아스 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 900120 | 씨엑스아이 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 900120 | 씨엑스아이 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 340810 | 시선AI | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 340810 | 시선AI | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 900120 | 씨엑스아이 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 900120 | 씨엑스아이 | paid_in_capital_increase | negative | -70.0 | 0.0 | 0.0 | 0.0 | -70.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 066430 | 아이로보틱스 | lawsuit | negative | -75.0 | 0.0 | 0.0 | 0.0 | -75.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |
| 006220 | 제주은행 | disclosure_violation | negative | -80.0 | 0.0 | 0.0 | 0.0 | -80.0 | risk_or_avoid_review | hold_insufficient_data | 0 | 0.00% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
