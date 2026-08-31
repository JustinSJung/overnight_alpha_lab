# Daily Stock Candidate Report - 2026-08-31

Generated at: 2026-08-31 01:14:17

ML dataset: `data/processed/ml_dataset_20260831.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 058730 | 다스코 | 6 | 2 | 100.00% | 3.22% | relatively_positive_history | 4.83 |
| 207940 | 삼성바이오로직스 | 10 | 5 | 100.00% | -1.28% | relatively_positive_history | 4.00 |
| 248070 | 솔루엠 | 8 | 3 | 100.00% | -2.11% | relatively_positive_history | 3.88 |
| 006120 | SK디스커버리 | 4 | 2 | 100.00% | 1.39% | relatively_positive_history | 3.50 |
| 267320 | 나인테크 | 2 | 1 | 100.00% | 2.30% | relatively_positive_history | 3.50 |
| 123750 | 알톤 | 3 | 1 | 100.00% | 1.02% | relatively_positive_history | 3.33 |
| 389680 | 유디엠텍 | 4 | 1 | 100.00% | 2.25% | relatively_positive_history | 3.25 |
| 030530 | 원익홀딩스 | 32 | 16 | 100.00% | -5.77% | relatively_positive_history | 2.50 |
| 226340 | 본느 | 17 | 8 | 100.00% | -4.43% | relatively_positive_history | 2.47 |
| 226330 | 신테카바이오 | 18 | 8 | 100.00% | -3.80% | relatively_positive_history | 2.44 |
| 009190 | 대양금속 | 14 | 3 | 100.00% | -3.14% | relatively_positive_history | 2.21 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| lawsuit | 95 | 4 | 100.00% | -1.27% | 4.00 |
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 282 | 35 | 48.57% | -1.60% | -2.00 |
| merger | 71 | 10 | 0.00% | 1.14% | -4.00 |
| paid_in_capital_increase | 319 | 63 | 39.68% | -1.33% | -5.00 |
| disclosure_violation | 52 | 4 | 0.00% | 0.00% | -6.00 |
| major_shareholder_change | 526 | 106 | 20.75% | 0.03% | -6.00 |
| investment_decision | 96 | 4 | 0.00% | 0.40% | -6.00 |
| spin_off | 24 | 6 | 33.33% | -0.57% | -6.00 |
| supply_contract | 303 | 60 | 20.00% | -1.40% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| lawsuit | 95 | 4 | 0 | 91 | 0.21 |
| convertible_bond | 282 | 17 | 18 | 247 | 0.11 |
| paid_in_capital_increase | 319 | 25 | 38 | 256 | 0.03 |
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| disclosure_violation | 52 | 0 | 4 | 48 | -0.23 |
| investment_decision | 96 | 0 | 4 | 92 | -0.29 |
| supply_contract | 303 | 12 | 48 | 243 | -0.59 |
| spin_off | 24 | 2 | 4 | 18 | -0.75 |

## Positive Candidates

### 1. 삼일씨엔에스 (004440)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **1.83**
- Adjusted recommendation score: **125.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.93%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.75%
- Next close return data: 0.93%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history added 1.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: 8월 28일 주식시장 주요공시 | 해상풍력 타워 및 하부구조물 글로벌 공급망 확보… 풍력 테마주에 매수... | [이넷뉴스 브랜드평판] 두산에너빌리티, 풍력에너지 상장기업 8월 1위·...

### 2. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **1.83**
- Adjusted recommendation score: **122.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.99%
- Next close return data: 0.77%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history added 1.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: 8월 28일 주식시장 주요공시 | 민선9기 미래산업 발맞춘 도의회… 관련 조례 '봇물' | 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성...

### 3. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **1.83**
- Adjusted recommendation score: **122.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.99%
- Next close return data: 0.77%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history added 1.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: 8월 28일 주식시장 주요공시 | 민선9기 미래산업 발맞춘 도의회… 관련 조례 '봇물' | 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성...

### 4. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **1.83**
- Adjusted recommendation score: **122.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.99%
- Next close return data: 0.77%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history added 1.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: 8월 28일 주식시장 주요공시 | 민선9기 미래산업 발맞춘 도의회… 관련 조례 '봇물' | 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성...

### 5. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **1.83**
- Adjusted recommendation score: **122.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.99%
- Next close return data: 0.77%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history added 1.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: 8월 28일 주식시장 주요공시 | 민선9기 미래산업 발맞춘 도의회… 관련 조례 '봇물' | 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 2. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 3. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 4. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 5. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 6. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 7. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 8. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 9. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

### 10. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-6.88**
- Adjusted recommendation score: **119.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -1.24%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.59 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 6.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 8월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-8월 31일] 美 증시, 워시 ‘매파 발언’에 투심 위... | 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니]

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
