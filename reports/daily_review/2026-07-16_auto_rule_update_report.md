# Auto Rule Update Report - 2026-07-16

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **11**
- Active learned rules: **0**
- Positive adjustment rules: **0**
- Negative adjustment rules: **0**
- Held due to insufficient data: **11**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| bonus_issue | 1 | 0 | 0 | 0 | 1 | 0.00% | 0.0 | hold_insufficient_data |
| convertible_bond | 63 | 0 | 0 | 0 | 63 | 0.00% | 0.0 | hold_insufficient_data |
| disclosure_violation | 13 | 0 | 0 | 0 | 13 | 0.00% | 0.0 | hold_insufficient_data |
| earnings_guidance | 2 | 0 | 0 | 0 | 2 | 0.00% | 0.0 | hold_insufficient_data |
| investment_decision | 33 | 0 | 0 | 0 | 33 | 0.00% | 0.0 | hold_insufficient_data |
| lawsuit | 40 | 0 | 0 | 0 | 40 | 0.00% | 0.0 | hold_insufficient_data |
| major_shareholder_change | 76 | 0 | 0 | 0 | 76 | 0.00% | 0.0 | hold_insufficient_data |
| merger | 18 | 0 | 0 | 0 | 18 | 0.00% | 0.0 | hold_insufficient_data |
| paid_in_capital_increase | 57 | 0 | 0 | 0 | 57 | 0.00% | 0.0 | hold_insufficient_data |
| spin_off | 2 | 0 | 0 | 0 | 2 | 0.00% | 0.0 | hold_insufficient_data |
| supply_contract | 76 | 0 | 0 | 0 | 76 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
