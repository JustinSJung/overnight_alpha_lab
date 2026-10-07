# Daily Stock Candidate Report - 2026-10-07

Generated at: 2026-10-07 02:54:10

ML dataset: `data/processed/ml_dataset_20261007.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 010950 | S-Oil | 9 | 9 | 88.89% | 5.68% | relatively_positive_history | 8.72 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 365 | 248 | 56.85% | -0.56% | 3.00 |
| paid_in_capital_increase | 1747 | 1342 | 58.72% | 0.23% | 3.00 |
| bonus_issue | 81 | 78 | 52.56% | 0.56% | 0.00 |
| convertible_bond | 901 | 603 | 53.73% | 0.70% | 0.00 |
| disclosure_violation | 129 | 74 | 51.35% | -0.13% | 0.00 |
| investment_decision | 359 | 246 | 51.22% | 0.26% | 0.00 |
| bond_with_warrant | 76 | 65 | 9.23% | 0.07% | -6.00 |
| major_shareholder_change | 1727 | 1162 | 34.34% | -0.68% | -6.00 |
| merger | 354 | 263 | 19.77% | 0.59% | -6.00 |
| spin_off | 84 | 54 | 31.48% | 0.62% | -6.00 |
| supply_contract | 1007 | 707 | 29.00% | -0.69% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1747 | 788 | 554 | 405 | 1.30 |
| lawsuit | 365 | 141 | 107 | 117 | 1.05 |
| convertible_bond | 901 | 324 | 279 | 298 | 0.87 |
| disclosure_violation | 129 | 38 | 36 | 55 | 0.64 |
| bonus_issue | 81 | 41 | 37 | 3 | -0.22 |
| investment_decision | 359 | 126 | 120 | 113 | -0.58 |
| supply_contract | 1007 | 205 | 502 | 300 | -1.22 |
| bond_with_warrant | 76 | 6 | 59 | 11 | -1.93 |
| major_shareholder_change | 1727 | 399 | 763 | 565 | -1.94 |

## Positive Candidates

### 1. 테라뷰 (950250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.12**
- Adjusted recommendation score: **137.90**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 12.86%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.51%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.12 points. Stock pattern label is not_enough_data.
- Related news examples: 테라뷰, 포춘 500 '하이퍼스케일러' 신규 고객사 확보 | HBM·첨단 패키징 투자 확대 기대…반도체 장비주 상승 행렬 | 10월 7일 개장 전 주요 공시

### 2. 유비온 (084440)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **127.28**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 5.80%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.21%
- Next close return data: 5.80%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [코스피·코스닥, 삼성전기 IPARK현대산업개발 한미반도체 넥스틴 알테... | [N2 모닝 경제 브리핑-10월 7일] 美 증시, 국채금리 꺾이자 기술주 반등... | 기업 공시 [10월 6일]

### 3. 유비온 (084440)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **127.28**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 5.80%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.21%
- Next close return data: 5.80%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [코스피·코스닥, 삼성전기 IPARK현대산업개발 한미반도체 넥스틴 알테... | [N2 모닝 경제 브리핑-10월 7일] 美 증시, 국채금리 꺾이자 기술주 반등... | 기업 공시 [10월 6일]

### 4. 포스코퓨처엠 (003670)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **123.40**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -2.05%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.87%
- Next close return data: -6.79%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 포스코퓨처엠, 삼성SDI 소재 밸류체인 구축 | 포스코퓨처엠 주가, 10월 7일 장중 193,600원 5.33% 하락 | 포스코퓨처엠, 삼성SDI에 6조원 LFP 양극재 공급…배터리 소재 확대

### 5. 엠아이큐브솔루션 (373170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.65**
- Adjusted recommendation score: **113.43**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 80.00%, avg next close: 23.51%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.84%
- Next close return data: -1.87%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.65 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 모닝 경제 브리핑-10월 7일] 美 증시, 국채금리 꺾이자 기술주 반등... | 5G부터 AI·핀테크까지… IT서비스 업종에 매수세 몰렸다 | 유튜브 타고 K-커머스 영토 넓힌다… 카페24, 글로벌 실적 고공행진 예...

### 6. 엠아이큐브솔루션 (373170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.65**
- Adjusted recommendation score: **113.43**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 80.00%, avg next close: 23.51%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.84%
- Next close return data: -1.87%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.65 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 모닝 경제 브리핑-10월 7일] 美 증시, 국채금리 꺾이자 기술주 반등... | 5G부터 AI·핀테크까지… IT서비스 업종에 매수세 몰렸다 | 유튜브 타고 K-커머스 영토 넓힌다… 카페24, 글로벌 실적 고공행진 예...

### 7. 엠아이큐브솔루션 (373170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.65**
- Adjusted recommendation score: **113.43**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 80.00%, avg next close: 23.51%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.84%
- Next close return data: -1.87%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.65 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 모닝 경제 브리핑-10월 7일] 美 증시, 국채금리 꺾이자 기술주 반등... | 5G부터 AI·핀테크까지… IT서비스 업종에 매수세 몰렸다 | 유튜브 타고 K-커머스 영토 넓힌다… 카페24, 글로벌 실적 고공행진 예...

### 8. 엠아이큐브솔루션 (373170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.65**
- Adjusted recommendation score: **113.43**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 80.00%, avg next close: 23.51%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.84%
- Next close return data: -1.87%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.65 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 모닝 경제 브리핑-10월 7일] 美 증시, 국채금리 꺾이자 기술주 반등... | 5G부터 AI·핀테크까지… IT서비스 업종에 매수세 몰렸다 | 유튜브 타고 K-커머스 영토 넓힌다… 카페24, 글로벌 실적 고공행진 예...

### 9. 아이티아이즈 (372800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **107.28**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.86%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.34%
- Next close return data: 0.86%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 5G부터 AI·핀테크까지… IT서비스 업종에 매수세 몰렸다 | 우리기술투자 주가 8%↑…토큰증권 제도화에 STO 관련주 '흥얼흥얼' | 유튜브 타고 K-커머스 영토 넓힌다… 카페24, 글로벌 실적 고공행진 예...

### 10. 한미반도체 (042700)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **101.40**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -1.13%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -1.97%
- Next close return data: -2.87%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 한미반도체 곽동신, 자사주 누적 702억 취득 완료…"성장 자신감" | ‘AI 자신감’ 곽동신 한미반도체 회장, 올해만 167억원 사재 매입 | 곽동신 한미반도체 회장, 올해 자사주 167억 매입…누적 702억·지분 33.6...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. IPARK현대산업개발 (294870)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.58**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-2.62**
- Adjusted recommendation score: **91.80**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 13, success rate: 38.46%, avg next close: 0.17%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.00%
- Next close return data: 2.53%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 0.58 points. Event-type performance did not change the score. Stock-specific history subtracted 2.62 points. Stock pattern label is weak_historical_reaction.
- Related news examples: IPARK현대산업개발, 2812억 규모 부산 연산13구역 재개발 수주 | 신설역 들어서니 집값도 '쑥'…철도 따라 달라진 주거 선호 | 삼성전기, AI 타고 ‘퀀텀점프’…글로벌 시장 점유율 40% 독주

### 2. 케이아이이 (009140)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-0.22**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **94.28**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.30%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.42%
- Next close return data: -2.30%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 0.22 points. Event-type performance did not change the score. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [전날 애프터마켓] 모비릭스·아톤 상한가…삼전·SK하닉 반등 | [코스피·코스닥, 삼성전기 IPARK현대산업개발 한미반도체 넥스틴 알테... | [아주증시포커스] 업계 반발에…법원 제동에…꼬이는 '부실기업 신속퇴...

### 3. 케이아이이 (009140)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-0.22**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **94.28**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.30%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.42%
- Next close return data: -2.30%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 0.22 points. Event-type performance did not change the score. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [전날 애프터마켓] 모비릭스·아톤 상한가…삼전·SK하닉 반등 | [코스피·코스닥, 삼성전기 IPARK현대산업개발 한미반도체 넥스틴 알테... | [아주증시포커스] 업계 반발에…법원 제동에…꼬이는 '부실기업 신속퇴...

### 4. 두산에너빌리티 (034020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **95.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -2.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.33%
- Next close return data: -0.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 두산로보틱스, 피지컬 AI 국책과제 2건 수주… 차세대 협동로봇·지능형... | 메가프로젝트에 LNG 숨통 트이나… 핵심 설비 가스터빈 기회이자 도전 | AGI 시대 준비하는 삼성SDI…"ESS가 새로운 성장 기회 창출"

### 5. 아스타 (246720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **100.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 동해시, 10월 연휴 산·바다·전통 아우르는 가을 행사 풍성 | 이번 연휴 어디 가지? 동해에서 즐기는 특별한 가을 연휴 | 10월 7일 개장 전 주요 공시

### 6. 유니온바이오메트릭스 (203450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **117.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -3.91%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.17%
- Next close return data: -3.91%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 유니온바이오메트릭스, 육군 과학화출입통제 사업 171억 원 수주 | 유니온바이오메트릭스, 171억원 육군 사업 수주…창사 이래 최대 규모 | 유니온바이오메트릭스, 172억 규모 육군 보안망 구축 수주…창사 이래 ...

### 7. 산일전기 (062040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **117.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 5.10%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: '큰손' 빅테크가 직접 주문…"전력기기 내년에도 고성장" | 검색 상위 20개 종목 상승·하락 10대 10… 삼성전자 오르고 SK하이닉스... | 하나증권 "AI 데이터센터 전력 확보 경쟁 재부각, 두산에너빌리티 한전...

### 8. 레이저쎌 (412350)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **120.78**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -4.06%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.72%
- Next close return data: -4.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: HBM·첨단 패키징 투자 확대 기대…반도체 장비주 상승 행렬 | [더벨][i-point] 레이저쎌, '글로벌 톱' 메모리 프로브카드 기업에 LPB 공... | 10월 7일 개장 전 주요 공시

### 9. 우원개발 (046940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **128.78**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -0.95%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.18%
- Next close return data: -1.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [데이터 뉴스룸] 건설 업체 50곳 올 상반기 미등기임원 평균 보수 1억 수... | 9월 30일 주식시장 주요공시 | [더벨][지배구조 분석 | 우원개발] 오너 2세 김정민 부회장, 대표이사 등...

### 10. 우원개발 (046940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.22**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **128.78**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -0.95%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.18%
- Next close return data: -1.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.22 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [데이터 뉴스룸] 건설 업체 50곳 올 상반기 미등기임원 평균 보수 1억 수... | 9월 30일 주식시장 주요공시 | [더벨][지배구조 분석 | 우원개발] 오너 2세 김정민 부회장, 대표이사 등...

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
