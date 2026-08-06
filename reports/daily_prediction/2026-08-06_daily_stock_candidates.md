# Daily Stock Candidate Report - 2026-08-06

Generated at: 2026-08-06 01:53:42

ML dataset: `data/processed/ml_dataset_20260806.csv`

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
| 396470 | 워트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 389680 | 유디엠텍 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 380540 | 옵티코어 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 378800 | 샤페론 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 375500 | DL이앤씨 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 373200 | 엑스플러스 | 27 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 368970 | 오에스피 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 9 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 128 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 31 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 72 | 0 | N/A | Not available | 0.00 |
| lawsuit | 69 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 184 | 0 | N/A | Not available | 0.00 |
| merger | 37 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 142 | 0 | N/A | Not available | 0.00 |
| spin_off | 8 | 0 | N/A | Not available | 0.00 |
| supply_contract | 125 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 9 | 0 | 0 | 9 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 128 | 0 | 0 | 128 | 0.00 |
| disclosure_violation | 31 | 0 | 0 | 31 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 72 | 0 | 0 | 72 | 0.00 |
| lawsuit | 69 | 0 | 0 | 69 | 0.00 |
| major_shareholder_change | 184 | 0 | 0 | 184 | 0.00 |
| merger | 37 | 0 | 0 | 37 | 0.00 |
| paid_in_capital_increase | 142 | 0 | 0 | 142 | 0.00 |

## Positive Candidates

### 1. 동아지질 (028100)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **145.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 재건축·인프라 기대감 살아났다… 건설 관련주 투자자 관심 집중 | [코스피] IPARK현대산업개발·보령·TBH글로벌 등 45개사, 6일 자사주 매... | 철도 전력 망의 '핵심 심장'… 선도전기, 수배전반·전력 변환 기술력으...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 바이오솔루션 (086820)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-127.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-127.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -8. Negative keyword count is 9. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 코스피 6300선 붕괴...하루 만에 매도 사이드카 | 맷집 사라진 코스피…반도체주 약세에 4% 급락 '매도 사이드카' | 코스피, 5%대 급락에 ‘매도 사이드카’… 6300선 하회

### 2. 한창제지 (009460)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-70.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-70.00**
- Risk level: **HIGH**
- Event type: `lawsuit`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]소송등의제기ㆍ신청(경영권분쟁소송)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is lawsuit. Initial direction is negative. Event score is -75. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피] IPARK현대산업개발·보령·TBH글로벌 등 45개사, 6일 자사주 매... | “받아들여야죠” 상폐 위기 몰린 중기들…시총미달 첫 ‘관리종목’ 나... | [코스피] iM금융·메리츠·KB금융 등 43개사, 5일 자사주 매입

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
