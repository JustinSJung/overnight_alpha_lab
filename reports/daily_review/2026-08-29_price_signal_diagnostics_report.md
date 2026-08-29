# Price Signal Diagnostics Report - 2026-08-29

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **60363**
- Success count: **26177**
- Failure count: **34186**
- Pending count: **64152**
- Raw success rate: **43.37%**
- Wilson reliability score: **43.0 / 100**
- Rolling 7-day success rate: **38.52%**
- Rolling 30-day success rate: **35.48%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **47882**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 272 | 75 | 197 | 27.57% | -1.76% | -0.72% |
| Top 20 | 570 | 197 | 373 | 34.56% | -1.33% | -0.24% |
| Top 50 | 1435 | 627 | 808 | 43.69% | 0.33% | 0.58% |
| Top 100 | 2779 | 1291 | 1488 | 46.46% | 0.41% | 0.64% |
| Rest | 57584 | 24886 | 32698 | 43.22% | 0.28% | -0.15% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 272 | 76.11 | 4.71 |
| Top 20 | 570 | 75.45 | 4.62 |
| Top 50 | 1435 | 73.05 | 5.23 |
| Top 100 | 2779 | 70.49 | 5.29 |
| Rest | 57584 | 34.20 | 8.96 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 81 | 29 | 52 | 35.80% | -0.77% | 2.55% |
| high | 3930 | 1759 | 2171 | 44.76% | 0.23% | 0.28% |
| medium | 3852 | 1700 | 2152 | 44.13% | -0.20% | -0.43% |
| low | 40019 | 16282 | 23737 | 40.69% | 0.81% | -0.39% |
| unknown | 12481 | 6407 | 6074 | 51.33% | -1.21% | 1.08% |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 7693 | 3796 | 3897 | 49.34% | -0.62% | -0.52% |
| high | 2763 | 1330 | 1433 | 48.14% | -0.35% | -0.89% |
| medium | 2935 | 1412 | 1523 | 48.11% | 1.00% | 0.62% |
| low | 34491 | 13232 | 21259 | 38.36% | 1.02% | -0.33% |
| unknown | 12481 | 6407 | 6074 | 51.33% | -1.21% | 1.08% |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 143 | 29 | 114 | 20.28% | -2.07% | -0.65% |
| high | 3930 | 1759 | 2171 | 44.76% | 0.23% | 0.28% |
| medium | 3945 | 1762 | 2183 | 44.66% | -0.08% | -0.35% |
| low | 42146 | 17173 | 24973 | 40.75% | 0.77% | -0.47% |
| unknown | 10199 | 5454 | 4745 | 53.48% | -1.52% | 1.89% |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 143 | 29 | 114 | 20.28% | -2.07% | -0.65% |
| high | 3930 | 1759 | 2171 | 44.76% | 0.23% | 0.28% |
| medium | 3945 | 1762 | 2183 | 44.66% | -0.08% | -0.35% |
| low | 42146 | 17173 | 24973 | 40.75% | 0.77% | -0.47% |
| unknown | 10199 | 5454 | 4745 | 53.48% | -1.52% | 1.89% |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 1370 | 405 | 965 | 29.56% | -2.49% | 1.13% |
| high | 4910 | 2042 | 2868 | 41.59% | 0.01% | 0.69% |
| medium | 4465 | 1873 | 2592 | 41.95% | -0.34% | -0.19% |
| low | 49618 | 21857 | 27761 | 44.05% | 0.45% | -0.22% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 130 | 42 | 88 | 32.31% | -0.28% | -3.36% |
| nan | 55814 | 24169 | 31645 | 43.30% | 0.31% | -0.18% |
| no_risk_noise | 1697 | 833 | 864 | 49.09% | 0.74% | 1.47% |
| risk_noise_detected | 2722 | 1133 | 1589 | 41.62% | -0.48% | 0.38% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 152 | 105 | 47 | 69.08% | -5.32% | -6.41% |
| low_attention | 2271 | 930 | 1341 | 40.95% | -0.48% | 0.68% |
| medium_attention | 2126 | 973 | 1153 | 45.77% | 0.85% | 1.22% |
| nan | 55814 | 24169 | 31645 | 43.30% | 0.31% | -0.18% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 5992 | 2810 | 3182 | 46.90% | -0.14% | 0.70% |
| normal | 47859 | 21404 | 26455 | 44.72% | 0.51% | -0.11% |
| unknown | 3215 | 136 | 3079 | 4.23% | 0.01% | -0.56% |
| very_high | 3297 | 1827 | 1470 | 55.41% | -1.92% | -1.37% |

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
| 114450 |  |  | 2026-07-23 | 2026-07-23 | 31.0 | 71.43 | 71.43 | v2_conservative_ranker | 71.43 | 71.43 | 0.22 | 0.0 | 1.0 | 1.0865 | -0.0048 |  | failure |

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