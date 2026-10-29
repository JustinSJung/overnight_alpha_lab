# Auto Rule Update Report - 2026-10-20

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
| paid_in_capital_increase | 2196 | 1676 | 965 | 711 | 520 | 57.58% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2120 | 1487 | 525 | 962 | 633 | 35.31% | -5.0 | mild_negative_learning |
| supply_contract | 1231 | 905 | 270 | 635 | 326 | 29.83% | -10.0 | negative_learning |
| convertible_bond | 1087 | 755 | 396 | 359 | 332 | 52.45% | 0.0 | neutral_learning |
| merger | 418 | 323 | 63 | 260 | 95 | 19.50% | -15.0 | strong_negative_learning |
| lawsuit | 413 | 292 | 170 | 122 | 121 | 58.22% | 5.0 | mild_positive_learning |
| investment_decision | 394 | 279 | 153 | 126 | 115 | 54.84% | 0.0 | neutral_learning |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -15.0 | strong_negative_learning |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | -5.0 | mild_negative_learning |
| disclosure_violation | 168 | 98 | 48 | 50 | 70 | 48.98% | 0.0 | neutral_learning |
| spin_off | 112 | 80 | 41 | 39 | 32 | 51.25% | 0.0 | neutral_learning |
| earnings_guidance | 8 | 4 | 4 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
