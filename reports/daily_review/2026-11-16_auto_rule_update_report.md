# Auto Rule Update Report - 2026-11-16

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
| major_shareholder_change | 3158 | 2524 | 955 | 1569 | 634 | 37.84% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 2906 | 2385 | 1309 | 1076 | 521 | 54.88% | 0.0 | neutral_learning |
| supply_contract | 1786 | 1460 | 532 | 928 | 326 | 36.44% | -5.0 | mild_negative_learning |
| convertible_bond | 1569 | 1236 | 698 | 538 | 333 | 56.47% | 5.0 | mild_positive_learning |
| merger | 862 | 766 | 354 | 412 | 96 | 46.21% | 0.0 | neutral_learning |
| lawsuit | 613 | 492 | 239 | 253 | 121 | 48.58% | 0.0 | neutral_learning |
| investment_decision | 599 | 484 | 246 | 238 | 115 | 50.83% | 0.0 | neutral_learning |
| bond_with_warrant | 161 | 149 | 63 | 86 | 12 | 42.28% | -5.0 | mild_negative_learning |
| disclosure_violation | 217 | 147 | 61 | 86 | 70 | 41.50% | -5.0 | mild_negative_learning |
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
