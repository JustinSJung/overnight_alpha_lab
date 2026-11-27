# Daily Stock Candidate Report - 2026-11-27

Generated at: 2026-11-27 05:32:08

ML dataset: `data/processed/ml_dataset_20261127.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 037350 | 성도이엔지 | 3 | 3 | 100.00% | 3.87% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 10 | 10 | 100.00% | 16.52% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 010170 | 대한광통신 | 46 | 46 | 100.00% | 3.06% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 1011 | 915 | 51.26% | 4.76% | 4.00 |
| convertible_bond | 1776 | 1443 | 57.80% | 0.38% | 3.00 |
| paid_in_capital_increase | 3224 | 2703 | 55.94% | -0.20% | 3.00 |
| bonus_issue | 132 | 129 | 52.71% | 0.58% | 0.00 |
| investment_decision | 677 | 562 | 50.36% | 0.19% | 0.00 |
| lawsuit | 698 | 577 | 52.86% | -0.43% | 0.00 |
| disclosure_violation | 233 | 163 | 42.94% | -0.80% | -3.00 |
| bond_with_warrant | 171 | 159 | 39.62% | 0.13% | -3.00 |
| spin_off | 159 | 123 | 39.02% | 0.81% | -3.00 |
| major_shareholder_change | 3493 | 2859 | 40.22% | -0.71% | -3.00 |
| supply_contract | 2067 | 1741 | 36.47% | -0.62% | -3.00 |
| earnings_guidance | 100 | 96 | 29.17% | -1.54% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1776 | 834 | 609 | 333 | 1.32 |
| paid_in_capital_increase | 3224 | 1512 | 1191 | 521 | 1.24 |
| lawsuit | 698 | 305 | 272 | 121 | 1.02 |
| disclosure_violation | 233 | 70 | 93 | 70 | 0.30 |
| bond_with_warrant | 171 | 63 | 96 | 12 | 0.16 |
| bonus_issue | 132 | 68 | 61 | 3 | 0.04 |
| merger | 1011 | 469 | 446 | 96 | -0.77 |
| investment_decision | 677 | 283 | 279 | 115 | -0.79 |
| supply_contract | 2067 | 635 | 1106 | 326 | -0.96 |
| earnings_guidance | 100 | 28 | 68 | 4 | -1.28 |

## Positive Candidates

### 1. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 2. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 3. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 4. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 5. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 6. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 7. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 8. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 9. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

### 10. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **172.00**
- Error-note adjustment score: **-0.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.27**
- Adjusted recommendation score: **167.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 117, success rate: 64.10%, avg next close: -5.05%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.97%
- Next close return data: -8.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 17. Negative keyword count is 1. Historical error notes subtracted 0.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.27 points. Stock pattern label is relatively_positive_history.
- Related news examples: [더벨][i-point] 넥사다이내믹스, 컴퓨팅 AI 서버 755억 추가 수주 | 넥사다이내믹스, 한 달여 만에 AI 서버 755억 후속 수주 | 넥사다이내믹스, AI 서버 755억 추가 수주…하반기 누적 1000억 넘어

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
