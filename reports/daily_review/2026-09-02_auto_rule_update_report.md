# Auto Rule Update Report - 2026-09-02

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **2**
- Negative adjustment rules: **7**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| major_shareholder_change | 666 | 246 | 54 | 192 | 420 | 21.95% | -15.0 | strong_negative_learning |
| paid_in_capital_increase | 476 | 220 | 117 | 103 | 256 | 53.18% | 0.0 | neutral_learning |
| supply_contract | 459 | 216 | 37 | 179 | 243 | 17.13% | -15.0 | strong_negative_learning |
| convertible_bond | 400 | 153 | 107 | 46 | 247 | 69.93% | 10.0 | positive_learning |
| lawsuit | 125 | 34 | 31 | 3 | 91 | 91.18% | 15.0 | strong_positive_learning |
| merger | 86 | 25 | 2 | 23 | 61 | 8.00% | -11.25 | strong_negative_learning |
| investment_decision | 115 | 23 | 11 | 12 | 92 | 47.83% | 0.0 | neutral_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| spin_off | 27 | 8 | 3 | 5 | 19 | 37.50% | -2.5 | mild_negative_learning |
| bonus_issue | 11 | 8 | 0 | 8 | 3 | 0.00% | -7.5 | strong_negative_learning |
| disclosure_violation | 54 | 6 | 1 | 5 | 48 | 16.67% | -7.5 | strong_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
