# Auto Rule Update Report - 2026-10-16

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **7**
- Positive adjustment rules: **2**
- Negative adjustment rules: **5**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2081 | 1561 | 885 | 676 | 520 | 56.69% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2020 | 1387 | 494 | 893 | 633 | 35.62% | -5.0 | mild_negative_learning |
| supply_contract | 1174 | 848 | 256 | 592 | 326 | 30.19% | -10.0 | negative_learning |
| convertible_bond | 1058 | 726 | 378 | 348 | 332 | 52.07% | 0.0 | neutral_learning |
| merger | 403 | 308 | 60 | 248 | 95 | 19.48% | -15.0 | strong_negative_learning |
| lawsuit | 396 | 276 | 156 | 120 | 120 | 56.52% | 5.0 | mild_positive_learning |
| investment_decision | 381 | 266 | 143 | 123 | 115 | 53.76% | 0.0 | neutral_learning |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | -5.0 | mild_negative_learning |
| bond_with_warrant | 107 | 95 | 15 | 80 | 12 | 15.79% | -15.0 | strong_negative_learning |
| disclosure_violation | 157 | 87 | 42 | 45 | 70 | 48.28% | 0.0 | neutral_learning |
| spin_off | 112 | 80 | 41 | 39 | 32 | 51.25% | 0.0 | neutral_learning |
| earnings_guidance | 8 | 4 | 4 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
