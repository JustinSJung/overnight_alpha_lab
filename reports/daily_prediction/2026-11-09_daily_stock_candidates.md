# Daily Stock Candidate Report - 2026-11-09

Generated at: 2026-11-09 02:28:13

ML dataset: `data/processed/ml_dataset_20261109.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 248170 | 샘표식품 | 21 | 21 | 100.00% | 27.77% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1422 | 1089 | 58.03% | 0.36% | 3.00 |
| paid_in_capital_increase | 2708 | 2187 | 57.43% | -0.32% | 3.00 |
| merger | 797 | 701 | 44.94% | 5.30% | 1.00 |
| investment_decision | 537 | 422 | 49.76% | -0.01% | 0.00 |
| lawsuit | 557 | 436 | 51.15% | -0.43% | 0.00 |
| disclosure_violation | 209 | 139 | 40.29% | -0.28% | -3.00 |
| bond_with_warrant | 146 | 134 | 40.30% | 0.21% | -3.00 |
| bonus_issue | 107 | 104 | 42.31% | -0.51% | -3.00 |
| spin_off | 150 | 114 | 38.60% | 0.99% | -3.00 |
| major_shareholder_change | 2823 | 2190 | 39.50% | -0.85% | -3.00 |
| earnings_guidance | 63 | 59 | 27.12% | 0.28% | -6.00 |
| supply_contract | 1689 | 1363 | 34.70% | -0.72% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2708 | 1256 | 931 | 521 | 1.29 |
| convertible_bond | 1422 | 632 | 457 | 333 | 1.26 |
| lawsuit | 557 | 223 | 213 | 121 | 0.85 |
| bond_with_warrant | 146 | 54 | 80 | 12 | 0.21 |
| disclosure_violation | 209 | 56 | 83 | 70 | 0.15 |
| investment_decision | 537 | 210 | 212 | 115 | -0.81 |
| supply_contract | 1689 | 473 | 890 | 326 | -1.02 |
| bonus_issue | 107 | 44 | 60 | 3 | -1.05 |
| earnings_guidance | 63 | 16 | 43 | 4 | -1.16 |
| merger | 797 | 315 | 386 | 96 | -1.41 |

## Positive Candidates

### 1. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 2. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 3. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 4. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 5. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 6. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 7. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 8. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 9. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

### 10. 라온텍 (418420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.85**
- Adjusted recommendation score: **130.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 94.12%, avg next close: 0.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -3.21%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.85 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시셀렉트] 코미코, 운영자금 차입 보증 1년 연장…라온텍은 고객사 ... | 11월 6일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 브리지텍 (064480)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **160.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **149.23**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.16%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -3.49%
- Next close return data: -1.16%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Historical error notes subtracted 1.02 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 6일 주식시장 주요공시 | 11월 9일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-11월 9일] 美 증시, 3대 지수 혼조…반도체주 반등...

## Data Readiness

At this stage, candidates are still generated using rule-based scoring. The system now also uses historical error-note patterns, event-type performance statistics, and stock-specific historical reaction patterns. These adjustments will become more meaningful after enough evaluated event-reaction samples are accumulated.

## How to Read This Report

- Positive Candidates: relatively favorable event and news conditions.
- Volatile Watchlist: potentially important events with uncertain direction.
- General Watchlist: events worth monitoring but not strong enough for positive classification.
- Risk / Avoid Review List: negative or high-risk events such as capital increases, CB/BW, lawsuits, or disclosure violations.
- Error-note adjustment score: learning signal from previous advanced error notes.
- Event-type performance adjustment score: success-rate and average-return based adjustment by event type.
- Stock-specific pattern adjustment score: success-rate, average-return, and confidence-bias adjustment by stock code.

## Next Step

The next step is to add market index and sector movement features, so the system can distinguish stock-specific signals from broader market movement.
