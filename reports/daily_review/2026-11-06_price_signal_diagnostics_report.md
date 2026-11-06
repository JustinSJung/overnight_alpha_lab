# Price Signal Diagnostics Report - 2026-11-06

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

Evaluation snapshots are deduplicated by the shared stable prediction identity before counting outcomes or assigning daily ranks.
평가 수와 일별 순위는 공통 예측 식별자로 반복 스냅샷을 제거한 뒤 집계합니다.

- Cumulative evaluated cases: **19365**
- Success count: **9650**
- Failure count: **9715**
- Pending count: **20968**
- Raw success rate: **49.83%**
- Wilson reliability score: **49.1 / 100**
- Rolling 7-day success rate: **55.15%**
- Rolling 30-day success rate: **52.71%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **18961**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 627 | 271 | 356 | 43.22% | -0.05% | 0.54% |
| Top 20 | 1104 | 483 | 621 | 43.75% | -0.11% | 0.64% |
| Top 50 | 1791 | 787 | 1004 | 43.94% | -0.25% | 0.55% |
| Top 100 | 2490 | 1068 | 1422 | 42.89% | -0.08% | 0.61% |
| Rest | 16875 | 8582 | 8293 | 50.86% | -0.26% | 0.11% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 627 | 69.60 | 5.12 |
| Top 20 | 1104 | 67.50 | 5.27 |
| Top 50 | 1791 | 65.84 | 5.17 |
| Top 100 | 2490 | 61.51 | 5.13 |
| Rest | 16875 | 32.62 | 7.11 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 31 | 11 | 20 | 35.48% | -0.36% | 1.86% |
| high | 804 | 353 | 451 | 43.91% | 0.01% | 0.69% |
| medium | 1156 | 492 | 664 | 42.56% | -0.34% | 0.55% |
| low | 16970 | 8595 | 8375 | 50.65% | -0.21% | 0.10% |
| unknown | 404 | 199 | 205 | 49.26% | -1.34% | N/A |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 1650 | 765 | 885 | 46.36% | -0.22% | 0.68% |
| high | 876 | 401 | 475 | 45.78% | -0.40% | 0.48% |
| medium | 594 | 320 | 274 | 53.87% | -0.33% | 0.05% |
| low | 15841 | 7965 | 7876 | 50.28% | -0.19% | 0.09% |
| unknown | 404 | 199 | 205 | 49.26% | -1.34% | N/A |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 33 | 11 | 22 | 33.33% | -0.57% | 1.86% |
| high | 804 | 353 | 451 | 43.91% | 0.01% | 0.69% |
| medium | 1159 | 494 | 665 | 42.62% | -0.33% | 0.55% |
| low | 17031 | 8620 | 8411 | 50.61% | -0.21% | 0.10% |
| unknown | 338 | 172 | 166 | 50.89% | -1.72% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 33 | 11 | 22 | 33.33% | -0.57% | 1.86% |
| high | 804 | 353 | 451 | 43.91% | 0.01% | 0.69% |
| medium | 1159 | 494 | 665 | 42.62% | -0.33% | 0.55% |
| low | 17031 | 8620 | 8411 | 50.61% | -0.21% | 0.10% |
| unknown | 338 | 172 | 166 | 50.89% | -1.72% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 72 | 21 | 51 | 29.17% | -1.68% | 1.86% |
| high | 835 | 362 | 473 | 43.35% | -0.04% | 0.69% |
| medium | 1184 | 504 | 680 | 42.57% | -0.38% | 0.55% |
| low | 17274 | 8763 | 8511 | 50.73% | -0.23% | 0.10% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 32 | 14 | 18 | 43.75% | -0.06% | 0.28% |
| nan | 17897 | 8921 | 8976 | 49.85% | -0.23% | 0.15% |
| no_risk_noise | 656 | 351 | 305 | 53.51% | -0.59% | 0.04% |
| risk_noise_detected | 780 | 364 | 416 | 46.67% | -0.07% | 0.07% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 63 | 38 | 25 | 60.32% | -1.87% | -0.71% |
| low_attention | 696 | 335 | 361 | 48.13% | -0.23% | 0.05% |
| medium_attention | 709 | 356 | 353 | 50.21% | -0.23% | 0.15% |
| nan | 17897 | 8921 | 8976 | 49.85% | -0.23% | 0.15% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 894 | 426 | 468 | 47.65% | -0.30% | 0.84% |
| normal | 17421 | 8933 | 8488 | 51.28% | -0.20% | 0.12% |
| unknown | 600 | 33 | 567 | 5.50% | -0.25% | 0.20% |
| very_high | 450 | 258 | 192 | 57.33% | -1.14% | 0.25% |

## Failure Clusters

### High score but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 | 2026-07-07 | 2026-07-07 | 1.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 | -0.0316 |  | failure |
| 368970 |  |  | 2026-07-07 | 2026-07-07 | 4.0 |  |  |  |  | 91.23 |  |  |  | 0.371 | 0.0 |  | failure |
| 065770 |  | CS | 2026-07-07 | 2026-07-07 | 5.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 | -0.0352 |  | failure |
| 002780 |  |  | 2026-07-07 | 2026-07-07 | 6.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 | -0.0561 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 | 7.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 | -0.1234 |  | failure |

