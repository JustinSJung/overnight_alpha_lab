# Auto Rule Update Report - 2026-11-04

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **3**
- Negative adjustment rules: **6**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2577 | 2056 | 1184 | 872 | 521 | 57.59% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2639 | 2006 | 785 | 1221 | 633 | 39.13% | -5.0 | mild_negative_learning |
| supply_contract | 1597 | 1271 | 435 | 836 | 326 | 34.23% | -10.0 | negative_learning |
| convertible_bond | 1369 | 1036 | 600 | 436 | 333 | 57.92% | 5.0 | mild_positive_learning |
| merger | 759 | 663 | 311 | 352 | 96 | 46.91% | 0.0 | neutral_learning |
| investment_decision | 515 | 400 | 196 | 204 | 115 | 49.00% | 0.0 | neutral_learning |
| lawsuit | 507 | 386 | 218 | 168 | 121 | 56.48% | 5.0 | mild_positive_learning |
| disclosure_violation | 203 | 133 | 54 | 79 | 70 | 40.60% | -5.0 | mild_negative_learning |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | -5.0 | mild_negative_learning |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | -5.0 | mild_negative_learning |
| spin_off | 118 | 86 | 44 | 42 | 32 | 51.16% | 0.0 | neutral_learning |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
