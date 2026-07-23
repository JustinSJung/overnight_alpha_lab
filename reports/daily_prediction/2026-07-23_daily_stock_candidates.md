# Daily Stock Candidate Report - 2026-07-23

Generated at: 2026-07-23 03:21:09

ML dataset: `data/processed/ml_dataset_20260723.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 000500 | 가온전선 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 0009K0 | 에임드바이오 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001470 | 삼부토건 | 13 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001840 | 이화공영 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002020 | 코오롱 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002070 | 비비안 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002210 | 동성제약 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002780 | 진흥기업 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002810 | 삼영무역 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002880 | 디와이에이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002990 | 금호건설 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 14 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 76 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 20 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 40 | 0 | N/A | Not available | 0.00 |
| lawsuit | 51 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 87 | 0 | N/A | Not available | 0.00 |
| merger | 37 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 83 | 0 | N/A | Not available | 0.00 |
| spin_off | 2 | 0 | N/A | Not available | 0.00 |
| supply_contract | 93 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 14 | 0 | 0 | 14 | 0.00 |
| convertible_bond | 76 | 0 | 0 | 76 | 0.00 |
| disclosure_violation | 20 | 0 | 0 | 20 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 40 | 0 | 0 | 40 | 0.00 |
| lawsuit | 51 | 0 | 0 | 51 | 0.00 |
| major_shareholder_change | 87 | 0 | 0 | 87 | 0.00 |
| merger | 37 | 0 | 0 | 37 | 0.00 |
| paid_in_capital_increase | 83 | 0 | 0 | 83 | 0.00 |
| spin_off | 2 | 0 | 0 | 2 | 0.00 |

## Positive Candidates

### 1. 뉴로메카 (348340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **97.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 휴머노이드 로봇주 급등…피지컬 AI 기대감에 뭉칫돈 유입 뚜렷 | 코스피, 장중 7,166 찍고 6,797로 밀려...상승폭 대부분 반납 | [속보] 레인보우로보틱스 두산로보틱스 휴림로봇 등 주가↑…국내 로봇...

### 2. 뉴로메카 (348340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **97.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 휴머노이드 로봇주 급등…피지컬 AI 기대감에 뭉칫돈 유입 뚜렷 | 코스피, 장중 7,166 찍고 6,797로 밀려...상승폭 대부분 반납 | [속보] 레인보우로보틱스 두산로보틱스 휴림로봇 등 주가↑…국내 로봇...

### 3. 뉴로메카 (348340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **97.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 휴머노이드 로봇주 급등…피지컬 AI 기대감에 뭉칫돈 유입 뚜렷 | 코스피, 장중 7,166 찍고 6,797로 밀려...상승폭 대부분 반납 | [속보] 레인보우로보틱스 두산로보틱스 휴림로봇 등 주가↑…국내 로봇...

### 4. 뉴로메카 (348340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **97.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 휴머노이드 로봇주 급등…피지컬 AI 기대감에 뭉칫돈 유입 뚜렷 | 코스피, 장중 7,166 찍고 6,797로 밀려...상승폭 대부분 반납 | [속보] 레인보우로보틱스 두산로보틱스 휴림로봇 등 주가↑…국내 로봇...

### 5. 티앤엘 (340570)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **77.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **77.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 티앤엘, 100% 무상증자 결정 | 티앤엘, 무상증자 결의→주권매매거래 7월23일 정지 | 코스닥 제약업종 톱50 시총 전년비 27조원↓

### 6. 티앤엘 (340570)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **77.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **77.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 티앤엘, 100% 무상증자 결정 | 티앤엘, 무상증자 결의→주권매매거래 7월23일 정지 | 코스닥 제약업종 톱50 시총 전년비 27조원↓

### 7. 티앤엘 (340570)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **77.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **77.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 티앤엘, 100% 무상증자 결정 | 티앤엘, 무상증자 결의→주권매매거래 7월23일 정지 | 코스닥 제약업종 톱50 시총 전년비 27조원↓

### 8. 티앤엘 (340570)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **77.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **77.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 티앤엘, 100% 무상증자 결정 | 티앤엘, 무상증자 결의→주권매매거래 7월23일 정지 | 코스닥 제약업종 톱50 시총 전년비 27조원↓

### 9. 티앤엘 (340570)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **77.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **77.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 티앤엘, 100% 무상증자 결정 | 티앤엘, 무상증자 결의→주권매매거래 7월23일 정지 | 코스닥 제약업종 톱50 시총 전년비 27조원↓

### 10. 티앤엘 (340570)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **77.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **77.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 티앤엘, 100% 무상증자 결정 | 티앤엘, 무상증자 결의→주권매매거래 7월23일 정지 | 코스닥 제약업종 톱50 시총 전년비 27조원↓

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
