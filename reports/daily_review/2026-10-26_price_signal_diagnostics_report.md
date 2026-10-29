# Price Signal Diagnostics Report - 2026-10-26

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **376843**
- Success count: **174982**
- Failure count: **201861**
- Pending count: **459648**
- Raw success rate: **46.43%**
- Wilson reliability score: **46.3 / 100**
- Rolling 7-day success rate: **67.14%**
- Rolling 30-day success rate: **51.89%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **358906**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 563 | 170 | 393 | 30.20% | -1.27% | -0.51% |
| Top 20 | 1175 | 362 | 813 | 30.81% | -1.25% | -0.60% |
| Top 50 | 2950 | 977 | 1973 | 33.12% | -0.86% | -0.38% |
| Top 100 | 5911 | 2255 | 3656 | 38.15% | -0.30% | 0.18% |
| Rest | 370932 | 172727 | 198205 | 46.57% | 0.14% | 0.12% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 563 | 75.87 | 4.71 |
| Top 20 | 1175 | 75.61 | 4.68 |
| Top 50 | 2950 | 74.52 | 4.74 |
| Top 100 | 5911 | 72.95 | 4.95 |
| Rest | 370932 | 36.50 | 8.58 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 647 | 199 | 448 | 30.76% | -0.90% | 0.66% |
| high | 23259 | 10165 | 13094 | 43.70% | 0.09% | 0.10% |
| medium | 30548 | 13238 | 17310 | 43.34% | -0.20% | 0.12% |
| low | 304452 | 142396 | 162056 | 46.77% | 0.26% | 0.10% |
| unknown | 17937 | 8984 | 8953 | 50.09% | -1.27% | 0.92% |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 47852 | 22217 | 25635 | 46.43% | -0.19% | 0.04% |
| high | 23227 | 10667 | 12560 | 45.93% | -0.29% | -0.00% |
| medium | 17298 | 8878 | 8420 | 51.32% | 0.32% | 0.42% |
| low | 270529 | 124236 | 146293 | 45.92% | 0.31% | 0.10% |
| unknown | 17937 | 8984 | 8953 | 50.09% | -1.27% | 0.92% |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 781 | 199 | 582 | 25.48% | -1.40% | -0.06% |
| high | 23259 | 10165 | 13094 | 43.70% | 0.09% | 0.10% |
| medium | 30756 | 13376 | 17380 | 43.49% | -0.17% | 0.14% |
| low | 309010 | 144290 | 164720 | 46.69% | 0.25% | 0.08% |
| unknown | 13037 | 6952 | 6085 | 53.33% | -1.82% | 1.99% |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 781 | 199 | 582 | 25.48% | -1.40% | -0.06% |
| high | 23259 | 10165 | 13094 | 43.70% | 0.09% | 0.10% |
| medium | 30756 | 13376 | 17380 | 43.49% | -0.17% | 0.14% |
| low | 309010 | 144290 | 164720 | 46.69% | 0.25% | 0.08% |
| unknown | 13037 | 6952 | 6085 | 53.33% | -1.82% | 1.99% |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2233 | 648 | 1585 | 29.02% | -1.66% | 1.06% |
| high | 24405 | 10485 | 13920 | 42.96% | 0.01% | 0.20% |
| medium | 31777 | 13760 | 18017 | 43.30% | -0.26% | 0.16% |
| low | 318428 | 150089 | 168339 | 47.13% | 0.19% | 0.11% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 772 | 258 | 514 | 33.42% | 1.35% | 0.82% |
| nan | 344314 | 159771 | 184543 | 46.40% | 0.14% | 0.11% |
| no_risk_noise | 13158 | 6500 | 6658 | 49.40% | 0.06% | 0.18% |
| risk_noise_detected | 18599 | 8453 | 10146 | 45.45% | 0.05% | 0.39% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 1234 | 759 | 475 | 61.51% | -2.21% | -2.00% |
| low_attention | 16178 | 7477 | 8701 | 46.22% | -0.06% | 0.22% |
| medium_attention | 15117 | 6975 | 8142 | 46.14% | 0.42% | 0.61% |
| nan | 344314 | 159771 | 184543 | 46.40% | 0.14% | 0.11% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 24751 | 11499 | 13252 | 46.46% | -0.05% | 0.44% |
| normal | 322737 | 154746 | 167991 | 47.95% | 0.23% | 0.17% |
| unknown | 15878 | 760 | 15118 | 4.79% | -0.27% | -0.38% |
| very_high | 13477 | 7977 | 5500 | 59.19% | -1.35% | -1.09% |

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
| 114450 |  |  | 2026-07-23 | 2026-07-23 | 70.0 | 71.43 | 71.43 | v2_conservative_ranker | 71.43 | 71.43 | 0.22 | 0.0 | 1.0 | 1.0865 | -0.0048 |  | failure |

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

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.
- Current ranking diagnosis: Ranking inverted / 랭킹 역방향 가능성
- V2 scoring impact should be judged after several new daily runs.
- V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.