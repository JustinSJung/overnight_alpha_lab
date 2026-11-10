# Auto Rule Update Report - 2026-11-10

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **10**
- Positive adjustment rules: **2**
- Negative adjustment rules: **8**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2767 | 2246 | 1260 | 986 | 521 | 56.10% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2857 | 2223 | 885 | 1338 | 634 | 39.81% | -5.0 | mild_negative_learning |
| supply_contract | 1706 | 1380 | 484 | 896 | 326 | 35.07% | -5.0 | mild_negative_learning |
| convertible_bond | 1463 | 1130 | 646 | 484 | 333 | 57.17% | 5.0 | mild_positive_learning |
| merger | 798 | 702 | 315 | 387 | 96 | 44.87% | -5.0 | mild_negative_learning |
| investment_decision | 566 | 451 | 238 | 213 | 115 | 52.77% | 0.0 | neutral_learning |
| lawsuit | 566 | 445 | 230 | 215 | 121 | 51.69% | 0.0 | neutral_learning |
| disclosure_violation | 211 | 141 | 58 | 83 | 70 | 41.13% | -5.0 | mild_negative_learning |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | -5.0 | mild_negative_learning |
| spin_off | 152 | 116 | 44 | 72 | 36 | 37.93% | -5.0 | mild_negative_learning |
| bonus_issue | 107 | 104 | 44 | 60 | 3 | 42.31% | -5.0 | mild_negative_learning |
| earnings_guidance | 66 | 62 | 16 | 46 | 4 | 25.81% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
