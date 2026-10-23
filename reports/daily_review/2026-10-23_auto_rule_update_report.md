# Auto Rule Update Report - 2026-10-23

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
| paid_in_capital_increase | 2272 | 1752 | 1013 | 739 | 520 | 57.82% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2182 | 1549 | 541 | 1008 | 633 | 34.93% | -10.0 | negative_learning |
| supply_contract | 1314 | 988 | 302 | 686 | 326 | 30.57% | -10.0 | negative_learning |
| convertible_bond | 1145 | 812 | 415 | 397 | 333 | 51.11% | 0.0 | neutral_learning |
| merger | 447 | 352 | 70 | 282 | 95 | 19.89% | -15.0 | strong_negative_learning |
| lawsuit | 440 | 319 | 176 | 143 | 121 | 55.17% | 5.0 | mild_positive_learning |
| investment_decision | 421 | 306 | 159 | 147 | 115 | 51.96% | 0.0 | neutral_learning |
| disclosure_violation | 182 | 112 | 49 | 63 | 70 | 43.75% | -5.0 | mild_negative_learning |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -15.0 | strong_negative_learning |
| bonus_issue | 103 | 100 | 42 | 58 | 3 | 42.00% | -5.0 | mild_negative_learning |
| spin_off | 113 | 81 | 41 | 40 | 32 | 50.62% | 0.0 | neutral_learning |
| earnings_guidance | 15 | 11 | 9 | 2 | 4 | 81.82% | 11.25 | strong_positive_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
