# Daily Stock Candidate Report - 2026-08-27

Generated at: 2026-08-27 03:24:09

ML dataset: `data/processed/ml_dataset_20260827.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950220 | 네오이뮨텍 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000210 | DL | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000500 | 가온전선 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000660 | SK하이닉스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000950 | 전방 | 7 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 0009K0 | 에임드바이오 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 431190 | 케이쓰리아이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 419540 | 비스토스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 418620 | E8 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 407400 | 꿈비 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 403490 | 우듬지팜 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 212 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 44 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| investment_decision | 88 | 0 | N/A | Not available | 0.00 |
| lawsuit | 87 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 314 | 0 | N/A | Not available | 0.00 |
| merger | 51 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 192 | 0 | N/A | Not available | 0.00 |
| spin_off | 12 | 0 | N/A | Not available | 0.00 |
| supply_contract | 180 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 212 | 0 | 0 | 212 | 0.00 |
| disclosure_violation | 44 | 0 | 0 | 44 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 88 | 0 | 0 | 88 | 0.00 |
| lawsuit | 87 | 0 | 0 | 87 | 0.00 |
| major_shareholder_change | 314 | 0 | 0 | 314 | 0.00 |
| merger | 51 | 0 | 0 | 51 | 0.00 |
| paid_in_capital_increase | 192 | 0 | 0 | 192 | 0.00 |

## Positive Candidates

### 1. 피델릭스 (032580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **139.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: HBM과 후공정 장비주 동반 강세… 반도체 업종 전반 강한 반등 장세 주도 | 중국 소비심리 개선 조짐… 오가닉티코스메틱, 현지 사업 모멘텀 재가동 | "확신의 매수 구간"…비중확대 추천한 반도체 종목은

### 2. 이노메트리 (302430)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **135.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 IR] 제일기획ㆍ아이티센글로벌ㆍ피엔티 등 | 원전·반도체장비·가상자산·바이오 테마 강세 | [EBN 데이터센터] 25일 상승 종목 30選…6개 종목 상한가

### 3. 우진아이엔에스 (010400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **114.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 8월 21일 주식시장 주요공시 | 8월 14일 주식시장 주요공시 | 8월 18일 개장 전 주요 공시

## Volatile Watchlist

### 1. 미원에스씨 (268280)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [데이터 뉴스룸] 석화업체 50곳 중 80% 넘게 상반기 매출 성적에 방긋…... | [공시] 27일, 코스피 상장사 55개 종목 자사주 매수 신청 | [공시] 26일, 코스피 상장사 55개 종목 자사주 매수 신청

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
