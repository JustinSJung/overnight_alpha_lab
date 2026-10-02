# Daily Stock Candidate Report - 2026-10-02

Generated at: 2026-10-02 03:11:24

ML dataset: `data/processed/ml_dataset_20261002.csv`

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
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 3 | 3 | 100.00% | 9.98% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 010950 | S-Oil | 9 | 9 | 88.89% | 5.68% | relatively_positive_history | 8.72 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 344 | 231 | 58.87% | -0.61% | 3.00 |
| paid_in_capital_increase | 1670 | 1299 | 57.81% | 0.33% | 3.00 |
| bonus_issue | 79 | 76 | 53.95% | 0.64% | 0.00 |
| convertible_bond | 877 | 589 | 53.48% | 0.69% | 0.00 |
| disclosure_violation | 129 | 74 | 51.35% | -0.13% | 0.00 |
| investment_decision | 346 | 240 | 51.25% | 0.26% | 0.00 |
| merger | 266 | 186 | 26.88% | 1.34% | -4.00 |
| bond_with_warrant | 74 | 63 | 9.52% | 0.01% | -6.00 |
| major_shareholder_change | 1659 | 1120 | 34.11% | -0.86% | -6.00 |
| spin_off | 77 | 53 | 30.19% | 0.50% | -6.00 |
| supply_contract | 952 | 674 | 29.82% | -0.65% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1670 | 751 | 548 | 371 | 1.26 |
| lawsuit | 344 | 136 | 95 | 113 | 1.15 |
| convertible_bond | 877 | 315 | 274 | 288 | 0.86 |
| disclosure_violation | 129 | 38 | 36 | 55 | 0.64 |
| bonus_issue | 79 | 41 | 35 | 3 | -0.05 |
| investment_decision | 346 | 123 | 117 | 106 | -0.59 |
| supply_contract | 952 | 201 | 473 | 278 | -1.19 |
| bond_with_warrant | 74 | 6 | 57 | 11 | -1.91 |
| major_shareholder_change | 1659 | 382 | 738 | 539 | -1.96 |

## Positive Candidates

### 1. 디아이 (003160)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **131.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.88%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -3.06%
- Next close return data: 1.88%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 증시 풍향계] 반도체 소부장株 신고가 행진…머큐리 ‘상한가’, 이... | [52주] 신고가 8개, 신저가 6개... 장 초반 상승세 | 펨트론·엔투텍 급등 주도…고성능 검사·공정 장비주 매수세 유입 뚜렷

### 2. LG에너지솔루션 (373220)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **130.31**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.97%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.14%
- Next close return data: 0.97%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 코스피, 동반 매도에 6,960선 등락…반도체 투톱 '희비' | 코스피, 美고용지표 경계감···6970선 강보합 | K-배터리 3사 모두 뚫은 포스코퓨처엠…'자원 공급자' 날개 달았다

### 3. 씨케이솔루션 (480370)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **128.43**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: -2.35%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.06%
- Next close return data: -1.17%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 2차전지 장비업계, 수주 모멘텀 속 체질 개선 집중… 투자 전략은? | 10월 1일 주식시장 주요공시 | [전일 주요공시] LS일렉트릭ㆍ두산에너빌리티ㆍ아이에스동서 등

### 4. 스카이랩스 (386380)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **125.31**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.87%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.87%
- Next close return data: 0.87%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 스카이랩스, 대웅제약에 ‘카트 오투’ 49억 규모 공급 | 10월 1일 주식시장 주요공시 | 스카이랩스, 반지형 산소포화도 측정기 '카트 오투' 대웅제약에 49억 규...

### 5. 세미파이브 (490470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.31**
- Adjusted recommendation score: **123.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.52%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.49%
- Next close return data: 1.23%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 1일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 2일] 美 증시, 치솟던 금리 꺾이자 반등…3대... | 세미파이브, 모빌린트와 K-온디바이스 AI 로봇 반도체 상용화 나서

### 6. LS (006260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.05**
- Adjusted recommendation score: **122.86**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.92%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.34%
- Next close return data: -1.17%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.05 points. Stock pattern label is not_enough_data.
- Related news examples: iM증권, 일상툰 임햄찌 연재..'고인물' LS증권 인스타에 도전장 | K-배터리 3사 모두 뚫은 포스코퓨처엠…'자원 공급자' 날개 달았다 | 직스테크놀로지·한신공영·정도, AI 기반 ‘데이터센터 스마트 건설’...

