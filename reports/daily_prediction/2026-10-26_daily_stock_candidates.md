# Daily Stock Candidate Report - 2026-10-26

Generated at: 2026-10-26 00:56:22

ML dataset: `data/processed/ml_dataset_20261026.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 044380 | 주연테크 | 18 | 13 | 92.31% | 6.24% | relatively_positive_history | 8.58 |
| 290690 | 아리바이오홀딩스 | 20 | 20 | 80.00% | 7.78% | relatively_positive_history | 8.54 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 15 | 11 | 81.82% | 2.91% | 8.00 |
| paid_in_capital_increase | 2308 | 1788 | 58.39% | -0.06% | 3.00 |
| spin_off | 113 | 81 | 50.62% | 1.76% | 2.00 |
| convertible_bond | 1151 | 818 | 51.22% | 0.98% | 0.00 |
| lawsuit | 460 | 339 | 53.39% | -0.16% | 0.00 |
| investment_decision | 423 | 308 | 51.95% | -0.23% | 0.00 |
| bonus_issue | 104 | 101 | 41.58% | -0.49% | -3.00 |
| disclosure_violation | 182 | 112 | 43.75% | -0.36% | -3.00 |
| bond_with_warrant | 117 | 105 | 23.81% | 0.47% | -6.00 |
| major_shareholder_change | 2222 | 1589 | 34.80% | -0.65% | -6.00 |
| merger | 461 | 366 | 20.77% | 0.25% | -6.00 |
| supply_contract | 1334 | 1008 | 30.36% | -0.71% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 15 | 9 | 2 | 4 | 2.07 |
| paid_in_capital_increase | 2308 | 1044 | 744 | 520 | 1.29 |
| lawsuit | 460 | 181 | 158 | 121 | 0.94 |
| convertible_bond | 1151 | 419 | 399 | 333 | 0.78 |
| disclosure_violation | 182 | 49 | 63 | 70 | 0.31 |
| investment_decision | 423 | 160 | 148 | 115 | -0.56 |
| spin_off | 113 | 41 | 40 | 32 | -0.66 |
| bond_with_warrant | 117 | 25 | 80 | 12 | -0.98 |
| bonus_issue | 104 | 42 | 59 | 3 | -1.14 |
| supply_contract | 1334 | 306 | 702 | 326 | -1.21 |

## Positive Candidates

### 1. 기가비스 (420770)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.80**
- Adjusted recommendation score: **135.59**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: -0.09%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.80%
- Next close return data: 0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.80 points. Stock pattern label is relatively_positive_history.
- Related news examples: 메리츠증권 "기가비스, 역대 최대 계약.. 해외 수주도 기대" | 10월 23일 주식시장 주요공시 | iM증권 "기가비스, 수주잔고 계속 급증 전망…목표가↑"

### 2. 삼성물산 (028260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.48**
- Adjusted recommendation score: **95.27**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 23, success rate: 82.61%, avg next close: 0.89%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.87%
- Next close return data: 1.57%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.48 points. Stock pattern label is relatively_positive_history.
- Related news examples: 삼성물산, 창원 용호1구역 1315가구 재건축 수주...7381억 규모 | 삼성물산, 창원 용호1구역에 46층 래미안 조성 | 삼성물산, 7381억 규모 창원 용호1구역 재건축 시공사 선정

### 3. 코오롱 (002020)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.42**
- Adjusted recommendation score: **93.21**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 81.25%, avg next close: -0.37%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -0.48%
- Next close return data: -0.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.42 points. Stock pattern label is relatively_positive_history.
- Related news examples: 이수화학, 제조 AX 지원사업 선정…AI 기 공정관리 추진 | 이수화학, 석유화학 공정 AX 본격화…AI 운전 지원체계 구축 | 이수화학, AI로 화학공장 운전 최적화···공정 이상 사전 감지 추진

### 4. 한전KPS (051600)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.92**
- Adjusted recommendation score: **91.71**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 1.16%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.86%
- Next close return data: -0.61%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.92 points. Stock pattern label is relatively_positive_history.
- Related news examples: 나주시, 발전5사 통합본사 유치 총력…국회서 결의대회 | 10월 23일 주식시장 주요공시 | 가수 배재열, 35년 직장생활 넘어 노래로 인생을 이야기하다

### 5. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.10**
- Adjusted recommendation score: **87.89**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 58.82%, avg next close: -2.84%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 1.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.10 points. Stock pattern label is relatively_positive_history.
- Related news examples: KLPGA 4승의 조아연의 은퇴선언 | 10월 23일 주식시장 주요공시 | 200만 건설인 가을축제 '제14회 전국 건설인 축구대회' 성료

### 6. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.10**
- Adjusted recommendation score: **87.89**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 58.82%, avg next close: -2.84%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 1.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.10 points. Stock pattern label is relatively_positive_history.
- Related news examples: KLPGA 4승의 조아연의 은퇴선언 | 10월 23일 주식시장 주요공시 | 200만 건설인 가을축제 '제14회 전국 건설인 축구대회' 성료

### 7. 엘앤씨바이오 (290650)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **79.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.44**
- Adjusted recommendation score: **74.42**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 72, success rate: 62.50%, avg next close: -4.18%, pattern: relatively_positive_history
- Disclosure title: 권리락              (무상증자)
- Next open return data: -0.83%
- Next close return data: -11.74%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.14 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.44 points. Stock pattern label is relatively_positive_history.
- Related news examples: 휴메딕스, ‘리투오’ 매출 5배 성장…필러 부진 메운다 [Why 바이오] | [N2 모닝 경제 브리핑-10월 26일] 美 증시, 중동 긴장에 3대 지수 하락…... | [mhn포토] 이대한, 파워 실어 날리는 티샷

## Volatile Watchlist

### 1. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-3.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **40.29**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 4.58%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: 0.00%
- Next close return data: 0.22%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 3.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: [종합] 최원철 "부득이" vs 이지은 "법 비웃는 습관"… 감사로 못 끊은 ... | 대림에서 DL이앤씨까지…‘e편한세상·아크로’로 바꾼 주거 기준 [건설... | 군포시, 산본신도시 4개 구역 특별정비구역 지정 제안 수용

### 2. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-3.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **40.29**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 4.58%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: 0.00%
- Next close return data: 0.22%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 3.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: [종합] 최원철 "부득이" vs 이지은 "법 비웃는 습관"… 감사로 못 끊은 ... | 대림에서 DL이앤씨까지…‘e편한세상·아크로’로 바꾼 주거 기준 [건설... | 군포시, 산본신도시 4개 구역 특별정비구역 지정 제안 수용

### 3. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-3.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **40.29**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 4.58%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: 0.00%
- Next close return data: 0.22%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 3.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: [종합] 최원철 "부득이" vs 이지은 "법 비웃는 습관"… 감사로 못 끊은 ... | 대림에서 DL이앤씨까지…‘e편한세상·아크로’로 바꾼 주거 기준 [건설... | 군포시, 산본신도시 4개 구역 특별정비구역 지정 제안 수용

### 4. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-3.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **40.29**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 4.58%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: 0.00%
- Next close return data: 0.22%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 3.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: [종합] 최원철 "부득이" vs 이지은 "법 비웃는 습관"… 감사로 못 끊은 ... | 대림에서 DL이앤씨까지…‘e편한세상·아크로’로 바꾼 주거 기준 [건설... | 군포시, 산본신도시 4개 구역 특별정비구역 지정 제안 수용

### 5. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-3.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **40.29**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 4.58%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: 0.00%
- Next close return data: 0.22%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 3.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: [종합] 최원철 "부득이" vs 이지은 "법 비웃는 습관"… 감사로 못 끊은 ... | 대림에서 DL이앤씨까지…‘e편한세상·아크로’로 바꾼 주거 기준 [건설... | 군포시, 산본신도시 4개 구역 특별정비구역 지정 제안 수용

### 6. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-3.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **40.29**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 4.58%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: 0.00%
- Next close return data: 0.22%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 3.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: [종합] 최원철 "부득이" vs 이지은 "법 비웃는 습관"… 감사로 못 끊은 ... | 대림에서 DL이앤씨까지…‘e편한세상·아크로’로 바꾼 주거 기준 [건설... | 군포시, 산본신도시 4개 구역 특별정비구역 지정 제안 수용

### 7. 우성 (006980)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-3.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.87**
- Adjusted recommendation score: **40.29**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 17, success rate: 52.94%, avg next close: 4.58%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: 0.00%
- Next close return data: 0.22%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 3.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.87 points. Stock pattern label is relatively_positive_history.
- Related news examples: [종합] 최원철 "부득이" vs 이지은 "법 비웃는 습관"… 감사로 못 끊은 ... | 대림에서 DL이앤씨까지…‘e편한세상·아크로’로 바꾼 주거 기준 [건설... | 군포시, 산본신도시 4개 구역 특별정비구역 지정 제안 수용

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 대창솔루션 (096350)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.88**
- Adjusted recommendation score: **74.67**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 2.24%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.72%
- Next close return data: -1.85%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 5. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.88 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 23일 주식시장 주요공시 | 대창솔루션, 미국 특수강 계약액 늘리고 납기 연장 | 미국 증시 기술주 부진 속 국내 원전주 동반 하락…두산에너빌리티 3%대...

### 2. CNT85 (056730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **93.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.33**
- Adjusted recommendation score: **78.46**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 20.00%, avg next close: -2.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -4.93%
- Next close return data: -4.93%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.33 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 23일 주식시장 주요공시 | CNT85 김해 소각설비 계약 종료일 26일로 변경 | "국내 분양 경기 침체 부담"… 건설 관련주, 숨고르기 장세 뚜렷

### 3. 대한과학 (131220)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **90.54**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.42%
- Next close return data: -0.56%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 누리호 발사 성공과 부처님 가르침 | 우주군·극초음속·AI·드론…바뀌는 전장 패러다임, 기술 헤게모니 잡... | 국민이 쓰는 '모두의 AI' 브랜드, 국민이 직접 만든다…공모전 개최

### 4. 그린리소스 (402490)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **92.29**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.49%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -2.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 23일 주식시장 주요공시 | 그린리소스, 공급계약 종료일 6개월 연장 | 애니보다 먼저 시작, 스마일게이트 '데드 어카운트'의 원작 존중법

### 5. 금양그린파워 (282720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.36**
- Adjusted recommendation score: **92.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 40.00%, avg next close: -1.61%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: -1.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.36 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 23일 주식시장 주요공시 | 금양그린파워, 현대건설과 '신한울 3·4호기' 공사계약 증액… 322억 규... | 금양그린파워 신한울 3·4호기 계약 10억5277만원 증액

### 6. 금양그린파워 (282720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.36**
- Adjusted recommendation score: **92.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 40.00%, avg next close: -1.61%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: -1.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.36 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 23일 주식시장 주요공시 | 금양그린파워, 현대건설과 '신한울 3·4호기' 공사계약 증액… 322억 규... | 금양그린파워 신한울 3·4호기 계약 10억5277만원 증액

### 7. 금양그린파워 (282720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.36**
- Adjusted recommendation score: **92.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 40.00%, avg next close: -1.61%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: -1.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.36 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 23일 주식시장 주요공시 | 금양그린파워, 현대건설과 '신한울 3·4호기' 공사계약 증액… 322억 규... | 금양그린파워 신한울 3·4호기 계약 10억5277만원 증액

### 8. 금양그린파워 (282720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.36**
- Adjusted recommendation score: **92.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 40.00%, avg next close: -1.61%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.74%
- Next close return data: -1.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.36 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 23일 주식시장 주요공시 | 금양그린파워, 현대건설과 '신한울 3·4호기' 공사계약 증액… 322억 규... | 금양그린파워 신한울 3·4호기 계약 10억5277만원 증액

### 9. 우진아이엔에스 (010400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **92.54**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 0.00%, avg next close: -2.66%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.62%
- Next close return data: -1.62%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 23일 주식시장 주요공시 | [더벨][네이밍&셰이밍 이사회 역할론] 우량 코스피 종목도 도마 위…장... | [저PBR 망신주기 D-7]저PBR 개선계획 62곳 제출…실효성은 미지수

### 10. KSS해운 (044450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **103.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **92.79**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.42%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 4. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 항공 예약정보 새고 선박까지 위협…기업들 '사이버 방어선' 재점검 | 10월 23일 주식시장 주요공시 | KSS해운 TRAMMO 장기대선 계약금액 1317억원으로 정정

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
