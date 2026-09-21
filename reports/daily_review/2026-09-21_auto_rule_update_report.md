# Auto Rule Update Report - 2026-09-21

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
| paid_in_capital_increase | 1350 | 1047 | 636 | 411 | 303 | 60.74% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1436 | 953 | 326 | 627 | 483 | 34.21% | -10.0 | negative_learning |
| supply_contract | 780 | 518 | 149 | 369 | 262 | 28.76% | -10.0 | negative_learning |
| convertible_bond | 686 | 413 | 227 | 186 | 273 | 54.96% | 0.0 | neutral_learning |
| investment_decision | 304 | 203 | 105 | 98 | 101 | 51.72% | 0.0 | neutral_learning |
| lawsuit | 248 | 150 | 91 | 59 | 98 | 60.67% | 5.0 | mild_positive_learning |
| merger | 184 | 106 | 24 | 82 | 78 | 22.64% | -15.0 | strong_negative_learning |
| disclosure_violation | 116 | 66 | 33 | 33 | 50 | 50.00% | 0.0 | neutral_learning |
| bonus_issue | 64 | 61 | 29 | 32 | 3 | 47.54% | 0.0 | neutral_learning |
| spin_off | 69 | 46 | 13 | 33 | 23 | 28.26% | -10.0 | negative_learning |
| bond_with_warrant | 27 | 17 | 1 | 16 | 10 | 5.88% | -11.25 | strong_negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
