# Daily Stock Candidate Report - 2026-11-02

Generated at: 2026-11-02 02:02:33

ML dataset: `data/processed/ml_dataset_20261102.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 112610 | 씨에스윈드 | 3 | 3 | 100.00% | 3.12% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 248170 | 샘표식품 | 20 | 20 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 737 | 641 | 46.65% | 5.87% | 4.00 |
| convertible_bond | 1342 | 1009 | 57.48% | 0.44% | 3.00 |
| lawsuit | 504 | 383 | 56.14% | -0.48% | 3.00 |
| paid_in_capital_increase | 2533 | 2012 | 57.90% | -0.22% | 3.00 |
| spin_off | 117 | 85 | 51.76% | 1.61% | 2.00 |
| investment_decision | 487 | 372 | 48.39% | 0.08% | 0.00 |
| bond_with_warrant | 145 | 133 | 39.85% | 0.23% | -3.00 |
| bonus_issue | 105 | 102 | 41.18% | -0.58% | -3.00 |
| disclosure_violation | 190 | 120 | 42.50% | -0.26% | -3.00 |
| major_shareholder_change | 2514 | 1881 | 38.38% | -0.72% | -3.00 |
| earnings_guidance | 63 | 59 | 27.12% | 0.28% | -6.00 |
| supply_contract | 1537 | 1211 | 33.61% | -0.65% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2533 | 1165 | 847 | 521 | 1.30 |
| convertible_bond | 1342 | 580 | 429 | 333 | 1.20 |
| lawsuit | 504 | 215 | 168 | 121 | 1.13 |
| disclosure_violation | 190 | 51 | 69 | 70 | 0.25 |
| bond_with_warrant | 145 | 53 | 80 | 12 | 0.17 |
| spin_off | 117 | 44 | 41 | 32 | -0.57 |
| investment_decision | 487 | 180 | 192 | 115 | -0.91 |
| supply_contract | 1537 | 407 | 804 | 326 | -1.07 |
| bonus_issue | 105 | 42 | 60 | 3 | -1.16 |
| earnings_guidance | 63 | 16 | 43 | 4 | -1.16 |

## Positive Candidates

### 1. 동신건설 (025950)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.40**
- Adjusted recommendation score: **126.53**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: -1.14%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.34%
- Next close return data: 2.63%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.40 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 30일 주식시장 주요공시 | [주요공시] 삼성전자, SK하이닉스, 삼성전기, 한화에어로스페이스, 삼성... | 동신건설, 청도 한재지구 하수도 정비 45억 계약

### 2. 씨에스윈드 (112610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **125.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 3.12%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.53%
- Next close return data: 7.95%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시] 씨에스윈드, 영국에 풍력타워 공급···831억원 규모 | [공시] 씨에스윈드, 약 831억원 윈드 타워 공급계약 체결 | 씨에스윈드, 831억 규모 윈드 타워 공급계약

### 3. 성도이엔지 (037350)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **123.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 2.61%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.14%
- Next close return data: 4.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 30일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 2일] 美 증시, AI 투자 우려에 기술주 투매…... | [주요공시] 삼성전자, SK하이닉스, 삼성전기, 한화에어로스페이스, 삼성...

### 4. 워트 (396470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.12**
- Adjusted recommendation score: **122.05**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.21%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.68%
- Next close return data: 2.71%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.12 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 30일 주식시장 주요공시 | 11월 2일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-11월 2일] 美 증시, AI 투자 우려에 기술주 투매…...

### 5. 에이스토리 (241840)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **116.43**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.11%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.36%
- Next close return data: 2.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 30일 주식시장 주요공시 | 시청률 0%→17% '기적'… 일본도 탐낸 한국 드라마, 뮤지컬로 재탄생한... | ‘크래시2’ 곽선영, 긴 머리 싹둑 자르고 돌아왔다…더 날렵해진 민소...

### 6. 한미글로벌 (053690)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.25**
- Adjusted recommendation score: **114.68**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: -0.95%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.87%
- Next close return data: 3.16%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.25 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 30일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 2일] 美 증시, AI 투자 우려에 기술주 투매…... | [주요공시] 삼성전자, SK하이닉스, 삼성전기, 한화에어로스페이스, 삼성...

### 7. 디바이스 (187870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.31**
- Adjusted recommendation score: **113.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: -0.26%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.50%
- Next close return data: 4.02%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 대구광역시, 아태의용생체공학회 개최...400여 명 참석 예정 | 노을, 파나마 국가 검진 체계에 AI 자궁경부암 진단 솔루션 공급 | 라즈베리파이, AI 생태계 확장…“뇌 구조 닮은 뉴로모픽 AI 지원”

### 8. SK디스커버리 (006120)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **111.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 1.37%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.53%
- Next close return data: 5.09%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: SK그룹·HL그룹, 사장단·임원 인사 단행 | [SK 인사 줌인]⑥ SK가스 키운 윤병석, SK디스커버리 미래 설계 | SK, 사장단 인사 단행... 주요 CEO 유임 속 에너지·글로벌 조직 개편

### 9. E8 (418620)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **109.80**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 91, success rate: 94.51%, avg next close: -6.87%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 30일 주식시장 주요공시 | GAC Debuts E8 MPV in Macao With Prices Reaching HKD 369,800 | E8, 삼성전자 디지털트윈 계약 종료일 12월 15일로 연장

### 10. 위드텍 (348350)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.62**
- Adjusted recommendation score: **108.55**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 1.75%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.07%
- Next close return data: 4.04%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.62 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 30일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 2일] 美 증시, AI 투자 우려에 기술주 투매…... | 반도체 성장 기회 맞은 대전…기술기업인 리더십 주목

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. CNT85 (056730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **116.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.73**
- Adjusted recommendation score: **101.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 7.14%, avg next close: -2.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.98%
- Next close return data: -2.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.73 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 신고가 6개, 신저가 177개... 강보합 전환 | 10월 30일 주식시장 주요공시 | CNT85 성서 설비 계약액 46억2600만원으로 증가

### 2. CNT85 (056730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **116.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.73**
- Adjusted recommendation score: **101.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 7.14%, avg next close: -2.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.98%
- Next close return data: -2.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.73 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 신고가 6개, 신저가 177개... 강보합 전환 | 10월 30일 주식시장 주요공시 | CNT85 성서 설비 계약액 46억2600만원으로 증가

### 3. CNT85 (056730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **116.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.73**
- Adjusted recommendation score: **101.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 7.14%, avg next close: -2.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.98%
- Next close return data: -2.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.73 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 신고가 6개, 신저가 177개... 강보합 전환 | 10월 30일 주식시장 주요공시 | CNT85 성서 설비 계약액 46억2600만원으로 증가

### 4. 에이치브이엠 (295310)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.27**
- Adjusted recommendation score: **101.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 90.91%, avg next close: 2.30%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.34%
- Next close return data: 0.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: 오늘의 메모[11월 3일] | 10월 30일 주식시장 주요공시 | 에이치브이엠 슈퍼알로이 계약 종료일 연장

### 5. CNT85 (056730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **116.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.73**
- Adjusted recommendation score: **101.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 7.14%, avg next close: -2.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.98%
- Next close return data: -2.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.73 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 신고가 6개, 신저가 177개... 강보합 전환 | 10월 30일 주식시장 주요공시 | CNT85 성서 설비 계약액 46억2600만원으로 증가

### 6. CNT85 (056730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **116.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.73**
- Adjusted recommendation score: **101.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 7.14%, avg next close: -2.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.98%
- Next close return data: -2.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.73 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 신고가 6개, 신저가 177개... 강보합 전환 | 10월 30일 주식시장 주요공시 | CNT85 성서 설비 계약액 46억2600만원으로 증가

### 7. 다원넥스뷰 (323350)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **106.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **101.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.41%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.81%
- Next close return data: 0.41%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 30일 주식시장 주요공시 | 10월 급등주 전면 교체…상폐 유예·보안주 강세 두드러져 | 다원넥스뷰, 115억원 장비 납품 후 공시유보 지속

### 8. 진흥기업 (002780)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.91**
- Adjusted recommendation score: **102.02**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 37.50%, avg next close: 0.24%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.36%
- Next close return data: 3.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.91 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 30일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 2일] 美 증시, AI 투자 우려에 기술주 투매…... | 중견사, 도시정비 92곳 시공권 확보

### 9. 삼호개발 (010960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.62**
- Adjusted recommendation score: **102.31**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 27.78%, avg next close: -0.25%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -1.18%
- Next close return data: 1.34%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.62 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한화 글로벌부문, 국내 최초 MG 스마트천공기 개발…6개월 현장 실증 완... | 한화, 국내 첫 스마트천공기 개발···6개월 현장 실증 완료 | 한화, 국내 최초 스마트천공기 개발…건설현장 생산성 높인다

### 10. 피엔티엠에스 (257370)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.07**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **102.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.08%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -5.80%
- Next close return data: -1.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.07 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 30일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 2일] 美 증시, AI 투자 우려에 기술주 투매…... | [주요공시] 삼성전자, SK하이닉스, 삼성전기, 한화에어로스페이스, 삼성...

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
