# Auto Rule Update Report - 2026-09-03

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **11**
- Positive adjustment rules: **4**
- Negative adjustment rules: **7**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 600 | 344 | 224 | 120 | 256 | 65.12% | 10.0 | positive_learning |
| major_shareholder_change | 706 | 286 | 59 | 227 | 420 | 20.63% | -15.0 | strong_negative_learning |
| supply_contract | 484 | 241 | 40 | 201 | 243 | 16.60% | -15.0 | strong_negative_learning |
| convertible_bond | 407 | 160 | 113 | 47 | 247 | 70.63% | 10.0 | positive_learning |
| lawsuit | 134 | 43 | 36 | 7 | 91 | 83.72% | 15.0 | strong_positive_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| investment_decision | 126 | 34 | 19 | 15 | 92 | 55.88% | 5.0 | mild_positive_learning |
| merger | 89 | 28 | 2 | 26 | 61 | 7.14% | -11.25 | strong_negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| spin_off | 27 | 8 | 3 | 5 | 19 | 37.50% | -2.5 | mild_negative_learning |
| disclosure_violation | 55 | 7 | 1 | 6 | 48 | 14.29% | -7.5 | strong_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
