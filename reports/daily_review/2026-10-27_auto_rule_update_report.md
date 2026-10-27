# Auto Rule Update Report - 2026-10-27

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
| paid_in_capital_increase | 2351 | 1831 | 1049 | 782 | 520 | 57.29% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2270 | 1637 | 568 | 1069 | 633 | 34.70% | -10.0 | negative_learning |
| supply_contract | 1386 | 1060 | 345 | 715 | 326 | 32.55% | -10.0 | negative_learning |
| convertible_bond | 1158 | 825 | 424 | 401 | 333 | 51.39% | 0.0 | neutral_learning |
| merger | 520 | 425 | 99 | 326 | 95 | 23.29% | -15.0 | strong_negative_learning |
| lawsuit | 466 | 345 | 183 | 162 | 121 | 53.04% | 0.0 | neutral_learning |
| investment_decision | 435 | 320 | 168 | 152 | 115 | 52.50% | 0.0 | neutral_learning |
| disclosure_violation | 182 | 112 | 49 | 63 | 70 | 43.75% | -5.0 | mild_negative_learning |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -15.0 | strong_negative_learning |
| bonus_issue | 104 | 101 | 42 | 59 | 3 | 41.58% | -5.0 | mild_negative_learning |
| spin_off | 114 | 82 | 41 | 41 | 32 | 50.00% | 0.0 | neutral_learning |
| earnings_guidance | 21 | 17 | 15 | 2 | 4 | 88.24% | 11.25 | strong_positive_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
