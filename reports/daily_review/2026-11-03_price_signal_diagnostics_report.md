# Price Signal Diagnostics Report - 2026-11-03

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

Evaluation snapshots are deduplicated by the shared stable prediction identity before counting outcomes or assigning daily ranks.
평가 수와 일별 순위는 공통 예측 식별자로 반복 스냅샷을 제거한 뒤 집계합니다.

- Cumulative evaluated cases: **17672**
- Success count: **8524**
- Failure count: **9148**
- Pending count: **19357**
- Raw success rate: **48.23%**
- Wilson reliability score: **47.5 / 100**
- Rolling 7-day success rate: **30.38%**
- Rolling 30-day success rate: **49.71%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **17271**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 606 | 258 | 348 | 42.57% | -0.09% | 0.18% |
| Top 20 | 1053 | 456 | 597 | 43.30% | -0.13% | 0.37% |
| Top 50 | 1678 | 732 | 946 | 43.62% | -0.26% | 0.38% |
| Top 100 | 2375 | 1015 | 1360 | 42.74% | -0.09% | 0.48% |
| Rest | 15297 | 7509 | 7788 | 49.09% | -0.07% | -0.07% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 606 | 69.30 | 5.09 |
| Top 20 | 1053 | 67.28 | 5.30 |
| Top 50 | 1678 | 65.79 | 5.17 |
| Top 100 | 2375 | 61.25 | 5.16 |
| Rest | 15297 | 32.65 | 7.44 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 29 | 8 | 21 | 27.59% | -0.58% | 1.66% |
| high | 761 | 328 | 433 | 43.10% | -0.04% | 0.40% |
| medium | 1086 | 462 | 624 | 42.54% | -0.32% | 0.51% |
| low | 15395 | 7530 | 7865 | 48.91% | -0.02% | -0.08% |
| unknown | 401 | 196 | 205 | 48.88% | -1.36% | N/A |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 1594 | 726 | 868 | 45.55% | -0.20% | 0.55% |
| high | 852 | 391 | 461 | 45.89% | -0.39% | 0.41% |
| medium | 592 | 312 | 280 | 52.70% | -0.03% | 0.18% |
| low | 14233 | 6899 | 7334 | 48.47% | -0.00% | -0.10% |
| unknown | 401 | 196 | 205 | 48.88% | -1.36% | N/A |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 31 | 8 | 23 | 25.81% | -0.78% | 1.66% |
| high | 761 | 328 | 433 | 43.10% | -0.04% | 0.40% |
| medium | 1089 | 464 | 625 | 42.61% | -0.31% | 0.51% |
| low | 15456 | 7556 | 7900 | 48.89% | -0.02% | -0.08% |
| unknown | 335 | 168 | 167 | 50.15% | -1.67% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 31 | 8 | 23 | 25.81% | -0.78% | 1.66% |
| high | 761 | 328 | 433 | 43.10% | -0.04% | 0.40% |
| medium | 1089 | 464 | 625 | 42.61% | -0.31% | 0.51% |
| low | 15456 | 7556 | 7900 | 48.89% | -0.02% | -0.08% |
| unknown | 335 | 168 | 167 | 50.15% | -1.67% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 70 | 18 | 52 | 25.71% | -1.81% | 1.66% |
| high | 792 | 337 | 455 | 42.55% | -0.10% | 0.40% |
| medium | 1112 | 472 | 640 | 42.45% | -0.36% | 0.51% |
| low | 15698 | 7697 | 8001 | 49.03% | -0.04% | -0.08% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 30 | 13 | 17 | 43.33% | 0.42% | 0.39% |
| nan | 16328 | 7870 | 8458 | 48.20% | -0.06% | -0.02% |
| no_risk_noise | 576 | 295 | 281 | 51.22% | -0.39% | -0.14% |
| risk_noise_detected | 738 | 346 | 392 | 46.88% | 0.02% | 0.05% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 55 | 32 | 23 | 58.18% | -2.15% | -1.60% |
| low_attention | 650 | 309 | 341 | 47.54% | -0.11% | 0.03% |
| medium_attention | 639 | 313 | 326 | 48.98% | -0.01% | 0.05% |
| nan | 16328 | 7870 | 8458 | 48.20% | -0.06% | -0.02% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 801 | 372 | 429 | 46.44% | -0.14% | 0.60% |
| normal | 15871 | 7888 | 7983 | 49.70% | -0.04% | -0.05% |
| unknown | 583 | 26 | 557 | 4.46% | -0.20% | 0.03% |
| very_high | 417 | 238 | 179 | 57.07% | -1.03% | 0.13% |

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