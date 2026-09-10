# Auto Rule Update Report - 2026-09-10

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
| paid_in_capital_increase | 942 | 639 | 405 | 234 | 303 | 63.38% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1058 | 575 | 159 | 416 | 483 | 27.65% | -10.0 | negative_learning |
| supply_contract | 602 | 340 | 90 | 250 | 262 | 26.47% | -10.0 | negative_learning |
| convertible_bond | 541 | 268 | 148 | 120 | 273 | 55.22% | 5.0 | mild_positive_learning |
| investment_decision | 196 | 95 | 59 | 36 | 101 | 62.11% | 5.0 | mild_positive_learning |
| lawsuit | 188 | 91 | 72 | 19 | 97 | 79.12% | 15.0 | strong_positive_learning |
| merger | 149 | 71 | 10 | 61 | 78 | 14.08% | -15.0 | strong_negative_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| spin_off | 54 | 32 | 7 | 25 | 22 | 21.88% | -15.0 | strong_negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| disclosure_violation | 65 | 15 | 1 | 14 | 50 | 6.67% | -11.25 | strong_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
