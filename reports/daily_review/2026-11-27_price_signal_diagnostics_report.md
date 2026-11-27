# Price Signal Diagnostics Report - 2026-11-27

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

Evaluation snapshots are deduplicated by the shared stable prediction identity before counting outcomes or assigning daily ranks.
평가 수와 일별 순위는 공통 예측 식별자로 반복 스냅샷을 제거한 뒤 집계합니다.

- Cumulative evaluated cases: **29065**
- Success count: **14699**
- Failure count: **14366**
- Pending count: **29045**
- Raw success rate: **50.57%**
- Wilson reliability score: **50.0 / 100**
- Rolling 7-day success rate: **51.67%**
- Rolling 30-day success rate: **51.62%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **28806**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 732 | 307 | 425 | 41.94% | -0.25% | 0.42% |
| Top 20 | 1348 | 583 | 765 | 43.25% | -0.19% | 0.68% |
| Top 50 | 2433 | 1063 | 1370 | 43.69% | -0.27% | 0.50% |
| Top 100 | 3164 | 1340 | 1824 | 42.35% | -0.21% | 0.43% |
| Rest | 25901 | 13359 | 12542 | 51.58% | -0.22% | 0.08% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 732 | 71.24 | 5.09 |
| Top 20 | 1348 | 68.91 | 5.26 |
| Top 50 | 2433 | 66.80 | 5.20 |
| Top 100 | 3164 | 64.79 | 5.06 |
| Rest | 25901 | 32.03 | 6.97 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 48 | 12 | 36 | 25.00% | -0.89% | 1.36% |
| high | 1277 | 547 | 730 | 42.83% | -0.20% | 0.42% |
| medium | 1606 | 683 | 923 | 42.53% | -0.30% | 0.41% |
| low | 25875 | 13326 | 12549 | 51.50% | -0.21% | 0.08% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2341 | 1048 | 1293 | 44.77% | -0.35% | 0.47% |
| high | 1279 | 583 | 696 | 45.58% | -0.39% | 0.28% |
| medium | 801 | 436 | 365 | 54.43% | -0.18% | 0.11% |
| low | 24385 | 12501 | 11884 | 51.27% | -0.19% | 0.08% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 48 | 12 | 36 | 25.00% | -0.89% | 1.36% |
| high | 1277 | 547 | 730 | 42.83% | -0.20% | 0.42% |
| medium | 1606 | 683 | 923 | 42.53% | -0.30% | 0.41% |
| low | 25875 | 13326 | 12549 | 51.50% | -0.21% | 0.08% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 48 | 12 | 36 | 25.00% | -0.89% | 1.36% |
| high | 1277 | 547 | 730 | 42.83% | -0.20% | 0.42% |
| medium | 1606 | 683 | 923 | 42.53% | -0.30% | 0.41% |
| low | 25875 | 13326 | 12549 | 51.50% | -0.21% | 0.08% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 80 | 20 | 60 | 25.00% | -2.00% | 1.36% |
| high | 1303 | 555 | 748 | 42.59% | -0.21% | 0.42% |
| medium | 1618 | 686 | 932 | 42.40% | -0.31% | 0.41% |
| low | 26064 | 13438 | 12626 | 51.56% | -0.21% | 0.08% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 46 | 20 | 26 | 43.48% | 0.98% | 1.73% |
| nan | 27046 | 13692 | 13354 | 50.62% | -0.22% | 0.11% |
| no_risk_noise | 929 | 485 | 444 | 52.21% | -0.46% | 0.11% |
| risk_noise_detected | 1044 | 502 | 542 | 48.08% | -0.24% | 0.02% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 84 | 50 | 34 | 59.52% | -1.68% | -0.58% |
| low_attention | 954 | 476 | 478 | 49.90% | -0.43% | 0.17% |
| medium_attention | 981 | 481 | 500 | 49.03% | -0.08% | 0.11% |
| nan | 27046 | 13692 | 13354 | 50.62% | -0.22% | 0.11% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 1770 | 801 | 969 | 45.25% | -0.10% | 0.25% |
| normal | 25772 | 13391 | 12381 | 51.96% | -0.20% | 0.10% |
| unknown | 724 | 47 | 677 | 6.49% | -0.43% | 0.23% |
| very_high | 799 | 460 | 339 | 57.57% | -1.09% | -0.04% |

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
| 004780 |  |  | 2026-07-29 | 2026-07-29 | 3.0 | 66.83 | 66.83 | v2_conservative_ranker | 66.83 | 66.83 | 0.0 | 0.0 | 0.0 | 1.7211 | -0.0037 |  | failure |
| 114450 |  |  | 2026-07-30 | 2026-07-30 | 1.0 | 70.24 | 70.24 | v2_conservative_ranker | 70.24 | 70.24 | 0.44 | 0.0 | 2.0 | 0.852 | -0.0659 |  | failure |
| 018470 |  |  | 2026-07-31 | 2026-08-02 | 5.0 | 65.81 | 65.81 | v2_conservative_ranker | 65.81 | 65.81 | 0.0 | 0.0 | 2.0 | 1.3634 | -0.0461 |  | failure |
| 005710 |  |  | 2026-08-04 | 2026-08-04 | 1.0 | 75.46 | 75.46 | v2_conservative_ranker | 75.46 | 75.46 | 0.0 | 0.0 | 1.0 | 1.4661 | -0.0009 |  | failure |
| 008470 |  |  | 2026-08-04 | 2026-08-04 | 7.0 | 67.01 | 67.01 | v2_conservative_ranker | 67.01 | 67.01 | 3.32 | 0.0 | 1.0 | 1.5753 | -0.0119 |  | failure |

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