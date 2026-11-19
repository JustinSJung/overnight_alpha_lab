# Daily Stock Candidate Report - 2026-11-19

Generated at: 2026-11-19 04:22:43

ML dataset: `data/processed/ml_dataset_20261119.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 870 | 774 | 45.87% | 5.00% | 4.00 |
| convertible_bond | 1658 | 1325 | 59.17% | 0.29% | 3.00 |
| paid_in_capital_increase | 2986 | 2465 | 55.86% | -0.16% | 3.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| investment_decision | 616 | 501 | 50.10% | 0.19% | 0.00 |
| lawsuit | 633 | 512 | 50.20% | -0.34% | 0.00 |
| disclosure_violation | 219 | 149 | 40.94% | -0.38% | -3.00 |
| bond_with_warrant | 162 | 150 | 42.00% | 0.03% | -3.00 |
| spin_off | 157 | 121 | 39.67% | 0.84% | -3.00 |
| major_shareholder_change | 3262 | 2628 | 37.94% | -0.72% | -3.00 |
| supply_contract | 1890 | 1564 | 36.38% | -0.57% | -3.00 |
| earnings_guidance | 96 | 92 | 26.09% | -1.87% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1658 | 784 | 541 | 333 | 1.39 |
| paid_in_capital_increase | 2986 | 1377 | 1088 | 521 | 1.21 |
| lawsuit | 633 | 257 | 255 | 121 | 0.82 |
| bond_with_warrant | 162 | 63 | 87 | 12 | 0.33 |
| disclosure_violation | 219 | 61 | 88 | 70 | 0.19 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 616 | 251 | 250 | 115 | -0.80 |
| supply_contract | 1890 | 569 | 995 | 326 | -0.92 |
| merger | 870 | 355 | 419 | 96 | -1.33 |
| earnings_guidance | 96 | 24 | 68 | 4 | -1.54 |

## Positive Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 2. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 3. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 4. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 5. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 6. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 7. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 8. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 9. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

### 10. 빅텍 (065450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-0.92**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.52**
- Adjusted recommendation score: **102.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 76.00%, avg next close: 0.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.19%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 0.92 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 18일 주식시장 주요공시 | 주요 공시(18일)-DB하이텍·한국금융지주·STX엔진 등 | 빅텍, K21 피아식별기 공급계약 종료일 두 달 연장

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
