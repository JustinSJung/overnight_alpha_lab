# Auto Rule Update Report - 2026-10-07

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
| paid_in_capital_increase | 1747 | 1342 | 788 | 554 | 405 | 58.72% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1727 | 1162 | 399 | 763 | 565 | 34.34% | -10.0 | negative_learning |
| supply_contract | 1007 | 707 | 205 | 502 | 300 | 29.00% | -10.0 | negative_learning |
| convertible_bond | 901 | 603 | 324 | 279 | 298 | 53.73% | 0.0 | neutral_learning |
| merger | 354 | 263 | 52 | 211 | 91 | 19.77% | -15.0 | strong_negative_learning |
| lawsuit | 365 | 248 | 141 | 107 | 117 | 56.85% | 5.0 | mild_positive_learning |
| investment_decision | 359 | 246 | 126 | 120 | 113 | 51.22% | 0.0 | neutral_learning |
| bonus_issue | 81 | 78 | 41 | 37 | 3 | 52.56% | 0.0 | neutral_learning |
| disclosure_violation | 129 | 74 | 38 | 36 | 55 | 51.35% | 0.0 | neutral_learning |
| bond_with_warrant | 76 | 65 | 6 | 59 | 11 | 9.23% | -15.0 | strong_negative_learning |
| spin_off | 84 | 54 | 17 | 37 | 30 | 31.48% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
