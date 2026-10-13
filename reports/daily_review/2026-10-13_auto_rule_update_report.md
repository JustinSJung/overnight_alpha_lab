# Auto Rule Update Report - 2026-10-13

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **8**
- Positive adjustment rules: **2**
- Negative adjustment rules: **6**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 1957 | 1439 | 862 | 577 | 518 | 59.90% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1862 | 1229 | 441 | 788 | 633 | 35.88% | -5.0 | mild_negative_learning |
| supply_contract | 1086 | 760 | 212 | 548 | 326 | 27.89% | -10.0 | negative_learning |
| convertible_bond | 984 | 652 | 344 | 308 | 332 | 52.76% | 0.0 | neutral_learning |
| merger | 360 | 265 | 52 | 213 | 95 | 19.62% | -15.0 | strong_negative_learning |
| investment_decision | 373 | 258 | 136 | 122 | 115 | 52.71% | 0.0 | neutral_learning |
| lawsuit | 377 | 257 | 149 | 108 | 120 | 57.98% | 5.0 | mild_positive_learning |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | -5.0 | mild_negative_learning |
| disclosure_violation | 152 | 82 | 41 | 41 | 70 | 50.00% | 0.0 | neutral_learning |
| bond_with_warrant | 77 | 65 | 6 | 59 | 12 | 9.23% | -15.0 | strong_negative_learning |
| spin_off | 90 | 58 | 20 | 38 | 32 | 34.48% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
