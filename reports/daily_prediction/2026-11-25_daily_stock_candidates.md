# Daily Stock Candidate Report - 2026-11-25

Generated at: 2026-11-25 05:30:59

ML dataset: `data/processed/ml_dataset_20261125.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 10 | 10 | 100.00% | 16.52% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 248170 | 샘표식품 | 22 | 22 | 95.45% | 26.45% | relatively_positive_history | 8.89 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 922 | 826 | 46.25% | 4.82% | 4.00 |
| convertible_bond | 1711 | 1378 | 59.72% | 0.16% | 3.00 |
| paid_in_capital_increase | 3172 | 2651 | 56.51% | -0.23% | 3.00 |
| bonus_issue | 120 | 117 | 47.86% | 0.36% | 0.00 |
| investment_decision | 662 | 547 | 51.01% | 0.16% | 0.00 |
| lawsuit | 672 | 551 | 51.54% | -0.42% | 0.00 |
| disclosure_violation | 232 | 162 | 43.21% | -0.85% | -3.00 |
| bond_with_warrant | 163 | 151 | 41.72% | 0.04% | -3.00 |
| spin_off | 159 | 123 | 39.02% | 0.81% | -3.00 |
| major_shareholder_change | 3414 | 2780 | 40.04% | -0.81% | -3.00 |
| supply_contract | 2004 | 1678 | 35.64% | -0.70% | -3.00 |
| earnings_guidance | 96 | 92 | 26.09% | -1.87% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1711 | 823 | 555 | 333 | 1.43 |
| paid_in_capital_increase | 3172 | 1498 | 1153 | 521 | 1.27 |
| lawsuit | 672 | 284 | 267 | 121 | 0.92 |
| disclosure_violation | 232 | 70 | 92 | 70 | 0.32 |
| bond_with_warrant | 163 | 63 | 88 | 12 | 0.31 |
| bonus_issue | 120 | 56 | 61 | 3 | -0.46 |
| investment_decision | 662 | 279 | 268 | 115 | -0.73 |
| supply_contract | 2004 | 598 | 1080 | 326 | -1.02 |
| merger | 922 | 382 | 444 | 96 | -1.30 |
| earnings_guidance | 96 | 24 | 68 | 4 | -1.54 |

## Positive Candidates

### 1. 에코심플렉스 (038870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **123.48**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 0.41%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 1.84%
- Next close return data: 0.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 24일 주식시장 주요공시 | 11월 25일 개장 전 주요 공시 | 에코심플렉스, 수도권매립지 운영관리 9억5300만원 계약

### 2. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **117.13**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 3. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **117.13**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 4. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **117.13**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 5. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **117.13**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 6. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.08**
- Adjusted recommendation score: **105.06**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 57.14%, avg next close: 1.76%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.20%
- Next close return data: -0.40%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.08 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 목감천 하천정비사업 공사비 98억원 증액…총 998억원 | [2026 SCCI] (1) 삼성물산, 역대 최초 ‘AAA’…현대·GS·대우·포스코 ‘... | [2026 SCCI] (2) 스마트건설 현장적용 81.5점…삼성·대우·롯데·호반·우...

### 7. 삼성E&A (028050)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.50**
- Adjusted recommendation score: **102.48**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 1.20%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.17%
- Next close return data: 3.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [인사] 삼성E&A | [건설 Pick] 현대건설·대우건설·삼성E&A, 스타트업 협업·사회공헌 최... | <오늘의 인사>

### 8. 스피어 (347700)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.11**
- Adjusted recommendation score: **91.09**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 54.17%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.95%
- Next close return data: 2.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 0.11 points. Stock pattern label is relatively_positive_history.
- Related news examples: "해외 병원·빅파마 정조준"… 뷰노·뉴로핏, 글로벌 성과 가시화에 주... | 폴2: 데드포인트, 극장 나와도 이어지는 고소공포 | "주 1회 주사도 번거롭다, 이제 한 달에 한 번"…인벤티지랩·올릭스, 차...

### 9. 스피어 (347700)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.11**
- Adjusted recommendation score: **91.09**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 54.17%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.95%
- Next close return data: 2.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 0.11 points. Stock pattern label is relatively_positive_history.
- Related news examples: "해외 병원·빅파마 정조준"… 뷰노·뉴로핏, 글로벌 성과 가시화에 주... | 폴2: 데드포인트, 극장 나와도 이어지는 고소공포 | "주 1회 주사도 번거롭다, 이제 한 달에 한 번"…인벤티지랩·올릭스, 차...

### 10. 스피어 (347700)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.11**
- Adjusted recommendation score: **91.09**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 54.17%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.95%
- Next close return data: 2.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 0.11 points. Stock pattern label is relatively_positive_history.
- Related news examples: "해외 병원·빅파마 정조준"… 뷰노·뉴로핏, 글로벌 성과 가시화에 주... | 폴2: 데드포인트, 극장 나와도 이어지는 고소공포 | "주 1회 주사도 번거롭다, 이제 한 달에 한 번"…인벤티지랩·올릭스, 차...

## Volatile Watchlist

### 1. SK이노베이션 (096770)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **70.00**
- Error-note adjustment score: **-1.30**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-0.52**
- Adjusted recommendation score: **72.18**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 14, success rate: 57.14%, avg next close: -3.59%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.66%
- Next close return data: -0.44%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.30 points. Event-type performance added 4.00 points. Stock-specific history subtracted 0.52 points. Stock pattern label is relatively_positive_history.
- Related news examples: 현대엔지니어링, 용인·호남 발전소 연속 수주…두달 새 2.3조 규모 | 현대ENG, 용인·호남 발전소 2.28조 수주…우협 선정 두 달 만에 본계약 | "겁먹고 주식 팔았는데 어쩌나"…코스피 '바닥 신호' 나왔다 [한경우의...

### 2. HJ중공업 (097230)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-0.73**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **65.42**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.73 points. Event-type performance did not change the score. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 3. HJ중공업 (097230)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-0.73**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **65.42**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.73 points. Event-type performance did not change the score. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 4. HJ중공업 (097230)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-0.73**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **65.42**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.73 points. Event-type performance did not change the score. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 5. HJ중공업 (097230)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-0.73**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **1.15**
- Adjusted recommendation score: **65.42**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 38, success rate: 60.53%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.49%
- Next close return data: 0.29%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.73 points. Event-type performance did not change the score. Stock-specific history added 1.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: HJ중공업, 해경 중형 공기부양정 1척 건조 수주 | HJ중공업, 해경 중형 공기부양정 1척 건조 계약…248억원 규모 | HJ重, 해경 공기부양정 건조 수주

### 6. 에이프로 (262260)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-1.30**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.17**
- Adjusted recommendation score: **57.87**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 4.91%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: 2.49%
- Next close return data: -1.58%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.30 points. Event-type performance added 4.00 points. Stock-specific history added 8.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 24일 주식시장 주요공시 | 모친상 한 달 만…손나은, "아무리 애써도 버티기 힘들어"→가슴 먹먹한... | 마무리 캠프 ‘사즉생 캠프’

### 7. SK (034730)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-1.30**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **1.07**
- Adjusted recommendation score: **50.77**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 13, success rate: 61.54%, avg next close: -1.71%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)(자회사의 주요경영사항)              
- Next open return data: -2.71%
- Next close return data: -7.58%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.30 points. Event-type performance added 4.00 points. Stock-specific history added 1.07 points. Stock pattern label is relatively_positive_history.
- Related news examples: 현대엔지니어링, 용인·호남 발전소 연속 수주…두달 새 2.3조 규모 | '젠슨 황 랠리' 하루 천하…亞 증시, AI 거품 공포에 다시 급락 | “한국이 돈 쓸어담을 절호의 기회”…‘이것’ 확보에 사활 거는 빅테...

### 8. SK아이이테크놀로지 (361610)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **44.00**
- Error-note adjustment score: **-1.30**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **3.75**
- Adjusted recommendation score: **50.45**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 7, success rate: 71.43%, avg next close: -2.14%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.56%
- Next close return data: -2.16%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.30 points. Event-type performance added 4.00 points. Stock-specific history added 3.75 points. Stock pattern label is relatively_positive_history.
- Related news examples: [단독] 프리미어, 한국펀드파트너스 인수 본계약…PTA 지분 20% 재출자 | SKIET, 내년 2월 1일 소멸…SK이노베이션에 흡수합병 | K배터리 엇갈린 실적…다음 과제는 'ESS 납품'

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 미래에셋비전스팩7호 (482680)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **63.00**
- Error-note adjustment score: **-1.30**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **62.70**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 4. Historical error notes subtracted 1.30 points. Event-type performance added 4.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 24일 주식시장 주요공시 | 휘청이는 증시에 VC주도 '파란불'… 우리기술투자·아주IB투자 낙폭 어디... | 상승보다 하락 종목 많았다…스팩 테마주에 무슨 일?

### 2. 코아스템켐온 (166480)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **71.98**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -5.79%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.62%
- Next close return data: -5.79%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 생물공학 상장기업 2026년 11월 브랜드평판...알테오젠, 에이비엘바이오... | 11월 24일 주식시장 주요공시 | 알테오젠, 11월 생물공학 상장기업 브랜드평판 1위...에이비엘바이오·...

### 3. 수산인더스트리 (126720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **72.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.16**
- Adjusted recommendation score: **72.14**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 29, success rate: 86.21%, avg next close: -2.76%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.11%
- Next close return data: -0.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 6. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.16 points. Stock pattern label is relatively_positive_history.
- Related news examples: [52주] 최저가 95개, 최고가 3개... 코스피 4700대로 | 11월 24일 주식시장 주요공시 | 금양그린파워 주가 '불기둥'…두산에너빌리티·효성중공업도 원전주 견...

### 4. OCI (456040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **87.00**
- Error-note adjustment score: **-0.73**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **81.77**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.02%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: -1.12%
- Next close return data: -1.02%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 0.73 points. Event-type performance did not change the score. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [애널픽] 신재생에너지, 내년 '옥석 가리기'...OCI홀딩스·씨에스윈드 주... | 시장 커지는데 공장 멈춘다? 보급·제조 따로 노는 태양광 정책 | 짓기도 사오기도 어려워진 폴리실리콘 … 생산기지 확보한 OCI '반사이익...

### 5. 한전기술 (052690)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.42**
- Adjusted recommendation score: **84.56**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: -0.70%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.97%
- Next close return data: -1.79%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.42 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한전기술, 서남권 해상풍력 확산1단지 사업 불참 최종 결정 | 한화오션, 서남권 해상풍력 확산1단지 사업 최종 불참 결정 | 11월 24일 주식시장 주요공시

### 6. 일성건설 (013360)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-8.32**
- Adjusted recommendation score: **104.66**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 33.33%, avg next close: -3.20%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.07%
- Next close return data: -6.03%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 8.32 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한국기술교육대 '산업안전정책 최고경영자과정' 제5기 수료식 성황 | 한기대, 산업안전정책 최고경영자과정 제5기 수료식 | 11월 24일 주식시장 주요공시

### 7. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.97**
- Adjusted recommendation score: **117.01**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 22, success rate: 36.36%, avg next close: -0.13%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.17%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.97 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 24일 주식시장 주요공시 | [창간 40주년 특집] "건설 통해 나라에 보답 신념 원칙·가치 우선 정도... | 중소형 건설주 줄줄이 하락… 웰크론한텍·신원종합개발은 선방

### 8. 엠엑스로보틱스 (007820)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-3.38**
- Adjusted recommendation score: **129.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.92%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.55%
- Next close return data: -2.92%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 3.38 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 24일 주식시장 주요공시 | 로보티즈·휴림로봇 기계주 '후끈'…로봇에서 건설장비까지 매수 온기 ... | SK하이닉스 실적 성장 기대에 그룹주 들썩…SK텔레콤·SK바이오팜도 올...

### 9. 유니테스트 (086390)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **130.73**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -3.02%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -1.43%
- Next close return data: -4.07%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 24일 주식시장 주요공시 | [코스피·코스닥, 삼성E&A 에코프로비엠 일성건설 제일기획 유니테스트... | [N2 모닝 경제 브리핑-11월 25일] 美 증시, 엔비디아발 랠리 하루 만에 ...

### 10. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **138.73**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 0.00%, avg next close: -1.92%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.54%
- Next close return data: -0.09%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 네오셈, 삼성전자에 CLT INTERFACE BOARD 국내 공급 계약 | 11월 24일 주식시장 주요공시 | [코스피·코스닥, 삼성E&A 에코프로비엠 일성건설 제일기획 유니테스트...

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
