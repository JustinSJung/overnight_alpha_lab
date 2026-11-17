# Auto Rule Update Report - 2026-11-17

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **8**
- Positive adjustment rules: **2**
- Negative adjustment rules: **6**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| major_shareholder_change | 3204 | 2570 | 978 | 1592 | 634 | 38.05% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 2937 | 2416 | 1333 | 1083 | 521 | 55.17% | 5.0 | mild_positive_learning |
| supply_contract | 1839 | 1513 | 548 | 965 | 326 | 36.22% | -5.0 | mild_negative_learning |
| convertible_bond | 1608 | 1275 | 735 | 540 | 333 | 57.65% | 5.0 | mild_positive_learning |
| merger | 869 | 773 | 354 | 419 | 96 | 45.80% | 0.0 | neutral_learning |
| lawsuit | 620 | 499 | 246 | 253 | 121 | 49.30% | 0.0 | neutral_learning |
| investment_decision | 605 | 490 | 250 | 240 | 115 | 51.02% | 0.0 | neutral_learning |
| bond_with_warrant | 162 | 150 | 63 | 87 | 12 | 42.00% | -5.0 | mild_negative_learning |
| disclosure_violation | 218 | 148 | 61 | 87 | 70 | 41.22% | -5.0 | mild_negative_learning |
| spin_off | 155 | 119 | 47 | 72 | 36 | 39.50% | -5.0 | mild_negative_learning |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 0.0 | neutral_learning |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
