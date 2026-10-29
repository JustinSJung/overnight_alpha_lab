# Auto Rule Update Report - 2026-10-14

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
| paid_in_capital_increase | 2036 | 1518 | 871 | 647 | 518 | 57.38% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1911 | 1278 | 442 | 836 | 633 | 34.59% | -10.0 | negative_learning |
| supply_contract | 1114 | 788 | 220 | 568 | 326 | 27.92% | -10.0 | negative_learning |
| convertible_bond | 997 | 665 | 355 | 310 | 332 | 53.38% | 0.0 | neutral_learning |
| merger | 364 | 269 | 53 | 216 | 95 | 19.70% | -15.0 | strong_negative_learning |
| investment_decision | 378 | 263 | 141 | 122 | 115 | 53.61% | 0.0 | neutral_learning |
| lawsuit | 379 | 259 | 151 | 108 | 120 | 58.30% | 5.0 | mild_positive_learning |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | -5.0 | mild_negative_learning |
| disclosure_violation | 153 | 83 | 41 | 42 | 70 | 49.40% | 0.0 | neutral_learning |
| bond_with_warrant | 86 | 74 | 15 | 59 | 12 | 20.27% | -15.0 | strong_negative_learning |
| spin_off | 90 | 58 | 20 | 38 | 32 | 34.48% | -10.0 | negative_learning |
| earnings_guidance | 8 | 4 | 4 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
