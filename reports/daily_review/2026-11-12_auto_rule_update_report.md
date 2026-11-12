# Auto Rule Update Report - 2026-11-12

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **2**
- Negative adjustment rules: **7**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2846 | 2325 | 1301 | 1024 | 521 | 55.96% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2930 | 2296 | 923 | 1373 | 634 | 40.20% | -5.0 | mild_negative_learning |
| supply_contract | 1741 | 1415 | 507 | 908 | 326 | 35.83% | -5.0 | mild_negative_learning |
| convertible_bond | 1531 | 1198 | 692 | 506 | 333 | 57.76% | 5.0 | mild_positive_learning |
| merger | 824 | 728 | 319 | 409 | 96 | 43.82% | -5.0 | mild_negative_learning |
| investment_decision | 580 | 465 | 240 | 225 | 115 | 51.61% | 0.0 | neutral_learning |
| lawsuit | 578 | 457 | 238 | 219 | 121 | 52.08% | 0.0 | neutral_learning |
| disclosure_violation | 214 | 144 | 59 | 85 | 70 | 40.97% | -5.0 | mild_negative_learning |
| bond_with_warrant | 154 | 142 | 62 | 80 | 12 | 43.66% | -5.0 | mild_negative_learning |
| spin_off | 154 | 118 | 46 | 72 | 36 | 38.98% | -5.0 | mild_negative_learning |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 0.0 | neutral_learning |
| earnings_guidance | 86 | 82 | 16 | 66 | 4 | 19.51% | -15.0 | strong_negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
