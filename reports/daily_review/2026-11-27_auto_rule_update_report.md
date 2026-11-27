# Auto Rule Update Report - 2026-11-27

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
| major_shareholder_change | 3493 | 2859 | 1150 | 1709 | 634 | 40.22% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 3224 | 2703 | 1512 | 1191 | 521 | 55.94% | 5.0 | mild_positive_learning |
| supply_contract | 2067 | 1741 | 635 | 1106 | 326 | 36.47% | -5.0 | mild_negative_learning |
| convertible_bond | 1776 | 1443 | 834 | 609 | 333 | 57.80% | 5.0 | mild_positive_learning |
| merger | 1011 | 915 | 469 | 446 | 96 | 51.26% | 0.0 | neutral_learning |
| lawsuit | 698 | 577 | 305 | 272 | 121 | 52.86% | 0.0 | neutral_learning |
| investment_decision | 677 | 562 | 283 | 279 | 115 | 50.36% | 0.0 | neutral_learning |
| disclosure_violation | 233 | 163 | 70 | 93 | 70 | 42.94% | -5.0 | mild_negative_learning |
| bond_with_warrant | 171 | 159 | 63 | 96 | 12 | 39.62% | -5.0 | mild_negative_learning |
| bonus_issue | 132 | 129 | 68 | 61 | 3 | 52.71% | 0.0 | neutral_learning |
| spin_off | 159 | 123 | 48 | 75 | 36 | 39.02% | -5.0 | mild_negative_learning |
| earnings_guidance | 100 | 96 | 28 | 68 | 4 | 29.17% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
