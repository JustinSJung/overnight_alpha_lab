# Auto Rule Update Report - 2026-09-09

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **10**
- Positive adjustment rules: **3**
- Negative adjustment rules: **7**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 893 | 590 | 374 | 216 | 303 | 63.39% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1024 | 541 | 149 | 392 | 483 | 27.54% | -10.0 | negative_learning |
| supply_contract | 579 | 317 | 83 | 234 | 262 | 26.18% | -10.0 | negative_learning |
| convertible_bond | 502 | 229 | 140 | 89 | 273 | 61.14% | 5.0 | mild_positive_learning |
| lawsuit | 168 | 72 | 53 | 19 | 96 | 73.61% | 10.0 | positive_learning |
| investment_decision | 164 | 63 | 29 | 34 | 101 | 46.03% | 0.0 | neutral_learning |
| merger | 135 | 57 | 8 | 49 | 78 | 14.04% | -15.0 | strong_negative_learning |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -10.0 | negative_learning |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -11.25 | strong_negative_learning |
| spin_off | 37 | 15 | 6 | 9 | 22 | 40.00% | -3.75 | mild_negative_learning |
| disclosure_violation | 65 | 15 | 1 | 14 | 50 | 6.67% | -11.25 | strong_negative_learning |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | 0.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
