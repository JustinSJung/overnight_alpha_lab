# Daily Stock Candidate Report - 2026-06-26

Generated at: 2026-06-26 09:55:47

ML dataset: `data/processed/ml_dataset_20260626.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 001470 | 삼부토건 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 005960 | 동부건설 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 007460 | 에이프로젠 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 012510 | 더존비즈온 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 013700 | 까뮤이앤씨 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 033310 | 엠투엔 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 043260 | 성호전자 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 054930 | 유신 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 059270 | 해성에어로보틱스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 068270 | 셀트리온 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 085660 | 차바이오텍 | 5 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 148250 | 알엔투테크놀로지 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1 | 0 | N/A | Not available | 0.00 |
| investment_decision | 5 | 0 | N/A | Not available | 0.00 |
| lawsuit | 3 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 4 | 0 | N/A | Not available | 0.00 |
| merger | 2 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 5 | 0 | N/A | Not available | 0.00 |
| supply_contract | 14 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1 | 0 | 0 | 1 | 0.00 |
| investment_decision | 5 | 0 | 0 | 5 | 0.00 |
| lawsuit | 3 | 0 | 0 | 3 | 0.00 |
| major_shareholder_change | 4 | 0 | 0 | 4 | 0.00 |
| merger | 2 | 0 | 0 | 2 | 0.00 |
| paid_in_capital_increase | 5 | 0 | 0 | 5 | 0.00 |
| supply_contract | 14 | 0 | 0 | 14 | 0.00 |

## Positive Candidates

### 1. 까뮤이앤씨 (013700)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **117.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [데이터 뉴스룸] 건설業, 1분기 영업성적에 희비 교차…대우건설 웃고 ... | "PF 리스크 없다"...남화토건, 독보적 대금 회수력으로 '저평가 탈출' 시... | 일성건설 주가 파죽지세… 건설주 혼조세 속 투자 기회는 어디?

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 2. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 3. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 4. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 5. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 6. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 7. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 8. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 9. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

### 10. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 솔디펜스, 한화시스템과 17억 1천만 원대 공급계약→국내 항공산업 협력... | 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락

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
