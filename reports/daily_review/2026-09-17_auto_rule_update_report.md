# Auto Rule Update Report - 2026-09-17

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **8**
- Positive adjustment rules: **3**
- Negative adjustment rules: **5**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 1322 | 1019 | 616 | 403 | 303 | 60.45% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1395 | 912 | 310 | 602 | 483 | 33.99% | -10.0 | negative_learning |
| supply_contract | 752 | 490 | 140 | 350 | 262 | 28.57% | -10.0 | negative_learning |
| convertible_bond | 660 | 387 | 209 | 178 | 273 | 54.01% | 0.0 | neutral_learning |
| investment_decision | 258 | 157 | 103 | 54 | 101 | 65.61% | 10.0 | positive_learning |
| lawsuit | 227 | 129 | 83 | 46 | 98 | 64.34% | 5.0 | mild_positive_learning |
| merger | 170 | 92 | 21 | 71 | 78 | 22.83% | -15.0 | strong_negative_learning |
| disclosure_violation | 115 | 65 | 33 | 32 | 50 | 50.77% | 0.0 | neutral_learning |
| bonus_issue | 64 | 61 | 29 | 32 | 3 | 47.54% | 0.0 | neutral_learning |
| spin_off | 66 | 43 | 13 | 30 | 23 | 30.23% | -10.0 | negative_learning |
| bond_with_warrant | 27 | 17 | 1 | 16 | 10 | 5.88% | -11.25 | strong_negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
