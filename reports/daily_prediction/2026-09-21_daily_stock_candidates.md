# Daily Stock Candidate Report - 2026-09-21

Generated at: 2026-09-21 01:03:37

ML dataset: `data/processed/ml_dataset_20260921.csv`

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
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 003060 | 에이프로젠바이오로직스 | 4 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.31 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |
| 003850 | 보령 | 6 | 6 | 100.00% | 2.48% | relatively_positive_history | 7.50 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 248 | 150 | 60.67% | -0.57% | 3.00 |
| paid_in_capital_increase | 1350 | 1047 | 60.74% | 0.24% | 3.00 |
| convertible_bond | 686 | 413 | 54.96% | 1.39% | 2.00 |
| bonus_issue | 64 | 61 | 47.54% | 0.59% | 0.00 |
| disclosure_violation | 116 | 66 | 50.00% | -0.08% | 0.00 |
| investment_decision | 304 | 203 | 51.72% | 0.29% | 0.00 |
| bond_with_warrant | 27 | 17 | 5.88% | -0.11% | -6.00 |
| spin_off | 69 | 46 | 28.26% | 0.14% | -6.00 |
| merger | 184 | 106 | 22.64% | 0.87% | -6.00 |
| supply_contract | 780 | 518 | 28.76% | -0.76% | -6.00 |
| major_shareholder_change | 1436 | 953 | 34.21% | -1.13% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1350 | 636 | 411 | 303 | 1.44 |
| lawsuit | 248 | 91 | 59 | 98 | 1.12 |
| convertible_bond | 686 | 227 | 186 | 273 | 0.84 |
| disclosure_violation | 116 | 33 | 33 | 50 | 0.57 |
| investment_decision | 304 | 105 | 98 | 101 | -0.53 |
| bonus_issue | 64 | 29 | 32 | 3 | -0.86 |
| supply_contract | 780 | 149 | 369 | 262 | -1.16 |
| bond_with_warrant | 27 | 1 | 16 | 10 | -1.59 |
| major_shareholder_change | 1436 | 326 | 627 | 483 | -1.92 |

## Positive Candidates

### 1. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **124.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 75, success rate: 94.67%, avg next close: -6.22%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.30%
- Next close return data: -1.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 일본 IT기업과 115만달러 AI 서버 공급계약 | 넥사다이내믹스, 경영진 개편 직후 해외 수주 성공 | 9월 18일 주식시장 주요공시

### 2. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **124.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 75, success rate: 94.67%, avg next close: -6.22%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.30%
- Next close return data: -1.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 일본 IT기업과 115만달러 AI 서버 공급계약 | 넥사다이내믹스, 경영진 개편 직후 해외 수주 성공 | 9월 18일 주식시장 주요공시

### 3. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **124.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 75, success rate: 94.67%, avg next close: -6.22%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.30%
- Next close return data: -1.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 일본 IT기업과 115만달러 AI 서버 공급계약 | 넥사다이내믹스, 경영진 개편 직후 해외 수주 성공 | 9월 18일 주식시장 주요공시

### 4. 넥사다이내믹스 (351320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.53**
- Adjusted recommendation score: **124.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 75, success rate: 94.67%, avg next close: -6.22%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.30%
- Next close return data: -1.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.53 points. Stock pattern label is relatively_positive_history.
- Related news examples: 넥사다이내믹스, 일본 IT기업과 115만달러 AI 서버 공급계약 | 넥사다이내믹스, 경영진 개편 직후 해외 수주 성공 | 9월 18일 주식시장 주요공시

### 5. 삼성물산 (028260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.04**
- Adjusted recommendation score: **111.88**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 87.50%, avg next close: 1.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.14%
- Next close return data: 1.41%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.04 points. Stock pattern label is relatively_positive_history.
- Related news examples: 1.8조원대 성수3지구 재개발 시공사에 삼성물산[부동산AtoZ] | 삼성물산, ‘1.8조 대어’ 성수3지구 품었다…‘래미안 레비르 성수’ ... | [개장시황] 코스피 0.9% 상승 출발…삼성전자 2%대 강세

### 6. 삼성물산 (028260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.04**
- Adjusted recommendation score: **111.88**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 87.50%, avg next close: 1.04%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.14%
- Next close return data: 1.41%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.04 points. Stock pattern label is relatively_positive_history.
- Related news examples: 1.8조원대 성수3지구 재개발 시공사에 삼성물산[부동산AtoZ] | 삼성물산, ‘1.8조 대어’ 성수3지구 품었다…‘래미안 레비르 성수’ ... | [개장시황] 코스피 0.9% 상승 출발…삼성전자 2%대 강세

### 7. 덱스터 (206560)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **107.34**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.66%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 0.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: K콘텐츠 해외 진출 방식 바뀐다…BCWW서 공동제작·포맷 개발 논의 | 9월 18일 주식시장 주요공시 | 콘진원, 39개국 1292개사 참가한 BCWW 성료... 2,540건 상담 성사

