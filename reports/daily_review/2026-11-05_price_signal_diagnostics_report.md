# Price Signal Diagnostics Report - 2026-11-05

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

Evaluation snapshots are deduplicated by the shared stable prediction identity before counting outcomes or assigning daily ranks.
평가 수와 일별 순위는 공통 예측 식별자로 반복 스냅샷을 제거한 뒤 집계합니다.

- Cumulative evaluated cases: **19074**
- Success count: **9310**
- Failure count: **9764**
- Pending count: **20150**
- Raw success rate: **48.81%**
- Wilson reliability score: **48.1 / 100**
- Rolling 7-day success rate: **48.13%**
- Rolling 30-day success rate: **51.08%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **18668**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 626 | 265 | 361 | 42.33% | -0.07% | 0.42% |
| Top 20 | 1095 | 469 | 626 | 42.83% | -0.11% | 0.46% |
| Top 50 | 1777 | 774 | 1003 | 43.56% | -0.25% | 0.40% |
| Top 100 | 2503 | 1064 | 1439 | 42.51% | -0.07% | 0.48% |
| Rest | 16571 | 8246 | 8325 | 49.76% | -0.12% | -0.01% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 626 | 69.58 | 5.09 |
| Top 20 | 1095 | 67.47 | 5.30 |
| Top 50 | 1777 | 65.81 | 5.22 |
| Top 100 | 2503 | 61.24 | 5.20 |
| Rest | 16571 | 32.62 | 7.32 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 32 | 10 | 22 | 31.25% | -0.49% | 1.62% |
| high | 806 | 346 | 460 | 42.93% | -0.04% | 0.47% |
| medium | 1140 | 484 | 656 | 42.46% | -0.28% | 0.52% |
| low | 16690 | 8269 | 8421 | 49.54% | -0.08% | -0.01% |
| unknown | 406 | 201 | 205 | 49.51% | -1.36% | N/A |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 1663 | 757 | 906 | 45.52% | -0.16% | 0.58% |
| high | 888 | 405 | 483 | 45.61% | -0.37% | 0.46% |
| medium | 613 | 325 | 288 | 53.02% | -0.17% | 0.04% |
| low | 15504 | 7622 | 7882 | 49.16% | -0.06% | -0.03% |
| unknown | 406 | 201 | 205 | 49.51% | -1.36% | N/A |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 34 | 10 | 24 | 29.41% | -0.68% | 1.62% |
| high | 806 | 346 | 460 | 42.93% | -0.04% | 0.47% |
| medium | 1143 | 486 | 657 | 42.52% | -0.27% | 0.52% |
| low | 16756 | 8297 | 8459 | 49.52% | -0.08% | -0.01% |
| unknown | 335 | 171 | 164 | 51.04% | -1.69% | N/A |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 34 | 10 | 24 | 29.41% | -0.68% | 1.62% |
| high | 806 | 346 | 460 | 42.93% | -0.04% | 0.47% |
| medium | 1143 | 486 | 657 | 42.52% | -0.27% | 0.52% |
| low | 16756 | 8297 | 8459 | 49.52% | -0.08% | -0.01% |
| unknown | 335 | 171 | 164 | 51.04% | -1.69% | N/A |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 73 | 20 | 53 | 27.40% | -1.72% | 1.62% |
| high | 837 | 355 | 482 | 42.41% | -0.09% | 0.47% |
| medium | 1167 | 496 | 671 | 42.50% | -0.33% | 0.52% |
| low | 16997 | 8439 | 8558 | 49.65% | -0.10% | -0.01% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 35 | 16 | 19 | 45.71% | -0.28% | 0.03% |
| nan | 17603 | 8580 | 9023 | 48.74% | -0.11% | 0.04% |
| no_risk_noise | 648 | 337 | 311 | 52.01% | -0.38% | -0.07% |
| risk_noise_detected | 788 | 377 | 411 | 47.84% | -0.07% | 0.05% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 60 | 36 | 24 | 60.00% | -2.16% | -1.72% |
| low_attention | 708 | 344 | 364 | 48.59% | -0.22% | 0.05% |
| medium_attention | 703 | 350 | 353 | 49.79% | -0.03% | 0.10% |
| nan | 17603 | 8580 | 9023 | 48.74% | -0.11% | 0.04% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 872 | 404 | 468 | 46.33% | -0.08% | 0.71% |
| normal | 17128 | 8611 | 8517 | 50.27% | -0.09% | 0.01% |
| unknown | 616 | 31 | 585 | 5.03% | -0.28% | 0.03% |
| very_high | 458 | 264 | 194 | 57.64% | -1.16% | 0.12% |

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