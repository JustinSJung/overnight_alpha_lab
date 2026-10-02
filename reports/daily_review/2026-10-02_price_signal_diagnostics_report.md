# Price Signal Diagnostics Report - 2026-10-02

This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.
이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.

## Overall Performance

- Cumulative evaluated cases: **191386**
- Success count: **85747**
- Failure count: **105639**
- Pending count: **232097**
- Raw success rate: **44.80%**
- Wilson reliability score: **44.6 / 100**
- Rolling 7-day success rate: **52.74%**
- Rolling 30-day success rate: **49.80%**
- Score version: **v2_conservative_ranker**
- V2 evaluated cases: **175750**
- Current ranking diagnosis: **Ranking inverted / 랭킹 역방향 가능성**

## Rank Bucket Performance

Ranks are recalculated within each signal/prediction day using final_price_signal_score_v2 first, then final_price_signal_score, prediction_score, and price_candidate_score as fallbacks. Each Top N row below is cumulative per day before being aggregated across all evaluated days.
랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| Top 10 | 439 | 137 | 302 | 31.21% | -1.46% | -0.93% |
| Top 20 | 919 | 294 | 625 | 31.99% | -1.30% | -0.88% |
| Top 50 | 2326 | 827 | 1499 | 35.55% | -0.74% | -0.46% |
| Top 100 | 4671 | 2070 | 2601 | 44.32% | 0.06% | 0.19% |
| Rest | 186715 | 83677 | 103038 | 44.82% | 0.27% | -0.03% |

## V2 Penalty Diagnostics by Rank Bucket

Average v2 score and penalties are shown when evaluated rows contain v2 component columns.
평가 데이터에 v2 구성 컬럼이 있을 때 평균 v2 점수와 페널티를 표시합니다.

| bucket | Evaluated | Avg V2 Score | Avg Total V2 Penalty |
|---|---:|---:|---:|
| Top 10 | 439 | 75.58 | 4.88 |
| Top 20 | 919 | 75.08 | 4.87 |
| Top 50 | 2326 | 73.72 | 5.04 |
| Top 100 | 4671 | 71.72 | 5.23 |
| Rest | 186715 | 35.89 | 9.26 |

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.

## Score Bucket Performance

### final_price_signal_score_v2

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 242 | 78 | 164 | 32.23% | -1.50% | 0.59% |
| high | 12324 | 5418 | 6906 | 43.96% | 0.15% | 0.07% |
| medium | 15240 | 6579 | 8661 | 43.17% | -0.17% | -0.13% |
| low | 147944 | 65776 | 82168 | 44.46% | 0.49% | -0.09% |
| unknown | 15636 | 7896 | 7740 | 50.50% | -1.25% | 0.92% |

### price_signal_score_v1

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 25458 | 12007 | 13451 | 47.16% | -0.34% | -0.25% |
| high | 11495 | 5358 | 6137 | 46.61% | -0.30% | -0.33% |
| medium | 9937 | 5062 | 4875 | 50.94% | 0.43% | 0.32% |
| low | 128860 | 55424 | 73436 | 43.01% | 0.61% | -0.06% |
| unknown | 15636 | 7896 | 7740 | 50.50% | -1.25% | 0.92% |

### prediction_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 349 | 78 | 271 | 22.35% | -2.19% | -0.99% |
| high | 12324 | 5418 | 6906 | 43.96% | 0.15% | 0.07% |
| medium | 15401 | 6686 | 8715 | 43.41% | -0.12% | -0.10% |
| low | 151489 | 67255 | 84234 | 44.40% | 0.48% | -0.13% |
| unknown | 11823 | 6310 | 5513 | 53.37% | -1.71% | 1.99% |

### final_price_signal_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 349 | 78 | 271 | 22.35% | -2.19% | -0.99% |
| high | 12324 | 5418 | 6906 | 43.96% | 0.15% | 0.07% |
| medium | 15401 | 6686 | 8715 | 43.41% | -0.12% | -0.10% |
| low | 151489 | 67255 | 84234 | 44.40% | 0.48% | -0.13% |
| unknown | 11823 | 6310 | 5513 | 53.37% | -1.71% | 1.99% |

### price_candidate_score

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| very_high | 1698 | 497 | 1201 | 29.27% | -2.06% | 1.18% |
| high | 13393 | 5723 | 7670 | 42.73% | 0.03% | 0.22% |
| medium | 16214 | 6955 | 9259 | 42.90% | -0.26% | -0.05% |
| low | 160081 | 72572 | 87509 | 45.33% | 0.37% | -0.05% |
| unknown | 0 | 0 | 0 | Insufficient data / 데이터 부족 | N/A | N/A |

## Volume and Supplementary Signal Diagnostics

### risk_noise_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_risk_noise | 435 | 127 | 308 | 29.20% | 1.87% | 0.41% |
| nan | 174148 | 77856 | 96292 | 44.71% | 0.28% | -0.06% |
| no_risk_noise | 6734 | 3301 | 3433 | 49.02% | 0.28% | 0.31% |
| risk_noise_detected | 10069 | 4463 | 5606 | 44.32% | 0.02% | 0.37% |

### social_attention_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high_attention | 609 | 385 | 224 | 63.22% | -2.68% | -2.92% |
| low_attention | 8556 | 3867 | 4689 | 45.20% | -0.05% | 0.26% |
| medium_attention | 8073 | 3639 | 4434 | 45.08% | 0.60% | 0.69% |
| nan | 174148 | 77856 | 96292 | 44.71% | 0.28% | -0.06% |

### volume_ratio_bucket

| bucket | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |
|---|---:|---:|---:|---:|---:|---:|
| high | 14612 | 6723 | 7889 | 46.01% | -0.06% | 0.40% |
| normal | 159484 | 73795 | 85689 | 46.27% | 0.42% | 0.03% |
| unknown | 9170 | 443 | 8727 | 4.83% | -0.24% | -0.62% |
| very_high | 8120 | 4786 | 3334 | 58.94% | -1.52% | -1.34% |

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
| 114450 |  |  | 2026-07-23 | 2026-07-23 | 54.0 | 71.43 | 71.43 | v2_conservative_ranker | 71.43 | 71.43 | 0.22 | 0.0 | 1.0 | 1.0865 | -0.0048 |  | failure |

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