### 7. 팬오션 (028670)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **120.31**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 2.59%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 1.19%
- Next close return data: 3.92%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 1일 주식시장 주요공시 | [코스피·코스닥,두산에너빌리티 현대차 팬오션 기아 아이에스동서 LG C... | 10월 2일 개장 전 주요 공시

### 8. 뉴로메카 (348340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.00**
- Adjusted recommendation score: **112.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 5.76%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.48%
- Next close return data: 5.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 뉴로메카, KAIST와 손목 카메라 없는 휴머노이드 정밀조작 AI 기술 개발 | 뉴로메카, 카이스트와 '단일 카메라 기반 정밀 작업 로봇 AI' 개발 | AI중심대학 18곳·AX대학원 15곳 선정

### 9. 엘에스일렉트릭 (010120)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.12**
- Adjusted recommendation score: **87.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.10%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.21%
- Next close return data: 0.97%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 1일 주식시장 주요공시 | [데이터 뉴스룸] 에너지업체 50곳 영업益 성적 3%대 후퇴…영업곳간, 가... | [이슈] LS그룹, 글로벌 제조 역량에 'AI' 접목 본격화 한다

## Volatile Watchlist

### 1. 오이솔루션 (138080)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **96.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 3.56%, pattern: relatively_positive_history
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: 3.34%
- Next close return data: 8.36%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 16. Historical error notes subtracted 1.96 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 증시 풍향계] 반도체 소부장株 신고가 행진…머큐리 ‘상한가’, 이... | 광통신주, 장초반 줄상승...AI 인프라 확대 기대감 | [특징주] 광통신株, 빅테크 데이터센터 투자 기대감…강세

### 2. 오이솔루션 (138080)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **96.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 3.56%, pattern: relatively_positive_history
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: 3.34%
- Next close return data: 8.36%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 16. Historical error notes subtracted 1.96 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 증시 풍향계] 반도체 소부장株 신고가 행진…머큐리 ‘상한가’, 이... | 광통신주, 장초반 줄상승...AI 인프라 확대 기대감 | [특징주] 광통신株, 빅테크 데이터센터 투자 기대감…강세

### 3. 오이솔루션 (138080)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **96.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 3.56%, pattern: relatively_positive_history
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: 3.34%
- Next close return data: 8.36%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 16. Historical error notes subtracted 1.96 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 증시 풍향계] 반도체 소부장株 신고가 행진…머큐리 ‘상한가’, 이... | 광통신주, 장초반 줄상승...AI 인프라 확대 기대감 | [특징주] 광통신株, 빅테크 데이터센터 투자 기대감…강세

### 4. 지아이이노베이션 (358570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **-0.59**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-0.50**
- Adjusted recommendation score: **70.91**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: -3.43%, pattern: relatively_positive_history
- Disclosure title: [기재정정]투자판단관련주요경영사항(임상시험계획변경승인)              (GI102 제1/2상 임상시험계획 변경승인 )
- Next open return data: 1.39%
- Next close return data: -3.43%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 0.59 points. Event-type performance did not change the score. Stock-specific history subtracted 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 2차전지 장비업계, 수주 모멘텀 속 체질 개선 집중… 투자 전략은? | 원일티엔아이·덕우전자 30% 육박…윈팩 26% 급등 | [주식] 바이오株 활기 되찾나...알지노믹스·지투지 20%↑

### 5. 에스에스알 (275630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.64**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **1.00**
- Adjusted recommendation score: **69.36**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: -2.62%, pattern: relatively_positive_history
- Disclosure title: 합병등종료보고서(영업양수도)
- Next open return data: -0.39%
- Next close return data: -2.62%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 2.64 points. Event-type performance subtracted 4.00 points. Stock-specific history added 1.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [오늘의 증시일정] KR모터스·NHN·한중엔시스 등 | 9월 23일 주식시장 주요공시 | IT 경기 회복 및 보안 사고 대응 기대… 보안 섹터에 온기 확산

