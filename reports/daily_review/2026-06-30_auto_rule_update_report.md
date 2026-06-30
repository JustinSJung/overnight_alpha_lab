# Auto Rule Update Report - 2026-06-30

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **9**
- Active learned rules: **0**
- Positive adjustment rules: **0**
- Negative adjustment rules: **0**
- Held due to insufficient data: **9**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| convertible_bond | 12 | 0 | 0 | 0 | 12 | 0.00% | 0.0 | hold_insufficient_data |
| disclosure_violation | 6 | 0 | 0 | 0 | 6 | 0.00% | 0.0 | hold_insufficient_data |
| investment_decision | 15 | 0 | 0 | 0 | 15 | 0.00% | 0.0 | hold_insufficient_data |
| lawsuit | 9 | 0 | 0 | 0 | 9 | 0.00% | 0.0 | hold_insufficient_data |
| major_shareholder_change | 17 | 0 | 0 | 0 | 17 | 0.00% | 0.0 | hold_insufficient_data |
| merger | 6 | 0 | 0 | 0 | 6 | 0.00% | 0.0 | hold_insufficient_data |
| paid_in_capital_increase | 18 | 0 | 0 | 0 | 18 | 0.00% | 0.0 | hold_insufficient_data |
| spin_off | 1 | 0 | 0 | 0 | 1 | 0.00% | 0.0 | hold_insufficient_data |
| supply_contract | 41 | 0 | 0 | 0 | 41 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
