# Daily Stock Candidate Report - 2026-09-04

Generated at: 2026-09-04 00:45:09

ML dataset: `data/processed/ml_dataset_20260904.csv`

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
| 267250 | HD현대 | 21 | 20 | 100.00% | 3.04% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 288980 | 모아데이타 | 16 | 10 | 80.00% | 4.48% | relatively_positive_history | 8.31 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 006840 | AK홀딩스 | 3 | 3 | 100.00% | -0.53% | relatively_positive_history | 6.00 |
| 003920 | 남양유업 | 10 | 9 | 100.00% | -0.86% | relatively_positive_history | 5.90 |
| 378340 | 필에너지 | 1 | 1 | 100.00% | 7.40% | relatively_positive_history | 5.50 |
| 028260 | 삼성물산 | 21 | 14 | 85.71% | 0.99% | relatively_positive_history | 5.50 |
| 100840 | SNT에너지 | 2 | 2 | 100.00% | 9.57% | relatively_positive_history | 5.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| investment_decision | 127 | 35 | 57.14% | 5.23% | 7.00 |
| paid_in_capital_increase | 703 | 447 | 67.34% | -0.17% | 6.00 |
| convertible_bond | 433 | 186 | 67.20% | -1.48% | 4.00 |
| lawsuit | 153 | 62 | 77.42% | -1.08% | 4.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| spin_off | 27 | 8 | 37.50% | 1.02% | -1.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| disclosure_violation | 58 | 10 | 10.00% | 0.85% | -6.00 |
| major_shareholder_change | 805 | 385 | 30.13% | -0.53% | -6.00 |
| merger | 89 | 28 | 7.14% | -0.20% | -6.00 |
| supply_contract | 508 | 265 | 23.02% | -1.34% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 703 | 301 | 146 | 256 | 1.52 |
| lawsuit | 153 | 48 | 14 | 91 | 1.29 |
| convertible_bond | 433 | 125 | 61 | 247 | 1.02 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 127 | 20 | 15 | 92 | -0.04 |
| disclosure_violation | 58 | 1 | 9 | 48 | -0.38 |
| spin_off | 27 | 3 | 5 | 19 | -0.74 |
| supply_contract | 508 | 61 | 204 | 243 | -1.18 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 805 | 116 | 269 | 420 | -1.62 |

## Positive Candidates

### 1. 티에스아이 (277880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **131.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.54%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 2.94%
- Next close return data: 1.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 티에스아이, ‘믹싱장비 원천기술국’ 일본서 241억 규모 설비 공급 수... | 9월 3일 주식시장 주요공시 | 티에스아이, 日 DJK와 241억 이차전지 믹싱설비 공급계약

### 2. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 3. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 4. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 5. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 6. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 7. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 8. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 9. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

### 10. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **93.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.23%
- Next close return data: 3.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 노동장관, 삼성·SK·현대차·LG에 "청년 더 뽑아달라" | 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증...

## Volatile Watchlist

