# Daily Stock Candidate Report - 2026-10-14

Generated at: 2026-10-14 02:04:04

ML dataset: `data/processed/ml_dataset_20261014.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 010950 | S-Oil | 9 | 9 | 88.89% | 5.68% | relatively_positive_history | 8.72 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 044380 | 주연테크 | 18 | 13 | 92.31% | 6.24% | relatively_positive_history | 8.58 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 100.00% | 1.92% | 8.00 |
| lawsuit | 379 | 259 | 58.30% | -0.62% | 3.00 |
| paid_in_capital_increase | 2036 | 1518 | 57.38% | 0.20% | 3.00 |
| convertible_bond | 997 | 665 | 53.38% | 1.03% | 2.00 |
| disclosure_violation | 153 | 83 | 49.40% | -0.32% | 0.00 |
| investment_decision | 378 | 263 | 53.61% | -0.02% | 0.00 |
| bonus_issue | 102 | 99 | 41.41% | -0.40% | -3.00 |
| bond_with_warrant | 86 | 74 | 20.27% | -0.04% | -6.00 |
| major_shareholder_change | 1911 | 1278 | 34.59% | -0.75% | -6.00 |
| merger | 364 | 269 | 19.70% | 0.56% | -6.00 |
| spin_off | 90 | 58 | 34.48% | 0.21% | -6.00 |
| supply_contract | 1114 | 788 | 27.92% | -0.85% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 0 | 4 | 2.50 |
| paid_in_capital_increase | 2036 | 871 | 647 | 518 | 1.19 |
| lawsuit | 379 | 151 | 108 | 120 | 1.14 |
| convertible_bond | 997 | 355 | 310 | 332 | 0.85 |
| disclosure_violation | 153 | 41 | 42 | 70 | 0.52 |
| investment_decision | 378 | 141 | 122 | 115 | -0.39 |
| bonus_issue | 102 | 41 | 58 | 3 | -1.15 |
| bond_with_warrant | 86 | 15 | 59 | 12 | -1.19 |
| supply_contract | 1114 | 220 | 568 | 326 | -1.31 |
| spin_off | 90 | 20 | 38 | 32 | -1.84 |

## Positive Candidates

### 1. 세보엠이씨 (011560)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.25**
- Adjusted recommendation score: **144.94**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 1.44%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.23%
- Next close return data: 1.64%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.25 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 13일 주식시장 주요공시 | [코스피·코스닥, 삼성전자 신한지주 LS머트리얼즈 SK네트웍스 대우건설... | [리스트] MVP 상위 20선...한양디지텍, 에프앤가이드 등 - 14일

### 2. LS머트리얼즈 (417200)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **125.19**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 5.45%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.84%
- Next close return data: 5.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: LS머트리얼즈, AI 데이터센터 전력 안정화 기술 확대…美 수소연료전지... | [속보] LS머트리얼즈 VI 발동, 오전장 주가 급등 | LS마린, 8200억원 곳간 채우고 뱃길 넓힌다

### 3. 코오롱 (002020)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.42**
- Adjusted recommendation score: **108.11**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 84.62%, avg next close: -0.74%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -2.56%
- Next close return data: 1.86%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.42 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코오롱인더스트리, 2026년 채용전환형 인턴 모집…19일까지 접수 | 코오롱인더스트리, 20개 부문 신입사원 채용…19일까지 접수 | “물류 현장서 사람 개입 최소화”…로브로스, 조선소·반도체 공장 공...

### 4. 태영건설 (009410)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.54**
- Adjusted recommendation score: **103.23**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 100.00%, avg next close: 0.15%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 1.19%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.54 points. Stock pattern label is relatively_positive_history.
- Related news examples: 태영건설, 고창 덕산지구에 '고창 데시앙' 11월 분양 | 태영건설, 고창 덕산지구에 데시앙 888세대 분양 | 태영건설, '고창 데시앙' 11월 분양 예정

### 5. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.10**
- Adjusted recommendation score: **97.79**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 0.24%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.09%
- Next close return data: 2.17%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.10 points. Stock pattern label is not_enough_data.
- Related news examples: [기업들] AI·디지털 전환부터 주거 안전까지…교원라이프·HD현대·현대... | HD현대·지멘스, 부산에 조선 디지털 전환 거점 구축 | 조의장, 그리스서 경제협력 간담회…방산·첨단산업 세일즈외교

### 6. 코어라인소프트 (384470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **79.00**
- Error-note adjustment score: **2.50**
- Event-type performance adjustment score: **8.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **93.50**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 1.69%, pattern: relatively_positive_history
- Disclosure title: 연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 3.59%
- Next close return data: 1.69%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes added 2.50 points. Event-type performance added 8.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코어라인소프트, 日 원격판독망 뚫었다…심혈관 AI 공급 | 10월 13일 주식시장 주요공시 | [오늘의 IR] SK리츠·삼양컴텍·명신산업 등

### 7. 코어라인소프트 (384470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **79.00**
- Error-note adjustment score: **2.50**
- Event-type performance adjustment score: **8.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **93.50**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 1.69%, pattern: relatively_positive_history
- Disclosure title: 연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 3.59%
- Next close return data: 1.69%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes added 2.50 points. Event-type performance added 8.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코어라인소프트, 日 원격판독망 뚫었다…심혈관 AI 공급 | 10월 13일 주식시장 주요공시 | [오늘의 IR] SK리츠·삼양컴텍·명신산업 등

### 8. HD현대중공업 (329180)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.25**
- Adjusted recommendation score: **92.44**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.72%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.04%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.25 points. Stock pattern label is not_enough_data.
- Related news examples: 울산시, 21개 기업과 사회공헌 협약…지역 나눔 이어간다 | [기업들] AI·디지털 전환부터 주거 안전까지…교원라이프·HD현대·현대... | HD현대·지멘스, 부산에 조선 디지털 전환 거점 구축

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 2. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 3. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 4. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 5. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 6. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 7. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 8. 팅크웨어 (084730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-9.50**
- Adjusted recommendation score: **63.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -4.76%
- Next close return data: -5.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 9.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | [개장 전 주요 공시] 삼성전자·SK네트웍스·DL이앤씨·두산퓨얼셀·STX ... | 팅크웨어, BMW에 293억원 블랙박스 공급

### 9. 에이직랜드 (445090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **84.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **72.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.15%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.15%
- Next close return data: -2.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | 메모리 넘어 피지컬 AI까지…‘SEDEX 2026’ 반도체 미래 기술 총출동 | SEDEX 14일 개막…삼전·SK하닉, AI 반도체 기술 전시…KT·카카오 [기업...

### 10. KC코트렐 (119650)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **88.00**
- Error-note adjustment score: **-1.31**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.50**
- Adjusted recommendation score: **78.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 4. Historical error notes subtracted 1.31 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 13일 주식시장 주요공시 | KC코트렐, 영흥 5호기 교체공사 계약 100억8025만원으로 증액 | 10월 12일 주식시장 주요공시

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
