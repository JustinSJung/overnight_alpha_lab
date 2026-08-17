# Auto Rule Update Report - 2026-08-17

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **0**
- Positive adjustment rules: **0**
- Negative adjustment rules: **0**
- Held due to insufficient data: **12**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| bond_with_warrant | 10 | 0 | 0 | 0 | 10 | 0.00% | 0.0 | hold_insufficient_data |
| bonus_issue | 3 | 0 | 0 | 0 | 3 | 0.00% | 0.0 | hold_insufficient_data |
| convertible_bond | 150 | 0 | 0 | 0 | 150 | 0.00% | 0.0 | hold_insufficient_data |
| disclosure_violation | 35 | 0 | 0 | 0 | 35 | 0.00% | 0.0 | hold_insufficient_data |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |
| investment_decision | 85 | 0 | 0 | 0 | 85 | 0.00% | 0.0 | hold_insufficient_data |
| lawsuit | 82 | 0 | 0 | 0 | 82 | 0.00% | 0.0 | hold_insufficient_data |
| major_shareholder_change | 275 | 0 | 0 | 0 | 275 | 0.00% | 0.0 | hold_insufficient_data |
| merger | 46 | 0 | 0 | 0 | 46 | 0.00% | 0.0 | hold_insufficient_data |
| paid_in_capital_increase | 150 | 0 | 0 | 0 | 150 | 0.00% | 0.0 | hold_insufficient_data |
| spin_off | 8 | 0 | 0 | 0 | 8 | 0.00% | 0.0 | hold_insufficient_data |
| supply_contract | 148 | 0 | 0 | 0 | 148 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
