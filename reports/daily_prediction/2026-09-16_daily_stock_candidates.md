# Daily Stock Candidate Report - 2026-09-16

Generated at: 2026-09-16 01:20:09

ML dataset: `data/processed/ml_dataset_20260916.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 003850 | 보령 | 5 | 5 | 100.00% | 3.46% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 14 | 9 | 100.00% | 7.29% | relatively_positive_history | 8.64 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 003060 | 에이프로젠바이오로직스 | 4 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.31 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| investment_decision | 245 | 144 | 70.83% | 0.06% | 6.00 |
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 211 | 113 | 73.45% | -2.05% | 4.00 |
| paid_in_capital_increase | 1249 | 946 | 61.84% | 0.08% | 3.00 |
| convertible_bond | 659 | 386 | 53.89% | 1.51% | 2.00 |
| bonus_issue | 58 | 55 | 52.73% | 0.86% | 0.00 |
| disclosure_violation | 98 | 48 | 35.42% | 0.87% | -3.00 |
| merger | 169 | 91 | 21.98% | 1.12% | -4.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| spin_off | 64 | 41 | 29.27% | 0.25% | -6.00 |
| supply_contract | 742 | 480 | 28.12% | -0.79% | -6.00 |
| major_shareholder_change | 1323 | 840 | 35.00% | -1.46% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| lawsuit | 211 | 83 | 30 | 98 | 1.54 |
| paid_in_capital_increase | 1249 | 585 | 361 | 303 | 1.47 |
| investment_decision | 245 | 102 | 42 | 101 | 0.88 |
| convertible_bond | 659 | 208 | 178 | 273 | 0.77 |
| disclosure_violation | 98 | 17 | 31 | 50 | -0.08 |
| bonus_issue | 58 | 29 | 26 | 3 | -0.64 |
| supply_contract | 742 | 135 | 345 | 262 | -1.15 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 1323 | 294 | 546 | 483 | -1.78 |

## Positive Candidates

### 1. 신화프리텍 (095190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **140.35**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -0.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 7.12%
- Next close return data: 0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 15일 주식시장 주요공시 | [박정식의 국내 주식시황] 미 10년물 금리 5%대 진입…반도체 투자심리... | [이넷뉴스 브랜드평판] 두산에너빌리티, 원자력발전 상장기업 9월 1위.....

### 2. 쎄크 (081180)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **138.35**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 14.97%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 6.33%
- Next close return data: 14.97%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 15일 주식시장 주요공시 | 리서치알음 “쎄크, HBM 적층 후 X-ray 검사장비 공급사 선정 임박…적정... | [클릭 e종목]"쎄크, HBM 수율 경쟁 올라탄 X-ray 검사장비"

### 3. 두산퓨얼셀 (336260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.28**
- Adjusted recommendation score: **133.13**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 66.67%, avg next close: 8.34%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.12%
- Next close return data: -2.31%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.28 points. Stock pattern label is relatively_positive_history.
- Related news examples: 페로타임즈 손바닥뉴스 9월16일(수) | 9월 15일 주식시장 주요공시 | [코스피·코스닥, 두산퓨얼셀 한전기술 금호석유화학 카카오게임즈 유한...

### 4. 아시아나IDT (267850)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.12**
- Adjusted recommendation score: **117.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.43%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.87%
- Next close return data: -1.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: 9월 15일 주식시장 주요공시 | 마일리지 산 넘은 대한항공…남은 건 조종사 서열·계열사 정리 | [N2 모닝 경제 브리핑-9월 16일] 美 증시, ‘금리·유가’ 겹악재에 휘청...

### 5. 비츠로넥스텍 (488900)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **116.35**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.40%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.60%
- Next close return data: 2.40%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 15일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 16일] 美 증시, ‘금리·유가’ 겹악재에 휘청... | [오늘의 주요공시] 두산퓨얼셀ㆍ효성중공업ㆍ금호석유화학 등

### 6. 미트박스 (475460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-0.64**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **113.36**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 5.44%, pattern: relatively_positive_history
- Disclosure title: 권리락              (무상증자)
- Next open return data: 5.42%
- Next close return data: 5.60%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 0.64 points. Event-type performance did not change the score. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: "'인조 고기'에 '고기(meat)' 글자 빼라(?)" 축산업계와 바이오업체간 갈... | 월간 활성 이용자 40만명 패덤, 슈퍼휴먼이 인수 | 알서포트, K-ICT WEEK 2026서 AI 회의록·원격제어 솔루션 공개…"제조현...

### 7. 효성 (004800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.39**
- Adjusted recommendation score: **101.46**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 50.00%, avg next close: -1.84%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.71%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 추석 앞둔 건설현장 안전점검… 개구부·난간 추락위험 살펴 | 어둠 속에 짙게 퍼진 1300년의 맥놀이… 계속 들을 수 있을까 | 대기업 생산기지, 영남·충청에 57.8% 소재 ... 호남권은 15.4%

### 8. 효성 (004800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.39**
- Adjusted recommendation score: **101.46**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 50.00%, avg next close: -1.84%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.71%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 추석 앞둔 건설현장 안전점검… 개구부·난간 추락위험 살펴 | 어둠 속에 짙게 퍼진 1300년의 맥놀이… 계속 들을 수 있을까 | 대기업 생산기지, 영남·충청에 57.8% 소재 ... 호남권은 15.4%

### 9. 효성 (004800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.39**
- Adjusted recommendation score: **101.46**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 50.00%, avg next close: -1.84%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.71%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 추석 앞둔 건설현장 안전점검… 개구부·난간 추락위험 살펴 | 어둠 속에 짙게 퍼진 1300년의 맥놀이… 계속 들을 수 있을까 | 대기업 생산기지, 영남·충청에 57.8% 소재 ... 호남권은 15.4%

### 10. 효성 (004800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.39**
- Adjusted recommendation score: **101.46**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 50.00%, avg next close: -1.84%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.71%
- Next close return data: -0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 추석 앞둔 건설현장 안전점검… 개구부·난간 추락위험 살펴 | 어둠 속에 짙게 퍼진 1300년의 맥놀이… 계속 들을 수 있을까 | 대기업 생산기지, 영남·충청에 57.8% 소재 ... 호남권은 15.4%

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.72**
- Adjusted recommendation score: **94.13**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 40.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.15%
- Next close return data: -0.96%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.72 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 현대건설, 9월 건설회사 브랜드평판 1위...롯데건설·대우건설 뒤이어 | '지식의 나무가 숲으로'…롯데건설이 그린 목동 재건축 '소르본 프로젝... | 9월 15일 주식시장 주요공시

### 2. 한전산업 (130660)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.12**
- Adjusted recommendation score: **96.73**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.52%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.61%
- Next close return data: -2.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼일PwC "민간 송전망 투자, 회수·위험배분 구체화해야" | 尹정부·대통령실 YTN매각 부당개입… 방미통위 의결 오리무중 | 삼일PwC “송전망 민간투자, 투자비 회수·위험 배분 기준 구체화해야”

### 3. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **109.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **97.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.26%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 1.32%
- Next close return data: -2.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 15일 주식시장 주요공시 | [개장 전 주요 공시] 미투온·현대산업개발·비케이홀딩스·다원시스 등 | AI 시대 보안 수요 커진다…정보보안 테마 아이티센피엔에스 '훨훨'

### 4. 한전기술 (052690)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **99.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -6.01%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.47%
- Next close return data: -6.01%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [애널픽] 산업 지형도 바꾼 이란전쟁…韓, 방산·정유·건설 '반사이익... | 9월 15일 주식시장 주요공시 | [개장 전 주요 공시] 미투온·현대산업개발·비케이홀딩스·다원시스 등

### 5. 티와이홀딩스 (363280)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **106.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.00**
- Adjusted recommendation score: **100.85**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.24%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.72%
- Next close return data: 0.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 15일 주식시장 주요공시 | [개장 전 주요 공시] 미투온·현대산업개발·비케이홀딩스·다원시스 등 | 자회사 가치 재평가 기대감에 지주사 들썩…종목별 희비

### 6. HDC (012630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.32**
- Adjusted recommendation score: **104.53**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 20.00%, avg next close: 0.69%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.18%
- Next close return data: -1.63%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.32 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 지방 분양시장 침체 속 양극화 심화…'브랜드·역세권' 단지로 수요 집... | HDC현대산업개발, 하이엔드로 '숙대입구역세권 재개발' 출사표 | 실적 회복한 IPARK현대산업개발, '용산 벨트' 확장….숙대입구역세권 개...

### 7. 스피어 (347700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.83**
- Adjusted recommendation score: **106.02**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -1.69%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.74%
- Next close return data: -0.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.83 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "AI 역량이 필수 기본기"…비개발 직무 공고 325%↑ 급증 | "AI 할 줄 아세요?"…기획·콘텐츠까지 번진 채용시장 | 잡코리아 "상반기 AI 직무 공고 128%↑…22%는 비개발 직무"

### 8. 기가비스 (420770)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **109.10**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.59%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.69%
- Next close return data: -1.59%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 15일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 16일] 美 증시, ‘금리·유가’ 겹악재에 휘청... | [오늘의 주요공시] 두산퓨얼셀ㆍ효성중공업ㆍ금호석유화학 등

### 9. 선익시스템 (171090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.25**
- Adjusted recommendation score: **109.60**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -3.99%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.14%
- Next close return data: -3.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 15일 주식시장 주요공시 | 삼성D, 12인치 RGB OLEDoS 양산에 3000억 투자 | LGD '플립'용 OLED 증착기, 야스·선익시스템 공급 경쟁 구도

### 10. 효성중공업 (298040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **116.00**
- Error-note adjustment score: **-1.15**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.31**
- Adjusted recommendation score: **114.16**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.00%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.18%
- Next close return data: 1.14%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 1.15 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 페로타임즈 손바닥뉴스 9월16일(수) | 한투證 "효성중공업, 비중 확대…변압기 수요 '피크아웃' 아냐" | “효성중공업 3900억 수주…초고압 변압기 피크아웃 아직 멀어”

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
