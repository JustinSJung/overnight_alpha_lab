# Daily Stock Candidate Report - 2026-08-11

Generated at: 2026-08-11 05:33:42

ML dataset: `data/processed/ml_dataset_20260811.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950220 | 네오이뮨텍 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000500 | 가온전선 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000660 | SK하이닉스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000950 | 전방 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 0009K0 | 에임드바이오 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 407400 | 꿈비 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 403490 | 우듬지팜 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 397030 | 에이프릴바이오 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 396470 | 워트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 389680 | 유디엠텍 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 383800 | LX홀딩스 | 16 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 9 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 133 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 32 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 77 | 0 | N/A | Not available | 0.00 |
| lawsuit | 73 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 238 | 0 | N/A | Not available | 0.00 |
| merger | 46 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 146 | 0 | N/A | Not available | 0.00 |
| spin_off | 8 | 0 | N/A | Not available | 0.00 |
| supply_contract | 143 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 9 | 0 | 0 | 9 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 133 | 0 | 0 | 133 | 0.00 |
| disclosure_violation | 32 | 0 | 0 | 32 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 77 | 0 | 0 | 77 | 0.00 |
| lawsuit | 73 | 0 | 0 | 73 | 0.00 |
| major_shareholder_change | 238 | 0 | 0 | 238 | 0.00 |
| merger | 46 | 0 | 0 | 46 | 0.00 |
| paid_in_capital_increase | 146 | 0 | 0 | 146 | 0.00 |

## Positive Candidates

### 1. 기가비스 (420770)

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
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [애널픽] 메모리 슈퍼사이클 낙수효과..."반도체 중소형주 타이밍 왔다... | 인텔·엔비디아 채택 기대감… 유리 기판 테마, 장비·소재주 동반 우상... | 웨이퍼 단에서 패키징까지… 반도체 장비·부품주 주가 파죽지세

### 2. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 3. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 4. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 5. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 6. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 7. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 8. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 9. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

### 10. 제이엔케이글로벌 (126880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **112.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제이엔케이글로벌, Dangote Petroleum Refinery and Petrochemicals와 Fired ... | [속보] 제이엔케이글로벌, 1713억원 규모 Fired Heaters 공급계약…지난... | 미·이란 충돌 격화에 치솟는 유가…정유株 강세

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

No candidates in this section.

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
