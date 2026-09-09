# Price Signal Diagnostics Report - 2026-09-09

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **90318**
- Success count: **39066**
- Failure count: **51252**
- Pending count: **103290**
- Raw success rate: **43.25%**
- Wilson reliability score: **42.9 / 100**
- Rolling 7-day success rate: **43.86%**
- Rolling 30-day success rate: **43.11%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **76804**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 331 | 107 | 224 | 32.33% | -1.39% | -0.54% |
| Top 20 | 686 | 200 | 486 | 29.15% | -1.54% | -0.76% |
| Top 50 | 1721 | 726 | 995 | 42.18% | -0.35% | -0.16% |
| Top 100 | 3404 | 1597 | 1807 | 46.92% | 0.51% | 0.86% |
| Rest | 86914 | 37469 | 49445 | 43.11% | 0.33% | -0.10% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 331 | 75.92 | 5.12 |
| Top 20 | 686 | 75.34 | 4.91 |
| Top 50 | 1721 | 73.35 | 5.18 |
| Top 100 | 3404 | 71.16 | 5.39 |
| Rest | 86914 | 35.16 | 9.48 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 128 | 44 | 84 | 34.38% | -0.98% | 1.75% |
| high | 6422 | 2831 | 3591 | 44.08% | 0.19% | 0.19% |
| medium | 6655 | 2857 | 3798 | 42.93% | -0.22% | -0.32% |
| low | 63599 | 26443 | 37156 | 41.58% | 0.74% | -0.23% |
| unknown | 13514 | 6891 | 6623 | 50.99% | -1.22% | 1.01% |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 12695 | 6097 | 6598 | 48.03% | -0.48% | -0.38% |
| high | 4783 | 2255 | 2528 | 47.15% | -0.34% | -0.63% |
| medium | 4963 | 2459 | 2504 | 49.55% | 0.69% | 0.46% |
| low | 54363 | 21364 | 32999 | 39.30% | 0.94% | -0.18% |
| unknown | 13514 | 6891 | 6623 | 50.99% | -1.22% | 1.01% |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 205 | 44 | 161 | 21.46% | -2.03% | -0.78% |
| high | 6422 | 2831 | 3591 | 44.08% | 0.19% | 0.19% |
| medium | 6771 | 2934 | 3837 | 43.33% | -0.14% | -0.25% |
| low | 66202 | 27530 | 38672 | 41.58% | 0.71% | -0.29% |
| unknown | 10718 | 5727 | 4991 | 53.43% | -1.59% | 1.96% |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 205 | 44 | 161 | 21.46% | -2.03% | -0.78% |
| high | 6422 | 2831 | 3591 | 44.08% | 0.19% | 0.19% |
| medium | 6771 | 2934 | 3837 | 43.33% | -0.14% | -0.25% |
| low | 66202 | 27530 | 38672 | 41.58% | 0.71% | -0.29% |
| unknown | 10718 | 5727 | 4991 | 53.43% | -1.59% | 1.96% |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 1469 | 434 | 1035 | 29.54% | -2.31% | 1.34% |
| high | 7423 | 3121 | 4302 | 42.04% | 0.03% | 0.46% |
| medium | 7385 | 3093 | 4292 | 41.88% | -0.34% | -0.14% |
| low | 74041 | 32418 | 41623 | 43.78% | 0.48% | -0.13% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 217 | 66 | 151 | 30.41% | 1.15% | -0.85% |
| nan | 83212 | 35906 | 47306 | 43.15% | 0.35% | -0.12% |
| no_risk_noise | 2664 | 1300 | 1364 | 48.80% | 0.57% | 0.90% |
| risk_noise_detected | 4225 | 1794 | 2431 | 42.46% | -0.14% | 0.56% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 255 | 158 | 97 | 61.96% | -3.87% | -4.50% |
| low_attention | 3498 | 1483 | 2015 | 42.40% | -0.11% | 0.69% |
| medium_attention | 3353 | 1519 | 1834 | 45.30% | 0.76% | 1.01% |
| nan | 83212 | 35906 | 47306 | 43.15% | 0.35% | -0.12% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 8677 | 4005 | 4672 | 46.16% | -0.10% | 0.52% |
| normal | 72120 | 32121 | 39999 | 44.54% | 0.54% | -0.03% |
| unknown | 4747 | 196 | 4551 | 4.13% | -0.01% | -0.50% |
| very_high | 4774 | 2744 | 2030 | 57.48% | -1.70% | -1.28% |

