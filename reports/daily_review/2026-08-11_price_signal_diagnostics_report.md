# Price Signal Diagnostics Report - 2026-08-11

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **22933**
- Success count: **10419**
- Failure count: **12514**
- Pending count: **21887**
- Raw success rate: **45.43%**
- Wilson reliability score: **44.8 / 100**
- Rolling 7-day success rate: **42.62%**
- Rolling 30-day success rate: **45.44%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **15067**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 172 | 66 | 106 | 38.37% | -1.13% | 1.85% |
| Top 20 | 356 | 150 | 206 | 42.13% | -0.84% | 0.46% |
| Top 50 | 876 | 442 | 434 | 50.46% | 0.62% | 1.46% |
| Top 100 | 1574 | 770 | 804 | 48.92% | 0.36% | 1.81% |
| Rest | 21359 | 9649 | 11710 | 45.18% | -0.00% | -0.14% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 172 | 75.37 | 4.02 |
| Top 20 | 356 | 73.40 | 4.17 |
| Top 50 | 876 | 69.57 | 4.26 |
| Top 100 | 1574 | 67.69 | 4.23 |
| Rest | 21359 | 29.99 | 7.36 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 28 | 14 | 14 | 50.00% | -0.89% | 4.41% |
| high | 667 | 325 | 342 | 48.73% | 0.48% | 2.35% |
| medium | 586 | 337 | 249 | 57.51% | 0.70% | 0.89% |
| low | 13786 | 5682 | 8104 | 41.22% | 0.69% | -0.49% |
| unknown | 7866 | 4061 | 3805 | 51.63% | -1.25% | 1.01% |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 1412 | 814 | 598 | 57.65% | -1.33% | 0.03% |
| high | 521 | 303 | 218 | 58.16% | -0.66% | -1.02% |
| medium | 708 | 319 | 389 | 45.06% | 1.99% | 1.69% |
| low | 12426 | 4922 | 7504 | 39.61% | 0.89% | -0.42% |
| unknown | 7866 | 4061 | 3805 | 51.63% | -1.25% | 1.01% |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 64 | 14 | 50 | 21.88% | -2.51% | -0.49% |
| high | 667 | 325 | 342 | 48.73% | 0.48% | 2.35% |
| medium | 640 | 373 | 267 | 58.28% | 1.02% | 1.07% |
| low | 15028 | 6204 | 8824 | 41.28% | 0.64% | -0.59% |
| unknown | 6534 | 3503 | 3031 | 53.61% | -1.53% | 1.79% |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 64 | 14 | 50 | 21.88% | -2.51% | -0.49% |
| high | 667 | 325 | 342 | 48.73% | 0.48% | 2.35% |
| medium | 640 | 373 | 267 | 58.28% | 1.02% | 1.07% |
| low | 15028 | 6204 | 8824 | 41.28% | 0.64% | -0.59% |
| unknown | 6534 | 3503 | 3031 | 53.61% | -1.53% | 1.79% |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 865 | 258 | 607 | 29.83% | -2.59% | 1.17% |
| high | 1306 | 512 | 794 | 39.20% | -0.16% | 2.64% |
| medium | 961 | 444 | 517 | 46.20% | 0.08% | 1.26% |
| low | 19801 | 9205 | 10596 | 46.49% | 0.14% | -0.26% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 69 | 25 | 44 | 36.23% | -0.64% | -2.77% |
| nan | 20806 | 9488 | 11318 | 45.60% | 0.05% | -0.11% |
| no_risk_noise | 799 | 390 | 409 | 48.81% | 0.69% | 2.34% |
| risk_noise_detected | 1259 | 516 | 743 | 40.98% | -0.80% | 0.70% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 56 | 50 | 6 | 89.29% | -7.81% | -8.44% |
| low_attention | 1083 | 428 | 655 | 39.52% | -0.90% | 1.02% |
| medium_attention | 988 | 453 | 535 | 45.85% | 0.92% | 2.00% |
| nan | 20806 | 9488 | 11318 | 45.60% | 0.05% | -0.11% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 2038 | 1035 | 1003 | 50.79% | -0.38% | 1.48% |
| normal | 18441 | 8672 | 9769 | 47.03% | 0.18% | -0.11% |
| unknown | 1167 | 58 | 1109 | 4.97% | 0.25% | -0.27% |
| very_high | 1287 | 654 | 633 | 50.82% | -1.90% | -0.86% |