### 6. 솔브레인홀딩스 (036830)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-2.64**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **67.36**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 9.98%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 0.91%
- Next close return data: 9.98%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 2.64 points. Event-type performance subtracted 4.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 1일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 2일] 美 증시, 치솟던 금리 꺾이자 반등…3대... | 솔브레인홀딩스, 솔브레인네트워크 흡수합병 결정

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 싸이토젠 (217330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-2.64**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **70.36**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 0.15%, pattern: weak_historical_reaction
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: 0.31%
- Next close return data: 0.46%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 2.64 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [HIT알공] HLB제약, 향남 신공장에 550억원 투자키로 | 싸이토젠 “지놈케어 합병으로 ‘CTC·유전체’ 시너지 본격화” | 싸이토젠, 지놈케어 흡수합병 완료…통합 BI로 정밀의료 가속

### 2. 선도전기 (007610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **86.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **72.31**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.48%
- Next close return data: -1.03%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 3. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 1일 주식시장 주요공시 | 10월 2일 개장 전 주요 공시 | 9월 30일 주식시장 주요공시

### 3. 우진아이엔에스 (010400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.40**
- Adjusted recommendation score: **82.41**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -1.98%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -4.68%
- Next close return data: -2.46%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.40 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 1일 주식시장 주요공시 | 우진아이엔에스, 2세 승계 마침표…밸류업 시험대 | 9월 30일 주식시장 주요공시

### 4. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.74**
- Adjusted recommendation score: **85.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 15, success rate: 46.67%, avg next close: -1.68%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.16%
- Next close return data: -0.08%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.74 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 연세세브란스 금기창 원장, 송도세브란스 20년 표류에 국감행…착공 시... | 금호건설, 안성 1079억 공사서 손배청구 282억…6개월 새 33억→90억→28... | 아파트도 생활방식 따라 달라진다…캠핑·펫공간 갖춘 '강릉 아테라' 공...

### 5. 두산에너빌리티 (034020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **87.56**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: -2.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.24%
- Next close return data: -2.19%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 코스피, 동반 매도에 6,960선 등락…반도체 투톱 '희비' | 두산에너빌리티 주가, 10월 2일 장중 81,200원 1.10% 하락 | 범한메카텍, AP1000 격납용기 수주 위해 데모 제작 착수

### 6. 두산에너빌리티 (034020)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **87.56**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: -2.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.24%
- Next close return data: -2.19%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 코스피, 동반 매도에 6,960선 등락…반도체 투톱 '희비' | 두산에너빌리티 주가, 10월 2일 장중 81,200원 1.10% 하락 | 범한메카텍, AP1000 격납용기 수주 위해 데모 제작 착수

### 7. 삼천당제약 (000250)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **91.06**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.10%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]투자판단관련주요경영사항              (황반변성치료제(아일리아/주성분 : Aflibercept) 바이오시밀러 SCD411(Vial&PFS)의 캐나다 독점판매권 공급계약 체결 및 중동 6개 국가 추가 계약 체결)
- Next open return data: -0.70%
- Next close return data: -1.10%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼천당제약 주가, 10월 2일 장중 195,700원 1.86% 하락 | 삼천당제약, 세계 최대 제약전시회 'CPHI 2026' 첫 단독부스 참가 | 코스피, 동반 매도에 6,960선 등락…반도체 투톱 '희비'

### 8. 뷰티스킨 (406820)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **99.06**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.38%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.20%
- Next close return data: -2.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 에비에코리아, '두바이 더마 2026' 참가…전문 관리부터 홈케어까지 중... | 피부 노화 예측하고 사용감도 데이터로…아모레퍼시픽, AI 뷰티 연구 공... | ‘피부 노화’ 예측하고 ‘발림성’ 수치화…아모레퍼시픽, AI 연구 성과...

### 9. MH에탄올 (023150)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-0.05**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **101.70**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -3.53%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: -0.66%
- Next close return data: -3.53%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.05 points. Event-type performance did not change the score. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 1일 주식시장 주요공시 | [전일 주요공시] LS일렉트릭ㆍ두산에너빌리티ㆍ아이에스동서 등 | [아주증시포커스] 마이크론發 '어닝 서프라이즈' 국내 증시에 훈풍…삼...

### 10. MH에탄올 (023150)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-0.05**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **101.70**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -3.53%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: -0.66%
- Next close return data: -3.53%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.05 points. Event-type performance did not change the score. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 1일 주식시장 주요공시 | [전일 주요공시] LS일렉트릭ㆍ두산에너빌리티ㆍ아이에스동서 등 | [아주증시포커스] 마이크론發 '어닝 서프라이즈' 국내 증시에 훈풍…삼...

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
