# Daily Stock Candidate Report - 2026-09-15

Generated at: 2026-09-15 01:44:47

ML dataset: `data/processed/ml_dataset_20260915.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 12 | 12 | 100.00% | 5.43% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 14 | 9 | 100.00% | 7.29% | relatively_positive_history | 8.64 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 336260 | 두산퓨얼셀 | 8 | 5 | 80.00% | 10.47% | relatively_positive_history | 8.41 |
| 003060 | 에이프로젠바이오로직스 | 4 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.31 |
| 418620 | E8 | 8 | 6 | 66.67% | 3.17% | relatively_positive_history | 8.31 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| investment_decision | 218 | 117 | 64.96% | 1.71% | 5.00 |
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 204 | 106 | 72.64% | -2.11% | 4.00 |
| paid_in_capital_increase | 1145 | 842 | 60.45% | 0.67% | 3.00 |
| convertible_bond | 620 | 347 | 50.14% | 2.16% | 2.00 |
| bonus_issue | 57 | 54 | 51.85% | 0.78% | 0.00 |
| merger | 168 | 90 | 22.22% | 1.15% | -4.00 |
| disclosure_violation | 95 | 45 | 33.33% | 1.03% | -4.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| major_shareholder_change | 1179 | 696 | 27.73% | -0.81% | -6.00 |
| spin_off | 58 | 35 | 20.00% | -0.17% | -6.00 |
| supply_contract | 707 | 445 | 27.87% | -0.81% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| lawsuit | 204 | 77 | 29 | 98 | 1.46 |
| paid_in_capital_increase | 1145 | 509 | 333 | 303 | 1.35 |
| convertible_bond | 620 | 174 | 173 | 273 | 0.57 |
| investment_decision | 218 | 76 | 41 | 101 | 0.43 |
| disclosure_violation | 95 | 15 | 30 | 50 | -0.16 |
| bonus_issue | 57 | 28 | 26 | 3 | -0.74 |
| supply_contract | 707 | 124 | 321 | 262 | -1.12 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 1179 | 193 | 503 | 483 | -2.17 |

## Positive Candidates

### 1. 효성 (004800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.95**
- Adjusted recommendation score: **141.83**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: -2.44%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.38%
- Next close return data: -0.95%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 효성중공업, 美 빅테크서 3865억 수주 … AI 데이터센터 전력 인프라 공... | 효성중공업, 美 빅테크 2곳서 초고압변압기 3865억원 수주 | 효성중공업, 美판매법인에 초고압변압기 3866억원 공급 계약[공시]

### 2. 세보엠이씨 (011560)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.67**
- Adjusted recommendation score: **121.55**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 1.34%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.05%
- Next close return data: 0.21%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.67 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 14일 주식시장 주요공시 | "반도체 증설 본격화에 배관·덕트 등 인프라 수요 증가" | 삼성·SK가 점찍은 클린룸 강자들…반도체 투자에 실적 훈풍

### 3. 대화제약 (067080)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.62**
- Adjusted recommendation score: **121.50**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 2.01%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: 1.79%
- Next close return data: 5.47%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.62 points. Stock pattern label is not_enough_data.
- Related news examples: 9월 14일 주식시장 주요공시 | [혁신형 인증 영향도] 대화제약, R&D 기준 '안정권' 불구 투자 부담 | 제약바이오 직원 1인당 매출 3.4억…SK바이오팜 최다

### 4. 베노티앤알 (206400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.83**
- Adjusted recommendation score: **117.05**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 21, success rate: 52.38%, avg next close: -5.52%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -3.66%
- Next close return data: -5.77%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: [개장 전 주요 공시] 동부건설·링크솔루션·포스코인터내셔널·효성중... | 9월 14일 주식시장 주요공시 | [김승원 청문회] ① <공시검증> 한동훈 ‘오빠 게이트’…제넨셀 임상승...

### 5. 코나아이 (052400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.74**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **101.76**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 16, success rate: 100.00%, avg next close: 1.74%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 1.74%
- Next close return data: 1.74%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.74 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코나아이, 인천e음 기반 청년 창업 생태계 확장 | 코나아이, 청년 창업 지원으로 인천경제 활성화 앞장 | 코나아이, 인천 청년 창업 지원…대학생 창업팀 2곳 선정

### 6. 코나아이 (052400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.74**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **101.76**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 16, success rate: 100.00%, avg next close: 1.74%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 1.74%
- Next close return data: 1.74%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.74 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코나아이, 인천e음 기반 청년 창업 생태계 확장 | 코나아이, 청년 창업 지원으로 인천경제 활성화 앞장 | 코나아이, 인천 청년 창업 지원…대학생 창업팀 2곳 선정

### 7. 코나아이 (052400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.74**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **101.76**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 16, success rate: 100.00%, avg next close: 1.74%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 1.74%
- Next close return data: 1.74%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.74 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코나아이, 인천e음 기반 청년 창업 생태계 확장 | 코나아이, 청년 창업 지원으로 인천경제 활성화 앞장 | 코나아이, 인천 청년 창업 지원…대학생 창업팀 2곳 선정

### 8. 코나아이 (052400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.74**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **101.76**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 16, success rate: 100.00%, avg next close: 1.74%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 1.74%
- Next close return data: 1.74%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.74 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코나아이, 인천e음 기반 청년 창업 생태계 확장 | 코나아이, 청년 창업 지원으로 인천경제 활성화 앞장 | 코나아이, 인천 청년 창업 지원…대학생 창업팀 2곳 선정

### 9. 코나아이 (052400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.74**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **101.76**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 16, success rate: 100.00%, avg next close: 1.74%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 1.74%
- Next close return data: 1.74%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.74 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코나아이, 인천e음 기반 청년 창업 생태계 확장 | 코나아이, 청년 창업 지원으로 인천경제 활성화 앞장 | 코나아이, 인천 청년 창업 지원…대학생 창업팀 2곳 선정

### 10. 코나아이 (052400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.74**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **101.76**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 16, success rate: 100.00%, avg next close: 1.74%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 1.74%
- Next close return data: 1.74%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.74 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코나아이, 인천e음 기반 청년 창업 생태계 확장 | 코나아이, 청년 창업 지원으로 인천경제 활성화 앞장 | 코나아이, 인천 청년 창업 지원…대학생 창업팀 2곳 선정

## Volatile Watchlist

### 1. 보로노이 (310210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **90.00**
- Error-note adjustment score: **0.43**
- Event-type performance adjustment score: **5.00**
- Stock-specific pattern adjustment score: **4.14**
- Adjusted recommendation score: **99.57**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 14, success rate: 85.71%, avg next close: -2.61%, pattern: relatively_positive_history
- Disclosure title: [기재정정]투자판단관련주요경영사항(임상시험계획변경승인)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: -0.21%
- Next close return data: 1.73%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 11. Historical error notes added 0.43 points. Event-type performance added 5.00 points. Stock-specific history added 4.14 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, VRN11 태국 1b/2상 IND 승인 | [더벨][thebell interview | WCLC 2026] 보로노이, 폐암 1차 치료제 자신감... | 보로노이, VRN11 태국 1b/2상 IND 승인…글로벌 임상 확대

### 2. 이뮨온시아 (424870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **0.43**
- Event-type performance adjustment score: **5.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **89.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 100.00%, avg next close: 21.21%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획변경승인신청)              (IMC-002의 제1상 임상시험계획 변경승인신청)
- Next open return data: 21.21%
- Next close return data: 21.21%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes added 0.43 points. Event-type performance added 5.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주] 이뮨온시아, CD47 항체 신약 후보물질 1b상 IND 변경 승인 소식... | 이뮨온시아 'IMC-002', 췌장암 임상 1b상 코호트 식약처 승인 | 이뮨온시아, CD47 항체 'IMC-002' 1b상 변경 승인 소식에 상한가

### 3. 이뮨온시아 (424870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **0.43**
- Event-type performance adjustment score: **5.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **89.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 100.00%, avg next close: 21.21%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획변경승인신청)              (IMC-002의 제1상 임상시험계획 변경승인신청)
- Next open return data: 21.21%
- Next close return data: 21.21%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes added 0.43 points. Event-type performance added 5.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주] 이뮨온시아, CD47 항체 신약 후보물질 1b상 IND 변경 승인 소식... | 이뮨온시아 'IMC-002', 췌장암 임상 1b상 코호트 식약처 승인 | 이뮨온시아, CD47 항체 'IMC-002' 1b상 변경 승인 소식에 상한가

### 4. 이뮨온시아 (424870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **0.43**
- Event-type performance adjustment score: **5.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **89.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 100.00%, avg next close: 21.21%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획변경승인신청)              (IMC-002의 제1상 임상시험계획 변경승인신청)
- Next open return data: 21.21%
- Next close return data: 21.21%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes added 0.43 points. Event-type performance added 5.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주] 이뮨온시아, CD47 항체 신약 후보물질 1b상 IND 변경 승인 소식... | 이뮨온시아 'IMC-002', 췌장암 임상 1b상 코호트 식약처 승인 | 이뮨온시아, CD47 항체 'IMC-002' 1b상 변경 승인 소식에 상한가

### 5. 이뮨온시아 (424870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **0.43**
- Event-type performance adjustment score: **5.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **89.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 100.00%, avg next close: 21.21%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획변경승인)              (IMC-002의 제1상 임상시험계획 변경승인)
- Next open return data: 21.21%
- Next close return data: 21.21%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes added 0.43 points. Event-type performance added 5.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주] 이뮨온시아, CD47 항체 신약 후보물질 1b상 IND 변경 승인 소식... | 이뮨온시아 'IMC-002', 췌장암 임상 1b상 코호트 식약처 승인 | 이뮨온시아, CD47 항체 'IMC-002' 1b상 변경 승인 소식에 상한가

### 6. 이뮨온시아 (424870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **0.43**
- Event-type performance adjustment score: **5.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **89.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 100.00%, avg next close: 21.21%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획변경승인)              (IMC-002의 제1상 임상시험계획 변경승인)
- Next open return data: 21.21%
- Next close return data: 21.21%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes added 0.43 points. Event-type performance added 5.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주] 이뮨온시아, CD47 항체 신약 후보물질 1b상 IND 변경 승인 소식... | 이뮨온시아 'IMC-002', 췌장암 임상 1b상 코호트 식약처 승인 | 이뮨온시아, CD47 항체 'IMC-002' 1b상 변경 승인 소식에 상한가

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 에코심플렉스 (038870)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **92.38**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.61%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -4.87%
- Next close return data: -2.61%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 14일 주식시장 주요공시 | 탄소감축 찬바람에도 CCUS는 살아남나… 미코·SGC에너지 강세 | 글로벌 풍력·원전 모멘텀 가시화... 씨에스윈드·태웅 장중 약진

### 2. 대아티아이 (045390)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **103.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.12**
- Adjusted recommendation score: **95.76**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.15%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.47%
- Next close return data: 1.73%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 4. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: [개장 전 주요 공시] 동부건설·링크솔루션·포스코인터내셔널·효성중... | 9월 14일 주식시장 주요공시 | 철도연-신호기술사회, ‘2026 국제 철도신호기술 세미나’ 개최

### 3. 현대건설 (000720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.75**
- Adjusted recommendation score: **96.13**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 28.57%, avg next close: -1.89%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.48%
- Next close return data: 0.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 양주-삼성-수원·상록수 잇는 GTX-C 본격 공사…착공식 2년 8개월 만 | 한국투자증권, ELW 268종목 신규상장 | 한국투자증권, ELW 268종목 신규 상장

### 4. 현대건설 (000720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.75**
- Adjusted recommendation score: **96.13**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 28.57%, avg next close: -1.89%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.48%
- Next close return data: 0.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 양주-삼성-수원·상록수 잇는 GTX-C 본격 공사…착공식 2년 8개월 만 | 한국투자증권, ELW 268종목 신규상장 | 한국투자증권, ELW 268종목 신규 상장

### 5. 씨엔플러스 (115530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **109.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.56**
- Adjusted recommendation score: **98.32**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -1.15%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.36%
- Next close return data: -1.96%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.56 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 14일 주식시장 주요공시 | "전기가 부족하다"…AI 데이터센터가 불붙인 풍력株 투자 열기 | 글로벌 풍력·원전 모멘텀 가시화... 씨에스윈드·태웅 장중 약진

### 6. 동부건설 (005960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.38**
- Adjusted recommendation score: **99.50**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -0.45%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.35%
- Next close return data: -0.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.38 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 동부건설, 임직원 대상 인사이트 특강 실시 | 동부건설, 新조직문화 프로그램 운영…첫 특강 개최 | 동부건설, 임직원 조직문화 프로그램 '동부 시너지 시리즈'

### 7. 우리로 (046970)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **107.63**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -3.09%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.25%
- Next close return data: -3.09%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 14일 주식시장 주요공시 | 칩 포스트 갱, 매끈한 알고리즘 찢는 파열음…불협이 빚어낸 가장 다정... | [N2 모닝 경제 브리핑-9월 15일] 美 증시, AI 경고·국채금리 급등에 3대...

### 8. 아이비젼웍스 (469750)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.12**
- Adjusted recommendation score: **110.76**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -0.47%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 14일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 15일] 美 증시, AI 경고·국채금리 급등에 3대... | 기업 공시 [9월 14일]

### 9. 삼성중공업 (010140)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.80**
- Adjusted recommendation score: **112.08**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 15, success rate: 0.00%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.13%
- Next close return data: -3.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.80 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주] 삼성중공업, LNG선·FLNG '쌍끌이' 기대…IBK투자증권 "매수" | 삼성重, 20만㎥급 LNG선 포함 1.6조 규모 수주 | 추석 전 타결이냐 공동파업이냐…조선업계 '운명의 일주일'

### 10. 자람테크놀로지 (389020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.12**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **117.63**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -4.27%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: -0.97%
- Next close return data: -4.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.12 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 자람테크놀로지, XGS-PON ASIC 2차 계약 해지 | 9월 14일 주식시장 주요공시 | [코스피·코스닥,삼성중공업 SK바이오팜 대신증권 포스코인터내셔널 코...

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
