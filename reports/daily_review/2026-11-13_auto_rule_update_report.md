# Auto Rule Update Report - 2026-11-13

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **7**
- Positive adjustment rules: **1**
- Negative adjustment rules: **6**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| major_shareholder_change | 3111 | 2477 | 935 | 1542 | 634 | 37.75% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 2891 | 2370 | 1302 | 1068 | 521 | 54.94% | 0.0 | neutral_learning |
| supply_contract | 1768 | 1442 | 530 | 912 | 326 | 36.75% | -5.0 | mild_negative_learning |
| convertible_bond | 1543 | 1210 | 692 | 518 | 333 | 57.19% | 5.0 | mild_positive_learning |
| merger | 858 | 762 | 352 | 410 | 96 | 46.19% | 0.0 | neutral_learning |
| lawsuit | 609 | 488 | 238 | 250 | 121 | 48.77% | 0.0 | neutral_learning |
| investment_decision | 592 | 477 | 244 | 233 | 115 | 51.15% | 0.0 | neutral_learning |
| disclosure_violation | 214 | 144 | 59 | 85 | 70 | 40.97% | -5.0 | mild_negative_learning |
| bond_with_warrant | 154 | 142 | 62 | 80 | 12 | 43.66% | -5.0 | mild_negative_learning |
| spin_off | 155 | 119 | 47 | 72 | 36 | 39.50% | -5.0 | mild_negative_learning |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 0.0 | neutral_learning |
| earnings_guidance | 90 | 86 | 20 | 66 | 4 | 23.26% | -15.0 | strong_negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
