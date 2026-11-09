# Auto Rule Update Report - 2026-11-09

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
| major_shareholder_change | 2823 | 2190 | 865 | 1325 | 633 | 39.50% | -5.0 | mild_negative_learning |
| paid_in_capital_increase | 2708 | 2187 | 1256 | 931 | 521 | 57.43% | 5.0 | mild_positive_learning |
| supply_contract | 1689 | 1363 | 473 | 890 | 326 | 34.70% | -10.0 | negative_learning |
| convertible_bond | 1422 | 1089 | 632 | 457 | 333 | 58.03% | 5.0 | mild_positive_learning |
| merger | 797 | 701 | 315 | 386 | 96 | 44.94% | -5.0 | mild_negative_learning |
| lawsuit | 557 | 436 | 223 | 213 | 121 | 51.15% | 0.0 | neutral_learning |
| investment_decision | 537 | 422 | 210 | 212 | 115 | 49.76% | 0.0 | neutral_learning |
| disclosure_violation | 209 | 139 | 56 | 83 | 70 | 40.29% | -5.0 | mild_negative_learning |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | -5.0 | mild_negative_learning |
| spin_off | 150 | 114 | 44 | 70 | 36 | 38.60% | -5.0 | mild_negative_learning |
| bonus_issue | 107 | 104 | 44 | 60 | 3 | 42.31% | -5.0 | mild_negative_learning |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