### High-score failures under v2

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 053580 |  |  | 2026-07-23 | 2026-07-23 | 4.0 | 70.3 | 70.3 | v2_conservative_ranker | 70.3 | 70.3 | 0.0 | 0.0 | 2.0 | 1.5666 | -0.009 |  | failure |
| 134790 |  |  | 2026-07-27 | 2026-07-27 | 1.0 | 78.04 | 78.04 | v2_conservative_ranker | 78.04 | 78.04 | 0.0 | 0.0 | 2.0 | 1.7208 | -0.0188 |  | failure |
| 340570 |  |  | 2026-07-27 | 2026-07-27 | 5.0 | 68.05 | 68.05 | v2_conservative_ranker | 68.05 | 68.05 | 1.62 | 0.0 | 2.0 | 2.6676 | -0.0514 |  | failure |
| 114450 |  |  | 2026-07-28 | 2026-07-28 | 1.0 | 80.24 | 80.24 | v2_conservative_ranker | 80.24 | 80.24 | 0.66 | 0.0 | 2.0 | 2.0011 | -0.029 |  | failure |
| 004780 |  |  | 2026-07-29 | 2026-07-29 | 3.0 | 66.83 | 66.83 | v2_conservative_ranker | 66.83 | 66.83 | 0.0 | 0.0 | 0.0 | 1.7211 | -0.0037 |  | failure |

### High volume but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065770 |  | CS | 2026-07-07 | 2026-07-07 | 5.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 | -0.0352 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 | 7.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 | -0.1234 |  | failure |
| 263800 |  |  | 2026-07-09 | 2026-07-09 | 1.0 |  |  |  |  | 119.0 |  |  |  | 14.6426 | -0.0544 |  | failure |
| 189330 |  |  | 2026-07-09 | 2026-07-09 | 3.0 |  |  |  |  | 103.0 |  |  |  | 12.8721 | -0.0685 |  | failure |
| 036630 |  |  | 2026-07-09 | 2026-07-09 | 7.0 |  |  |  |  | 83.0 |  |  |  | 9.3765 | -0.0129 |  | failure |

### High risk noise and failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 | 2026-07-07 | 2026-07-07 | 1.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 | -0.0316 |  | failure |
| 368970 |  |  | 2026-07-07 | 2026-07-07 | 4.0 |  |  |  |  | 91.23 |  |  |  | 0.371 | 0.0 |  | failure |
| 065770 |  | CS | 2026-07-07 | 2026-07-07 | 5.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 | -0.0352 |  | failure |
| 002780 |  |  | 2026-07-07 | 2026-07-07 | 6.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 | -0.0561 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 | 7.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 | -0.1234 |  | failure |

### Low score but succeeded

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0126Z0 |  |  | 2026-07-07 | 2026-07-07 | 34.0 |  |  |  |  | 39.08 |  |  |  | 1.0887 | -0.0685 |  | success |
| 025980 |  |  | 2026-07-07 | 2026-07-07 | 35.0 |  |  |  |  | 36.9 |  |  |  | 0.6787 | -0.0401 |  | success |
| 049950 |  |  | 2026-07-07 | 2026-07-07 | 36.0 |  |  |  |  | 36.37 |  |  |  | 0.7108 | -0.051 |  | success |
| 004380 |  |  | 2026-07-07 | 2026-07-07 | 37.0 |  |  |  |  | 35.0 |  |  |  | 0.3365 | -0.0319 |  | success |
| 019570 |  |  | 2026-07-07 | 2026-07-07 | 38.0 |  |  |  |  | 32.09 |  |  |  | 0.0 | -0.1806 |  | success |

### Low-score successes under v2

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010960 |  | 삼호개발 | 2026-07-07 | 2026-07-07 | 2.0 |  |  |  |  | 103.0 |  |  |  | 3.6331 | 0.0644 |  | success |
| 091590 |  | 남화토건 | 2026-07-07 | 2026-07-07 | 3.0 |  |  |  |  | 97.84 |  |  |  | 1.6403 | 0.0797 |  | success |
| 189330 |  | 씨이랩 | 2026-07-07 | 2026-07-07 | 10.0 |  |  |  |  | 78.0 |  |  |  | 0.7827 | 0.2997 |  | success |
| 419540 |  |  | 2026-07-07 | 2026-07-07 | 14.0 |  |  |  |  | 69.23 |  |  |  | 0.4112 | 0.0231 |  | success |
| 008930 |  | 한미사이언스 | 2026-07-07 | 2026-07-07 | 15.0 |  |  |  |  | 68.76 |  |  |  | 0.7538 | 0.0632 |  | success |

## Summary Judgment

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.
- Current ranking diagnosis: Ranking inverted / 랭킹 역방향 가능성
- V2 scoring impact should be judged after several new daily runs.
- V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.