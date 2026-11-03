# Auto Rule Update Report - 2026-11-03

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **3**
- Negative adjustment rules: **6**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2555 | 2034 | 1166 | 868 | 521 | 57.33% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2584 | 1951 | 770 | 1181 | 633 | 39.47% | -5.0 | mild_negative_learning |
| supply_contract | 1584 | 1258 | 433 | 825 | 326 | 34.42% | -10.0 | negative_learning |
| convertible_bond | 1350 | 1017 | 585 | 432 | 333 | 57.52% | 5.0 | mild_positive_learning |
| merger | 754 | 658 | 311 | 347 | 96 | 47.26% | 0.0 | neutral_learning |
| investment_decision | 508 | 393 | 196 | 197 | 115 | 49.87% | 0.0 | neutral_learning |
| lawsuit | 504 | 383 | 215 | 168 | 121 | 56.14% | 5.0 | mild_positive_learning |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | -5.0 | mild_negative_learning |
| disclosure_violation | 202 | 132 | 53 | 79 | 70 | 40.15% | -5.0 | mild_negative_learning |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | -5.0 | mild_negative_learning |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | 0.0 | neutral_learning |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
