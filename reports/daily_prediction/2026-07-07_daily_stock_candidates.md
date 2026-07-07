# Daily Stock Candidate Report - 2026-07-07

Generated at: 2026-07-07 23:19:51

ML dataset: `data/processed/ml_dataset_20260707.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001470 | 삼부토건 | 13 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002070 | 비비안 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002780 | 진흥기업 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002880 | 디와이에이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003060 | 에이프로젠바이오로직스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003350 | 한국화장품제조 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003490 | 대한항공 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 004440 | 삼일씨엔에스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 004990 | 롯데지주 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 005320 | 온타이드 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 005610 | 삼립 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 18 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 6 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 16 | 0 | N/A | Not available | 0.00 |
| lawsuit | 14 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 45 | 0 | N/A | Not available | 0.00 |
| merger | 8 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 23 | 0 | N/A | Not available | 0.00 |
| spin_off | 1 | 0 | N/A | Not available | 0.00 |
| supply_contract | 61 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 18 | 0 | 0 | 18 | 0.00 |
| disclosure_violation | 6 | 0 | 0 | 6 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 16 | 0 | 0 | 16 | 0.00 |
| lawsuit | 14 | 0 | 0 | 14 | 0.00 |
| major_shareholder_change | 45 | 0 | 0 | 45 | 0.00 |
| merger | 8 | 0 | 0 | 8 | 0.00 |
| paid_in_capital_increase | 23 | 0 | 0 | 23 | 0.00 |
| spin_off | 1 | 0 | 0 | 1 | 0.00 |
| supply_contract | 61 | 0 | 0 | 61 | 0.00 |

## Positive Candidates

### 1. 신성이엔지 (011930)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **152.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **152.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 반도체 호황에 태양광 국책과제까지…이지선 신성이엔지 대표, 지분 매... | 신성이엔지, 대표 등 임원 자사주 매입 러시…"주주가치 제고 의지" | 메가 프로젝트에 12차 전기본 다시 짠다…에너지믹스 재조정 주목

### 2. LG씨엔에스 (064400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **129.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-7월 8일] 美 증시, 반도체주 급락 여파·유가 급등... | [주요공시] 삼성전자, LG에너지솔루션, 씨에스윈드, 다원넥스뷰, 윈하이... | [특징주] LG씨엔에스, LG전자와 1897억원 AI 인프라 계약…AX 확대 기대

### 3. 남화토건 (091590)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **127.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시] 금호건설 '거래 정지', 아이티아이즈 '투자경고', 남화토건 '공매... | 지역 증시 부진 속 ‘호남 반도체 클러스터’ 관련주 폭등 | 광주·전남 상장법인, 시총 줄었지만 건설·산업주 '급등'…왜?(종합)

### 4. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **122.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼성SDS, 동탄 데이터센터 구축 본격화…협력사와 7500억대 계약 | 씨이랩, 3,151억 2천만 원 공급계약→IT서비스사업 확대 | [속보] 씨이랩, 삼성SDS와 3,151억원 규모 AI 컴퓨팅 사업 공급계약 체결...

### 5. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **122.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼성SDS, 동탄 데이터센터 구축 본격화…협력사와 7500억대 계약 | 씨이랩, 3,151억 2천만 원 공급계약→IT서비스사업 확대 | [속보] 씨이랩, 삼성SDS와 3,151억원 규모 AI 컴퓨팅 사업 공급계약 체결...

### 6. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **122.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼성SDS, 동탄 데이터센터 구축 본격화…협력사와 7500억대 계약 | 씨이랩, 3,151억 2천만 원 공급계약→IT서비스사업 확대 | [속보] 씨이랩, 삼성SDS와 3,151억원 규모 AI 컴퓨팅 사업 공급계약 체결...

### 7. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **122.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼성SDS, 동탄 데이터센터 구축 본격화…협력사와 7500억대 계약 | 씨이랩, 3,151억 2천만 원 공급계약→IT서비스사업 확대 | [속보] 씨이랩, 삼성SDS와 3,151억원 규모 AI 컴퓨팅 사업 공급계약 체결...

### 8. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **122.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼성SDS, 동탄 데이터센터 구축 본격화…협력사와 7500억대 계약 | 씨이랩, 3,151억 2천만 원 공급계약→IT서비스사업 확대 | [속보] 씨이랩, 삼성SDS와 3,151억원 규모 AI 컴퓨팅 사업 공급계약 체결...

### 9. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **122.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼성SDS, 동탄 데이터센터 구축 본격화…협력사와 7500억대 계약 | 씨이랩, 3,151억 2천만 원 공급계약→IT서비스사업 확대 | [속보] 씨이랩, 삼성SDS와 3,151억원 규모 AI 컴퓨팅 사업 공급계약 체결...

### 10. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **122.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 삼성SDS, 동탄 데이터센터 구축 본격화…협력사와 7500억대 계약 | 씨이랩, 3,151억 2천만 원 공급계약→IT서비스사업 확대 | [속보] 씨이랩, 삼성SDS와 3,151억원 규모 AI 컴퓨팅 사업 공급계약 체결...

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
