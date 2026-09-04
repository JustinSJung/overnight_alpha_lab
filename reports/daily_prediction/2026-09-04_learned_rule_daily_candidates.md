# Learned-Rule Daily Candidate Report - 2026-09-04

## Purpose

This report applies learned event-rule score adjustments to the daily candidate scoring formula.

The current v4 score formula is:

```text
base_event_score
+ market_adjusted_score_adjustment
+ trading_volume_score_adjustment
+ learned_event_score_adjustment
= final_learned_rule_score
```

This report is for research and portfolio demonstration purposes only. It is not investment advice.

## Summary

- Total candidate rows: **1547**
- Rows with active learned-rule adjustment: **1547**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 845 |
| general_review | 677 |
| watchlist_candidate | 24 |
| volatile_watchlist | 1 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 012170 | 아센디오 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 042660 | 한화오션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 042660 | 한화오션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267850 | 아시아나IDT | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 073490 | LIG아큐버 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 002020 | 코오롱 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 042660 | 한화오션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 277880 | 티에스아이 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 003070 | 코오롱글로벌 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 002460 | HS화성 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 042660 | 한화오션 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -15.0 | 55.0 | watchlist_candidate | strong_negative_learning | 265 | 23.02% |
| 187660 | 페니트리움바이오 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 5.0 | 35.0 | volatile_watchlist | mild_positive_learning | 35 | 57.14% |
| 175250 | 아이큐어 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 385 | 30.13% |
| 175250 | 아이큐어 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 385 | 30.13% |
| 175250 | 아이큐어 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 385 | 30.13% |
| 175250 | 아이큐어 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 385 | 30.13% |
| 175250 | 아이큐어 | major_shareholder_change | volatile | 10.0 | 0.0 | 0.0 | -10.0 | 0.0 | general_review | negative_learning | 385 | 30.13% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