## Failure Clusters

### High score but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 119.0 |  |  |  |  | 91.23 |  |  |  | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 158.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 197.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 236.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |

### High-score failures under v2

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 005710 |  |  | 2026-07-21 | 2026-07-21 | 2.0 | 73.55 | 73.55 | v2_conservative_ranker | 73.55 | 73.55 | 0.0 | 0.0 | 1.0 | 1.4671 | -0.0176 |  | failure |
| 005710 |  |  | 2026-07-21 | 2026-07-21 | 3.0 | 73.55 | 73.55 | v2_conservative_ranker | 73.55 | 73.55 | 0.0 | 0.0 | 1.0 | 1.4671 | -0.0176 |  | failure |
| 005710 |  |  | 2026-07-21 | 2026-07-21 | 4.0 | 73.55 | 73.55 | v2_conservative_ranker | 73.55 | 73.55 | 0.0 | 0.0 | 1.0 | 1.4671 | -0.0176 |  | failure |
| 017670 | SK텔레콤 | SK텔레콤 | 2026-07-23 | 2026-07-23 | 2.0 | 81.95 | 81.95 | v2_conservative_ranker | 81.95 | 81.95 | 0.0 | 0.0 | 0.0 | 2.4701 | -0.001 |  | failure |
| 114450 |  |  | 2026-07-23 | 2026-07-23 | 39.0 | 71.43 | 71.43 | v2_conservative_ranker | 71.43 | 71.43 | 0.22 | 0.0 | 1.0 | 1.0865 | -0.0048 |  | failure |

### High volume but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065770 |  | CS |  |  | 158.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 038530 |  |  |  |  | 236.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |
| 065770 |  | CS | 2026-07-07 | 2026-07-07 | 160.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 | -0.0352 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 | 238.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 | -0.1234 |  | failure |
| 263800 |  |  | 2026-07-09 | 2026-07-09 | 3.0 |  |  |  |  | 119.0 |  |  |  | 14.6426 | -0.0544 |  | failure |

### High risk noise and failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 119.0 |  |  |  |  | 91.23 |  |  |  | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 158.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 197.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 236.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |

### Low score but succeeded

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0126Z0 |  |  |  |  | 1289.0 |  |  |  |  | 39.08 |  |  |  | 1.0887 |  |  |  |
| 025980 |  |  |  |  | 1328.0 |  |  |  |  | 36.9 |  |  |  | 0.6787 |  |  |  |
| 049950 |  |  |  |  | 1367.0 |  |  |  |  | 36.37 |  |  |  | 0.7108 |  |  |  |
| 004380 |  |  |  |  | 1406.0 |  |  |  |  | 35.0 |  |  |  | 0.3365 |  |  |  |
| 019570 |  |  |  |  | 1445.0 |  |  |  |  | 32.09 |  |  |  | 0.0 |  |  |  |

### Low-score successes under v2

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010960 |  | 삼호개발 |  |  | 41.0 |  |  |  |  | 103.0 |  |  |  | 3.6331 |  |  |  |
| 091590 |  | 남화토건 |  |  | 80.0 |  |  |  |  | 97.84 |  |  |  | 1.6403 |  |  |  |
| 189330 |  | 씨이랩 |  |  | 353.0 |  |  |  |  | 78.0 |  |  |  | 0.7827 |  |  |  |
| 419540 |  |  |  |  | 509.0 |  |  |  |  | 69.23 |  |  |  | 0.4112 |  |  |  |
| 008930 |  | 한미사이언스 |  |  | 548.0 |  |  |  |  | 68.76 |  |  |  | 0.7538 |  |  |  |

## Summary Judgment

- Ranking quality is still mixed; monitor Top 10 and Top 20 against the full pool over more evaluations.
- 랭킹 품질은 아직 혼재되어 있으므로 Top 10/Top 20과 전체 후보 풀을 더 비교해야 합니다.
- Current ranking diagnosis: Ranking inverted / 랭킹 역방향 가능성
- V2 scoring impact should be judged after several new daily runs.
- V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.