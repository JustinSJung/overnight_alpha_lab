# Daily Stock Candidate Report - 2026-10-16

Generated at: 2026-10-16 00:50:15

ML dataset: `data/processed/ml_dataset_20261016.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
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
| lawsuit | 396 | 276 | 56.52% | -0.51% | 3.00 |
| paid_in_capital_increase | 2081 | 1561 | 56.69% | 0.20% | 3.00 |
| spin_off | 112 | 80 | 51.25% | 1.80% | 2.00 |
| investment_decision | 381 | 266 | 53.76% | -0.06% | 0.00 |
| disclosure_violation | 157 | 87 | 48.28% | -0.23% | 0.00 |
| convertible_bond | 1058 | 726 | 52.07% | 0.95% | 0.00 |
| bonus_issue | 102 | 99 | 41.41% | -0.40% | -3.00 |
| major_shareholder_change | 2020 | 1387 | 35.62% | -0.53% | -3.00 |
| bond_with_warrant | 107 | 95 | 15.79% | 1.39% | -4.00 |
| merger | 403 | 308 | 19.48% | 0.44% | -6.00 |
| supply_contract | 1174 | 848 | 30.19% | -0.79% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 0 | 4 | 2.50 |
| paid_in_capital_increase | 2081 | 885 | 676 | 520 | 1.15 |
| lawsuit | 396 | 156 | 120 | 120 | 1.06 |
| convertible_bond | 1058 | 378 | 348 | 332 | 0.80 |
| disclosure_violation | 157 | 42 | 45 | 70 | 0.48 |
| investment_decision | 381 | 143 | 123 | 115 | -0.38 |
| spin_off | 112 | 41 | 39 | 32 | -0.61 |
| bonus_issue | 102 | 41 | 58 | 3 | -1.15 |
| supply_contract | 1174 | 256 | 592 | 326 | -1.18 |
| bond_with_warrant | 107 | 15 | 80 | 12 | -1.54 |

## Positive Candidates

### 1. LG씨엔에스 (064400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.88**
- Adjusted recommendation score: **134.70**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 2.48%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.12%
- Next close return data: 3.59%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.88 points. Stock pattern label is relatively_positive_history.
- Related news examples: LG씨엔에스, 금융·클라우드 성장···3Q 실적 개선 전망 | 10월 15일 주식시장 주요공시 | [전일 주요공시] STX·아이파크영창·인터지스·KG스틸 ·HMM 등

### 2. LG씨엔에스 (064400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.88**
- Adjusted recommendation score: **134.70**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 2.48%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.12%
- Next close return data: 3.59%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.88 points. Stock pattern label is relatively_positive_history.
- Related news examples: LG씨엔에스, 금융·클라우드 성장···3Q 실적 개선 전망 | 10월 15일 주식시장 주요공시 | [전일 주요공시] STX·아이파크영창·인터지스·KG스틸 ·HMM 등

### 3. LG씨엔에스 (064400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.88**
- Adjusted recommendation score: **134.70**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 2.48%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.12%
- Next close return data: 3.59%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.88 points. Stock pattern label is relatively_positive_history.
- Related news examples: LG씨엔에스, 금융·클라우드 성장···3Q 실적 개선 전망 | 10월 15일 주식시장 주요공시 | [전일 주요공시] STX·아이파크영창·인터지스·KG스틸 ·HMM 등

### 4. 대한전선 (001440)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **131.82**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.84%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 3.72%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [한국 건설, 80년의 기록]⑫ 광주 임대주택 짓던 호반건설, 대한전선·한... | 하나증권 "구리 가격 역사점 고점에 공급도 부족, 수혜주 풍산 LS 대한전... | 10월 15일 주식시장 주요공시

### 5. 빅텍 (065450)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.88**
- Adjusted recommendation score: **129.70**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 1.38%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.43%
- Next close return data: 4.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.88 points. Stock pattern label is relatively_positive_history.
- Related news examples: 우주항공·방산주 동반 함박웃음... 한화에어로스페이스·한화시스템 고... | 10월 15일 주식시장 주요공시 | [코스피·코스닥,대한항공 HMM HD현대중공업 대한전선 이마트 KS인더스트...

### 6. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **125.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 10.99%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 3.11%
- Next close return data: 10.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 15일 주식시장 주요공시 | 태블릿·노트북도 OLED 시대…소재·장비주 주목 | [코스닥 기관] HPSP·피에스케이 담았다…브이엠·실리콘투는 폭풍 매도

### 7. 필에너지 (378340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **120.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 2.91%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 3.30%
- Next close return data: 1.16%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 전자장비·기기주 신바람…AI 반도체·로봇 부품 수요 확대 | [원자재 시황] 반도체 투매에 금값 반등…WTI 98달러 육박 | 10월 15일 주식시장 주요공시

### 8. 비아트론 (141000)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **119.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **115.82**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.31%
- Next close return data: 2.31%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 15일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 16일] 美 증시, 물가 충격에도 3대 지수 상승... | 비아트론, 262억 규모 디스플레이 제조용 장비 공급 계약

### 9. 제테마 (216080)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.17**
- Adjusted recommendation score: **114.99**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.52%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.22%
- Next close return data: 0.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: '국산 비만약 1호' 한미약품 출격…중외·이노엔·제테마도 도전 | 10월 15일 주식시장 주요공시 | 톡신 국가핵심기술 지정, "누굴 위한 규제인가"...업계 해제 목소리

### 10. 제테마 (216080)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.17**
- Adjusted recommendation score: **114.99**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.52%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.22%
- Next close return data: 0.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: '국산 비만약 1호' 한미약품 출격…중외·이노엔·제테마도 도전 | 10월 15일 주식시장 주요공시 | 톡신 국가핵심기술 지정, "누굴 위한 규제인가"...업계 해제 목소리

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 스피어 (347700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.10**
- Adjusted recommendation score: **93.72**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 41.67%, avg next close: -1.12%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 4.51%
- Next close return data: 4.51%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.10 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 잡코리아, 하반기 채용 시즌 ‘합격 페스타’ 참여자 1만 명 돌파 | 스피어, 인니 니켈 공장 완공…우주항공 소재 공급망 수직계열화 | “10대들이 방에 내 사진 안 붙여”…WWE 전설 에지, 두 번째 은퇴 예고

### 2. HDC (012630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.75**
- Adjusted recommendation score: **97.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 38.46%, avg next close: 0.57%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.68%
- Next close return data: 4.33%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 정몽규의 영창 인수, 오판이었나…20년 뒤 다시 법원에 맡겨진 운명 | 10월 15일 주식시장 주요공시 | [전일 주요공시] STX·아이파크영창·인터지스·KG스틸 ·HMM 등

### 3. HDC (012630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.75**
- Adjusted recommendation score: **97.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 38.46%, avg next close: 0.57%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.68%
- Next close return data: 4.33%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 정몽규의 영창 인수, 오판이었나…20년 뒤 다시 법원에 맡겨진 운명 | 10월 15일 주식시장 주요공시 | [전일 주요공시] STX·아이파크영창·인터지스·KG스틸 ·HMM 등

### 4. 이노에이엑스 (296640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.38**
- Adjusted recommendation score: **101.44**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -1.84%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.49%
- Next close return data: -2.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.38 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 15일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 16일] 美 증시, 물가 충격에도 3대 지수 상승... | AI 위조 잡고 실적까지 터졌다… 라온시큐어로 쏠린 시장 매수세 뚜렷

### 5. 탑머티리얼 (360070)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **102.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.32%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 전자장비·기기주 신바람…AI 반도체·로봇 부품 수요 확대 | 10월 15일 주식시장 주요공시 | "DGIST 차세대 양극재·AI 코드리뷰 기술, 사업화 가능성 높아"

### 6. AP시스템 (265520)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **106.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **102.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.83%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.54%
- Next close return data: 1.83%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 15일 주식시장 주요공시 | 태블릿·노트북도 OLED 시대…소재·장비주 주목 | 플렉서블 디스플레이 시장 확대 기대…실적주 선별 필요

### 7. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.13**
- Adjusted recommendation score: **105.69**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 7.69%, avg next close: -2.60%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.50%
- Next close return data: 2.10%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.13 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 화성 주요 산단 직주근접…‘향남역 그로브 스위첸’ 분양 | 10월 15일 주식시장 주요공시 | [코스피·코스닥,대한항공 HMM HD현대중공업 대한전선 이마트 KS인더스트...

### 8. SK이터닉스 (475150)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.75**
- Adjusted recommendation score: **107.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -2.45%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 3.66%
- Next close return data: -0.37%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 15일 주식시장 주요공시 | [더벨]한앤코, SK디앤디 지원 이어간다…8년간 세 번 증자 참여 | [전일 주요공시] STX·아이파크영창·인터지스·KG스틸 ·HMM 등

### 9. 인스웨이브 (450520)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **114.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.88%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.06%
- Next close return data: -3.57%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 15일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 16일] 美 증시, 물가 충격에도 3대 지수 상승... | 인스웨이브, LG CNS와 89억원 규모 새마을금고 차세대 웹단말 전환 사업...

### 10. IPARK현대산업개발 (294870)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.57**
- Adjusted recommendation score: **122.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 42.86%, avg next close: 0.41%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.24%
- Next close return data: 3.61%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 15일 주식시장 주요공시 | '시티오씨엘 9단지 오션파크뷰' 19일(월) 무순위 청약 예정 | [코스피·코스닥,대한항공 HMM HD현대중공업 대한전선 이마트 KS인더스트...

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
