# Auto Rule Update Report - 2026-09-30

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
| paid_in_capital_increase | 1610 | 1239 | 698 | 541 | 371 | 56.34% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1623 | 1084 | 357 | 727 | 539 | 32.93% | -10.0 | negative_learning |
| supply_contract | 931 | 653 | 192 | 461 | 278 | 29.40% | -10.0 | negative_learning |
| convertible_bond | 863 | 575 | 301 | 274 | 288 | 52.35% | 0.0 | neutral_learning |
| investment_decision | 344 | 238 | 122 | 116 | 106 | 51.26% | 0.0 | neutral_learning |
| lawsuit | 335 | 222 | 127 | 95 | 113 | 57.21% | 5.0 | mild_positive_learning |
| merger | 246 | 166 | 41 | 125 | 80 | 24.70% | -15.0 | strong_negative_learning |
| bonus_issue | 77 | 74 | 41 | 33 | 3 | 55.41% | 5.0 | mild_positive_learning |
| disclosure_violation | 127 | 72 | 38 | 34 | 55 | 52.78% | 0.0 | neutral_learning |
| bond_with_warrant | 74 | 63 | 6 | 57 | 11 | 9.52% | -15.0 | strong_negative_learning |
| spin_off | 75 | 51 | 16 | 35 | 24 | 31.37% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
