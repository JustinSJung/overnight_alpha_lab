# Auto Rule Update Report - 2026-08-31

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **5**
- Positive adjustment rules: **0**
- Negative adjustment rules: **5**
- Held due to insufficient data: **6**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| major_shareholder_change | 526 | 106 | 22 | 84 | 420 | 20.75% | -15.0 | strong_negative_learning |
| paid_in_capital_increase | 319 | 63 | 25 | 38 | 256 | 39.68% | -5.0 | mild_negative_learning |
| supply_contract | 303 | 60 | 12 | 48 | 243 | 20.00% | -15.0 | strong_negative_learning |
| convertible_bond | 282 | 35 | 17 | 18 | 247 | 48.57% | 0.0 | neutral_learning |
| merger | 71 | 10 | 0 | 10 | 61 | 0.00% | -11.25 | strong_negative_learning |
| spin_off | 24 | 6 | 2 | 4 | 18 | 33.33% | -5.0 | negative_learning |
| lawsuit | 95 | 4 | 4 | 0 | 91 | 100.00% | 0.0 | hold_insufficient_data |
| disclosure_violation | 52 | 4 | 0 | 4 | 48 | 0.00% | 0.0 | hold_insufficient_data |
| investment_decision | 96 | 4 | 0 | 4 | 92 | 0.00% | 0.0 | hold_insufficient_data |
| bond_with_warrant | 10 | 0 | 0 | 0 | 10 | 0.00% | 0.0 | hold_insufficient_data |
| bonus_issue | 3 | 0 | 0 | 0 | 3 | 0.00% | 0.0 | hold_insufficient_data |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
