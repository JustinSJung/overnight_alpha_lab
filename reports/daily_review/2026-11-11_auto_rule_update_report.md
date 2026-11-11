# Auto Rule Update Report - 2026-11-11

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
| paid_in_capital_increase | 2819 | 2298 | 1290 | 1008 | 521 | 56.14% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2892 | 2258 | 902 | 1356 | 634 | 39.95% | -5.0 | mild_negative_learning |
| supply_contract | 1729 | 1403 | 503 | 900 | 326 | 35.85% | -5.0 | mild_negative_learning |
| convertible_bond | 1502 | 1169 | 675 | 494 | 333 | 57.74% | 5.0 | mild_positive_learning |
| merger | 821 | 725 | 318 | 407 | 96 | 43.86% | -5.0 | mild_negative_learning |
| investment_decision | 575 | 460 | 240 | 220 | 115 | 52.17% | 0.0 | neutral_learning |
| lawsuit | 576 | 455 | 236 | 219 | 121 | 51.87% | 0.0 | neutral_learning |
| disclosure_violation | 212 | 142 | 58 | 84 | 70 | 40.85% | -5.0 | mild_negative_learning |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | -5.0 | mild_negative_learning |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 0.0 | neutral_learning |
| spin_off | 152 | 116 | 44 | 72 | 36 | 37.93% | -5.0 | mild_negative_learning |
| earnings_guidance | 68 | 64 | 16 | 48 | 4 | 25.00% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
