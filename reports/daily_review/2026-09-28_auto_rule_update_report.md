# Auto Rule Update Report - 2026-09-28

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **7**
- Positive adjustment rules: **2**
- Negative adjustment rules: **5**
- Held due to insufficient data: **1**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 1536 | 1165 | 676 | 489 | 371 | 58.03% | 5.0 | mild_positive_learning |
| major_shareholder_change | 1554 | 1015 | 338 | 677 | 539 | 33.30% | -10.0 | negative_learning |
| supply_contract | 858 | 580 | 167 | 413 | 278 | 28.79% | -10.0 | negative_learning |
| convertible_bond | 801 | 513 | 251 | 262 | 288 | 48.93% | 0.0 | neutral_learning |
| investment_decision | 322 | 216 | 109 | 107 | 106 | 50.46% | 0.0 | neutral_learning |
| lawsuit | 295 | 182 | 111 | 71 | 113 | 60.99% | 5.0 | mild_positive_learning |
| merger | 197 | 117 | 25 | 92 | 80 | 21.37% | -15.0 | strong_negative_learning |
| disclosure_violation | 125 | 70 | 37 | 33 | 55 | 52.86% | 0.0 | neutral_learning |
| bonus_issue | 65 | 62 | 29 | 33 | 3 | 46.77% | 0.0 | neutral_learning |
| bond_with_warrant | 72 | 61 | 5 | 56 | 11 | 8.20% | -15.0 | strong_negative_learning |
| spin_off | 72 | 48 | 15 | 33 | 24 | 31.25% | -10.0 | negative_learning |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 0.0 | hold_insufficient_data |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
