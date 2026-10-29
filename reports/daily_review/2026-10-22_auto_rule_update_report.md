# Auto Rule Update Report - 2026-10-22

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
| paid_in_capital_increase | 2233 | 1713 | 980 | 733 | 520 | 57.21% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2160 | 1527 | 533 | 994 | 633 | 34.91% | -10.0 | negative_learning |
| supply_contract | 1299 | 973 | 300 | 673 | 326 | 30.83% | -10.0 | negative_learning |
| convertible_bond | 1127 | 795 | 412 | 383 | 332 | 51.82% | 0.0 | neutral_learning |
| merger | 419 | 324 | 63 | 261 | 95 | 19.44% | -15.0 | strong_negative_learning |
| lawsuit | 434 | 313 | 176 | 137 | 121 | 56.23% | 5.0 | mild_positive_learning |
| investment_decision | 410 | 295 | 157 | 138 | 115 | 53.22% | 0.0 | neutral_learning |
| disclosure_violation | 182 | 112 | 49 | 63 | 70 | 43.75% | -5.0 | mild_negative_learning |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -15.0 | strong_negative_learning |
| bonus_issue | 103 | 100 | 42 | 58 | 3 | 42.00% | -5.0 | mild_negative_learning |
| spin_off | 113 | 81 | 41 | 40 | 32 | 50.62% | 0.0 | neutral_learning |
| earnings_guidance | 10 | 6 | 4 | 2 | 4 | 66.67% | 5.0 | positive_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
