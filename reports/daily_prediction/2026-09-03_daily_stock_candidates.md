# Daily Stock Candidate Report - 2026-09-03

Generated at: 2026-09-03 00:55:18

ML dataset: `data/processed/ml_dataset_20260903.csv`

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
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 288980 | 모아데이타 | 15 | 9 | 88.89% | 5.12% | relatively_positive_history | 8.43 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 006840 | AK홀딩스 | 3 | 3 | 100.00% | -0.53% | relatively_positive_history | 6.00 |
| 003920 | 남양유업 | 10 | 9 | 100.00% | -0.86% | relatively_positive_history | 5.90 |
| 378340 | 필에너지 | 1 | 1 | 100.00% | 7.40% | relatively_positive_history | 5.50 |
| 225190 | LK삼양 | 1 | 1 | 100.00% | 13.37% | relatively_positive_history | 5.50 |
| 028260 | 삼성물산 | 21 | 14 | 85.71% | 0.99% | relatively_positive_history | 5.50 |
| 100840 | SNT에너지 | 2 | 2 | 100.00% | 9.57% | relatively_positive_history | 5.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| investment_decision | 126 | 34 | 55.88% | 5.57% | 7.00 |
| paid_in_capital_increase | 600 | 344 | 65.12% | 0.61% | 6.00 |
| convertible_bond | 407 | 160 | 70.62% | -2.15% | 4.00 |
| lawsuit | 134 | 43 | 83.72% | -1.26% | 4.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| spin_off | 27 | 8 | 37.50% | 1.02% | -1.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| disclosure_violation | 55 | 7 | 14.29% | 0.72% | -6.00 |
| major_shareholder_change | 706 | 286 | 20.63% | -0.50% | -6.00 |
| merger | 89 | 28 | 7.14% | -0.20% | -6.00 |
| supply_contract | 484 | 241 | 16.60% | -1.61% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 600 | 224 | 120 | 256 | 1.27 |
| lawsuit | 134 | 36 | 7 | 91 | 1.19 |
| convertible_bond | 407 | 113 | 47 | 247 | 1.04 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 126 | 19 | 15 | 92 | -0.08 |
| disclosure_violation | 55 | 1 | 6 | 48 | -0.24 |
| spin_off | 27 | 3 | 5 | 19 | -0.74 |
| supply_contract | 484 | 40 | 201 | 243 | -1.43 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 706 | 59 | 227 | 420 | -1.83 |

## Positive Candidates

### 1. SNT에너지 (100840)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **121.07**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 9.57%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.78%
- Next close return data: 9.57%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹... | [이넷뉴스 브랜드평판] 현대차, 전기차 상장기업 9월 1위... LG에너지솔루...

### 2. SNT에너지 (100840)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **121.07**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 9.57%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.78%
- Next close return data: 9.57%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹... | [이넷뉴스 브랜드평판] 현대차, 전기차 상장기업 9월 1위... LG에너지솔루...

### 3. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

### 4. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

### 5. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

### 6. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

### 7. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

### 8. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

### 9. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

### 10. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.98**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.02**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 5.43%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.66%
- Next close return data: 5.43%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 2.98 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 2일 주식시장 주요공시 | 코스피, 3.99% 급락 딛고 반등할까…美반도체주 강세 ‘훈풍’ | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. HL홀딩스 (060980)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **108.32**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.13%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.00%
- Next close return data: -0.13%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 2일 주식시장 주요공시 | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹... | [리스트] 국내 고배당주 20선

### 2. SNT홀딩스 (036530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.50**
- Adjusted recommendation score: **113.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.46%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.00%
- Next close return data: -1.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 2일 주식시장 주요공시 | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹... | [더벨][Company Watch] SNT모티브, 로보틱스 흡수합병…로봇 판 더 키운다

### 3. SNT홀딩스 (036530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.50**
- Adjusted recommendation score: **113.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.46%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.00%
- Next close return data: -1.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 2일 주식시장 주요공시 | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹... | [더벨][Company Watch] SNT모티브, 로보틱스 흡수합병…로봇 판 더 키운다

### 4. 비에이치아이 (083650)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **116.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.85%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.35%
- Next close return data: -1.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 비에이치아이, 1,453억 원 규모 쿠웨이트 발전·담수화 플랜트 HRSG 수주 | 9월 2일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 3일] 美 증시, 국채금리 숨고르기에 3대 지수...

### 5. HL D&I (014790)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **121.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.74%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.78%
- Next close return data: -1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 2일 주식시장 주요공시 | [코스피·코스닥, SK이노베이션 미 캐피털그룹 에코프로비엠 캐피털그룹... | [N2 모닝 경제 브리핑-9월 3일] 美 증시, 국채금리 숨고르기에 3대 지수...

### 6. 일신석재 (007110)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-1.88**
- Adjusted recommendation score: **123.69**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 1.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 2일 주식시장 주요공시 | 9월 3일 개장 전 주요 공시 | 28억 석공사 계약, 일신석재 GS건설 수주

### 7. 두산퓨얼셀 (336260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **147.00**
- Error-note adjustment score: **-1.43**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **133.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.97%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 3.36%
- Next close return data: -2.97%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Negative keyword count is 1. Historical error notes subtracted 1.43 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 메리츠증권 "두산퓨얼셀, 美 데이터센터 첫 진출…수출 성장 본격화" | 기다리던 美 수주에도 뒷걸음…두산퓨얼셀, 반전의 열쇠는 | 美증시 반등에 저가매수 유입…삼전·하이닉스 프리마켓 1%대↑

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
