# Daily Stock Candidate Report - 2026-07-23

Generated at: 2026-07-23 23:15:43

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
| 001260 | 남광토건 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001420 | 태원물산 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001470 | 삼부토건 | 13 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001840 | 이화공영 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002020 | 코오롱 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002070 | 비비안 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002210 | 동성제약 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002780 | 진흥기업 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002810 | 삼영무역 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 2 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 85 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 20 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 49 | 0 | N/A | Not available | 0.00 |
| lawsuit | 53 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 99 | 0 | N/A | Not available | 0.00 |
| merger | 37 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 76 | 0 | N/A | Not available | 0.00 |
| spin_off | 2 | 0 | N/A | Not available | 0.00 |
| supply_contract | 96 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 2 | 0 | 0 | 2 | 0.00 |
| convertible_bond | 85 | 0 | 0 | 85 | 0.00 |
| disclosure_violation | 20 | 0 | 0 | 20 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 49 | 0 | 0 | 49 | 0.00 |
| lawsuit | 53 | 0 | 0 | 53 | 0.00 |
| major_shareholder_change | 99 | 0 | 0 | 99 | 0.00 |
| merger | 37 | 0 | 0 | 37 | 0.00 |
| paid_in_capital_increase | 76 | 0 | 0 | 76 | 0.00 |
| spin_off | 2 | 0 | 0 | 2 | 0.00 |

## Positive Candidates

### 1. 대아티아이 (045390)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **130.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 철도주, 정책 기대감에 동반 강세…전력·신호·건설까지 폭풍 매수 | [데이터 뉴스룸] 에너지업체 50곳 중 22곳 임원 연봉 2억 넘어…인천도... | [단독] 철도공단 제천조차장역 불법하도급 의혹 "강원본부 신호공사 추...

### 2. 미래산업 (025560)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **125.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [더벨][thebell interview] "월배당, 노후 현금흐름으로…자금은 코스닥으... | 대구시, 노후산단 규제 전면 개편…제조업에 '네거티브 방식' 도입 | [차세대 오너진단] ⑧'확장'보다 '리밸런싱'…이규호의 코오롱, 미래사...

### 3. HB솔루션 (297890)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **124.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 24일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-7월 24일] 美 증시, AI 수익성 우려·중동 긴장에... | HB솔루션, SDV 장비공급 109억→매출 성장 기대

## Volatile Watchlist

### 1. 남광토건 (001260)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **55.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 24일 개장 전 주요 공시 | “수도권 정비사업 잡아라”…중견사 고군분투 | 부천 '역곡지구 하우스토리' 23일 청약 마감

### 2. 넥스턴앤롤코리아 (089140)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **54.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **54.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 방산부터 반도체·의료까지… 대성하이텍, 초정밀 선반 수주 박차 | 이브이첨단소재, 10대1 무상감자 결정…재무구조·주주가치 제고 목적 | 북미·유럽 인프라 투자 수혜… 공작기계 테마주, 실적 턴어라운드 시동

### 3. 에스트래픽 (234300)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **52.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 철도주, 정책 기대감에 동반 강세…전력·신호·건설까지 폭풍 매수 | 자동차를 넘어 모빌리티로… 현대오토에버, 차세대 소프트웨어 주도권... | 에스트래픽, 과기정통부 주관 ‘우수 기업부설연구소’ 지정

### 4. 에스트래픽 (234300)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **52.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 철도주, 정책 기대감에 동반 강세…전력·신호·건설까지 폭풍 매수 | 자동차를 넘어 모빌리티로… 현대오토에버, 차세대 소프트웨어 주도권... | 에스트래픽, 과기정통부 주관 ‘우수 기업부설연구소’ 지정

### 5. SK텔레콤 (017670)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **50.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 법원, SK텔레콤 5G 과장광고 과징금 취소…168억원 규모 | 이통 3사, AI 안경 '레이밴 메타' 동시 출격…플랫폼·체험존·할인 경쟁 | SKT, '아시아 AI 인프라 허브' 본격 시동…AI DC 사업개발 전문회사 신설

### 6. SK텔레콤 (017670)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **50.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 법원, SK텔레콤 5G 과장광고 과징금 취소…168억원 규모 | 이통 3사, AI 안경 '레이밴 메타' 동시 출격…플랫폼·체험존·할인 경쟁 | SKT, '아시아 AI 인프라 허브' 본격 시동…AI DC 사업개발 전문회사 신설

### 7. SK텔레콤 (017670)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **50.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 법원, SK텔레콤 5G 과장광고 과징금 취소…168억원 규모 | 이통 3사, AI 안경 '레이밴 메타' 동시 출격…플랫폼·체험존·할인 경쟁 | SKT, '아시아 AI 인프라 허브' 본격 시동…AI DC 사업개발 전문회사 신설

### 8. SK텔레콤 (017670)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **50.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 법원, SK텔레콤 5G 과장광고 과징금 취소…168억원 규모 | 이통 3사, AI 안경 '레이밴 메타' 동시 출격…플랫폼·체험존·할인 경쟁 | SKT, '아시아 AI 인프라 허브' 본격 시동…AI DC 사업개발 전문회사 신설

### 9. 금호건설 (002990)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **47.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 24일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-7월 24일] 美 증시, AI 수익성 우려·중동 긴장에... | “수도권 정비사업 잡아라”…중견사 고군분투

### 10. 휴맥스 (115160)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **47.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 휴맥스, 합병 거래 상대가 신세계푸드? 뜬금없는 오기 '갸우뚱' | [카&테크] 휴맥스모빌리티 AI 기반 주차 솔루션 | 오영현 피엔티엠에스 대표 "5년전 기술유출에 적극 대응"…건식분리막 ...

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 휴맥스홀딩스 (028080)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **36.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **36.00**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 휴맥스, 합병 거래 상대가 신세계푸드? 뜬금없는 오기 '갸우뚱' | [오늘의 IR] 에코프로비엠ㆍ한미반도체ㆍ세나테크놀로지 등 | SK디스커버리, 자회사 가치 재평가 속도…주주환원 확대로 시장 신뢰 제...

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
