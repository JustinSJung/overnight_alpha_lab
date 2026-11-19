# Auto Rule Update Report - 2026-11-19

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
| major_shareholder_change | 3262 | 2628 | 997 | 1631 | 634 | 37.94% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 2986 | 2465 | 1377 | 1088 | 521 | 55.86% | 5.0 | mild_positive_learning |
| supply_contract | 1890 | 1564 | 569 | 995 | 326 | 36.38% | -5.0 | mild_negative_learning |
| convertible_bond | 1658 | 1325 | 784 | 541 | 333 | 59.17% | 5.0 | mild_positive_learning |
| merger | 870 | 774 | 355 | 419 | 96 | 45.87% | 0.0 | neutral_learning |
| lawsuit | 633 | 512 | 257 | 255 | 121 | 50.20% | 0.0 | neutral_learning |
| investment_decision | 616 | 501 | 251 | 250 | 115 | 50.10% | 0.0 | neutral_learning |
| bond_with_warrant | 162 | 150 | 63 | 87 | 12 | 42.00% | -5.0 | mild_negative_learning |
| disclosure_violation | 219 | 149 | 61 | 88 | 70 | 40.94% | -5.0 | mild_negative_learning |
| spin_off | 157 | 121 | 48 | 73 | 36 | 39.67% | -5.0 | mild_negative_learning |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 0.0 | neutral_learning |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
