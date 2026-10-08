# Auto Rule Update Report - 2026-10-08

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
| paid_in_capital_increase | 1791 | 1385 | 813 | 572 | 406 | 58.70% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1747 | 1182 | 402 | 780 | 565 | 34.01% | -10.0 | negative_learning |
| supply_contract | 1024 | 724 | 210 | 514 | 300 | 29.01% | -10.0 | negative_learning |
| convertible_bond | 931 | 633 | 336 | 297 | 298 | 53.08% | 0.0 | neutral_learning |
| merger | 355 | 264 | 52 | 212 | 91 | 19.70% | -15.0 | strong_negative_learning |
| investment_decision | 364 | 251 | 131 | 120 | 113 | 52.19% | 0.0 | neutral_learning |
| lawsuit | 366 | 249 | 141 | 108 | 117 | 56.63% | 5.0 | mild_positive_learning |
| bonus_issue | 93 | 90 | 41 | 49 | 3 | 45.56% | 0.0 | neutral_learning |
| disclosure_violation | 132 | 77 | 38 | 39 | 55 | 49.35% | 0.0 | neutral_learning |
| bond_with_warrant | 76 | 65 | 6 | 59 | 11 | 9.23% | -15.0 | strong_negative_learning |
| spin_off | 85 | 55 | 18 | 37 | 30 | 32.73% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