### 8. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.33**
- Adjusted recommendation score: **88.17**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 1.47%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.27%
- Next close return data: -0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.33 points. Stock pattern label is not_enough_data.
- Related news examples: 도시의 옛 공간, 새 주거지로…분양시장 ‘장소의 기억’ 경쟁 | ‘익숙한 땅의 화려한 변신’…여의도 MBC·상봉터미널 이어 자이갤러리... | 아파트 의존 못 벗어난 건설사…지어봤자 100원 벌면 94원 나간다

### 9. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.33**
- Adjusted recommendation score: **88.17**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 1.47%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.27%
- Next close return data: -0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.33 points. Stock pattern label is not_enough_data.
- Related news examples: 도시의 옛 공간, 새 주거지로…분양시장 ‘장소의 기억’ 경쟁 | ‘익숙한 땅의 화려한 변신’…여의도 MBC·상봉터미널 이어 자이갤러리... | 아파트 의존 못 벗어난 건설사…지어봤자 100원 벌면 94원 나간다

### 10. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.33**
- Adjusted recommendation score: **88.17**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 1.47%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.27%
- Next close return data: -0.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.33 points. Stock pattern label is not_enough_data.
- Related news examples: 도시의 옛 공간, 새 주거지로…분양시장 ‘장소의 기억’ 경쟁 | ‘익숙한 땅의 화려한 변신’…여의도 MBC·상봉터미널 이어 자이갤러리... | 아파트 의존 못 벗어난 건설사…지어봤자 100원 벌면 94원 나간다

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 에코심플렉스 (038870)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **93.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.25**
- Adjusted recommendation score: **87.09**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 1.54%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.17%
- Next close return data: 5.69%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.25 points. Stock pattern label is not_enough_data.
- Related news examples: 9월 18일 주식시장 주요공시 | 9월 14일 주식시장 주요공시 | 탄소감축 찬바람에도 CCUS는 살아남나… 미코·SGC에너지 강세

### 2. DH오토넥스 (000300)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **88.84**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 18일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 21일] 美 증시, 금리·유가 부담 속 혼조…반... | 한섬, LS마린솔루션, 오름테라퓨틱, 스튜디오드래곤, 한국가스공사 외

### 3. 스튜디오드래곤 (253450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **90.59**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.95%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.43%
- Next close return data: -0.95%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: CJ ENM, 호주 지상파 ‘네트워크 10’과 맞손…오세아니아 전진기지 구축 | 관광공사, 'K-드라마 체험 전시'…'도깨비' 등 작품 촬영지 소개 | K-드라마 명장면이 여행지로…관광공사, 체험형 전시 개최

### 4. 효성 ITX (094280)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **103.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **91.34**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.41%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.41%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 4. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 18일 주식시장 주요공시 | AI 시대 업무환경 바뀌자… 스마트워크株에 매수세 유입 | 원격근무 타고 날았다… 파수AI, 문서 보안 솔루션 수주 폭발

### 5. HD현대마린엔진 (071970)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **92.59**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.22%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.77%
- Next close return data: -1.73%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 18일 주식시장 주요공시 | [Who Is ?] 김희철 한화오션 대표이사 사장 | 추석 앞두고 협력사 대금 조기 지급…중흥 700억·HD현대 3762억

### 6. 동아쏘시오홀딩스 (000640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.00**
- Adjusted recommendation score: **96.84**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.40%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 18일 주식시장 주요공시 | [전일 주요공시] 대우건설·한섬·코오롱티슈진 등 | 대형주 쏠림에 문턱 높아진 KRX 헬스케어…전통 제약·중소 바이오 줄줄...

### 7. HJ중공업 (097230)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.44**
- Adjusted recommendation score: **102.40**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.90%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.93%
- Next close return data: -1.64%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.44 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [미르의 글로벌 레이더]필리핀 해군, 한화오션·HD현대·HJ중공업 연쇄 ... | 9월 18일 주식시장 주요공시 | 中 독무대 된 ‘LNG 해상 주유소’… 벙커링선 주문 싹쓸이

### 8. 도화엔지니어링 (002150)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **102.59**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.20%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.40%
- Next close return data: -0.20%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 18일 주식시장 주요공시 | 철도망 넓어지자 관련주도 움직였다…전력·차량株 '휘파람' | "FDA 비용까지 댄다"…우즈벡, K-바이오 잡기 '파격 카드'

### 9. 남광토건 (001260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.91**
- Adjusted recommendation score: **103.93**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 15, success rate: 0.00%, avg next close: -0.34%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.91 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 18일 주식시장 주요공시 | 용인 반도체 CMR 심사 코앞인데…심사위원 풀 확대 ‘논란’ | “서울까지 몇 분?”…수도권 집값 가르는 ‘시간 프리미엄’

### 10. 나우로보틱스 (459510)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **116.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.12**
- Adjusted recommendation score: **104.72**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.45%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.89%
- Next close return data: -3.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 18일 주식시장 주요공시 | 산업 자동화 타고 날아오른 하이젠알앤엠… 로봇용 제어기 기술 부각 | 휴머노이드 관절 움직인다… 엔비알모션, 차세대 감속기 상용화 박차

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
