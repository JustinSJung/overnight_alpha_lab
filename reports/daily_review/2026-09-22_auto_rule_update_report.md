# Auto Rule Update Report - 2026-09-22

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
| paid_in_capital_increase | 1440 | 1137 | 666 | 471 | 303 | 58.58% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1463 | 980 | 329 | 651 | 483 | 33.57% | -10.0 | negative_learning |
| supply_contract | 814 | 552 | 157 | 395 | 262 | 28.44% | -10.0 | negative_learning |
| convertible_bond | 752 | 479 | 238 | 241 | 273 | 49.69% | 0.0 | neutral_learning |
| investment_decision | 310 | 209 | 107 | 102 | 101 | 51.20% | 0.0 | neutral_learning |
| lawsuit | 276 | 178 | 109 | 69 | 98 | 61.24% | 5.0 | mild_positive_learning |
| merger | 187 | 109 | 24 | 85 | 78 | 22.02% | -15.0 | strong_negative_learning |
| disclosure_violation | 119 | 69 | 36 | 33 | 50 | 52.17% | 0.0 | neutral_learning |
| bonus_issue | 64 | 61 | 29 | 32 | 3 | 47.54% | 0.0 | neutral_learning |
| bond_with_warrant | 71 | 61 | 5 | 56 | 10 | 8.20% | -15.0 | strong_negative_learning |
| spin_off | 69 | 46 | 13 | 33 | 23 | 28.26% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
