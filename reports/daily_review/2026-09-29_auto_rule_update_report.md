# Auto Rule Update Report - 2026-09-29

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
| paid_in_capital_increase | 1569 | 1198 | 684 | 514 | 371 | 57.10% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1584 | 1045 | 347 | 698 | 539 | 33.21% | -10.0 | negative_learning |
| supply_contract | 899 | 621 | 175 | 446 | 278 | 28.18% | -10.0 | negative_learning |
| convertible_bond | 858 | 570 | 298 | 272 | 288 | 52.28% | 0.0 | neutral_learning |
| investment_decision | 333 | 227 | 120 | 107 | 106 | 52.86% | 0.0 | neutral_learning |
| lawsuit | 318 | 205 | 113 | 92 | 113 | 55.12% | 5.0 | mild_positive_learning |
| merger | 200 | 120 | 25 | 95 | 80 | 20.83% | -15.0 | strong_negative_learning |
| disclosure_violation | 126 | 71 | 38 | 33 | 55 | 53.52% | 0.0 | neutral_learning |
| bond_with_warrant | 74 | 63 | 6 | 57 | 11 | 9.52% | -15.0 | strong_negative_learning |
| bonus_issue | 65 | 62 | 29 | 33 | 3 | 46.77% | 0.0 | neutral_learning |
| spin_off | 73 | 49 | 15 | 34 | 24 | 30.61% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
