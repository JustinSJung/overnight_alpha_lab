# Auto Rule Update Report - 2026-09-07

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
| paid_in_capital_increase | 797 | 494 | 324 | 170 | 303 | 65.59% | 10.0 | positive_learning |
| major_shareholder_change | 931 | 448 | 128 | 320 | 483 | 28.57% | -10.0 | negative_learning |
| supply_contract | 546 | 284 | 68 | 216 | 262 | 23.94% | -15.0 | strong_negative_learning |
| convertible_bond | 485 | 212 | 135 | 77 | 273 | 63.68% | 5.0 | mild_positive_learning |
| lawsuit | 163 | 67 | 52 | 15 | 96 | 77.61% | 15.0 | strong_positive_learning |
| merger | 123 | 45 | 8 | 37 | 78 | 17.78% | -15.0 | strong_negative_learning |
| investment_decision | 145 | 44 | 26 | 18 | 101 | 59.09% | 5.0 | mild_positive_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| disclosure_violation | 62 | 12 | 1 | 11 | 50 | 8.33% | -11.25 | strong_negative_learning |
| spin_off | 33 | 11 | 4 | 7 | 22 | 36.36% | -3.75 | mild_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
