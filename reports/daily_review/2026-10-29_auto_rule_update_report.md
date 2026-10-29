# Auto Rule Update Report - 2026-10-29

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
| paid_in_capital_increase | 2407 | 1887 | 1104 | 783 | 520 | 58.51% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2396 | 1763 | 658 | 1105 | 633 | 37.32% | -5.0 | mild_negative_learning |
| supply_contract | 1411 | 1085 | 354 | 731 | 326 | 32.63% | -10.0 | negative_learning |
| convertible_bond | 1205 | 872 | 471 | 401 | 333 | 54.01% | 0.0 | neutral_learning |
| merger | 584 | 488 | 159 | 329 | 96 | 32.58% | -10.0 | negative_learning |
| lawsuit | 493 | 372 | 210 | 162 | 121 | 56.45% | 5.0 | mild_positive_learning |
| investment_decision | 436 | 321 | 169 | 152 | 115 | 52.65% | 0.0 | neutral_learning |
| disclosure_violation | 188 | 118 | 51 | 67 | 70 | 43.22% | -5.0 | mild_negative_learning |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -15.0 | strong_negative_learning |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | -5.0 | mild_negative_learning |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | 0.0 | neutral_learning |
| earnings_guidance | 50 | 46 | 15 | 31 | 4 | 32.61% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
