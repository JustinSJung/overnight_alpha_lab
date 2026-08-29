# Daily Stock Candidate Report - 2026-08-29

Generated at: 2026-08-29 23:19:04

ML dataset: `data/processed/ml_dataset_20260829.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950220 | 네오이뮨텍 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000180 | 성창기업지주 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000210 | DL | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000500 | 가온전선 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000640 | 동아쏘시오홀딩스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000660 | SK하이닉스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000950 | 전방 | 7 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 0009K0 | 에임드바이오 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001040 | CJ | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 451220 | 아이엠티 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 440110 | 파두 | 5 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 247 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 48 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| investment_decision | 92 | 0 | N/A | Not available | 0.00 |
| lawsuit | 91 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 420 | 0 | N/A | Not available | 0.00 |
| merger | 61 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 256 | 0 | N/A | Not available | 0.00 |
| spin_off | 18 | 0 | N/A | Not available | 0.00 |
| supply_contract | 243 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 247 | 0 | 0 | 247 | 0.00 |
| disclosure_violation | 48 | 0 | 0 | 48 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 92 | 0 | 0 | 92 | 0.00 |
| lawsuit | 91 | 0 | 0 | 91 | 0.00 |
| major_shareholder_change | 420 | 0 | 0 | 420 | 0.00 |
| merger | 61 | 0 | 0 | 61 | 0.00 |
| paid_in_capital_increase | 256 | 0 | 0 | 256 | 0.00 |

## Positive Candidates

### 1. 진흥기업 (002780)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **140.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '해링턴플레이스 오룡역', 대치동 전문가 초청 대입 전략 설명회 개최 | 국가물산업클러스터, 지능형자동차부품진흥원와 손잡고 기업지원 강화 | 중기부, '2026년 상반기 적극행정 우수사례' 15건 선정

### 2. 진흥기업 (002780)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **140.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '해링턴플레이스 오룡역', 대치동 전문가 초청 대입 전략 설명회 개최 | 국가물산업클러스터, 지능형자동차부품진흥원와 손잡고 기업지원 강화 | 중기부, '2026년 상반기 적극행정 우수사례' 15건 선정

### 3. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **137.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성... | "도내 상장사 실적 턴어라운드"…상반기 순이익 1887억 흑자 전환 | 배터리 새 먹거리 열린다… ESS·BBU 기대에 2차전지주 '휘파람'

### 4. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **137.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성... | "도내 상장사 실적 턴어라운드"…상반기 순이익 1887억 흑자 전환 | 배터리 새 먹거리 열린다… ESS·BBU 기대에 2차전지주 '휘파람'

### 5. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **137.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성... | "도내 상장사 실적 턴어라운드"…상반기 순이익 1887억 흑자 전환 | 배터리 새 먹거리 열린다… ESS·BBU 기대에 2차전지주 '휘파람'

### 6. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **137.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경영권 매각 에넥스, 인수자 측 자금 모집 난항… 관리종목 지정 가능성... | "도내 상장사 실적 턴어라운드"…상반기 순이익 1887억 흑자 전환 | 배터리 새 먹거리 열린다… ESS·BBU 기대에 2차전지주 '휘파람'

### 7. 자이에스앤디 (317400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **132.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니] | 자이에스앤디, 남양주 진접4지구 공동주택 개발사업 수주 | [오늘의 주요공시] 삼성바이오로직스ㆍ한화엔진ㆍ대우건설 등

### 8. 삼일씨엔에스 (004440)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **132.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 해상풍력 타워 및 하부구조물 글로벌 공급망 확보… 풍력 테마주에 매수... | [이넷뉴스 브랜드평판] 두산에너빌리티, 풍력에너지 상장기업 8월 1위·... | 신재생에너지주 조정 본격화?... 풍력 관련주 대부분 '뚝 뚝'

### 9. 자이에스앤디 (317400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **132.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니] | 자이에스앤디, 남양주 진접4지구 공동주택 개발사업 수주 | [오늘의 주요공시] 삼성바이오로직스ㆍ한화엔진ㆍ대우건설 등

### 10. 자이에스앤디 (317400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **132.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼전닉스 덕분에 18조 번다고?…뒤에서 방긋 웃는 이 종목 [주末머니] | 자이에스앤디, 남양주 진접4지구 공동주택 개발사업 수주 | [오늘의 주요공시] 삼성바이오로직스ㆍ한화엔진ㆍ대우건설 등

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
