# Daily Stock Candidate Report - 2026-10-13

Generated at: 2026-10-13 03:54:06

ML dataset: `data/processed/ml_dataset_20261013.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 010950 | S-Oil | 9 | 9 | 88.89% | 5.68% | relatively_positive_history | 8.72 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 044380 | 주연테크 | 18 | 13 | 92.31% | 6.24% | relatively_positive_history | 8.58 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 377 | 257 | 57.98% | -0.62% | 3.00 |
| paid_in_capital_increase | 1957 | 1439 | 59.90% | 0.17% | 3.00 |
| convertible_bond | 984 | 652 | 52.76% | 1.06% | 2.00 |
| disclosure_violation | 152 | 82 | 50.00% | -0.32% | 0.00 |
| investment_decision | 373 | 258 | 52.71% | -0.01% | 0.00 |
| major_shareholder_change | 1862 | 1229 | 35.88% | -0.78% | -3.00 |
| bonus_issue | 102 | 99 | 41.41% | -0.40% | -3.00 |
| bond_with_warrant | 77 | 65 | 9.23% | 0.07% | -6.00 |
| merger | 360 | 265 | 19.62% | 0.58% | -6.00 |
| spin_off | 90 | 58 | 34.48% | 0.21% | -6.00 |
| supply_contract | 1086 | 760 | 27.89% | -0.83% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1957 | 862 | 577 | 518 | 1.32 |
| lawsuit | 377 | 149 | 108 | 120 | 1.12 |
| convertible_bond | 984 | 344 | 308 | 332 | 0.81 |
| disclosure_violation | 152 | 41 | 41 | 70 | 0.54 |
| investment_decision | 373 | 136 | 122 | 115 | -0.47 |
| bonus_issue | 102 | 41 | 58 | 3 | -1.15 |
| supply_contract | 1086 | 212 | 548 | 326 | -1.27 |
| major_shareholder_change | 1862 | 441 | 788 | 633 | -1.78 |
| spin_off | 90 | 20 | 38 | 32 | -1.84 |

## Positive Candidates

### 1. 이노시뮬레이션 (274400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **138.23**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 4.86%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.21%
- Next close return data: 4.86%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 12일 주식시장 주요공시 | 이노시뮬레이션, 현대차와 9억3600만원 계약 | [공시 Pick] 이노시뮬레이션, 현대차와 후속 수주에 주가 강세

### 2. 솔디펜스 (215090)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.56**
- Adjusted recommendation score: **134.29**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 5.21%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.55%
- Next close return data: 5.21%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.56 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 12일 주식시장 주요공시 | 솔디펜스, 한화시스템에 LAH 86억원 공급 | 10월 13일 개장 전 주요 공시

### 3. 서진시스템 (178320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **117.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 73, success rate: 80.82%, avg next close: -3.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -3.77%
- Next close return data: -6.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 12일 주식시장 주요공시 | [코스피·코스닥, 한화머시너리앤서비스홀딩스 셀트리온 KCC건설 코츠테... | 서진시스템, 블룸에너지에 SOFC 부품·모듈 1064억 공급

### 4. 서진시스템 (178320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **117.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 73, success rate: 80.82%, avg next close: -3.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -3.77%
- Next close return data: -6.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 12일 주식시장 주요공시 | [코스피·코스닥, 한화머시너리앤서비스홀딩스 셀트리온 KCC건설 코츠테... | 서진시스템, 블룸에너지에 SOFC 부품·모듈 1064억 공급

### 5. 서진시스템 (178320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **117.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 73, success rate: 80.82%, avg next close: -3.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -3.77%
- Next close return data: -6.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 12일 주식시장 주요공시 | [코스피·코스닥, 한화머시너리앤서비스홀딩스 셀트리온 KCC건설 코츠테... | 서진시스템, 블룸에너지에 SOFC 부품·모듈 1064억 공급

### 6. 서진시스템 (178320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **117.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 73, success rate: 80.82%, avg next close: -3.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -3.77%
- Next close return data: -6.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 12일 주식시장 주요공시 | [코스피·코스닥, 한화머시너리앤서비스홀딩스 셀트리온 KCC건설 코츠테... | 서진시스템, 블룸에너지에 SOFC 부품·모듈 1064억 공급

### 7. 핀텔 (291810)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.63**
- Adjusted recommendation score: **115.36**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 19, success rate: 78.95%, avg next close: -0.38%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.63 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 12일 주식시장 주요공시 | 핀텔, 인천공항 영상분석 계약 7억7558만6000원 | [N2 모닝 경제 브리핑-10월 13일] 美 증시, 반도체주 급락에 3대 지수 혼...

### 8. SNT에너지 (100840)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.42**
- Adjusted recommendation score: **111.15**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 5.23%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -3.12%
- Next close return data: -3.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.42 points. Stock pattern label is relatively_positive_history.
- Related news examples: SNT에너지, 세계석유총회 참가...사우디 발전시장 공략 | '에너지 확보' 총대 메고…포탄 오가는 사우디 찾은 산업부 공무원들 | [데이터 뉴스룸] 기계 업체 50곳 중 절반 올 상반기 미등기임원 평균 급...

### 9. 다스코 (058730)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.39**
- Adjusted recommendation score: **93.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 1.21%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.29%
- Next close return data: -1.62%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 주가 급락 속 테마주만 활개친다…‘호남 반도체’ 실체 없는 종목 급등... | 10월 12일 주식시장 주요공시 | [전날 애프터마켓] 금호전기 상한가 유지…삼전 낙폭 축소·SK하닉 보합

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **90.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -3.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.41%
- Next close return data: -3.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, 김대식 교수 초청…'AGI 시대' 미래 경쟁력 모색 | [굿모닝! 13일 건설업계 소식] GS건설·IPARK현대산업개발·호반건설·LH... | 의정부 중앙1구역, 수의계약으로 시공자 찾는다

### 2. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **90.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -3.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.41%
- Next close return data: -3.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, 김대식 교수 초청…'AGI 시대' 미래 경쟁력 모색 | [굿모닝! 13일 건설업계 소식] GS건설·IPARK현대산업개발·호반건설·LH... | 의정부 중앙1구역, 수의계약으로 시공자 찾는다

### 3. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **90.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -3.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.41%
- Next close return data: -3.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, 김대식 교수 초청…'AGI 시대' 미래 경쟁력 모색 | [굿모닝! 13일 건설업계 소식] GS건설·IPARK현대산업개발·호반건설·LH... | 의정부 중앙1구역, 수의계약으로 시공자 찾는다

### 4. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **90.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -3.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.41%
- Next close return data: -3.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, 김대식 교수 초청…'AGI 시대' 미래 경쟁력 모색 | [굿모닝! 13일 건설업계 소식] GS건설·IPARK현대산업개발·호반건설·LH... | 의정부 중앙1구역, 수의계약으로 시공자 찾는다

### 5. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **90.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -3.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.41%
- Next close return data: -3.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, 김대식 교수 초청…'AGI 시대' 미래 경쟁력 모색 | [굿모닝! 13일 건설업계 소식] GS건설·IPARK현대산업개발·호반건설·LH... | 의정부 중앙1구역, 수의계약으로 시공자 찾는다

### 6. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **90.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -3.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.41%
- Next close return data: -3.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, 김대식 교수 초청…'AGI 시대' 미래 경쟁력 모색 | [굿모닝! 13일 건설업계 소식] GS건설·IPARK현대산업개발·호반건설·LH... | 의정부 중앙1구역, 수의계약으로 시공자 찾는다

### 7. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **90.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -3.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.41%
- Next close return data: -3.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, 김대식 교수 초청…'AGI 시대' 미래 경쟁력 모색 | [굿모닝! 13일 건설업계 소식] GS건설·IPARK현대산업개발·호반건설·LH... | 의정부 중앙1구역, 수의계약으로 시공자 찾는다

### 8. 코윈로보틱스 (282880)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.62**
- Adjusted recommendation score: **94.11**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -3.62%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.14%
- Next close return data: -6.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.62 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 12일 주식시장 주요공시 | 코윈로보틱스, ‘화웨이·비야디 파트너’와 아·태 지능형 로봇 시장 ... | 2차전지 장비 테마 신바람… 전문가 "수주 잔고 탄탄한 기업에 올라타라...

### 9. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.93**
- Adjusted recommendation score: **99.80**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 20, success rate: 5.00%, avg next close: -1.42%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.08%
- Next close return data: -6.14%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.93 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 12일 주식시장 주요공시 | 유신·금호건설 주가 '불기둥'…건설 섹터는 단기 매물 폭탄에 '털썩' | '모아타운' 구로동 511, 시공자 현설에 2개사 참석

### 10. 플리토 (300080)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.75**
- Adjusted recommendation score: **102.98**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: -1.41%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.76%
- Next close return data: -3.03%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [AI Festa 2026] Part 2. 목적에 맞게 설계된 AI, 특화 솔루션의 현재는? | 10월 12일 주식시장 주요공시 | 플리토, 반도체 기업과 AI 통번역 구축 계약

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
