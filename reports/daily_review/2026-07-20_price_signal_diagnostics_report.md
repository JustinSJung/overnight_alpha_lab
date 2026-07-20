# Price Signal Diagnostics Report - 2026-07-20

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **1263**
- Success count: **637**
- Failure count: **626**
- Pending count: **1645**
- Raw success rate: **50.44%**
- Wilson reliability score: **47.7 / 100**
- Rolling 7-day success rate: **51.65%**
- Rolling 30-day success rate: **50.44%**

## Rank Bucket Performance

| rank_bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| Top 20 | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| Top 50 | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| Top 100 | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| Rest | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Score Bucket Performance

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| low | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| unknown | 1263 | 637 | 626 | 50.44% | -1.04% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| low | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| unknown | 1263 | 637 | 626 | 50.44% | -1.04% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 171 | 46 | 125 | 26.90% | -3.15% | N/A |
| high | 129 | 43 | 86 | 33.33% | -0.10% | N/A |
| medium | 57 | 17 | 40 | 29.82% | -1.54% | N/A |
| low | 906 | 531 | 375 | 58.61% | -0.75% | N/A |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 13 | 7 | 6 | 53.85% | -3.13% | N/A |
| nan | 1045 | 530 | 515 | 50.72% | -0.79% | N/A |
| no_risk_noise | 85 | 45 | 40 | 52.94% | -1.44% | N/A |
| risk_noise_detected | 120 | 55 | 65 | 45.83% | -2.72% | N/A |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| low_attention | 105 | 42 | 63 | 40.00% | -3.31% | N/A |
| medium_attention | 113 | 65 | 48 | 57.52% | -1.30% | N/A |
| nan | 1045 | 530 | 515 | 50.72% | -0.79% | N/A |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 109 | 46 | 63 | 42.20% | -0.61% | N/A |
| normal | 1018 | 563 | 455 | 55.30% | -0.72% | N/A |
| unknown | 58 | 7 | 51 | 12.07% | -1.90% | N/A |
| very_high | 78 | 21 | 57 | 26.92% | -5.10% | N/A |

## Failure Clusters

### High score but failed

No examples available.

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

No examples available.

## Summary Judgment

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.