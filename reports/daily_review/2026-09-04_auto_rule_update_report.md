# Auto Rule Update Report - 2026-09-04

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **11**
- Positive adjustment rules: **4**
- Negative adjustment rules: **7**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 703 | 447 | 301 | 146 | 256 | 67.34% | 10.0 | positive_learning |
| major_shareholder_change | 805 | 385 | 116 | 269 | 420 | 30.13% | -10.0 | negative_learning |
| supply_contract | 508 | 265 | 61 | 204 | 243 | 23.02% | -15.0 | strong_negative_learning |
| convertible_bond | 433 | 186 | 125 | 61 | 247 | 67.20% | 10.0 | positive_learning |
| lawsuit | 153 | 62 | 48 | 14 | 91 | 77.42% | 15.0 | strong_positive_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| investment_decision | 127 | 35 | 20 | 15 | 92 | 57.14% | 5.0 | mild_positive_learning |
| merger | 89 | 28 | 2 | 26 | 61 | 7.14% | -11.25 | strong_negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| disclosure_violation | 58 | 10 | 1 | 9 | 48 | 10.00% | -11.25 | strong_negative_learning |
| spin_off | 27 | 8 | 3 | 5 | 19 | 37.50% | -2.5 | mild_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
