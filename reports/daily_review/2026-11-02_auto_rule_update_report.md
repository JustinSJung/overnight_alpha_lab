# Auto Rule Update Report - 2026-11-02

## Purpose

This report summarizes automatically learned event-type score adjustments based on accumulated prediction success and failure history.

The original rule-based event scoring file is not overwritten. The learned rules are saved separately and can be safely used as an additional score layer.

## Summary

- Total event types: **12**
- Active learned rules: **9**
- Positive adjustment rules: **3**
- Negative adjustment rules: **6**
- Held due to insufficient data: **0**
- Minimum evaluated count: **5**

## Learned Event Rules

| event_type | total_count | evaluated_count | success_count | failure_count | pending_count | success_rate | learned_event_score_adjustment | learning_label |
|---|---|---|---|---|---|---|---|---|
| paid_in_capital_increase | 2533 | 2012 | 1165 | 847 | 521 | 57.90% | 5.0 | mild_positive_learning |
| major_shareholder_change | 2514 | 1881 | 722 | 1159 | 633 | 38.38% | -5.0 | mild_negative_learning |
| supply_contract | 1537 | 1211 | 407 | 804 | 326 | 33.61% | -10.0 | negative_learning |
| convertible_bond | 1342 | 1009 | 580 | 429 | 333 | 57.48% | 5.0 | mild_positive_learning |
| merger | 737 | 641 | 299 | 342 | 96 | 46.65% | 0.0 | neutral_learning |
| lawsuit | 504 | 383 | 215 | 168 | 121 | 56.14% | 5.0 | mild_positive_learning |
| investment_decision | 487 | 372 | 180 | 192 | 115 | 48.39% | 0.0 | neutral_learning |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | -5.0 | mild_negative_learning |
| disclosure_violation | 190 | 120 | 51 | 69 | 70 | 42.50% | -5.0 | mild_negative_learning |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | -5.0 | mild_negative_learning |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | 0.0 | neutral_learning |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -10.0 | negative_learning |

## Interpretation

- Positive adjustments mean the event type has shown stronger historical performance.
- Negative adjustments mean the event type has shown weaker historical performance.
- Held rules mean there are not enough evaluated cases yet.
- This is a conservative learning layer and should not be interpreted as investment advice.

## Next Step

The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula.