### 1. 페니트리움바이오 (187660)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **54.00**
- Error-note adjustment score: **-0.04**
- Event-type performance adjustment score: **7.00**
- Stock-specific pattern adjustment score: **-1.30**
- Adjusted recommendation score: **59.66**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: -6.27%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획승인신청등결정)              (재발성 또는 불응성 진행성 고형암 임상 2a상 임상시험계획 숭인)
- Next open return data: 0.39%
- Next close return data: -6.27%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 0.04 points. Event-type performance added 7.00 points. Stock-specific history subtracted 1.30 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 3일 주식시장 주요공시 | 페니트리움바이오, 美 FDA 임상 2a상 승인…'가짜내성' 항암제 검증 나선... | [코스피·코스닥, 한화오션 삼성화재  삼호개발 에이프로젠바이오로직...

### 2. 엔시트론 (101400)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **39.00**
- Error-note adjustment score: **-1.62**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.50**
- Adjusted recommendation score: **30.88**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -3.08%, pattern: relatively_positive_history
- Disclosure title: 최대주주변경              
- Next open return data: 0.00%
- Next close return data: -3.08%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.62 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 3일 주식시장 주요공시 | 9월 4일 개장 전 주요 공시 | 엔시트론 품는 캑터스PE, 론다코리아와 '반도체 동맹'

### 3. 엔시트론 (101400)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **39.00**
- Error-note adjustment score: **-1.62**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.50**
- Adjusted recommendation score: **30.88**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -3.08%, pattern: relatively_positive_history
- Disclosure title: 최대주주변경              
- Next open return data: 0.00%
- Next close return data: -3.08%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.62 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 3일 주식시장 주요공시 | 9월 4일 개장 전 주요 공시 | 엔시트론 품는 캑터스PE, 론다코리아와 '반도체 동맹'

### 4. 대원전선 (006340)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.62**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.25**
- Adjusted recommendation score: **22.13**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 0.92%, pattern: not_enough_data
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.13%
- Next close return data: 3.38%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.62 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.25 points. Stock pattern label is not_enough_data.
- Related news examples: [금융 HOT 뉴스] KB자산운용, 'AI전력인프라 ETF' 주목 | 한화투자증권, '올 가을 투자의 시작' 비대면 이벤트 실시 外 | [운용 NOW] 미래에셋자산운용·한국투자신탁운용·KB자산운용

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **39.00**
- Error-note adjustment score: **-1.62**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.42**
- Adjusted recommendation score: **25.96**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 12, success rate: 16.67%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.06%
- Next close return data: 2.34%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.62 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.42 points. Stock pattern label is weak_historical_reaction.
- Related news examples: AI·6G 투자 시계 빨라진다…통신주 성장 기대감 '쑥'[애널리스트의 시... | [어제장 오늘장] 코스피 30분 급락 후 급반등…커지는 변동성, 오늘은? | "코스피, 5% 금리 레드라인 넘지 않는다면 반등 여력 충분"

### 2. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **39.00**
- Error-note adjustment score: **-1.62**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.42**
- Adjusted recommendation score: **25.96**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 12, success rate: 16.67%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.06%
- Next close return data: 2.34%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.62 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.42 points. Stock pattern label is weak_historical_reaction.
- Related news examples: AI·6G 투자 시계 빨라진다…통신주 성장 기대감 '쑥'[애널리스트의 시... | [어제장 오늘장] 코스피 30분 급락 후 급반등…커지는 변동성, 오늘은? | "코스피, 5% 금리 레드라인 넘지 않는다면 반등 여력 충분"

### 3. HS화성 (002460)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **64.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.55**
- Adjusted recommendation score: **47.27**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -1.42%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.02%
- Next close return data: -0.28%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -1. Negative keyword count is 7. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.55 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 3일 주식시장 주요공시 | [더벨][Company Watch] '에크라' 앞세운 HS화성, 서울 상급지 수주 잰걸음 | 건설주 혼조…GS건설·DL이앤씨 2%대 상승, 미국 이란 전쟁 확산 여부 변...

### 4. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **73.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **0.05**
- Adjusted recommendation score: **63.87**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.00%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 1.70%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -1. Negative keyword count is 4. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 0.05 points. Stock pattern label is not_enough_data.
- Related news examples: 9월 3일 주식시장 주요공시 | '성장에만 눈멀었나'…신호철 카카오페이증권, 민원 829% 폭증에 금감원... | SK하이닉스·삼성전자 거래대금 7.7조…포스코인터내셔널 2조

### 5. 코오롱 (002020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **78.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **5.42**
- Adjusted recommendation score: **74.24**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 0.35%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.20%
- Next close return data: 0.20%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 5.42 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 3일 주식시장 주요공시 | [티슈진發 코오롱 재무변동성]②주가 급락한 티슈진, 1385억 CB 내년 현금... | [Weekly New패션] 한낮엔 여름인데, 벌써 나온 경량패딩

### 6. 코오롱글로벌 (003070)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-5.41**
- Adjusted recommendation score: **82.41**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 12.50%, avg next close: -0.30%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.65%
- Next close return data: 0.21%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 5.41 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 3일 주식시장 주요공시 | [더벨][노타 밸류업] 모바일서 로봇까지…AI 최적화 영토 넓힌다 | [더벨][CFO 워치] 코오롱생명과학, 지주조달통 CFO로 영입

### 7. HD한국조선해양 (009540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-1.88**
- Adjusted recommendation score: **85.94**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.15%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 1.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 마키나락스, '어텐션 2026' AI 컨퍼런스 개최 | [미르의 글로벌 레이더] HD현대, 美 프레이저 ‘2년내 10만제곱피트 증... | 9월 3일 주식시장 주요공시

### 8. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **111.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-5.85**
- Adjusted recommendation score: **95.97**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 11.11%, avg next close: -0.52%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.48%
- Next close return data: 0.48%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 3. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 5.85 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 3일 주식시장 주요공시 | [코스피·코스닥, 한화오션 삼성화재  삼호개발 에이프로젠바이오로직... | 9월 4일 개장 전 주요 공시

### 9. LIG아큐버 (073490)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **103.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **97.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.23%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.75%
- Next close return data: 1.23%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 4. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 3일 주식시장 주요공시 | [애널픽] 무선통신장비주 주목..."피지컬AI 통신망 투자 본격화" | [아주증시포커스] 규정강화 후 상폐 1호 '코이즈'…시총 미달·동전주 8...

### 10. 한화오션 (042660)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-2.47**
- Adjusted recommendation score: **105.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 44.44%, avg next close: -0.23%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.35%
- Next close return data: 0.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 2.47 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 3일 주식시장 주요공시 | "민관군 힘 합쳐 25조 미 해군 MRO시장 적극 공략해야" | [K-방산의 민낯②] 비리기업 처벌하면 멈추는 안보…딜레마 빠진 정부

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
