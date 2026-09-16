# Auto Rule Update Report - 2026-09-16

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **3**
- Negative adjustment rules: **6**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 1249 | 946 | 585 | 361 | 303 | 61.84% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1323 | 840 | 294 | 546 | 483 | 35.00% | -5.0 | mild_negative_learning |
| supply_contract | 742 | 480 | 135 | 345 | 262 | 28.12% | -10.0 | negative_learning |
| convertible_bond | 659 | 386 | 208 | 178 | 273 | 53.89% | 0.0 | neutral_learning |
| investment_decision | 245 | 144 | 102 | 42 | 101 | 70.83% | 10.0 | positive_learning |
| lawsuit | 211 | 113 | 83 | 30 | 98 | 73.45% | 10.0 | positive_learning |
| merger | 169 | 91 | 20 | 71 | 78 | 21.98% | -15.0 | strong_negative_learning |
| bonus_issue | 58 | 55 | 29 | 26 | 3 | 52.73% | 0.0 | neutral_learning |
| disclosure_violation | 98 | 48 | 17 | 31 | 50 | 35.42% | -5.0 | mild_negative_learning |
| spin_off | 64 | 41 | 12 | 29 | 23 | 29.27% | -10.0 | negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