## Failure Clusters

### High score but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 83.0 |  |  |  |  | 91.23 |  |  |  | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 110.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 137.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 164.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |

### High-score failures under v2

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 005710 |  |  | 2026-07-21 | 2026-07-21 | 2.0 | 73.55 | 73.55 | v2_conservative_ranker | 73.55 | 73.55 | 0.0 | 0.0 | 1.0 | 1.4671 | -0.0176 |  | failure |
| 005710 |  |  | 2026-07-21 | 2026-07-21 | 3.0 | 73.55 | 73.55 | v2_conservative_ranker | 73.55 | 73.55 | 0.0 | 0.0 | 1.0 | 1.4671 | -0.0176 |  | failure |
| 005710 |  |  | 2026-07-21 | 2026-07-21 | 4.0 | 73.55 | 73.55 | v2_conservative_ranker | 73.55 | 73.55 | 0.0 | 0.0 | 1.0 | 1.4671 | -0.0176 |  | failure |
| 017670 | SK텔레콤 | SK텔레콤 | 2026-07-23 | 2026-07-23 | 2.0 | 81.95 | 81.95 | v2_conservative_ranker | 81.95 | 81.95 | 0.0 | 0.0 | 0.0 | 2.4701 | -0.001 |  | failure |
| 114450 |  |  | 2026-07-23 | 2026-07-23 | 18.0 | 71.43 | 71.43 | v2_conservative_ranker | 71.43 | 71.43 | 0.22 | 0.0 | 1.0 | 1.0865 | -0.0048 |  | failure |

### High volume but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065770 |  | CS |  |  | 110.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 038530 |  |  |  |  | 164.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |
| 065770 |  | CS | 2026-07-07 | 2026-07-07 | 112.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 | -0.0352 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 | 166.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 | -0.1234 |  | failure |
| 263800 |  |  | 2026-07-09 | 2026-07-09 | 3.0 |  |  |  |  | 119.0 |  |  |  | 14.6426 | -0.0544 |  | failure |

### High risk noise and failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 83.0 |  |  |  |  | 91.23 |  |  |  | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 110.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 137.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 164.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |

### Low score but succeeded

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0126Z0 |  |  |  |  | 893.0 |  |  |  |  | 39.08 |  |  |  | 1.0887 |  |  |  |
| 025980 |  |  |  |  | 920.0 |  |  |  |  | 36.9 |  |  |  | 0.6787 |  |  |  |
| 049950 |  |  |  |  | 947.0 |  |  |  |  | 36.37 |  |  |  | 0.7108 |  |  |  |
| 004380 |  |  |  |  | 974.0 |  |  |  |  | 35.0 |  |  |  | 0.3365 |  |  |  |
| 019570 |  |  |  |  | 1001.0 |  |  |  |  | 32.09 |  |  |  | 0.0 |  |  |  |

### Low-score successes under v2

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010960 |  | 삼호개발 |  |  | 29.0 |  |  |  |  | 103.0 |  |  |  | 3.6331 |  |  |  |
| 091590 |  | 남화토건 |  |  | 56.0 |  |  |  |  | 97.84 |  |  |  | 1.6403 |  |  |  |
| 189330 |  | 씨이랩 |  |  | 245.0 |  |  |  |  | 78.0 |  |  |  | 0.7827 |  |  |  |
| 419540 |  |  |  |  | 353.0 |  |  |  |  | 69.23 |  |  |  | 0.4112 |  |  |  |
| 008930 |  | 한미사이언스 |  |  | 380.0 |  |  |  |  | 68.76 |  |  |  | 0.7538 |  |  |  |

## Summary Judgment

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.
- Current ranking diagnosis: Ranking inverted / 랭킹 역방향 가능성
- V2 scoring impact should be judged after several new daily runs.
- V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.