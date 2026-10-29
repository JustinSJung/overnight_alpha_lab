# Auto Rule Update Report - 2026-10-15

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **8**
- Positive adjustment rules: **2**
- Negative adjustment rules: **6**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2070 | 1550 | 884 | 666 | 520 | 57.03% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1946 | 1313 | 454 | 859 | 633 | 34.58% | -10.0 | negative_learning |
| supply_contract | 1131 | 805 | 220 | 585 | 326 | 27.33% | -10.0 | negative_learning |
| convertible_bond | 1019 | 687 | 377 | 310 | 332 | 54.88% | 0.0 | neutral_learning |
| merger | 371 | 276 | 58 | 218 | 95 | 21.01% | -15.0 | strong_negative_learning |
| lawsuit | 395 | 275 | 156 | 119 | 120 | 56.73% | 5.0 | mild_positive_learning |
| investment_decision | 381 | 266 | 143 | 123 | 115 | 53.76% | 0.0 | neutral_learning |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | -5.0 | mild_negative_learning |
| disclosure_violation | 155 | 85 | 42 | 43 | 70 | 49.41% | 0.0 | neutral_learning |
| bond_with_warrant | 86 | 74 | 15 | 59 | 12 | 20.27% | -15.0 | strong_negative_learning |
| spin_off | 92 | 60 | 21 | 39 | 32 | 35.00% | -5.0 | mild_negative_learning |
| earnings_guidance | 8 | 4 | 4 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
