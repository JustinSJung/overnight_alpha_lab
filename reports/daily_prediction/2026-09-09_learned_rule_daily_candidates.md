# Learned-Rule Daily Candidate Report - 2026-09-09

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

- Total candidate rows: **499**
- Rows with active learned-rule adjustment: **495**

## Candidate Buckets

| Bucket | Count |
|---|---:|
| risk_or_avoid_review | 368 |
| general_review | 113 |
| watchlist_candidate | 18 |

## Top Candidates

| stock_code | corp_name | event_type | prediction_direction | base_event_score_v4 | market_adjusted_score_adjustment | trading_volume_score_adjustment | learned_event_score_adjustment | final_learned_rule_score | candidate_bucket | learning_label | evaluated_count | success_rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 389260 | 대명에너지 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 009540 | HD한국조선해양 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 317400 | 자이에스앤디 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 267250 | HD현대 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 076080 | 웰크론한텍 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 002780 | 진흥기업 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 037370 | EG | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 003070 | 코오롱글로벌 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 002020 | 코오롱 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 011200 | HMM | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 011370 | 서한 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 010960 | 삼호개발 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 002990 | 금호건설 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 490470 | 세미파이브 | supply_contract | positive | 70.0 | 0.0 | 0.0 | -10.0 | 60.0 | watchlist_candidate | negative_learning | 317 | 26.18% |
| 226950 | 올릭스 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 63 | 46.03% |
| 096350 | 대창솔루션 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 63 | 46.03% |
| 096350 | 대창솔루션 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 63 | 46.03% |
| 096350 | 대창솔루션 | investment_decision | volatile | 30.0 | 0.0 | 0.0 | 0.0 | 30.0 | watchlist_candidate | neutral_learning | 63 | 46.03% |
| 203400 | 에이비온 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -3.75 | 26.25 | general_review | mild_negative_learning | 15 | 40.00% |
| 050110 | 캠시스 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -3.75 | 26.25 | general_review | mild_negative_learning | 15 | 40.00% |
| 033340 | 좋은사람들 | spin_off | volatile | 30.0 | 0.0 | 0.0 | -3.75 | 26.25 | general_review | mild_negative_learning | 15 | 40.00% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 199730 | 바이오인프라 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |
| 033290 | 로젠 | merger | volatile | 30.0 | 0.0 | 0.0 | -15.0 | 15.0 | general_review | strong_negative_learning | 57 | 14.04% |

## Interpretation

- Positive learned-rule adjustments mean that the event type has historically performed better.
- Negative learned-rule adjustments mean that the event type has historically performed worse.
- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.
- This layer is conservative and does not overwrite the original event scoring rules.
