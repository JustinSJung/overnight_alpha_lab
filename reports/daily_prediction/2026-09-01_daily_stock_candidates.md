# Daily Stock Candidate Report - 2026-09-01

Generated at: 2026-09-01 02:02:02

ML dataset: `data/processed/ml_dataset_20260901.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 288980 | 모아데이타 | 14 | 8 | 100.00% | 5.76% | relatively_positive_history | 8.57 |
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 006840 | AK홀딩스 | 3 | 3 | 100.00% | -0.53% | relatively_positive_history | 6.00 |
| 028260 | 삼성물산 | 21 | 14 | 85.71% | 0.99% | relatively_positive_history | 5.50 |
| 225190 | LK삼양 | 1 | 1 | 100.00% | 13.37% | relatively_positive_history | 5.50 |
| 378340 | 필에너지 | 1 | 1 | 100.00% | 7.40% | relatively_positive_history | 5.50 |
| 002020 | 코오롱 | 11 | 4 | 100.00% | 0.39% | relatively_positive_history | 5.36 |
| 060900 | 에이전트AI | 50 | 36 | 66.67% | -0.41% | relatively_positive_history | 5.30 |
| 058730 | 다스코 | 6 | 2 | 100.00% | 3.22% | relatively_positive_history | 4.83 |
| 071200 | 인피니트헬스케어 | 9 | 8 | 100.00% | -1.21% | relatively_positive_history | 4.39 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 392 | 136 | 56.62% | 2.28% | 5.00 |
| lawsuit | 107 | 16 | 87.50% | -1.20% | 4.00 |
| convertible_bond | 309 | 62 | 64.52% | -1.69% | 1.00 |
| bond_with_warrant | 11 | 1 | 100.00% | -2.57% | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| spin_off | 25 | 7 | 42.86% | 1.42% | -1.00 |
| investment_decision | 114 | 22 | 45.45% | -2.07% | -2.00 |
| disclosure_violation | 54 | 6 | 16.67% | 0.02% | -6.00 |
| major_shareholder_change | 576 | 156 | 25.64% | -0.12% | -6.00 |
| merger | 77 | 16 | 6.25% | 0.41% | -6.00 |
| supply_contract | 416 | 173 | 19.65% | -1.44% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| lawsuit | 107 | 14 | 2 | 91 | 0.60 |
| paid_in_capital_increase | 392 | 77 | 59 | 256 | 0.53 |
| bond_with_warrant | 11 | 1 | 0 | 10 | 0.45 |
| convertible_bond | 309 | 40 | 22 | 247 | 0.43 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| disclosure_violation | 54 | 1 | 5 | 48 | -0.19 |
| investment_decision | 114 | 10 | 12 | 92 | -0.30 |
| spin_off | 25 | 3 | 4 | 18 | -0.52 |
| major_shareholder_change | 576 | 40 | 116 | 420 | -1.06 |

## Positive Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 2. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 3. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 4. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 5. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 6. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 7. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 8. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 9. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

### 10. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **118.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.16%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 31일 주식시장 주요공시 | 8월 27일 주식시장 주요공시 | 다시 한번 속도 내는 건설산업 이미지 개선

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
