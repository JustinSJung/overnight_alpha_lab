# Daily Stock Candidate Report - 2026-11-17

Generated at: 2026-11-17 05:39:53

ML dataset: `data/processed/ml_dataset_20261117.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 869 | 773 | 45.80% | 4.98% | 4.00 |
| convertible_bond | 1608 | 1275 | 57.65% | 0.41% | 3.00 |
| paid_in_capital_increase | 2937 | 2416 | 55.17% | -0.17% | 3.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| investment_decision | 605 | 490 | 51.02% | 0.21% | 0.00 |
| lawsuit | 620 | 499 | 49.30% | -0.30% | 0.00 |
| disclosure_violation | 218 | 148 | 41.22% | -0.38% | -3.00 |
| bond_with_warrant | 162 | 150 | 42.00% | 0.03% | -3.00 |
| spin_off | 155 | 119 | 39.50% | 0.89% | -3.00 |
| major_shareholder_change | 3204 | 2570 | 38.05% | -0.70% | -3.00 |
| supply_contract | 1839 | 1513 | 36.22% | -0.57% | -3.00 |
| earnings_guidance | 96 | 92 | 26.09% | -1.87% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1608 | 735 | 540 | 333 | 1.28 |
| paid_in_capital_increase | 2937 | 1333 | 1083 | 521 | 1.16 |
| lawsuit | 620 | 246 | 253 | 121 | 0.76 |
| bond_with_warrant | 162 | 63 | 87 | 12 | 0.33 |
| disclosure_violation | 218 | 61 | 87 | 70 | 0.20 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 605 | 250 | 240 | 115 | -0.71 |
| supply_contract | 1839 | 548 | 965 | 326 | -0.91 |
| merger | 869 | 354 | 419 | 96 | -1.34 |
| earnings_guidance | 96 | 24 | 68 | 4 | -1.54 |

## Positive Candidates

### 1. 케이씨텍 (281820)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **151.59**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 7.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.28%
- Next close return data: 3.25%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: SK하이닉스, 케이씨텍에 반도체 장비 699억원 추가 발주…내년 6월 납기 | 11월 16일 주식시장 주요공시 | [개장 전 주요 공시] 두산에너빌리티·포스코·아이크래프트·동부건설...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 2. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 3. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 4. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 5. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 6. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 7. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 8. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 9. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

### 10. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.91**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **138.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 64, success rate: 39.06%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -1.21%
- Next close return data: -1.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.91 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 신테카바이오, 美 카이메라 테라퓨틱스와 5.3억원 규모 계약 2건 해지 | 신테카바이오 "美카이메라와 맺은 계약 2건 해지" | 진단부터 신약개발까지 투심 확산… 의료AI 관련주 온도차 '눈에 띄네'

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
