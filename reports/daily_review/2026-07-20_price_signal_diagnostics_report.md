# Price Signal Diagnostics Report - 2026-07-20

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **985**
- Success count: **486**
- Failure count: **499**
- Pending count: **1288**
- Raw success rate: **49.34%**
- Wilson reliability score: **46.2 / 100**
- Rolling 7-day success rate: **50.00%**
- Rolling 30-day success rate: **49.34%**

## Rank Bucket Performance

| rank_bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 40 | 13 | 27 | 32.50% | -3.50% | N/A |
| Top 20 | 83 | 23 | 60 | 27.71% | -3.19% | N/A |
| Top 50 | 205 | 48 | 157 | 23.41% | -3.15% | N/A |
| Top 100 | 278 | 86 | 192 | 30.94% | -1.73% | N/A |
| Rest | 707 | 400 | 307 | 56.58% | -0.58% | N/A |

## Score Bucket Performance

### prediction_score

Insufficient data / 데이터 부족

### final_price_signal_score

Insufficient data / 데이터 부족

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 139 | 37 | 102 | 26.62% | -3.29% | N/A |
| high | 102 | 35 | 67 | 34.31% | 0.16% | N/A |
| medium | 44 | 14 | 30 | 31.82% | -1.46% | N/A |
| low | 700 | 400 | 300 | 57.14% | -0.54% | N/A |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 11 | 6 | 5 | 54.55% | -3.13% | N/A |
| nan | 803 | 396 | 407 | 49.32% | -0.60% | N/A |
| no_risk_noise | 72 | 38 | 34 | 52.78% | -1.34% | N/A |
| risk_noise_detected | 99 | 46 | 53 | 46.46% | -2.77% | N/A |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| low_attention | 87 | 35 | 52 | 40.23% | -3.30% | N/A |
| medium_attention | 95 | 55 | 40 | 57.89% | -1.29% | N/A |
| nan | 803 | 396 | 407 | 49.32% | -0.60% | N/A |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 87 | 36 | 51 | 41.38% | -0.58% | N/A |
| normal | 791 | 428 | 363 | 54.11% | -0.49% | N/A |
| unknown | 45 | 6 | 39 | 13.33% | -2.05% | N/A |
| very_high | 62 | 16 | 46 | 25.81% | -5.71% | N/A |

## Failure Clusters

### High score but failed

| stock_code | corp_name | signal_date | prediction_date | candidate_rank | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|
| 024720 | 콜마홀딩스 |  |  | 3.0 | 109.59 | 1.8376 |  |  |  |
| 368970 |  |  |  | 12.0 | 91.23 | 0.371 |  |  |  |
| 065770 | CS |  |  | 14.0 | 91.11 | 13.4174 |  |  |  |
| 002780 |  |  |  | 17.0 | 88.59 | 1.9443 |  |  |  |
| 038530 |  |  |  | 20.0 | 85.24 | 4.9367 |  |  |  |

### High volume but failed

| stock_code | corp_name | signal_date | prediction_date | candidate_rank | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|
| 065770 | CS |  |  | 14.0 | 91.11 | 13.4174 |  |  |  |
| 038530 |  |  |  | 20.0 | 85.24 | 4.9367 |  |  |  |
| 065770 | CS | 2026-07-07 | 2026-07-07 | 26.0 | 91.11 | 13.4174 | -0.0352 |  | failure |
| 038530 |  | 2026-07-07 | 2026-07-07 | 38.0 | 85.24 | 4.9367 | -0.1234 |  | failure |
| 263800 |  | 2026-07-09 | 2026-07-09 | 2.0 | 119.0 | 14.6426 | -0.0544 |  | failure |

### High risk noise and failed

| stock_code | corp_name | signal_date | prediction_date | candidate_rank | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|
| 024720 | 콜마홀딩스 |  |  | 3.0 | 109.59 | 1.8376 |  |  |  |
| 368970 |  |  |  | 12.0 | 91.23 | 0.371 |  |  |  |
| 065770 | CS |  |  | 14.0 | 91.11 | 13.4174 |  |  |  |
| 002780 |  |  |  | 17.0 | 88.59 | 1.9443 |  |  |  |
| 038530 |  |  |  | 20.0 | 85.24 | 4.9367 |  |  |  |

### Low score but succeeded

| stock_code | corp_name | signal_date | prediction_date | candidate_rank | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|
| 0126Z0 |  |  |  | 106.0 | 39.08 | 1.0887 |  |  |  |
| 025980 |  |  |  | 110.0 | 36.9 | 0.6787 |  |  |  |
| 049950 |  |  |  | 112.0 | 36.37 | 0.7108 |  |  |  |
| 004380 |  |  |  | 116.0 | 35.0 | 0.3365 |  |  |  |
| 019570 |  |  |  | 121.0 | 32.09 | 0.0 |  |  |  |

## Summary Judgment

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.