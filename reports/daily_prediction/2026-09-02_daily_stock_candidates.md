# Daily Stock Candidate Report - 2026-09-02

Generated at: 2026-09-02 00:49:30

ML dataset: `data/processed/ml_dataset_20260902.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 288980 | 모아데이타 | 15 | 9 | 88.89% | 5.12% | relatively_positive_history | 8.43 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 006840 | AK홀딩스 | 3 | 3 | 100.00% | -0.53% | relatively_positive_history | 6.00 |
| 003920 | 남양유업 | 10 | 9 | 100.00% | -0.86% | relatively_positive_history | 5.90 |
| 028260 | 삼성물산 | 21 | 14 | 85.71% | 0.99% | relatively_positive_history | 5.50 |
| 225190 | LK삼양 | 1 | 1 | 100.00% | 13.37% | relatively_positive_history | 5.50 |
| 378340 | 필에너지 | 1 | 1 | 100.00% | 7.40% | relatively_positive_history | 5.50 |
| 002020 | 코오롱 | 11 | 4 | 100.00% | 0.39% | relatively_positive_history | 5.36 |
| 058730 | 다스코 | 6 | 2 | 100.00% | 3.22% | relatively_positive_history | 4.83 |
| 012200 | 계양전기 | 20 | 20 | 100.00% | -1.66% | relatively_positive_history | 4.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 400 | 153 | 69.93% | -2.17% | 4.00 |
| lawsuit | 125 | 34 | 91.18% | -1.39% | 4.00 |
| paid_in_capital_increase | 476 | 220 | 53.18% | 1.54% | 2.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| spin_off | 27 | 8 | 37.50% | 1.02% | -1.00 |
| investment_decision | 115 | 23 | 47.83% | -2.14% | -2.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| bonus_issue | 11 | 8 | 0.00% | -0.36% | -6.00 |
| disclosure_violation | 54 | 6 | 16.67% | 0.02% | -6.00 |
| major_shareholder_change | 666 | 246 | 21.95% | -0.47% | -6.00 |
| merger | 86 | 25 | 8.00% | -0.11% | -6.00 |
| supply_contract | 459 | 216 | 17.13% | -1.50% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| lawsuit | 125 | 31 | 3 | 91 | 1.17 |
| convertible_bond | 400 | 107 | 46 | 247 | 0.99 |
| paid_in_capital_increase | 476 | 117 | 103 | 256 | 0.58 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| disclosure_violation | 54 | 1 | 5 | 48 | -0.19 |
| investment_decision | 115 | 11 | 12 | 92 | -0.25 |
| spin_off | 27 | 3 | 5 | 19 | -0.74 |
| supply_contract | 459 | 37 | 179 | 243 | -1.34 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 666 | 54 | 192 | 420 | -1.61 |

## Positive Candidates

### 1. 유한양행 (000100)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **128.16**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.48%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 0.48%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: "1천310억원 규모"…유한양행, 글로벌 제약사와 원료의약품 공급계약 '잭... | 9월 1일 주식시장 주요공시 | KB證 “주주환원이 주가를 올리려면… 어려울 때도 주주 우선하는 신뢰...

### 2. 에이텍 (045660)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **123.16**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.65%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 1일 주식시장 주요공시 | 9월 2일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-9월 2일] 美 증시, 미·이란 충돌 격화에 3대 지수...

### 3. 삼화네트웍스 (046390)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **104.66**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.92%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.92%
- Next close return data: 1.92%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 1일 주식시장 주요공시 | 하이브, 9월 엔터 브랜드평판 1위…JYP·카카오 순 | 하이브 1위 지켰지만 '흔들'…JYP·카카오 무섭게 치고 올라왔다

## Volatile Watchlist

### 1. 온코크로스 (382150)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-0.25**
- Event-type performance adjustment score: **-2.00**
- Stock-specific pattern adjustment score: **-0.50**
- Adjusted recommendation score: **97.25**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: -3.56%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (앱티스와 ADC 또는 BsADC 후보물질 공동연구 및 개발 계약 체결)
- Next open return data: 1.45%
- Next close return data: -3.56%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 13. Historical error notes subtracted 0.25 points. Event-type performance subtracted 2.00 points. Stock-specific history subtracted 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 1일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 2일] 美 증시, 미·이란 충돌 격화에 3대 지수... | [HIT알공] 유한양행, 1311억원 원료의약품 공급 계약

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 두산에너빌리티 (034020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **75.41**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -2.70%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -3.19%
- Next close return data: -2.70%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 美-이란 교전 재개, 국제유가 '요동'...코스피 '급락 출발' | 부산대, 동남권 AX 혁신 전면에… '거점국립대 패키지 지원사업' 선정 | 헬기로 수색견 이송...기업 오늘도 공중수색 시도

### 2. 두산에너빌리티 (034020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **75.41**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -2.70%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -3.19%
- Next close return data: -2.70%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 美-이란 교전 재개, 국제유가 '요동'...코스피 '급락 출발' | 부산대, 동남권 AX 혁신 전면에… '거점국립대 패키지 지원사업' 선정 | 헬기로 수색견 이송...기업 오늘도 공중수색 시도

### 3. 두산에너빌리티 (034020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **75.41**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -2.70%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.19%
- Next close return data: -2.70%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 美-이란 교전 재개, 국제유가 '요동'...코스피 '급락 출발' | 부산대, 동남권 AX 혁신 전면에… '거점국립대 패키지 지원사업' 선정 | 헬기로 수색견 이송...기업 오늘도 공중수색 시도

### 4. 두산에너빌리티 (034020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **75.41**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -2.70%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.19%
- Next close return data: -2.70%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 美-이란 교전 재개, 국제유가 '요동'...코스피 '급락 출발' | 부산대, 동남권 AX 혁신 전면에… '거점국립대 패키지 지원사업' 선정 | 헬기로 수색견 이송...기업 오늘도 공중수색 시도

### 5. 한성크린텍 (066980)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **93.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.00**
- Adjusted recommendation score: **79.66**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.67%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -1.91%
- Next close return data: -4.46%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 1일 주식시장 주요공시 | 8월 28일 주식시장 주요공시 | '국민학교떡볶이' 러시아 2000여개 매장 진출…초도 45만개 직수출

### 6. 인텍플러스 (064290)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **80.16**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.04%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -4.08%
- Next close return data: -2.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 1일 주식시장 주요공시 | “HBM만 보지 마세요”…반도체 증설 본격화, 후공정주도 소·부·장 볕... | [주간 코스닥 외국인] 실리콘투 집중 매수…반도체·바이오도 담았다

### 7. 스피어 (347700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-3.21**
- Adjusted recommendation score: **84.45**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.84%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.03%
- Next close return data: -2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 3.21 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 하나에어로다이내믹스, 코스닥 상장예비심사 통과 | 잡코리아 채용공고, 잡플래닛에도 뜬다…웍스피어 첫 서비스 연동 | 잡코리아, 잡플래닛과 첫 공고 연동 서비스 론칭

### 8. 스피어 (347700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-3.21**
- Adjusted recommendation score: **84.45**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.84%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.03%
- Next close return data: -2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 3.21 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 하나에어로다이내믹스, 코스닥 상장예비심사 통과 | 잡코리아 채용공고, 잡플래닛에도 뜬다…웍스피어 첫 서비스 연동 | 잡코리아, 잡플래닛과 첫 공고 연동 서비스 론칭

### 9. HJ중공업 (097230)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **90.91**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.61%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.18%
- Next close return data: -2.61%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 부산시 정비사업 현황과 전망(1)- 부산진구 | 부산시 '2026 부산 건축취업박람회' 청년 구직 지원 확대 | 9월 1일 주식시장 주요공시

### 10. 센서뷰 (321370)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.34**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-3.50**
- Adjusted recommendation score: **91.16**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.06%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.09%
- Next close return data: -1.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.34 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 3.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [드론전 위클리(Drone war weekly)] 숨가뿐 드론 전장, 드론 생산 전쟁 | 9월 1일 주식시장 주요공시 | [주식마감] '탈모 치료제' 기대감에 현대약품·JW신약 상한가... SK디앤디...

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
