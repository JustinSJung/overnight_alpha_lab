# Auto Rule Update Report - 2026-10-02

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
| paid_in_capital_increase | 1670 | 1299 | 751 | 548 | 371 | 57.81% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1659 | 1120 | 382 | 738 | 539 | 34.11% | -10.0 | negative_learning |
| supply_contract | 952 | 674 | 201 | 473 | 278 | 29.82% | -10.0 | negative_learning |
| convertible_bond | 877 | 589 | 315 | 274 | 288 | 53.48% | 0.0 | neutral_learning |
| investment_decision | 346 | 240 | 123 | 117 | 106 | 51.25% | 0.0 | neutral_learning |
| lawsuit | 344 | 231 | 136 | 95 | 113 | 58.87% | 5.0 | mild_positive_learning |
| merger | 266 | 186 | 50 | 136 | 80 | 26.88% | -10.0 | negative_learning |
| bonus_issue | 79 | 76 | 41 | 35 | 3 | 53.95% | 0.0 | neutral_learning |
| disclosure_violation | 129 | 74 | 38 | 36 | 55 | 51.35% | 0.0 | neutral_learning |
| bond_with_warrant | 74 | 63 | 6 | 57 | 11 | 9.52% | -15.0 | strong_negative_learning |
| spin_off | 77 | 53 | 16 | 37 | 24 | 30.19% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
