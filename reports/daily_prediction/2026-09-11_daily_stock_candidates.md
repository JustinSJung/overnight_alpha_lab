# Daily Stock Candidate Report - 2026-09-11

Generated at: 2026-09-11 01:09:57

ML dataset: `data/processed/ml_dataset_20260911.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 12 | 12 | 100.00% | 5.43% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 14 | 9 | 100.00% | 7.29% | relatively_positive_history | 8.64 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 223310 | 사토시홀딩스 | 57 | 40 | 77.50% | 3.49% | relatively_positive_history | 8.43 |
| 336260 | 두산퓨얼셀 | 7 | 4 | 75.00% | 11.15% | relatively_positive_history | 8.32 |
| 418620 | E8 | 8 | 6 | 66.67% | 3.17% | relatively_positive_history | 8.31 |
| 288980 | 모아데이타 | 24 | 17 | 88.24% | 2.16% | relatively_positive_history | 7.00 |
| 326030 | 에스케이바이오팜 | 5 | 5 | 100.00% | -0.40% | relatively_positive_history | 6.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| lawsuit | 191 | 94 | 78.72% | -2.62% | 4.00 |
| investment_decision | 199 | 98 | 62.24% | -0.68% | 3.00 |
| paid_in_capital_increase | 1032 | 729 | 59.81% | 0.79% | 3.00 |
| convertible_bond | 575 | 302 | 51.66% | 2.43% | 2.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| merger | 165 | 87 | 20.69% | 1.27% | -4.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| disclosure_violation | 69 | 19 | 26.32% | 0.23% | -6.00 |
| major_shareholder_change | 1114 | 631 | 26.47% | -0.66% | -6.00 |
| spin_off | 56 | 34 | 20.59% | -0.17% | -6.00 |
| supply_contract | 638 | 376 | 26.60% | -0.81% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| lawsuit | 191 | 74 | 20 | 97 | 1.62 |
| paid_in_capital_increase | 1032 | 436 | 293 | 303 | 1.26 |
| convertible_bond | 575 | 156 | 146 | 273 | 0.59 |
| investment_decision | 199 | 61 | 37 | 101 | 0.23 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| disclosure_violation | 69 | 5 | 14 | 50 | -0.25 |
| supply_contract | 638 | 100 | 276 | 262 | -1.14 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 1114 | 167 | 464 | 483 | -2.17 |
| merger | 165 | 18 | 69 | 78 | -2.38 |

## Positive Candidates

### 1. 비에이치아이 (083650)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **160.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.12**
- Adjusted recommendation score: **152.98**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.85%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: 비에이치아이 주가, 9월 10일 66,900원 0.30% 상승 마감 | 비에이치아이, 미국 원전 시장 수주 국면 전환 수혜 기대 - 맥쿼리證 | 투자 심리 위축된 에너지 시장… 개별 모멘텀 품은 종목만 살아남는다

### 2. 다우기술 (023590)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **123.36**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 3.38%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.95%
- Next close return data: 3.38%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 9월 11일 개장 전 주요 공시 | [주요공시] S-Oi, 삼성바이오로직스, HD현대중공업, 피델릭스, 다우기술...

### 3. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.00**
- Adjusted recommendation score: **104.86**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 3.49%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: 3.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 인천 분양가 3.3㎡당 2236만원 돌파…공사비 상승 속 신규 공급 이어져 | '금리 리스크' 노출도 커진 GS건설 | 해양진흥공사, 韓 기업 해외 물류 거점 확보 지원 강화

### 4. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.00**
- Adjusted recommendation score: **104.86**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 3.49%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: 3.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 인천 분양가 3.3㎡당 2236만원 돌파…공사비 상승 속 신규 공급 이어져 | '금리 리스크' 노출도 커진 GS건설 | 해양진흥공사, 韓 기업 해외 물류 거점 확보 지원 강화

### 5. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.00**
- Adjusted recommendation score: **104.86**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 3.49%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: 3.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 인천 분양가 3.3㎡당 2236만원 돌파…공사비 상승 속 신규 공급 이어져 | '금리 리스크' 노출도 커진 GS건설 | 해양진흥공사, 韓 기업 해외 물류 거점 확보 지원 강화

### 6. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.00**
- Adjusted recommendation score: **104.86**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 3.49%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: 3.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 인천 분양가 3.3㎡당 2236만원 돌파…공사비 상승 속 신규 공급 이어져 | '금리 리스크' 노출도 커진 GS건설 | 해양진흥공사, 韓 기업 해외 물류 거점 확보 지원 강화

### 7. 자연과환경 (043910)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **93.86**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.49%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 2.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 아산 영인산산림박물관, 교육 뮤지컬 '주토피아' 운영 | 알라미아, GEFFA 2026 참여…세계 어린이·가족과 지속가능한 일상 가치... | [세대공감] 개발이 아닌 재난, 발전이 아닌 파괴

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 2. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 3. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 4. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 5. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 6. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 7. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 8. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 9. 삼성바이오로직스 (207940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.95**
- Adjusted recommendation score: **85.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 35.71%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.19%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.95 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 삼성전자·SK하이닉스 4%대 급락… 코스피 파란불 | [개장 전 주요 공시] 한화에어로스페이스·삼성E&A·자이에스앤디·SKC 등 | 美 증시 악재에 삼성전자·SK하이닉스 3% 하락 [마켓시그널]

### 10. 코미팜 (041960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **93.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **88.36**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.65%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 오늘의 메모[9월 11일] | [주식] GC녹십자웰빙 '지방분해 주사' 중국 문 열까...주가 16%↑ | 양 제약지수 동반 하락, 경남제약 10.68% ↓

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
