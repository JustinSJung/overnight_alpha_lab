# Auto Rule Update Report - 2026-11-23

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **8**
- Positive adjustment rules: **2**
- Negative adjustment rules: **6**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| major_shareholder_change | 3344 | 2710 | 1063 | 1647 | 634 | 39.23% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 3034 | 2513 | 1419 | 1094 | 521 | 56.47% | 5.0 | mild_positive_learning |
| supply_contract | 1963 | 1637 | 574 | 1063 | 326 | 35.06% | -5.0 | mild_negative_learning |
| convertible_bond | 1692 | 1359 | 809 | 550 | 333 | 59.53% | 5.0 | mild_positive_learning |
| merger | 895 | 799 | 363 | 436 | 96 | 45.43% | 0.0 | neutral_learning |
| lawsuit | 647 | 526 | 267 | 259 | 121 | 50.76% | 0.0 | neutral_learning |
| investment_decision | 638 | 523 | 272 | 251 | 115 | 52.01% | 0.0 | neutral_learning |
| disclosure_violation | 228 | 158 | 70 | 88 | 70 | 44.30% | -5.0 | mild_negative_learning |
| bond_with_warrant | 162 | 150 | 63 | 87 | 12 | 42.00% | -5.0 | mild_negative_learning |
| spin_off | 158 | 122 | 48 | 74 | 36 | 39.34% | -5.0 | mild_negative_learning |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 0.0 | neutral_learning |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
