# Auto Rule Update Report - 2026-09-08

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **11**
- Positive adjustment rules: **3**
- Negative adjustment rules: **8**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 836 | 533 | 356 | 177 | 303 | 66.79% | 10.0 | positive_learning |
| major_shareholder_change | 996 | 513 | 149 | 364 | 483 | 29.04% | -10.0 | negative_learning |
| supply_contract | 565 | 303 | 74 | 229 | 262 | 24.42% | -15.0 | strong_negative_learning |
| convertible_bond | 488 | 215 | 138 | 77 | 273 | 64.19% | 5.0 | mild_positive_learning |
| lawsuit | 165 | 69 | 53 | 16 | 96 | 76.81% | 15.0 | strong_positive_learning |
| investment_decision | 160 | 59 | 26 | 33 | 101 | 44.07% | -5.0 | mild_negative_learning |
| merger | 123 | 45 | 8 | 37 | 78 | 17.78% | -15.0 | strong_negative_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| disclosure_violation | 65 | 15 | 1 | 14 | 50 | 6.67% | -11.25 | strong_negative_learning |
| spin_off | 34 | 12 | 5 | 7 | 22 | 41.67% | -3.75 | mild_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
