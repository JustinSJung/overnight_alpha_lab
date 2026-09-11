# Auto Rule Update Report - 2026-09-11

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
| paid_in_capital_increase | 1032 | 729 | 436 | 293 | 303 | 59.81% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1114 | 631 | 167 | 464 | 483 | 26.47% | -10.0 | negative_learning |
| supply_contract | 638 | 376 | 100 | 276 | 262 | 26.60% | -10.0 | negative_learning |
| convertible_bond | 575 | 302 | 156 | 146 | 273 | 51.66% | 0.0 | neutral_learning |
| investment_decision | 199 | 98 | 61 | 37 | 101 | 62.24% | 5.0 | mild_positive_learning |
| lawsuit | 191 | 94 | 74 | 20 | 97 | 78.72% | 15.0 | strong_positive_learning |
| merger | 165 | 87 | 18 | 69 | 78 | 20.69% | -15.0 | strong_negative_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| spin_off | 56 | 34 | 7 | 27 | 22 | 20.59% | -15.0 | strong_negative_learning |
| disclosure_violation | 69 | 19 | 5 | 14 | 50 | 26.32% | -7.5 | negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
