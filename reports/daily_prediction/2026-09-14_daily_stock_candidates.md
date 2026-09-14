# Daily Stock Candidate Report - 2026-09-14

Generated at: 2026-09-14 00:59:56

ML dataset: `data/processed/ml_dataset_20260914.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 12 | 12 | 100.00% | 5.43% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 14 | 9 | 100.00% | 7.29% | relatively_positive_history | 8.64 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 223310 | 사토시홀딩스 | 57 | 40 | 77.50% | 3.49% | relatively_positive_history | 8.43 |
| 336260 | 두산퓨얼셀 | 7 | 4 | 75.00% | 11.15% | relatively_positive_history | 8.32 |
| 418620 | E8 | 8 | 6 | 66.67% | 3.17% | relatively_positive_history | 8.31 |
| 003060 | 에이프로젠바이오로직스 | 4 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.31 |
| 288980 | 모아데이타 | 25 | 18 | 83.33% | 2.14% | relatively_positive_history | 6.95 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| lawsuit | 194 | 97 | 77.32% | -2.56% | 4.00 |
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| paid_in_capital_increase | 1079 | 776 | 59.54% | 0.86% | 3.00 |
| investment_decision | 206 | 105 | 63.81% | 0.30% | 3.00 |
| convertible_bond | 600 | 327 | 51.99% | 2.14% | 2.00 |
| merger | 167 | 89 | 21.35% | 1.22% | -4.00 |
| disclosure_violation | 92 | 42 | 30.95% | 1.10% | -4.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| major_shareholder_change | 1142 | 659 | 26.56% | -0.66% | -6.00 |
| spin_off | 57 | 35 | 20.00% | -0.17% | -6.00 |
| supply_contract | 679 | 417 | 27.82% | -0.72% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| lawsuit | 194 | 75 | 22 | 97 | 1.59 |
| paid_in_capital_increase | 1079 | 462 | 314 | 303 | 1.27 |
| convertible_bond | 600 | 170 | 157 | 273 | 0.63 |
| investment_decision | 206 | 67 | 38 | 101 | 0.33 |
| disclosure_violation | 92 | 13 | 29 | 50 | -0.24 |
| supply_contract | 679 | 116 | 301 | 262 | -1.12 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 1142 | 175 | 484 | 483 | -2.20 |
| merger | 167 | 19 | 70 | 78 | -2.37 |

## Positive Candidates

### 1. 인텔리안테크 (189300)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **175.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.25**
- Adjusted recommendation score: **167.63**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.23%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.89%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.25 points. Stock pattern label is not_enough_data.
- Related news examples: 인텔리안테크, NI와 409억원 위성통신 단말기 공급 계약…글로벌 국방시... | [개장 전 주요 공시] 한화시스템·삼성E&A·동부건설·LS 등 | 9월 11일 주식시장 주요공시

### 2. 지엔씨에너지 (119850)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.67**
- Adjusted recommendation score: **131.21**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -1.70%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.47%
- Next close return data: 1.58%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.67 points. Stock pattern label is not_enough_data.
- Related news examples: [개장 전 주요 공시] 한화시스템·삼성E&A·동부건설·LS 등 | 9월 11일 주식시장 주요공시 | [코스피·코스닥,삼성E&A 한화에어로스페이스 LGCNS 동부건설 한화시스...

### 3. 인티큐브 (070590)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **130.38**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.74%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 0.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | [코스피·코스닥,삼성E&A 한화에어로스페이스 LGCNS 동부건설 한화시스... | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…...

### 4. 코아스 (071950)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.33**
- Adjusted recommendation score: **127.21**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 83.33%, avg next close: -4.07%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -4.10%
- Next close return data: -8.87%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.33 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | [코스피·코스닥,삼성E&A 한화에어로스페이스 LGCNS 동부건설 한화시스... | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…...

### 5. 한화시스템 (272210)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **113.88**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.83%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.13%
- Next close return data: 1.83%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 바다 위 AI센터·가스공장…조선 빅3, 가스텍서 미래 먹거리 공개 | 5609일 전 "형우선배, 그때도 계셨다" 고영표 공부 '천적' 잡고 금자탑 ... | 지니틱스 中 자회사, 45억원 AI 인프라 첫 대규모 수주 성과

### 6. 유디엠텍 (389680)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.15**
- Adjusted recommendation score: **98.03**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 21, success rate: 52.38%, avg next close: 3.11%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.35%
- Next close return data: 3.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | AI 뜨자 에스피소프트·에스투더블유 폭등… IT서비스株 희비 | AI·로봇株 극심한 양극화…에스투더블유 26% 폭등랠리 '눈에 띄네'

### 7. 유디엠텍 (389680)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.15**
- Adjusted recommendation score: **98.03**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 21, success rate: 52.38%, avg next close: 3.11%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.35%
- Next close return data: 3.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | AI 뜨자 에스피소프트·에스투더블유 폭등… IT서비스株 희비 | AI·로봇株 극심한 양극화…에스투더블유 26% 폭등랠리 '눈에 띄네'

### 8. 유디엠텍 (389680)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.15**
- Adjusted recommendation score: **98.03**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 21, success rate: 52.38%, avg next close: 3.11%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.35%
- Next close return data: 3.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | AI 뜨자 에스피소프트·에스투더블유 폭등… IT서비스株 희비 | AI·로봇株 극심한 양극화…에스투더블유 26% 폭등랠리 '눈에 띄네'

### 9. 유디엠텍 (389680)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.15**
- Adjusted recommendation score: **98.03**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 21, success rate: 52.38%, avg next close: 3.11%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.35%
- Next close return data: 3.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | AI 뜨자 에스피소프트·에스투더블유 폭등… IT서비스株 희비 | AI·로봇株 극심한 양극화…에스투더블유 26% 폭등랠리 '눈에 띄네'

### 10. 유디엠텍 (389680)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.15**
- Adjusted recommendation score: **98.03**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 21, success rate: 52.38%, avg next close: 3.11%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.35%
- Next close return data: 3.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | AI 뜨자 에스피소프트·에스투더블유 폭등… IT서비스株 희비 | AI·로봇株 극심한 양극화…에스투더블유 26% 폭등랠리 '눈에 띄네'

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 코닉오토메이션 (391710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **96.38**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 8.08%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 6.04%
- Next close return data: 8.08%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 4. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 11일 주식시장 주요공시 | 9월 14일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…...

### 2. 한국정밀기계 (101680)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **117.63**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.74%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.08%
- Next close return data: -1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…... | [공시Pick] 한국정밀기계, TEI 추가 수주에 공시 직후 9%대까지 올라

### 3. 한국정밀기계 (101680)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **117.63**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.74%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.08%
- Next close return data: -1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…... | [공시Pick] 한국정밀기계, TEI 추가 수주에 공시 직후 9%대까지 올라

### 4. 한국정밀기계 (101680)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **117.63**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.74%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.08%
- Next close return data: -1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…... | [공시Pick] 한국정밀기계, TEI 추가 수주에 공시 직후 9%대까지 올라

### 5. 일성건설 (013360)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **136.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.44**
- Adjusted recommendation score: **121.44**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.49%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.94%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 3. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.44 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | GS건설· IPARK현대산업개발 주가 신바람… 주택 공급 정책 수혜 모멘텀... | 건설주 신바람… 원전·해외 수주 기대에 매수세 몰린다

### 6. 동부건설 (005960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.82**
- Adjusted recommendation score: **125.06**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -0.43%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.82 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [개장 전 주요 공시] 한화시스템·삼성E&A·동부건설·LS 등 | 9월 11일 주식시장 주요공시 | [코스피·코스닥,삼성E&A 한화에어로스페이스 LGCNS 동부건설 한화시스...

### 7. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.00**
- Adjusted recommendation score: **133.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 35, success rate: 42.86%, avg next close: 1.39%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…... | [제약공시 책갈피] 9월 2주차 - SK바이오팜·알리코제약 外

### 8. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.00**
- Adjusted recommendation score: **133.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 35, success rate: 42.86%, avg next close: 1.39%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…... | [제약공시 책갈피] 9월 2주차 - SK바이오팜·알리코제약 外

### 9. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.00**
- Adjusted recommendation score: **133.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 35, success rate: 42.86%, avg next close: 1.39%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…... | [제약공시 책갈피] 9월 2주차 - SK바이오팜·알리코제약 外

### 10. 신테카바이오 (226330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.00**
- Adjusted recommendation score: **133.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 35, success rate: 42.86%, avg next close: 1.39%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 14일] 美 증시, 5거래일 만에 3대 지수 반등…... | [제약공시 책갈피] 9월 2주차 - SK바이오팜·알리코제약 外

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
