# Daily Stock Candidate Report - 2026-11-06

Generated at: 2026-11-06 03:20:37

ML dataset: `data/processed/ml_dataset_20261106.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 248170 | 샘표식품 | 21 | 21 | 100.00% | 27.77% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 787 | 691 | 45.44% | 5.38% | 4.00 |
| convertible_bond | 1393 | 1060 | 57.83% | 0.39% | 3.00 |
| paid_in_capital_increase | 2673 | 2152 | 57.85% | -0.34% | 3.00 |
| investment_decision | 536 | 421 | 49.88% | -0.00% | 0.00 |
| lawsuit | 548 | 427 | 51.99% | -0.44% | 0.00 |
| disclosure_violation | 209 | 139 | 40.29% | -0.28% | -3.00 |
| bond_with_warrant | 146 | 134 | 40.30% | 0.21% | -3.00 |
| bonus_issue | 105 | 102 | 41.18% | -0.58% | -3.00 |
| spin_off | 150 | 114 | 38.60% | 0.99% | -3.00 |
| major_shareholder_change | 2760 | 2127 | 40.10% | -0.89% | -3.00 |
| earnings_guidance | 63 | 59 | 27.12% | 0.28% | -6.00 |
| supply_contract | 1636 | 1310 | 33.36% | -0.76% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2673 | 1245 | 907 | 521 | 1.31 |
| convertible_bond | 1393 | 613 | 447 | 333 | 1.24 |
| lawsuit | 548 | 222 | 205 | 121 | 0.90 |
| bond_with_warrant | 146 | 54 | 80 | 12 | 0.21 |
| disclosure_violation | 209 | 56 | 83 | 70 | 0.15 |
| investment_decision | 536 | 210 | 211 | 115 | -0.80 |
| supply_contract | 1636 | 437 | 873 | 326 | -1.11 |
| bonus_issue | 105 | 42 | 60 | 3 | -1.16 |
| earnings_guidance | 63 | 16 | 43 | 4 | -1.16 |
| merger | 787 | 314 | 377 | 96 | -1.36 |

## Positive Candidates

### 1. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.29**
- Adjusted recommendation score: **116.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 27, success rate: 66.67%, avg next close: 3.10%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.21%
- Next close return data: -2.62%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.29 points. Stock pattern label is relatively_positive_history.
- Related news examples: IPARK현대산업개발, 동절기 대비 경영진 현장 안전·품질 점검 실시 | 현대건설·IPARK현대산업개발, 기업 이념-역사 담은 초대형 그래픽 공개... | IPARK현대산업개발, 동절기 앞두고 김해서 경영진 현장 점검

### 2. 씨에스윈드 (112610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **84.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.17**
- Adjusted recommendation score: **82.06**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 66.67%, avg next close: 0.06%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -6.84%
- Next close return data: -4.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: [단독]K-GX, 국제사회로⋯정부, ‘에너지 팀코리아’ 가동 | [어제장 오늘장] 블루 쓰나미에 코스피 5% 급락…오늘 반도체주 더 빠지... | [오늘의 증시일정] 삼부토건·코웨이·LIG D&A 등

### 3. 씨에스윈드 (112610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **84.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.17**
- Adjusted recommendation score: **82.06**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 66.67%, avg next close: 0.06%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -6.84%
- Next close return data: -4.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: [단독]K-GX, 국제사회로⋯정부, ‘에너지 팀코리아’ 가동 | [어제장 오늘장] 블루 쓰나미에 코스피 5% 급락…오늘 반도체주 더 빠지... | [오늘의 증시일정] 삼부토건·코웨이·LIG D&A 등

### 4. 신성이엔지 (011930)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **84.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.30**
- Adjusted recommendation score: **79.19**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: -4.70%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -9.46%
- Next close return data: -6.86%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.30 points. Stock pattern label is relatively_positive_history.
- Related news examples: [오늘의 IR] 삼양식품ㆍ롯데쇼핑ㆍGS 등 | 신성이엔지 지붕태양광 계약 종료일 내년 11월 7일로 연장 | [현장] 데이터센터 건립·운영 단계별 최신 솔루션 대거 등장

## Volatile Watchlist

### 1. 에이치엠넥스 (036170)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.36**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-0.50**
- Adjusted recommendation score: **97.14**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: -3.68%, pattern: relatively_positive_history
- Disclosure title: 회사합병결정(종속회사의주요경영사항)              
- Next open return data: -8.05%
- Next close return data: -3.68%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.36 points. Event-type performance added 4.00 points. Stock-specific history subtracted 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [개장 전 주요 공시] 롯데렌탈·삼성바이오로직스·KT&G·LS·넷마블·코... | 11월 6일 개장 전 주요 공시 | 에이치엠넥스 자회사 에스엠아이, 가온누리시스템 흡수합병

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 카카오 (035720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.36**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-8.00**
- Adjusted recommendation score: **59.64**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 48, success rate: 0.00%, avg next close: -1.23%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -5.40%
- Next close return data: -1.23%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.36 points. Event-type performance added 4.00 points. Stock-specific history subtracted 8.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [단독]“일해보고 싶다”던 손님 받아줬더니…경찰 카페 매니저 폭행한... | [인터뷰] 이승목 미래에셋증권 본부장 "MAPS, 거래 앱 넘어 모든 고객의... | 컴퍼니케이파트너스, 스팩 선순환 구축…고유계정 확대일로

### 2. 진흥기업 (002780)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **79.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.50**
- Adjusted recommendation score: **66.39**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 33.33%, avg next close: -0.09%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.35%
- Next close return data: -2.71%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -1. Negative keyword count is 2. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "아이디어는 임업인이, 완성은 전문기관이"···임산물 신제품 2종 탄생 | [52주] 최저가 종목 500개 넘어... 시장 5%대 급락세 | 진흥기업 장위11-2구역 계약 600억8400만원으로 증액

### 3. SK가스 (018670)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.36**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **68.14**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 1.56%, pattern: weak_historical_reaction
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: -3.56%
- Next close return data: 1.56%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.36 points. Event-type performance added 4.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: iM證 "SK가스, LPG하락·LNG강세에 일석이조 수혜…목표가 33만원" | SK가스, SK어드밴스드와 무증자 합병 완료 | [공시] 11월 6일, 코스피 상장사 54개 종목 자사주 매수 신청

### 4. KBI동양철관 (008970)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **78.39**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.63%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -5.46%
- Next close return data: -2.63%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KBI동양철관, 단주 취득 자사주 1만8056주 소각 | KBI동양철관, 자기주식 1만8,056주 소각 결정…주주가치 제고 목적 | [주식마감] '경영권 분쟁 가능성' 한진칼·한진칼우 상한가... 깨끗한나...

### 5. KBI동양철관 (008970)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **78.39**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.63%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -5.46%
- Next close return data: -2.63%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KBI동양철관, 단주 취득 자사주 1만8056주 소각 | KBI동양철관, 자기주식 1만8,056주 소각 결정…주주가치 제고 목적 | [주식마감] '경영권 분쟁 가능성' 한진칼·한진칼우 상한가... 깨끗한나...

### 6. DGI (099520)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **86.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.25**
- Adjusted recommendation score: **80.14**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 1.09%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -6.40%
- Next close return data: -2.62%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 3. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.25 points. Stock pattern label is not_enough_data.
- Related news examples: CCTV·생체인식株 동반 부진…물리보안 업종에 찬바람 | [52주] 최저가 종목 500개 넘어... 시장 5%대 급락세 | DGI 케이블 계약 종료일 2028년 2월로 연장

### 7. 효성 (004800)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.01**
- Adjusted recommendation score: **81.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 45.83%, avg next close: -5.31%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -7.25%
- Next close return data: -6.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.01 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 미국 중간선거가 AI 투자 지형 흔드나…삼성전자·SK하이닉스 폭락, 데이... | [산업계 동향] 기아·HS효성더클래스·트리니티항공 | HS효성더클래스, 천안 서비스센터 ‘벤츠 정비 워크베이’ 20기 확보

### 8. 효성 (004800)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.01**
- Adjusted recommendation score: **81.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 45.83%, avg next close: -5.31%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -7.25%
- Next close return data: -6.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.01 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 미국 중간선거가 AI 투자 지형 흔드나…삼성전자·SK하이닉스 폭락, 데이... | [산업계 동향] 기아·HS효성더클래스·트리니티항공 | HS효성더클래스, 천안 서비스센터 ‘벤츠 정비 워크베이’ 20기 확보

### 9. 효성 (004800)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.01**
- Adjusted recommendation score: **81.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 45.83%, avg next close: -5.31%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -7.25%
- Next close return data: -6.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.01 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 미국 중간선거가 AI 투자 지형 흔드나…삼성전자·SK하이닉스 폭락, 데이... | [산업계 동향] 기아·HS효성더클래스·트리니티항공 | HS효성더클래스, 천안 서비스센터 ‘벤츠 정비 워크베이’ 20기 확보

### 10. 효성 (004800)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.11**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.01**
- Adjusted recommendation score: **81.88**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 45.83%, avg next close: -5.31%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -7.25%
- Next close return data: -6.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.11 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.01 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 미국 중간선거가 AI 투자 지형 흔드나…삼성전자·SK하이닉스 폭락, 데이... | [산업계 동향] 기아·HS효성더클래스·트리니티항공 | HS효성더클래스, 천안 서비스센터 ‘벤츠 정비 워크베이’ 20기 확보

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
