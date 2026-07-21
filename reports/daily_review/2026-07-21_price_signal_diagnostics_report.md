# Price Signal Diagnostics Report - 2026-07-21

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **1620**
- Success count: **838**
- Failure count: **782**
- Pending count: **2046**
- Raw success rate: **51.73%**
- Wilson reliability score: **49.3 / 100**
- Rolling 7-day success rate: **52.88%**
- Rolling 30-day success rate: **51.73%**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score, prediction_score, then price_candidate_score as fallback. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 43 | 9 | 34 | 20.93% | -2.50% | N/A |
| Top 20 | 84 | 28 | 56 | 33.33% | -2.35% | N/A |
| Top 50 | 204 | 59 | 145 | 28.92% | -2.88% | N/A |
| Top 100 | 386 | 118 | 268 | 30.57% | -1.79% | N/A |
| Rest | 1234 | 720 | 514 | 58.35% | -0.98% | N/A |

## Score Bucket Performance

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2 | 1 | 1 | 50.00% | 1.58% | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 3 | 1 | 2 | 33.33% | -0.84% | N/A |
| low | 69 | 44 | 25 | 63.77% | -1.08% | N/A |
| unknown | 1546 | 792 | 754 | 51.23% | -1.18% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2 | 1 | 1 | 50.00% | 1.58% | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 3 | 1 | 2 | 33.33% | -0.84% | N/A |
| low | 69 | 44 | 25 | 63.77% | -1.08% | N/A |
| unknown | 1546 | 792 | 754 | 51.23% | -1.18% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 205 | 56 | 149 | 27.32% | -3.01% | N/A |
| high | 156 | 51 | 105 | 32.69% | -0.26% | N/A |
| medium | 74 | 21 | 53 | 28.38% | -1.55% | N/A |
| low | 1185 | 710 | 475 | 59.92% | -0.96% | N/A |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 15 | 8 | 7 | 53.33% | -3.13% | N/A |
| nan | 1353 | 707 | 646 | 52.25% | -0.99% | N/A |
| no_risk_noise | 101 | 54 | 47 | 53.47% | -1.49% | N/A |
| risk_noise_detected | 151 | 69 | 82 | 45.70% | -2.47% | N/A |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 1 | 1 | 0 | 100.00% | -2.76% | N/A |
| low_attention | 132 | 54 | 78 | 40.91% | -3.25% | N/A |
| medium_attention | 134 | 76 | 58 | 56.72% | -1.07% | N/A |
| nan | 1353 | 707 | 646 | 52.25% | -0.99% | N/A |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 134 | 58 | 76 | 43.28% | -0.79% | N/A |
| normal | 1310 | 741 | 569 | 56.56% | -0.89% | N/A |
| unknown | 75 | 8 | 67 | 10.67% | -1.71% | N/A |
| very_high | 101 | 31 | 70 | 30.69% | -5.02% | N/A |

## Failure Clusters

### High score but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  | 109.59 | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 32.0 |  |  | 91.23 | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 42.0 |  |  | 91.11 | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 52.0 |  |  | 88.59 | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 62.0 |  |  | 85.24 | 4.9367 |  |  |  |

### High volume but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065770 |  | CS |  |  | 42.0 |  |  | 91.11 | 13.4174 |  |  |  |
| 038530 |  |  |  |  | 62.0 |  |  | 85.24 | 4.9367 |  |  |  |
| 065770 |  | CS | 2026-07-07 | 2026-07-07 | 44.0 |  |  | 91.11 | 13.4174 | -0.0352 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 | 64.0 |  |  | 85.24 | 4.9367 | -0.1234 |  | failure |
| 263800 |  |  | 2026-07-09 | 2026-07-09 | 3.0 |  |  | 119.0 | 14.6426 | -0.0544 |  | failure |

### High risk noise and failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  | 109.59 | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 32.0 |  |  | 91.23 | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 42.0 |  |  | 91.11 | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 52.0 |  |  | 88.59 | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 62.0 |  |  | 85.24 | 4.9367 |  |  |  |

### Low score but succeeded

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | prediction_score | price_candidate_score | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0126Z0 |  |  |  |  | 332.0 |  |  | 39.08 | 1.0887 |  |  |  |
| 025980 |  |  |  |  | 342.0 |  |  | 36.9 | 0.6787 |  |  |  |
| 049950 |  |  |  |  | 352.0 |  |  | 36.37 | 0.7108 |  |  |  |
| 004380 |  |  |  |  | 362.0 |  |  | 35.0 | 0.3365 |  |  |  |
| 019570 |  |  |  |  | 372.0 |  |  | 32.09 | 0.0 |  |  |  |

## Summary Judgment

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.