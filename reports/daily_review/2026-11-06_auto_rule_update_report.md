# Auto Rule Update Report - 2026-11-06

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **2**
- Negative adjustment rules: **7**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2673 | 2152 | 1245 | 907 | 521 | 57.85% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2760 | 2127 | 853 | 1274 | 633 | 40.10% | -5.0 | mild_negative_learning |
| supply_contract | 1636 | 1310 | 437 | 873 | 326 | 33.36% | -10.0 | negative_learning |
| convertible_bond | 1393 | 1060 | 613 | 447 | 333 | 57.83% | 5.0 | mild_positive_learning |
| merger | 787 | 691 | 314 | 377 | 96 | 45.44% | 0.0 | neutral_learning |
| lawsuit | 548 | 427 | 222 | 205 | 121 | 51.99% | 0.0 | neutral_learning |
| investment_decision | 536 | 421 | 210 | 211 | 115 | 49.88% | 0.0 | neutral_learning |
| disclosure_violation | 209 | 139 | 56 | 83 | 70 | 40.29% | -5.0 | mild_negative_learning |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | -5.0 | mild_negative_learning |
| spin_off | 150 | 114 | 44 | 70 | 36 | 38.60% | -5.0 | mild_negative_learning |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | -5.0 | mild_negative_learning |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
