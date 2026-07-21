# Price Signal Diagnostics Report - 2026-07-21

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **1624**
- Success count: **825**
- Failure count: **799**
- Pending count: **2059**
- Raw success rate: **50.80%**
- Wilson reliability score: **48.4 / 100**
- Rolling 7-day success rate: **51.77%**
- Rolling 30-day success rate: **50.80%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **0**
- Current ranking diagnosis: **Insufficient v2 data / v2 데이터 부족**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 44 | 10 | 34 | 22.73% | -2.20% | N/A |
| Top 20 | 86 | 30 | 56 | 34.88% | -2.11% | N/A |
| Top 50 | 207 | 61 | 146 | 29.47% | -2.83% | N/A |
| Top 100 | 389 | 120 | 269 | 30.85% | -1.76% | N/A |
| Rest | 1235 | 705 | 530 | 57.09% | -0.92% | N/A |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 44 | N/A | 0.00 |
| Top 20 | 86 | N/A | 0.00 |
| Top 50 | 207 | N/A | 0.00 |
| Top 100 | 389 | N/A | 0.00 |
| Rest | 1235 | N/A | 0.00 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| low | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| unknown | 1624 | 825 | 799 | 50.80% | -1.12% | N/A |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| low | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| unknown | 1624 | 825 | 799 | 50.80% | -1.12% | N/A |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2 | 0 | 2 | 0.00% | -3.77% | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 3 | 2 | 1 | 66.67% | 4.54% | N/A |
| low | 69 | 29 | 40 | 42.03% | 0.09% | N/A |
| unknown | 1550 | 794 | 756 | 51.23% | -1.18% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2 | 0 | 2 | 0.00% | -3.77% | N/A |
| high | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |
| medium | 3 | 2 | 1 | 66.67% | 4.54% | N/A |
| low | 69 | 29 | 40 | 42.03% | 0.09% | N/A |
| unknown | 1550 | 794 | 756 | 51.23% | -1.18% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 208 | 57 | 151 | 27.40% | -3.03% | N/A |
| high | 156 | 51 | 105 | 32.69% | -0.26% | N/A |
| medium | 74 | 22 | 52 | 29.73% | -1.32% | N/A |
| low | 1186 | 695 | 491 | 58.60% | -0.89% | N/A |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 15 | 8 | 7 | 53.33% | -3.13% | N/A |
| nan | 1355 | 693 | 662 | 51.14% | -0.93% | N/A |
| no_risk_noise | 102 | 56 | 46 | 54.90% | -1.44% | N/A |
| risk_noise_detected | 152 | 68 | 84 | 44.74% | -2.41% | N/A |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 1 | 1 | 0 | 100.00% | -5.19% | N/A |
| low_attention | 133 | 53 | 80 | 39.85% | -3.16% | N/A |
| medium_attention | 135 | 78 | 57 | 57.78% | -1.03% | N/A |
| nan | 1355 | 693 | 662 | 51.14% | -0.93% | N/A |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 137 | 60 | 77 | 43.80% | -0.82% | N/A |
| normal | 1310 | 726 | 584 | 55.42% | -0.82% | N/A |
| unknown | 76 | 8 | 68 | 10.53% | -1.69% | N/A |
| very_high | 101 | 31 | 70 | 30.69% | -5.03% | N/A |

## Failure Clusters

### High score but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 32.0 |  |  |  |  | 91.23 |  |  |  | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 42.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 52.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 62.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |

### High-score failures under v2

No examples available.

### High volume but failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 065770 |  | CS |  |  | 42.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 038530 |  |  |  |  | 62.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |
| 065770 |  | CS | 2026-07-07 | 2026-07-07 | 44.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 | -0.0352 |  | failure |
| 038530 |  |  | 2026-07-07 | 2026-07-07 | 64.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 | -0.1234 |  | failure |
| 263800 |  |  | 2026-07-09 | 2026-07-09 | 3.0 |  |  |  |  | 119.0 |  |  |  | 14.6426 | -0.0544 |  | failure |

### High risk noise and failed

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 024720 |  | 콜마홀딩스 |  |  | 2.0 |  |  |  |  | 109.59 |  |  |  | 1.8376 |  |  |  |
| 368970 |  |  |  |  | 32.0 |  |  |  |  | 91.23 |  |  |  | 0.371 |  |  |  |
| 065770 |  | CS |  |  | 42.0 |  |  |  |  | 91.11 |  |  |  | 13.4174 |  |  |  |
| 002780 |  |  |  |  | 52.0 |  |  |  |  | 88.59 |  |  |  | 1.9443 |  |  |  |
| 038530 |  |  |  |  | 62.0 |  |  |  |  | 85.24 |  |  |  | 4.9367 |  |  |  |

### Low score but succeeded

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0126Z0 |  |  |  |  | 332.0 |  |  |  |  | 39.08 |  |  |  | 1.0887 |  |  |  |
| 025980 |  |  |  |  | 342.0 |  |  |  |  | 36.9 |  |  |  | 0.6787 |  |  |  |
| 049950 |  |  |  |  | 352.0 |  |  |  |  | 36.37 |  |  |  | 0.7108 |  |  |  |
| 004380 |  |  |  |  | 362.0 |  |  |  |  | 35.0 |  |  |  | 0.3365 |  |  |  |
| 019570 |  |  |  |  | 372.0 |  |  |  |  | 32.09 |  |  |  | 0.0 |  |  |  |

### Low-score successes under v2

| stock_code | stock_name | corp_name | signal_date | prediction_date | candidate_rank | final_price_signal_score | final_price_signal_score_v2 | score_version | prediction_score | price_candidate_score | overextension_penalty | reversal_risk_penalty | news_risk_penalty | volume_ratio_20d | close_t1_return | excess_return_t1 | prediction_result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 010960 |  | 삼호개발 |  |  | 12.0 |  |  |  |  | 103.0 |  |  |  | 3.6331 |  |  |  |
| 091590 |  | 남화토건 |  |  | 22.0 |  |  |  |  | 97.84 |  |  |  | 1.6403 |  |  |  |
| 189330 |  | 씨이랩 |  |  | 92.0 |  |  |  |  | 78.0 |  |  |  | 0.7827 |  |  |  |
| 419540 |  |  |  |  | 132.0 |  |  |  |  | 69.23 |  |  |  | 0.4112 |  |  |  |
| 008930 |  | 한미사이언스 |  |  | 142.0 |  |  |  |  | 68.76 |  |  |  | 0.7538 |  |  |  |

## Summary Judgment

- Overall performance remains close to random; ranking quality is not yet clearly proven.
- 전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다.
- Current ranking diagnosis: Insufficient v2 data / v2 데이터 부족
- V2 scoring impact should be judged after several new daily runs.
- V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.
큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.