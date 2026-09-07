# Daily Stock Candidate Report - 2026-09-07

Generated at: 2026-09-07 00:27:32

ML dataset: `data/processed/ml_dataset_20260907.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 12 | 12 | 100.00% | 5.43% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 21 | 20 | 100.00% | 3.04% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 006980 | 우성 | 12 | 6 | 100.00% | 15.55% | relatively_positive_history | 8.50 |
| 288980 | 모아데이타 | 18 | 11 | 81.82% | 4.96% | relatively_positive_history | 8.33 |
| 336260 | 두산퓨얼셀 | 7 | 4 | 75.00% | 11.15% | relatively_positive_history | 8.32 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 006840 | AK홀딩스 | 3 | 3 | 100.00% | -0.53% | relatively_positive_history | 6.00 |
| 003920 | 남양유업 | 10 | 9 | 100.00% | -0.86% | relatively_positive_history | 5.90 |
| 225190 | LK삼양 | 1 | 1 | 100.00% | 13.37% | relatively_positive_history | 5.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| investment_decision | 145 | 44 | 59.09% | 4.66% | 7.00 |
| paid_in_capital_increase | 797 | 494 | 65.59% | 0.28% | 6.00 |
| lawsuit | 163 | 67 | 77.61% | -1.02% | 4.00 |
| convertible_bond | 485 | 212 | 63.68% | -1.19% | 1.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| spin_off | 33 | 11 | 36.36% | 0.41% | -3.00 |
| merger | 123 | 45 | 17.78% | 1.88% | -4.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| disclosure_violation | 62 | 12 | 8.33% | 0.72% | -6.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| major_shareholder_change | 931 | 448 | 28.57% | -0.56% | -6.00 |
| supply_contract | 546 | 284 | 23.94% | -1.04% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 797 | 324 | 170 | 303 | 1.39 |
| lawsuit | 163 | 52 | 15 | 96 | 1.32 |
| convertible_bond | 485 | 135 | 77 | 273 | 0.92 |
| investment_decision | 145 | 26 | 18 | 101 | 0.03 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| disclosure_violation | 62 | 1 | 11 | 50 | -0.45 |
| spin_off | 33 | 4 | 7 | 22 | -0.88 |
| supply_contract | 546 | 68 | 216 | 262 | -1.14 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 931 | 128 | 320 | 483 | -1.72 |

## Positive Candidates

### 1. 두산퓨얼셀 (336260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **149.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **148.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 11.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 4.10%
- Next close return data: 15.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [모닝 리포트] 두산퓨얼셀, 美 AI 데이터센터 5014억 수주…"PAFC 가능성... | 두산퓨얼셀, 미국 연료전지 수주… 내년 실적 반등 기대[애널리스트의 ... | NH투자증권 "두산퓨얼셀, 140MW 美 수주.. 목표가 7.06% 상향"

### 2. 두산퓨얼셀 (336260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **149.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **148.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 11.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 4.10%
- Next close return data: 15.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [모닝 리포트] 두산퓨얼셀, 美 AI 데이터센터 5014억 수주…"PAFC 가능성... | 두산퓨얼셀, 미국 연료전지 수주… 내년 실적 반등 기대[애널리스트의 ... | NH투자증권 "두산퓨얼셀, 140MW 美 수주.. 목표가 7.06% 상향"

### 3. 두산퓨얼셀 (336260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **149.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **148.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 11.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 4.10%
- Next close return data: 15.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [모닝 리포트] 두산퓨얼셀, 美 AI 데이터센터 5014억 수주…"PAFC 가능성... | 두산퓨얼셀, 미국 연료전지 수주… 내년 실적 반등 기대[애널리스트의 ... | NH투자증권 "두산퓨얼셀, 140MW 美 수주.. 목표가 7.06% 상향"

### 4. 두산퓨얼셀 (336260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **149.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **148.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 11.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 4.10%
- Next close return data: 15.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [모닝 리포트] 두산퓨얼셀, 美 AI 데이터센터 5014억 수주…"PAFC 가능성... | 두산퓨얼셀, 미국 연료전지 수주… 내년 실적 반등 기대[애널리스트의 ... | NH투자증권 "두산퓨얼셀, 140MW 美 수주.. 목표가 7.06% 상향"

### 5. 두산퓨얼셀 (336260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **149.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **148.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 11.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 4.10%
- Next close return data: 15.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [모닝 리포트] 두산퓨얼셀, 美 AI 데이터센터 5014억 수주…"PAFC 가능성... | 두산퓨얼셀, 미국 연료전지 수주… 내년 실적 반등 기대[애널리스트의 ... | NH투자증권 "두산퓨얼셀, 140MW 美 수주.. 목표가 7.06% 상향"

### 6. 두산퓨얼셀 (336260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **149.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **148.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 11.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 4.10%
- Next close return data: 15.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [모닝 리포트] 두산퓨얼셀, 美 AI 데이터센터 5014억 수주…"PAFC 가능성... | 두산퓨얼셀, 미국 연료전지 수주… 내년 실적 반등 기대[애널리스트의 ... | NH투자증권 "두산퓨얼셀, 140MW 美 수주.. 목표가 7.06% 상향"

### 7. APS이노베이션 (079810)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **2.00**
- Adjusted recommendation score: **127.86**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.12%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 2.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 4일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 7일] 美 증시, 고용 호조에 금리 인상 경계…... | APS이노베이션, 63억 규모 공급계약 체결

### 8. 세보엠이씨 (011560)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **126.36**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.48%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 1.66%
- Next close return data: 2.48%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 4일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 7일] 美 증시, 고용 호조에 금리 인상 경계…... | 세보엠이씨, 430억 규모 공급계약 체결

### 9. LS (006260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **4.75**
- Adjusted recommendation score: **117.61**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 3.01%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.50%
- Next close return data: 3.01%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 4.75 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터도 ‘조립식’으로…GS건설, 공장에서 만들고 현장서 붙인... | 9월 4일 주식시장 주요공시 | 폴리텍대학, 반도체·IT 등 내년도 신입생 5천550명 모집

### 10. 코오롱 (002020)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **89.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **5.25**
- Adjusted recommendation score: **85.11**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 83.33%, avg next close: 0.29%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.79%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history added 5.25 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 4일 주식시장 주요공시 | 3,500번의 가위질, 60년을 이어온 손끝의 철학 | [티슈진發 코오롱 재무변동성]③추가수혈 가능성↑…㈜코오롱 수익으로...

## Volatile Watchlist

### 1. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **-1.78**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **8.50**
- Adjusted recommendation score: **54.72**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 15.55%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 12.85%
- Next close return data: 15.55%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.78 points. Event-type performance subtracted 4.00 points. Stock-specific history added 8.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 롯데건설, 도곡우성아파트 재건축 수주…4002억원 규모 | 롯데건설, 도곡우성아파트 재건축 수주…도시정비 올해 누적 수주 4조 돌... | 9월 4일 주식시장 주요공시

### 2. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **-1.78**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **8.50**
- Adjusted recommendation score: **54.72**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 15.55%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 12.85%
- Next close return data: 15.55%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.78 points. Event-type performance subtracted 4.00 points. Stock-specific history added 8.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 롯데건설, 도곡우성아파트 재건축 수주…4002억원 규모 | 롯데건설, 도곡우성아파트 재건축 수주…도시정비 올해 누적 수주 4조 돌... | 9월 4일 주식시장 주요공시

### 3. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **-1.78**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **8.50**
- Adjusted recommendation score: **54.72**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 15.55%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 12.85%
- Next close return data: 15.55%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.78 points. Event-type performance subtracted 4.00 points. Stock-specific history added 8.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 롯데건설, 도곡우성아파트 재건축 수주…4002억원 규모 | 롯데건설, 도곡우성아파트 재건축 수주…도시정비 올해 누적 수주 4조 돌... | 9월 4일 주식시장 주요공시

### 4. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **-1.78**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **8.50**
- Adjusted recommendation score: **54.72**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 15.55%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 12.85%
- Next close return data: 15.55%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.78 points. Event-type performance subtracted 4.00 points. Stock-specific history added 8.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 롯데건설, 도곡우성아파트 재건축 수주…4002억원 규모 | 롯데건설, 도곡우성아파트 재건축 수주…도시정비 올해 누적 수주 4조 돌... | 9월 4일 주식시장 주요공시

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. SNT홀딩스 (036530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.78**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-5.90**
- Adjusted recommendation score: **55.32**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -0.85%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)(자회사의 주요경영사항)              
- Next open return data: 1.55%
- Next close return data: 1.00%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.78 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 5.90 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | SNT모티브, 로봇 자회사 흡수합병…실질 매출 창출 '과제' | 주주환원에 자회사 호재까지… 지주사주 '옥석 가리기'

### 2. SK이노베이션 (096770)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **-1.78**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **62.47**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.45%, pattern: weak_historical_reaction
- Disclosure title: 정정신고서제출요구( 2026.08.26. 제출 증권신고서(합병) )
- Next open return data: 0.07%
- Next close return data: -1.45%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.78 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [투자자 순매수 TOP5] 3대 수급 주체 동반 매도…SK하이닉스 순매도 1위 | 배터리 3사 부채비율 뜯어보니 | 하나證 “2차전지 비중확대⋯미국 BESS 탈중국 수혜 주목”

### 3. 현대바이오 (048410)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **7.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **64.78**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항(임상시험계획변경승인신청)              (전립선암 치료제 CPPCA07의 1상 임상시험계획 변경승인 신청)
- Next open return data: 0.97%
- Next close return data: 0.00%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes added 0.03 points. Event-type performance added 7.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 현대百그룹, 중소 협력사 결제대금 2738억원 조기 지급 | [Who's Who Legal Korea 2026] Corporate and M&A | 9월 4일 주식시장 주요공시

### 4. 오스코텍 (039200)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **7.00**
- Stock-specific pattern adjustment score: **-1.65**
- Adjusted recommendation score: **65.38**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.68%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항(임상시험결과)              (알츠하이머 치료 후보물질 ADELY01 임상 1a/1b상 임상시험결과보고서(CSR) 수령)
- Next open return data: 0.00%
- Next close return data: -0.68%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes added 0.03 points. Event-type performance added 7.00 points. Stock-specific history subtracted 1.65 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | [더벨][클리니컬 리포트] 오스코텍·아델 알츠하이머 신약 1상 종료, 다... | 오스코텍, 사노피 L/O '타우 항체' 1a/b상 "CSR 수령"

### 5. 금화피에스시 (036190)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **85.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-2.50**
- Adjusted recommendation score: **73.36**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -0.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.15%
- Next close return data: -0.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 5. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 2.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | 원전주 엇갈려…두산에너빌리티·우리기술↑, 금화피에스시는 ↓ | AI 데이터센터가 불붙인 원전株…두산에너빌리티·한전기술 주목

### 6. 이노메트리 (302430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **93.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-2.00**
- Adjusted recommendation score: **81.86**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.97%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.28%
- Next close return data: -0.97%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 2.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | 이노메트리, 북미 ESS 검사장비 수주 가속…"글로벌 고객사 추가 공급 협... | "정밀 모터 없으면 공장 안 돌아간다"… 에스테크엠, 독보적 기술로 실...

### 7. 엑시콘 (092870)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **84.61**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -4.75%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -4.75%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | [주간 코스닥 기관] 이오테크닉스 로보티즈 피노 ISC 담고 알테오젠 심... | [주간 코스닥 외국인] 주성엔지니어링 로보티즈 원익IPS 테스 실리콘투...

### 8. 코오롱글로벌 (003070)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-5.40**
- Adjusted recommendation score: **87.46**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 11.11%, avg next close: -0.32%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 5.40 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | 여성 연봉, 남성의 72%…5년 새 3%P 좁혔지만 격차 여전[2026 양성평등지... | 이사회 문은 열렸는데…승진해 오르는 미등기임원 여성은 6.5%뿐[2026 양성...

### 9. 인콘 (083640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-5.33**
- Adjusted recommendation score: **87.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 5.33 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | [코스피·코스닥,SKC 우성 듀켐바이오 두산퓨얼셀 SOOP톱텍 사토시홀딩... | [N2 모닝 경제 브리핑-9월 7일] 美 증시, 고용 호조에 금리 인상 경계…...

### 10. 인콘 (083640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-5.33**
- Adjusted recommendation score: **87.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 5.33 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 4일 주식시장 주요공시 | [코스피·코스닥,SKC 우성 듀켐바이오 두산퓨얼셀 SOOP톱텍 사토시홀딩... | [N2 모닝 경제 브리핑-9월 7일] 美 증시, 고용 호조에 금리 인상 경계…...

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
