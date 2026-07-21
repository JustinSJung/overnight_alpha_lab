# Price Signal Diagnostics Report - 2026-07-21

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **1619**
- Success count: **847**
- Failure count: **772**
- Pending count: **2043**
- Raw success rate: **52.32%**
- Wilson reliability score: **49.9 / 100**
- Rolling 7-day success rate: **53.58%**
- Rolling 30-day success rate: **52.32%**

## Rank Bucket Performance

| rank_bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 5 | 2 | 3 | 40.00% | 3.54% | N/A |
| Top 20 | 5 | 2 | 3 | 40.00% | 3.54% | N/A |
| Top 50 | 26 | 18 | 8 | 69.23% | -0.43% | N/A |
| Top 100 | 74 | 55 | 19 | 74.32% | -1.57% | N/A |
| Rest | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Score Bucket Performance

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2 | 1 | 1 | 50.00% | 8.06% | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 3 | 1 | 2 | 33.33% | 0.53% | N/A |
| low | 69 | 53 | 16 | 76.81% | -1.95% | N/A |
| unknown | 1545 | 792 | 753 | 51.26% | -1.18% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2 | 1 | 1 | 50.00% | 8.06% | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 3 | 1 | 2 | 33.33% | 0.53% | N/A |
| low | 69 | 53 | 16 | 76.81% | -1.95% | N/A |
| unknown | 1545 | 792 | 753 | 51.26% | -1.18% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 205 | 56 | 149 | 27.32% | -2.94% | N/A |
| high | 156 | 51 | 105 | 32.69% | -0.26% | N/A |
| medium | 73 | 21 | 52 | 28.77% | -1.50% | N/A |
| low | 1185 | 719 | 466 | 60.68% | -1.01% | N/A |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 15 | 8 | 7 | 53.33% | -3.13% | N/A |
| nan | 1352 | 716 | 636 | 52.96% | -1.00% | N/A |
| no_risk_noise | 101 | 54 | 47 | 53.47% | -1.51% | N/A |
| risk_noise_detected | 151 | 69 | 82 | 45.70% | -2.66% | N/A |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 1 | 1 | 0 | 100.00% | -2.21% | N/A |
| low_attention | 132 | 53 | 79 | 40.15% | -3.25% | N/A |
| medium_attention | 134 | 77 | 57 | 57.46% | -1.30% | N/A |
| nan | 1352 | 716 | 636 | 52.96% | -1.00% | N/A |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 134 | 59 | 75 | 44.03% | -0.66% | N/A |
| normal | 1309 | 749 | 560 | 57.22% | -0.91% | N/A |
| unknown | 75 | 8 | 67 | 10.67% | -1.71% | N/A |
| very_high | 101 | 31 | 70 | 30.69% | -5.34% | N/A |

## Failure Clusters

### High score but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 012160 |  |  | 2026-07-20 | 2026-07-20 | 1.0 | 103.0 | 103.0 | 103.0 | 3.3785 | -0.0392 |  | failure |

### High volume but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065770 |  | CS |  |  |  |  |  | 91.11 | 13.4174 |  |  |  |
| 038530 |  |  |  |  |  |  |  | 85.24 | 4.9367 |  |  |  |
| 065770 |  | CS | 2026-07-07 | 2026-07-07 |  |  |  | 91.11 | 13.4174 | -0.0352 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 |  |  |  | 85.24 | 4.9367 | -0.1234 |  | failure |
| 263800 |  |  | 2026-07-09 | 2026-07-09 |  |  |  | 119.0 | 14.6426 | -0.0544 |  | failure |

### High risk noise and failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  |  |  |  | 109.59 | 1.8376 |  |  |  |
| 368970 |  |  |  |  |  |  |  | 91.23 | 0.371 |  |  |  |
| 065770 |  | CS |  |  |  |  |  | 91.11 | 13.4174 |  |  |  |
| 002780 |  |  |  |  |  |  |  | 88.59 | 1.9443 |  |  |  |
| 038530 |  |  |  |  |  |  |  | 85.24 | 4.9367 |  |  |  |

### Low score but succeeded

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 033310 | 엠투엔 | 엠투엔 | 2026-07-20 | 2026-07-20 | 31.0 | 39.33 | 39.33 | 39.33 | 0.2998 | -0.0015 |  | success |
| 065770 |  |  | 2026-07-20 | 2026-07-20 | 32.0 | 38.89 | 38.89 | 38.89 | 0.3058 | -0.0388 |  | success |
| 321370 |  |  | 2026-07-20 | 2026-07-20 | 33.0 | 38.68 | 38.68 | 38.68 | 4.4367 | -0.0714 |  | success |
| 040910 |  |  | 2026-07-20 | 2026-07-20 | 34.0 | 38.43 | 38.43 | 38.43 | 1.1607 | -0.0125 |  | success |
| 112610 |  |  | 2026-07-20 | 2026-07-20 | 35.0 | 37.06 | 37.06 | 37.06 | 0.615 | -0.0154 |  | success |

## Summary Judgment

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.