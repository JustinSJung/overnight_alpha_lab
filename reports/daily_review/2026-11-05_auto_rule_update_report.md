# Auto Rule Update Report - 2026-11-05

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
| paid_in_capital_increase | 2600 | 2079 | 1188 | 891 | 521 | 57.14% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2669 | 2036 | 796 | 1240 | 633 | 39.10% | -5.0 | mild_negative_learning |
| supply_contract | 1609 | 1283 | 437 | 846 | 326 | 34.06% | -10.0 | negative_learning |
| convertible_bond | 1387 | 1054 | 609 | 445 | 333 | 57.78% | 5.0 | mild_positive_learning |
| merger | 760 | 664 | 312 | 352 | 96 | 46.99% | 0.0 | neutral_learning |
| lawsuit | 537 | 416 | 218 | 198 | 121 | 52.40% | 0.0 | neutral_learning |
| investment_decision | 523 | 408 | 204 | 204 | 115 | 50.00% | 0.0 | neutral_learning |
| disclosure_violation | 209 | 139 | 56 | 83 | 70 | 40.29% | -5.0 | mild_negative_learning |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | -5.0 | mild_negative_learning |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | -5.0 | mild_negative_learning |
| spin_off | 124 | 88 | 44 | 44 | 36 | 50.00% | 0.0 | neutral_learning |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
