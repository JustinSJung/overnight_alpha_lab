# Auto Rule Update Report - 2026-09-01

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **8**
- Positive adjustment rules: **3**
- Negative adjustment rules: **5**
- Held due to insufficient data: **3**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| supply_contract | 416 | 173 | 34 | 139 | 243 | 19.65% | -15.0 | strong_negative_learning |
| major_shareholder_change | 576 | 156 | 40 | 116 | 420 | 25.64% | -10.0 | negative_learning |
| paid_in_capital_increase | 392 | 136 | 77 | 59 | 256 | 56.62% | 5.0 | mild_positive_learning |
| convertible_bond | 309 | 62 | 40 | 22 | 247 | 64.52% | 5.0 | mild_positive_learning |
| investment_decision | 114 | 22 | 10 | 12 | 92 | 45.45% | 0.0 | neutral_learning |
| lawsuit | 107 | 16 | 14 | 2 | 91 | 87.50% | 11.25 | strong_positive_learning |
| merger | 77 | 16 | 1 | 15 | 61 | 6.25% | -11.25 | strong_negative_learning |
| spin_off | 25 | 7 | 3 | 4 | 18 | 42.86% | -2.5 | mild_negative_learning |
| disclosure_violation | 54 | 6 | 1 | 5 | 48 | 16.67% | -7.5 | strong_negative_learning |
| bond_with_warrant | 11 | 1 | 1 | 0 | 10 | 100.00% | 0.0 | hold_insufficient_data |
| bonus_issue | 3 | 0 | 0 | 0 | 3 | 0.00% | 0.0 | hold_insufficient_data |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
