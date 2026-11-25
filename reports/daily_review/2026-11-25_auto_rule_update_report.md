# Auto Rule Update Report - 2026-11-25

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
| major_shareholder_change | 3414 | 2780 | 1113 | 1667 | 634 | 40.04% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 3172 | 2651 | 1498 | 1153 | 521 | 56.51% | 5.0 | mild_positive_learning |
| supply_contract | 2004 | 1678 | 598 | 1080 | 326 | 35.64% | -5.0 | mild_negative_learning |
| convertible_bond | 1711 | 1378 | 823 | 555 | 333 | 59.72% | 5.0 | mild_positive_learning |
| merger | 922 | 826 | 382 | 444 | 96 | 46.25% | 0.0 | neutral_learning |
| lawsuit | 672 | 551 | 284 | 267 | 121 | 51.54% | 0.0 | neutral_learning |
| investment_decision | 662 | 547 | 279 | 268 | 115 | 51.01% | 0.0 | neutral_learning |
| disclosure_violation | 232 | 162 | 70 | 92 | 70 | 43.21% | -5.0 | mild_negative_learning |
| bond_with_warrant | 163 | 151 | 63 | 88 | 12 | 41.72% | -5.0 | mild_negative_learning |
| spin_off | 159 | 123 | 48 | 75 | 36 | 39.02% | -5.0 | mild_negative_learning |
| bonus_issue | 120 | 117 | 56 | 61 | 3 | 47.86% | 0.0 | neutral_learning |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
