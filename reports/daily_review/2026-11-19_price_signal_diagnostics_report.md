# Price Signal Diagnostics Report - 2026-11-19

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

Evaluation snapshots are deduplicated by the shared stable prediction identity before counting outcomes or assigning daily ranks.
평가 수와 일별 순위는 공통 예측 식별자로 반복 스냅샷을 제거한 뒤 집계합니다.

- Cumulative evaluated cases: **25329**
- Success count: **12657**
- Failure count: **12672**
- Pending count: **25449**
- Raw success rate: **49.97%**
- Wilson reliability score: **49.4 / 100**
- Rolling 7-day success rate: **56.05%**
- Rolling 30-day success rate: **53.48%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **25070**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 724 | 300 | 424 | 41.44% | -0.26% | 0.40% |
| Top 20 | 1285 | 545 | 740 | 42.41% | -0.22% | 0.66% |
| Top 50 | 2225 | 953 | 1272 | 42.83% | -0.32% | 0.45% |
| Top 100 | 3091 | 1294 | 1797 | 41.86% | -0.15% | 0.42% |
| Rest | 22238 | 11363 | 10875 | 51.10% | -0.20% | 0.11% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 724 | 70.60 | 5.19 |
| Top 20 | 1285 | 68.54 | 5.30 |
| Top 50 | 2225 | 66.54 | 5.22 |
| Top 100 | 3091 | 62.59 | 5.33 |
| Rest | 22238 | 32.23 | 7.19 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 46 | 14 | 32 | 30.43% | -0.66% | 1.72% |
| high | 1142 | 480 | 662 | 42.03% | -0.16% | 0.48% |
| medium | 1487 | 622 | 865 | 41.83% | -0.36% | 0.36% |
| low | 22395 | 11410 | 10985 | 50.95% | -0.17% | 0.10% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 2165 | 961 | 1204 | 44.39% | -0.31% | 0.59% |
| high | 1193 | 537 | 656 | 45.01% | -0.40% | 0.17% |
| medium | 765 | 417 | 348 | 54.51% | -0.21% | 0.19% |
| low | 20947 | 10611 | 10336 | 50.66% | -0.15% | 0.09% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 46 | 14 | 32 | 30.43% | -0.66% | 1.72% |
| high | 1142 | 480 | 662 | 42.03% | -0.16% | 0.48% |
| medium | 1487 | 622 | 865 | 41.83% | -0.36% | 0.36% |
| low | 22395 | 11410 | 10985 | 50.95% | -0.17% | 0.10% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 46 | 14 | 32 | 30.43% | -0.66% | 1.72% |
| high | 1142 | 480 | 662 | 42.03% | -0.16% | 0.48% |
| medium | 1487 | 622 | 865 | 41.83% | -0.36% | 0.36% |
| low | 22395 | 11410 | 10985 | 50.95% | -0.17% | 0.10% |
| unknown | 259 | 131 | 128 | 50.58% | -1.36% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 78 | 22 | 56 | 28.21% | -1.89% | 1.72% |
| high | 1168 | 488 | 680 | 41.78% | -0.17% | 0.48% |
| medium | 1499 | 625 | 874 | 41.69% | -0.37% | 0.36% |
| low | 22584 | 11522 | 11062 | 51.02% | -0.17% | 0.10% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 42 | 19 | 23 | 45.24% | 0.30% | 0.47% |
| nan | 23509 | 11765 | 11744 | 50.04% | -0.18% | 0.13% |
| no_risk_noise | 812 | 421 | 391 | 51.85% | -0.47% | 0.03% |
| risk_noise_detected | 966 | 452 | 514 | 46.79% | -0.17% | 0.19% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 82 | 50 | 32 | 60.98% | -1.79% | -0.29% |
| low_attention | 870 | 424 | 446 | 48.74% | -0.33% | 0.11% |
| medium_attention | 868 | 418 | 450 | 48.16% | -0.13% | 0.18% |
| nan | 23509 | 11765 | 11744 | 50.04% | -0.18% | 0.13% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 1496 | 667 | 829 | 44.59% | -0.07% | 0.30% |
| normal | 22466 | 11550 | 10916 | 51.41% | -0.16% | 0.12% |
| unknown | 680 | 42 | 638 | 6.18% | -0.45% | 0.21% |
| very_high | 687 | 398 | 289 | 57.93% | -1.06% | 0.01% |

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
| 053580 |  |  | 2026-07-23 | 2026-07-23 | 4.0 | 70.3 | 70.3 | v2_conservative_ranker | 70.3 | 70.3 | 0.0 | 0.0 | 2.0 | 1.5666 | -0.009 |  | failure |
| 134790 |  |  | 2026-07-27 | 2026-07-27 | 1.0 | 78.04 | 78.04 | v2_conservative_ranker | 78.04 | 78.04 | 0.0 | 0.0 | 2.0 | 1.7208 | -0.0188 |  | failure |
| 340570 |  |  | 2026-07-27 | 2026-07-27 | 5.0 | 68.05 | 68.05 | v2_conservative_ranker | 68.05 | 68.05 | 1.62 | 0.0 | 2.0 | 2.6676 | -0.0514 |  | failure |
| 114450 |  |  | 2026-07-28 | 2026-07-28 | 1.0 | 80.24 | 80.24 | v2_conservative_ranker | 80.24 | 80.24 | 0.66 | 0.0 | 2.0 | 2.0011 | -0.029 |  | failure |
| 004780 |  |  | 2026-07-29 | 2026-07-29 | 3.0 | 66.83 | 66.83 | v2_conservative_ranker | 66.83 | 66.83 | 0.0 | 0.0 | 0.0 | 1.7211 | -0.0037 |  | failure |

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