# Daily Stock Candidate Report - 2026-07-03

Generated at: 2026-07-03 01:42:27

ML dataset: `data/processed/ml_dataset_20260703.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001470 | 삼부토건 | 5 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002070 | 비비안 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002880 | 디와이에이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003060 | 에이프로젠바이오로직스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003350 | 한국화장품제조 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 004440 | 삼일씨엔에스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 005320 | 온타이드 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 005610 | 삼립 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 005960 | 동부건설 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 006040 | 동원산업 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 006360 | GS건설 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 12 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 6 | 0 | N/A | Not available | 0.00 |
| investment_decision | 15 | 0 | N/A | Not available | 0.00 |
| lawsuit | 9 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 22 | 0 | N/A | Not available | 0.00 |
| merger | 6 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 18 | 0 | N/A | Not available | 0.00 |
| spin_off | 1 | 0 | N/A | Not available | 0.00 |
| supply_contract | 38 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 12 | 0 | 0 | 12 | 0.00 |
| disclosure_violation | 6 | 0 | 0 | 6 | 0.00 |
| investment_decision | 15 | 0 | 0 | 15 | 0.00 |
| lawsuit | 9 | 0 | 0 | 9 | 0.00 |
| major_shareholder_change | 22 | 0 | 0 | 22 | 0.00 |
| merger | 6 | 0 | 0 | 6 | 0.00 |
| paid_in_capital_increase | 18 | 0 | 0 | 18 | 0.00 |
| spin_off | 1 | 0 | 0 | 1 | 0.00 |
| supply_contract | 38 | 0 | 0 | 38 | 0.00 |

## Positive Candidates

No candidates in this section.

## Volatile Watchlist

### 1. JW홀딩스 (096760)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **45.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **45.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제약바이오업계, ESG 공시 강화…그룹 통합 관리·글로벌 기준 적용 | 한미약품·대웅제약·동아제약…제약업계, R&D 성과·해외 진출 확대 | [주요공시] 동부건설, SK디앤디, 두산퓨얼셀, 선진뷰티사이언스, 디알텍...

### 2. JW홀딩스 (096760)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **45.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **45.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제약바이오업계, ESG 공시 강화…그룹 통합 관리·글로벌 기준 적용 | 한미약품·대웅제약·동아제약…제약업계, R&D 성과·해외 진출 확대 | [주요공시] 동부건설, SK디앤디, 두산퓨얼셀, 선진뷰티사이언스, 디알텍...

### 3. 티비에이치글로벌 (084870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **27.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **27.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시] 티비에이치글로벌, 12억 규모 자사주 58만주 취득 | 티비에이치글로벌, KB증권과 신탁계약 통해 자사주 58만주 취득 | 티비에이치글로벌, 주식소각 실시→유통주식 수 감소

### 4. 티비에이치글로벌 (084870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **27.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **27.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시] 티비에이치글로벌, 12억 규모 자사주 58만주 취득 | 티비에이치글로벌, KB증권과 신탁계약 통해 자사주 58만주 취득 | 티비에이치글로벌, 주식소각 실시→유통주식 수 감소

### 5. 티비에이치글로벌 (084870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **27.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **27.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시] 티비에이치글로벌, 12억 규모 자사주 58만주 취득 | 티비에이치글로벌, KB증권과 신탁계약 통해 자사주 58만주 취득 | 티비에이치글로벌, 주식소각 실시→유통주식 수 감소

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
