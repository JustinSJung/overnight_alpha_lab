# Auto Rule Update Report - 2026-10-30

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **10**
- Positive adjustment rules: **3**
- Negative adjustment rules: **7**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2482 | 1962 | 1137 | 825 | 520 | 57.95% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2427 | 1794 | 682 | 1112 | 633 | 38.02% | -5.0 | mild_negative_learning |
| supply_contract | 1465 | 1139 | 360 | 779 | 326 | 31.61% | -10.0 | negative_learning |
| convertible_bond | 1303 | 970 | 557 | 413 | 333 | 57.42% | 5.0 | mild_positive_learning |
| merger | 591 | 495 | 166 | 329 | 96 | 33.54% | -10.0 | negative_learning |
| lawsuit | 497 | 376 | 211 | 165 | 121 | 56.12% | 5.0 | mild_positive_learning |
| investment_decision | 439 | 324 | 171 | 153 | 115 | 52.78% | 0.0 | neutral_learning |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | -5.0 | mild_negative_learning |
| disclosure_violation | 189 | 119 | 51 | 68 | 70 | 42.86% | -5.0 | mild_negative_learning |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | -5.0 | mild_negative_learning |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | 0.0 | neutral_learning |
| earnings_guidance | 62 | 58 | 15 | 43 | 4 | 25.86% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
