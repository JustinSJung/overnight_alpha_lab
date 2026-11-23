# Daily Stock Candidate Report - 2026-11-23

Generated at: 2026-11-23 03:33:11

ML dataset: `data/processed/ml_dataset_20261123.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 424870 | 이뮨온시아 | 10 | 10 | 100.00% | 16.52% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 248170 | 샘표식품 | 22 | 22 | 95.45% | 26.45% | relatively_positive_history | 8.89 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 895 | 799 | 45.43% | 5.01% | 4.00 |
| convertible_bond | 1692 | 1359 | 59.53% | 0.23% | 3.00 |
| paid_in_capital_increase | 3034 | 2513 | 56.47% | -0.13% | 3.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| investment_decision | 638 | 523 | 52.01% | 0.09% | 0.00 |
| lawsuit | 647 | 526 | 50.76% | -0.43% | 0.00 |
| disclosure_violation | 228 | 158 | 44.30% | -0.93% | -3.00 |
| bond_with_warrant | 162 | 150 | 42.00% | 0.03% | -3.00 |
| spin_off | 158 | 122 | 39.34% | 0.83% | -3.00 |
| major_shareholder_change | 3344 | 2710 | 39.23% | -0.84% | -3.00 |
| supply_contract | 1963 | 1637 | 35.06% | -0.75% | -3.00 |
| earnings_guidance | 96 | 92 | 26.09% | -1.87% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1692 | 809 | 550 | 333 | 1.42 |
| paid_in_capital_increase | 3034 | 1419 | 1094 | 521 | 1.26 |
| lawsuit | 647 | 267 | 259 | 121 | 0.86 |
| disclosure_violation | 228 | 70 | 88 | 70 | 0.38 |
| bond_with_warrant | 162 | 63 | 87 | 12 | 0.33 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 638 | 272 | 251 | 115 | -0.62 |
| supply_contract | 1963 | 574 | 1063 | 326 | -1.06 |
| merger | 895 | 363 | 436 | 96 | -1.38 |
| earnings_guidance | 96 | 24 | 68 | 4 | -1.54 |

## Positive Candidates

### 1. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.78**
- Adjusted recommendation score: **142.72**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 29, success rate: 65.52%, avg next close: 2.91%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.24%
- Next close return data: -4.95%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.78 points. Stock pattern label is relatively_positive_history.
- Related news examples: IPARK현대산업개발, 부산 수안1구역 재개발 사업 수주 | IPARK현대산업개발, 3700억 규모 부산 수안1구역 재개발 시공사 선정 | IPARK현대산업개발, 부산 수안1구역 재개발 수주…도시정비 4.2조 돌파

### 2. 인포바인 (115310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **120.44**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.68%, pattern: relatively_positive_history
- Disclosure title: 유동성공급계약의체결              
- Next open return data: 2.60%
- Next close return data: 0.68%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [개장 전 주요 공시] 카카오·SK하이닉스·HD한국조선해양·삼성바이오에... | [N2 모닝 경제 브리핑-11월 23일] 美 증시, 엔비디아 회계 조사에 AI주 ‘... | PG부터 금융 데이터까지…전자결제 생태계 확장에 관련주 부각

### 3. 에어레인 (163280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **109.56**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -1.39%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.16%
- Next close return data: -5.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 11월 20일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 23일] 美 증시, 엔비디아 회계 조사에 AI주 ‘... | 에어레인, 당진 청정수소 패키지 98억원 공급계약

### 4. 제일테크노스 (038010)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **106.56**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -2.15%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -1.88%
- Next close return data: -4.69%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 11월 20일 주식시장 주요공시 | 제14회 포항철강산업대상 수상자 선정 | 코스피·코스닥 주요 공시(20일)

### 5. HLB펩 (196300)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **109.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-1.75**
- Adjusted recommendation score: **103.19**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -2.46%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.97%
- Next close return data: -4.68%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 1.75 points. Stock pattern label is not_enough_data.
- Related news examples: 선방하는 코스닥… ‘AI 악재’ 피해 로봇·화장품·여행·바이오 향했다... | 미국·유럽으로 뻗는 K-뷰티…한국화장품·에이피알 화색 가득 | 11월 20일 주식시장 주요공시

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-4.41**
- Adjusted recommendation score: **90.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 57, success rate: 36.84%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.61%
- Next close return data: -4.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 4.41 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 마음 돌리려면 조건 바꿔야…건설사 '손절'에 조합 속앓이 | 중도금대출 연기했던 3기 신도시 남양주왕숙, 대출 취급 완료했지만…대... | '남양주 왕숙' 흥행 이어갈까…'왕숙 한신더휴 센텀' 30일 청약 시작

### 2. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-4.41**
- Adjusted recommendation score: **90.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 57, success rate: 36.84%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.61%
- Next close return data: -4.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 4.41 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 마음 돌리려면 조건 바꿔야…건설사 '손절'에 조합 속앓이 | 중도금대출 연기했던 3기 신도시 남양주왕숙, 대출 취급 완료했지만…대... | '남양주 왕숙' 흥행 이어갈까…'왕숙 한신더휴 센텀' 30일 청약 시작

### 3. 아이에스티이 (212710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.70**
- Adjusted recommendation score: **91.24**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 40.00%, avg next close: -3.37%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.46%
- Next close return data: -8.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.70 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 최저가 493개, 최고가 1개...코스피 3%대 하락 | AI 반도체 설비투자 훈풍…한미반도체·원익IPS 등 장비주 '함박웃음' | 11월 20일 주식시장 주요공시

### 4. 인텍플러스 (064290)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **103.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.42**
- Adjusted recommendation score: **93.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 33.33%, avg next close: 0.56%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.79%
- Next close return data: -5.91%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 4. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.42 points. Stock pattern label is weak_historical_reaction.
- Related news examples: AI 기판 성장 기대에도 차익실현…이수페타시스·삼성전기 '휘청' | AI 반도체 설비투자 훈풍…한미반도체·원익IPS 등 장비주 '함박웃음' | 11월 20일 주식시장 주요공시

### 5. HDC (012630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.71**
- Adjusted recommendation score: **95.23**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 38.89%, avg next close: 0.06%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -1.69%
- Next close return data: -4.92%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.71 points. Stock pattern label is weak_historical_reaction.
- Related news examples: DB하이텍, 임직원·가족 40여 명과 벽화 그리기 봉사활동 | '다시 뜨겁게 당진' 기업인 화합 위한 자리 | IPARK현대산업개발, 용산구 취약계층에 겨울나기 물품 기증

### 6. 대신정보통신 (020180)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **97.69**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -3.73%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -1.22%
- Next close return data: -3.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 20일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 23일] 美 증시, 엔비디아 회계 조사에 AI주 ‘... | 대신정보통신, 199억 규모 용역계약 체결

### 7. 아센디오 (012170)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.33**
- Adjusted recommendation score: **98.27**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 66.67%, avg next close: -3.43%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.92%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 5. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.33 points. Stock pattern label is relatively_positive_history.
- Related news examples: 신성델타테크부터 덕성까지…초전도체주 투자심리 위축 무슨일? | 11월 20일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 23일] 美 증시, 엔비디아 회계 조사에 AI주 ‘...

### 8. 서전기전 (189860)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **109.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **98.94**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -4.02%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.43%
- Next close return data: -5.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: LS ELECTRIC은 오르고 일진전기는 내리고…엇갈린 전력주 흐름 | 11월 20일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 23일] 美 증시, 엔비디아 회계 조사에 AI주 ‘...

### 9. 파두 (440110)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-8.27**
- Adjusted recommendation score: **99.67**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 20.00%, avg next close: -4.05%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.95%
- Next close return data: -5.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 8.27 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "AI 데이터센터가 효자" 삼성전기·파두·아이에스시 실적 고공행진 | 차량용 반도체에서 AIDC까지…파두·엑시나 등 K-팹리스 맹활약 | 젠슨 황 스캔들·美 DC 규제…政 “부품·소재 수급 불안 선제 대응”

### 10. 유신 (054930)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.10**
- Adjusted recommendation score: **100.84**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: 0.23%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.64%
- Next close return data: -3.34%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.06 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.10 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 韓 참여 컨소, 95조 베트남 북남 고속철도 첫발…5600억 용역 수주 | 조희대 대법원은 신성불가침인가? | 최민희 "TV조선 재승인심사 사건에 공소청 항소? 언론계 조작기소 규명...

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
