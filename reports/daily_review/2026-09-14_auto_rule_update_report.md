# Auto Rule Update Report - 2026-09-14

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **10**
- Positive adjustment rules: **3**
- Negative adjustment rules: **7**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 1079 | 776 | 462 | 314 | 303 | 59.54% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1142 | 659 | 175 | 484 | 483 | 26.56% | -10.0 | negative_learning |
| supply_contract | 679 | 417 | 116 | 301 | 262 | 27.82% | -10.0 | negative_learning |
| convertible_bond | 600 | 327 | 170 | 157 | 273 | 51.99% | 0.0 | neutral_learning |
| investment_decision | 206 | 105 | 67 | 38 | 101 | 63.81% | 5.0 | mild_positive_learning |
| lawsuit | 194 | 97 | 75 | 22 | 97 | 77.32% | 15.0 | strong_positive_learning |
| merger | 167 | 89 | 19 | 70 | 78 | 21.35% | -15.0 | strong_negative_learning |
| disclosure_violation | 92 | 42 | 13 | 29 | 50 | 30.95% | -10.0 | negative_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| spin_off | 57 | 35 | 7 | 28 | 22 | 20.00% | -15.0 | strong_negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
