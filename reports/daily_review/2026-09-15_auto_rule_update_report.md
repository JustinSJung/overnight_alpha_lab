# Auto Rule Update Report - 2026-09-15

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **3**
- Negative adjustment rules: **6**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 1145 | 842 | 509 | 333 | 303 | 60.45% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1179 | 696 | 193 | 503 | 483 | 27.73% | -10.0 | negative_learning |
| supply_contract | 707 | 445 | 124 | 321 | 262 | 27.87% | -10.0 | negative_learning |
| convertible_bond | 620 | 347 | 174 | 173 | 273 | 50.14% | 0.0 | neutral_learning |
| investment_decision | 218 | 117 | 76 | 41 | 101 | 64.96% | 5.0 | mild_positive_learning |
| lawsuit | 204 | 106 | 77 | 29 | 98 | 72.64% | 10.0 | positive_learning |
| merger | 168 | 90 | 20 | 70 | 78 | 22.22% | -15.0 | strong_negative_learning |
| bonus_issue | 57 | 54 | 28 | 26 | 3 | 51.85% | 0.0 | neutral_learning |
| disclosure_violation | 95 | 45 | 15 | 30 | 50 | 33.33% | -10.0 | negative_learning |
| spin_off | 58 | 35 | 7 | 28 | 23 | 20.00% | -15.0 | strong_negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
