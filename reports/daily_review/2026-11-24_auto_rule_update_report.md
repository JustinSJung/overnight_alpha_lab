# Auto Rule Update Report - 2026-11-24

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
| major_shareholder_change | 3389 | 2755 | 1107 | 1648 | 634 | 40.18% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 3125 | 2604 | 1487 | 1117 | 521 | 57.10% | 5.0 | mild_positive_learning |
| supply_contract | 1986 | 1660 | 590 | 1070 | 326 | 35.54% | -5.0 | mild_negative_learning |
| convertible_bond | 1693 | 1360 | 809 | 551 | 333 | 59.49% | 5.0 | mild_positive_learning |
| merger | 914 | 818 | 377 | 441 | 96 | 46.09% | 0.0 | neutral_learning |
| lawsuit | 668 | 547 | 283 | 264 | 121 | 51.74% | 0.0 | neutral_learning |
| investment_decision | 655 | 540 | 279 | 261 | 115 | 51.67% | 0.0 | neutral_learning |
| disclosure_violation | 230 | 160 | 70 | 90 | 70 | 43.75% | -5.0 | mild_negative_learning |
| bond_with_warrant | 163 | 151 | 63 | 88 | 12 | 41.72% | -5.0 | mild_negative_learning |
| spin_off | 158 | 122 | 48 | 74 | 36 | 39.34% | -5.0 | mild_negative_learning |
| bonus_issue | 120 | 117 | 56 | 61 | 3 | 47.86% | 0.0 | neutral_learning |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
