# Daily Stock Candidate Report - 2026-09-23

Generated at: 2026-09-23 02:02:33

ML dataset: `data/processed/ml_dataset_20260923.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 003060 | 에이프로젠바이오로직스 | 4 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.31 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |
| 003850 | 보령 | 7 | 7 | 100.00% | 2.22% | relatively_positive_history | 7.50 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 280 | 182 | 60.99% | -0.58% | 3.00 |
| paid_in_capital_increase | 1468 | 1165 | 58.03% | 0.28% | 3.00 |
| convertible_bond | 786 | 513 | 48.93% | 1.08% | 2.00 |
| bonus_issue | 65 | 62 | 46.77% | 0.56% | 0.00 |
| disclosure_violation | 120 | 70 | 52.86% | -0.13% | 0.00 |
| investment_decision | 317 | 216 | 50.46% | 0.29% | 0.00 |
| bond_with_warrant | 71 | 61 | 8.20% | -0.04% | -6.00 |
| spin_off | 71 | 48 | 31.25% | 0.28% | -6.00 |
| merger | 195 | 117 | 21.37% | 0.83% | -6.00 |
| supply_contract | 842 | 580 | 28.79% | -0.74% | -6.00 |
| major_shareholder_change | 1498 | 1015 | 33.30% | -1.06% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1468 | 676 | 489 | 303 | 1.30 |
| lawsuit | 280 | 111 | 71 | 98 | 1.22 |
| disclosure_violation | 120 | 37 | 33 | 50 | 0.72 |
| convertible_bond | 786 | 251 | 262 | 273 | 0.60 |
| investment_decision | 317 | 109 | 107 | 101 | -0.64 |
| bonus_issue | 65 | 29 | 33 | 3 | -0.89 |
| supply_contract | 842 | 167 | 413 | 262 | -1.26 |
| bond_with_warrant | 71 | 5 | 56 | 10 | -2.01 |
| major_shareholder_change | 1498 | 338 | 677 | 483 | -2.04 |

## Positive Candidates

### 1. 포스코퓨처엠 (003670)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **136.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.69%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.05%
- Next close return data: 2.69%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 포스코퓨처엠, SK온에 LFP 양극재 1조1000억원 공급…음극재 넘어 협력 ... | 포스코퓨처엠, SK온에 LFP 양극재 공급…국내 배터리 3사 고객사 확보 | SK온, 포스코퓨처엠과 1.1조 LFP 공급계약…美 ESS 공략

### 2. 보령 (003850)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **110.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 100.00%, avg next close: 2.22%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.09%
- Next close return data: 0.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 태안군, 석탄발전 근로자 자격증 취득 지원 | 박수현 충남지사, 아산 방문… “삼성 113조 투자 지원·첨단 인프라 집... | 민주당 충남도당 첫 상무위…신임 당직자 인선

### 3. 한전산업 (130660)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.03**
- Adjusted recommendation score: **86.71**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: -0.79%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.38%
- Next close return data: -2.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.03 points. Stock pattern label is not_enough_data.
- Related news examples: 고려아연·현대모비스·KT&G·에스원·신세계·CJ ENM·한섬, 106분기 연속... | KB證 "대미투자 2호 '대형 원전' 전망…두산에너빌·한전기술 주목" | [이슈] 최고가격제에 추석 100원 할인까지…'기름값 방어' 장기전

### 4. 시공테크 (020710)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **84.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **80.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.08%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.27%
- Next close return data: 1.08%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 22일 주식시장 주요공시 | [핀포인트] [아이스크림에듀] 분할상장 잔혹사, 90% 폭락한 주가에 개미... | 인테리어 상장기업 브랜드평판 9월 빅데이터 분석결과…1위 KCC·2위 한샘...

## Volatile Watchlist

### 1. 케이앤에스아이앤씨 (487400)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-0.64**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **79.86**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 4.85%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              ([국책과제 선정]저궤도 상용위성통신 기반 잠수함 위성통신체계 개발 및 구축)
- Next open return data: 2.08%
- Next close return data: 4.85%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 0.64 points. Event-type performance did not change the score. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 꿀잠 매트리스·깨끗한 물 잡았다… 와이즈플래닛컴퍼니, 소매 시장서 ... | 케이앤에스아이앤씨, 73억 ‘잠수함 저궤도 위성통신’ 국책과제 협약…... | 케이앤에스아이앤씨, 73억원 규모 잠수함 위성통신 국책과제 수주

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 자이에스앤디 (317400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-0.64**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-6.90**
- Adjusted recommendation score: **72.46**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 19, success rate: 5.26%, avg next close: -1.17%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: -0.20%
- Next close return data: -3.88%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.64 points. Event-type performance did not change the score. Stock-specific history subtracted 6.90 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 포항 '더 퍼스트 48' 48층 랜드마크로…사업계획 승인 완료 부지에 조합... | 포항 '더 퍼스트 48' 주택홍보관 개관…조합원 365가구 모집 | 9월 22일 주식시장 주요공시

### 2. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **89.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.92**
- Adjusted recommendation score: **73.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: -2.02%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.30%
- Next close return data: -1.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.92 points. Stock pattern label is weak_historical_reaction.
- Related news examples: DK아시아, 9월 시행사 브랜드평판 1위 수성...BS산업 2위 도약도 | '3040 매수 비중 55.5%'···오남역 서희스타힐스 여의재 1단지 선착순... | 9월 22일 주식시장 주요공시

### 3. 진흥기업 (002780)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **91.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.72**
- Adjusted recommendation score: **78.02**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 16.67%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.17%
- Next close return data: -0.73%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 3. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.72 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 22일 주식시장 주요공시 | [Who Is ?] 허상희 동부건설 부회장 | 넷플릭스 첫 지자체 협약 이끈 제주콘텐츠진흥원… 행안부 장관 표창

### 4. 에코심플렉스 (038870)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.67**
- Adjusted recommendation score: **82.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: 0.57%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.92%
- Next close return data: -1.38%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 5. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.67 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 22일 주식시장 주요공시 | 9월 18일 주식시장 주요공시 | 9월 14일 주식시장 주요공시

### 5. 삼일씨엔에스 (004440)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.40**
- Adjusted recommendation score: **85.34**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: -0.34%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.39%
- Next close return data: -0.19%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 4. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.40 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 22일 주식시장 주요공시 | 해상풍력·전력망 투자 확대 기대…풍력 기자재株 상승세 | [이넷뉴스 브랜드평판] 두산에너빌리티, 풍력에너지 상장기업 9월 1위·...

### 6. 엘에스일렉트릭 (010120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-0.89**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **85.36**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.18%, pattern: weak_historical_reaction
- Disclosure title: 유무상증자결정(종속회사의주요경영사항)              
- Next open return data: 1.66%
- Next close return data: -1.18%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 0.89 points. Event-type performance did not change the score. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [이슈] LS그룹, 글로벌 제조 역량에 'AI' 접목 본격화 한다 | 국내 500대 기업 생산기지 23.8% 충청권 소재 | 국내 500대 기업 생산기지 57.8% 영남·충청권 몰려…호남·서울·강원·...

### 7. 선도전기 (007610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **87.24**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -0.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.22%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 22일 주식시장 주요공시 | 미국 전력 인프라 싹쓸이… 대한전선, 초고압 케이블 수주 잔고 대폭 늘... | 네오사피엔스 회전율 355%…상장주식 수의 3.6배

### 8. 선도전기 (007610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **87.24**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -0.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.22%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 22일 주식시장 주요공시 | 미국 전력 인프라 싹쓸이… 대한전선, 초고압 케이블 수주 잔고 대폭 늘... | 네오사피엔스 회전율 355%…상장주식 수의 3.6배

### 9. HD현대중공업 (329180)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **92.24**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.98%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.55%
- Next close return data: -1.98%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 코스피, 반도체 강세에 장 초반 1%대 상승(종합) | [개장시황] 코스피, 美 AI주 랠리에 1%대 상승 출발…반도체 위주 오름세 | 전직원 스톡옵션, 글로벌 선박 AS 개척…HD현대마린솔루션 3배 키운 KKR

### 10. 강원에너지 (114190)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.26**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.07**
- Adjusted recommendation score: **93.81**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.20%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.94%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.26 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.07 points. Stock pattern label is relatively_positive_history.
- Related news examples: 대신증권, 반도체·로봇·우주 중소형주 기업설명회 진행…"신사업·성... | 9월 22일 주식시장 주요공시 | 세미티에스·AP위성 등 8곳, 대신증권 콥데이 참가

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
