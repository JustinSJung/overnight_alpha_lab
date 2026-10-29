# Daily Stock Candidate Report - 2026-10-15

Generated at: 2026-10-15 01:06:52

ML dataset: `data/processed/ml_dataset_20261015.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 010950 | S-Oil | 9 | 9 | 88.89% | 5.68% | relatively_positive_history | 8.72 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 044380 | 주연테크 | 18 | 13 | 92.31% | 6.24% | relatively_positive_history | 8.58 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 100.00% | 1.92% | 8.00 |
| lawsuit | 395 | 275 | 56.73% | -0.52% | 3.00 |
| paid_in_capital_increase | 2070 | 1550 | 57.03% | 0.18% | 3.00 |
| disclosure_violation | 155 | 85 | 49.41% | -0.37% | 0.00 |
| convertible_bond | 1019 | 687 | 54.88% | 0.81% | 0.00 |
| investment_decision | 381 | 266 | 53.76% | -0.06% | 0.00 |
| bonus_issue | 102 | 99 | 41.41% | -0.40% | -3.00 |
| bond_with_warrant | 86 | 74 | 20.27% | -0.04% | -6.00 |
| major_shareholder_change | 1946 | 1313 | 34.58% | -0.76% | -6.00 |
| merger | 371 | 276 | 21.01% | 0.60% | -6.00 |
| spin_off | 92 | 60 | 35.00% | 0.14% | -6.00 |
| supply_contract | 1131 | 805 | 27.33% | -0.97% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 0 | 4 | 2.50 |
| paid_in_capital_increase | 2070 | 884 | 666 | 520 | 1.17 |
| lawsuit | 395 | 156 | 119 | 120 | 1.07 |
| convertible_bond | 1019 | 377 | 310 | 332 | 0.94 |
| disclosure_violation | 155 | 42 | 43 | 70 | 0.52 |
| investment_decision | 381 | 143 | 123 | 115 | -0.38 |
| bonus_issue | 102 | 41 | 58 | 3 | -1.15 |
| bond_with_warrant | 86 | 15 | 59 | 12 | -1.19 |
| supply_contract | 1131 | 220 | 585 | 326 | -1.35 |
| spin_off | 92 | 21 | 39 | 32 | -1.83 |

## Positive Candidates

### 1. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 2. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 3. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 4. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 5. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 6. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 7. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 8. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.28**
- Adjusted recommendation score: **159.93**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 106, success rate: 68.87%, avg next close: -4.86%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.95%
- Next close return data: -6.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 311억 규모 AI 서버 공급계약…턴어라운드 '신호탄' | 넥사다이내믹스, 311억원 규모 AI 서버 공급계약 체결 | 넥사다이내믹스, 311억 AI 서버 공급계약… 실적 턴어라운드 '신호탄'

### 9. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.02**
- Adjusted recommendation score: **109.63**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 15, success rate: 53.33%, avg next close: -3.36%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.91%
- Next close return data: -6.94%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.02 points. Stock pattern label is relatively_positive_history.
- Related news examples: 수출입은행, HJ중공업 컨테이너선 수출 금융 지원 | HJ중공업, 美 해군 군수지원함 MRO 완료...정비 역량 입증 | HJ중공업, 첫 미 해군 함정 MRO 완료…'아멜리아 에어하트' 출항

## Volatile Watchlist

### 1. 아이오케이이엔엠 (078860)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.38**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **1.62**
- Adjusted recommendation score: **56.24**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 1.06%, pattern: not_enough_data
- Disclosure title: [기재정정]투자판단관련주요경영사항              (경영정상화 위한 공개매각추진)
- Next open return data: -0.17%
- Next close return data: -2.71%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.38 points. Event-type performance did not change the score. Stock-specific history added 1.62 points. Stock pattern label is not_enough_data.
- Related news examples: K콘텐츠 글로벌 열풍에 엔터주 강세…하이브·에스엠·JYP '눈에 띄네' | 구혜선 "우리는 욕망 덩어리…부정하지 말고 실패 충분히 경험하세요" | 고윤, 숏폼드라마 ‘조선슬화핌’ 캐스팅…사극 로맨스 장르 출사표

### 2. 압타바이오 (293780)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-0.38**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-0.50**
- Adjusted recommendation score: **46.12**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: -5.44%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험결과)              (조영제유발급성신장손상(CIAKI) 치료제 Isuzinaxib(APX115)의 임상시험 제2상 Topline data수령)
- Next open return data: -2.21%
- Next close return data: -5.44%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 0.38 points. Event-type performance did not change the score. Stock-specific history subtracted 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 압타바이오, 아이수지낙시브 글로벌 2상서 1차 지표 달성 | 압타바이오 '아이수지낙시브', 글로벌 2상 1차 지표 충족…안전성 확인 | "치료제 아닌 예방" 건기식 시장 확대되나… 증시 반응은 '냉담'

### 3. 원포유 (122830)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **45.00**
- Error-note adjustment score: **-3.33**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **44.67**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 6.26%, pattern: relatively_positive_history
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: 3.86%
- Next close return data: -5.64%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 3.33 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [오늘의 증시일정] 이렘·유니온머티리얼·성우 등 | 원포유, 태광이노텍 59억원에 인수…AI 검사장비 시장 진출 | 원포유, 독자 특허 통합센서 기술 적용 ‘AI 공정 이상탐지ㆍ설비 예지...

### 4. 위메이드 (112040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.50**
- Adjusted recommendation score: **23.58**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -5.47%, pattern: relatively_positive_history
- Disclosure title: [기재정정]최대주주변경을수반하는주식양수도계약체결              
- Next open return data: -2.70%
- Next close return data: -5.47%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 위메이드 매각 두 달 연기…中 킹넷 증자등기에도 홍콩 출자금 납입 미... | 게임 상장기업 2026년 10월 브랜드평판...크래프톤, NC, 넷마블 順 | 10월 14일 주식시장 주요공시

### 5. 덴티움 (145720)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **27.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.92**
- Adjusted recommendation score: **23.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: -1.44%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.41%
- Next close return data: -2.56%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.92 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시] 10월 15일, 코스피 상장사 52개 종목 자사주 매수 신청 | [HIT 알공] 셀트리온, '짐펜트라' 류마티스 관절염 3상 IND 승인 | 글로벌 수출 기대 커진 의료기기주…종목별 온도 차

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 제일엠앤에스 (412540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **31.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.20**
- Adjusted recommendation score: **16.88**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 32, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              (최대주주의 의무보유 대상 확인 관련)
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.20 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 14일 주식시장 주요공시 | [개장 전 주요 공시] 에스원·LG디스플레이·셀트리온·해태제과식품 등 | [더벨]'최대 390억 베팅' 푸른인베스트먼트, 제일엠앤에스 인수

### 2. 제일엠앤에스 (412540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **31.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.20**
- Adjusted recommendation score: **16.88**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 32, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              (최대주주의 의무보유 대상 확인 관련)
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.20 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 14일 주식시장 주요공시 | [개장 전 주요 공시] 에스원·LG디스플레이·셀트리온·해태제과식품 등 | [더벨]'최대 390억 베팅' 푸른인베스트먼트, 제일엠앤에스 인수

### 3. 제일엠앤에스 (412540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **31.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.20**
- Adjusted recommendation score: **16.88**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 32, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.20 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 14일 주식시장 주요공시 | [개장 전 주요 공시] 에스원·LG디스플레이·셀트리온·해태제과식품 등 | [더벨]'최대 390억 베팅' 푸른인베스트먼트, 제일엠앤에스 인수

### 4. 제일엠앤에스 (412540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **31.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.20**
- Adjusted recommendation score: **16.88**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 32, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.20 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 14일 주식시장 주요공시 | [개장 전 주요 공시] 에스원·LG디스플레이·셀트리온·해태제과식품 등 | [더벨]'최대 390억 베팅' 푸른인베스트먼트, 제일엠앤에스 인수

### 5. 파라택시스이더리움 (290560)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **39.00**
- Error-note adjustment score: **-3.33**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.58**
- Adjusted recommendation score: **22.09**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 19, success rate: 5.26%, avg next close: -1.82%, pattern: weak_historical_reaction
- Disclosure title: 합병등종료보고서(자산양수도)
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 3.33 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.58 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 파라택시스이더리움, 이더리움 42억원어치 추가 취득…총 보유량 1만172... | 파라택시스이더리움, 이더리움 42억 매입 | 10월 15일 개장 전 주요 공시

### 6. 와이지-원 (019210)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **44.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.17**
- Adjusted recommendation score: **28.91**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: -1.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: -6.14%
- Next close return data: -6.57%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.17 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 14일 주식시장 주요공시 | JKL파트너스, 롯데손보 매각…4호 펀드 회수 '탄력' | 디케이락·씨케이솔루션·브릴스 급등… 기계업종 뜨거웠다

### 7. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-0.38**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-5.83**
- Adjusted recommendation score: **33.79**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: -0.67%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP13 SC(짐펜트라) 한국 임상 3상 시험계획 승인)
- Next open return data: -1.11%
- Next close return data: -1.33%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 0.38 points. Event-type performance did not change the score. Stock-specific history subtracted 5.83 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [제약브리핑] 동국제약 센텔리안24, '아마존 프라임 빅 딜 데이'서 최대... | 셀트리온, 유럽소화기학회서 램시마SC 경쟁력 알린다 | 셀트리온, 유럽 소화기학회서 '램시마SC' 경쟁력 알린다

### 8. 풍산홀딩스 (005810)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **51.00**
- Error-note adjustment score: **-1.92**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **37.08**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 20.00%, avg next close: -0.45%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -0.43%
- Next close return data: -2.75%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Negative keyword count is 3. Historical error notes subtracted 1.92 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [풍산홀딩스 자본방정식]② 내부거래 발판 '제조부문 성장' 핵심 축 풍산 | [풍산홀딩스 자본방정식]① 엇갈린 연결·별도 성적 '지분법·배당' 영향 | 전기차·방산 수요 기대에도 비철금속주 약세…실적 선별 중요

### 9. 사피엔반도체 (452430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **74.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **60.65**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -9.97%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -6.85%
- Next close return data: -9.97%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 7. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 14일 주식시장 주요공시 | 사피엔반도체 구동칩 계약 종료일 12월 11일로 연장 | 글로벌 메타버스·스마트글래스 시장 확대에... AR 관련주 러브콜 이어...

### 10. 에스아이리소스 (065420)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.35**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.10**
- Adjusted recommendation score: **85.55**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 4. Historical error notes subtracted 1.35 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.10 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 14일 주식시장 주요공시 | [오늘의 증시일정] 롯데리츠·판타지오·형지엘리트 등 | 9월 18일 주식시장 주요공시

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
