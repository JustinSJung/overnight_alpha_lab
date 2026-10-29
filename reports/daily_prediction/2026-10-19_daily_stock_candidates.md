# Daily Stock Candidate Report - 2026-10-19

Generated at: 2026-10-19 00:40:07

ML dataset: `data/processed/ml_dataset_20261019.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
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
| lawsuit | 408 | 288 | 57.99% | -0.77% | 3.00 |
| paid_in_capital_increase | 2181 | 1661 | 57.86% | 0.19% | 3.00 |
| spin_off | 112 | 80 | 51.25% | 1.80% | 2.00 |
| investment_decision | 382 | 267 | 53.56% | -0.06% | 0.00 |
| disclosure_violation | 166 | 96 | 50.00% | -0.51% | 0.00 |
| convertible_bond | 1074 | 742 | 51.62% | 0.94% | 0.00 |
| bonus_issue | 102 | 99 | 41.41% | -0.40% | -3.00 |
| bond_with_warrant | 116 | 104 | 23.08% | 0.54% | -6.00 |
| major_shareholder_change | 2075 | 1442 | 34.74% | -0.55% | -6.00 |
| merger | 411 | 316 | 18.99% | 0.43% | -6.00 |
| supply_contract | 1191 | 865 | 30.29% | -0.79% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 0 | 4 | 2.50 |
| paid_in_capital_increase | 2181 | 961 | 700 | 520 | 1.24 |
| lawsuit | 408 | 167 | 121 | 120 | 1.16 |
| convertible_bond | 1074 | 383 | 359 | 332 | 0.78 |
| disclosure_violation | 166 | 48 | 48 | 70 | 0.58 |
| investment_decision | 382 | 143 | 124 | 115 | -0.40 |
| spin_off | 112 | 41 | 39 | 32 | -0.61 |
| bond_with_warrant | 116 | 24 | 80 | 12 | -1.03 |
| bonus_issue | 102 | 41 | 58 | 3 | -1.15 |
| supply_contract | 1191 | 262 | 603 | 326 | -1.17 |

## Positive Candidates

### 1. 솔디펜스 (215090)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.74**
- Adjusted recommendation score: **134.57**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 2.04%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.44%
- Next close return data: 1.25%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.74 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 16일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 19일] 美 증시, AI 거품론에 기술주 투매…반... | 천무 중사거리 공급계약 35억2820만원…솔디펜스·퍼스텍

### 2. 솔디펜스 (215090)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.74**
- Adjusted recommendation score: **134.57**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 2.04%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.44%
- Next close return data: 1.25%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.74 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 16일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 19일] 美 증시, AI 거품론에 기술주 투매…반... | 천무 중사거리 공급계약 35억2820만원…솔디펜스·퍼스텍

### 3. 솔디펜스 (215090)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.74**
- Adjusted recommendation score: **134.57**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 2.04%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.44%
- Next close return data: 1.25%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.74 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 16일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 19일] 美 증시, AI 거품론에 기술주 투매…반... | 천무 중사거리 공급계약 35억2820만원…솔디펜스·퍼스텍

### 4. 솔디펜스 (215090)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.74**
- Adjusted recommendation score: **134.57**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 2.04%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.44%
- Next close return data: 1.25%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.74 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 16일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 19일] 美 증시, AI 거품론에 기술주 투매…반... | 천무 중사거리 공급계약 35억2820만원…솔디펜스·퍼스텍

### 5. 쎄노텍 (222420)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.42**
- Adjusted recommendation score: **131.41**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -1.61%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.42 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 16일 주식시장 주요공시 | [코스피·코스닥,대우건설 위드텍 쎄노텍 키움증권 신세계I&C 제넥신 동... | [N2 모닝 경제 브리핑-10월 19일] 美 증시, AI 거품론에 기술주 투매…반...

### 6. 동아지질 (028100)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.46**
- Adjusted recommendation score: **102.29**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 57.14%, avg next close: -0.78%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.51%
- Next close return data: 0.48%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.46 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 16일 주식시장 주요공시 | 동아지질 노원 전력구 공사 기간 7개월 연장 | 대우건설, 현장타설 '탄소저감 조강형 콘크리트' 탄소크레딧 인증 본궤...

## Volatile Watchlist

### 1. 영화금속 (012280)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.06**
- Adjusted recommendation score: **40.09**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 8, success rate: 62.50%, avg next close: -2.36%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.00%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.06 points. Stock pattern label is relatively_positive_history.
- Related news examples: 영화금속 최대주주 삼신정밀, 보통주 10만주 장내매수 | 글로벌 완성차 판매 확대 기대…자동차부품주 '부르릉' | 한국타이어앤테크놀로지·금호타이어 상승…현대모비스·한온시스템은...

### 2. 영화금속 (012280)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.06**
- Adjusted recommendation score: **40.09**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 8, success rate: 62.50%, avg next close: -2.36%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.00%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.06 points. Stock pattern label is relatively_positive_history.
- Related news examples: 영화금속 최대주주 삼신정밀, 보통주 10만주 장내매수 | 글로벌 완성차 판매 확대 기대…자동차부품주 '부르릉' | 한국타이어앤테크놀로지·금호타이어 상승…현대모비스·한온시스템은...

### 3. 영화금속 (012280)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.06**
- Adjusted recommendation score: **40.09**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 8, success rate: 62.50%, avg next close: -2.36%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.00%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.06 points. Stock pattern label is relatively_positive_history.
- Related news examples: 영화금속 최대주주 삼신정밀, 보통주 10만주 장내매수 | 글로벌 완성차 판매 확대 기대…자동차부품주 '부르릉' | 한국타이어앤테크놀로지·금호타이어 상승…현대모비스·한온시스템은...

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 비큐AI (148780)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **39.00**
- Error-note adjustment score: **-0.40**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **35.60**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -0.91%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              ([국책과제 선정] 독자 AI 파운데이션 모델 프로젝트 공동활용 데이터 지원사업(2차))
- Next open return data: -0.78%
- Next close return data: -1.43%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 0.40 points. Event-type performance did not change the score. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 16일 주식시장 주요공시 | [개장 전 주요 공시] 삼성물산·한화시스템·키움증권·DL·현대엘리베이... | 10월 19일 개장 전 주요 공시

### 2. 대원 (007680)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **48.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **36.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 1.05%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 0.35%
- Next close return data: 1.05%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 4. News sentiment score is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대원제약, 췌장 외분비 기능장애 치료제 '판크라원정25000' 출시 | 새우가 고래를 먹었다...핀다, 핀테크 최초 저축은행 인수 눈앞 | 성남 산성대로 미션 투어 운영…지역 소비에 최대 3만원 지급

### 3. 대원 (007680)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **48.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **36.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 1.05%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 0.35%
- Next close return data: 1.05%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 4. News sentiment score is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대원제약, 췌장 외분비 기능장애 치료제 '판크라원정25000' 출시 | 새우가 고래를 먹었다...핀다, 핀테크 최초 저축은행 인수 눈앞 | 성남 산성대로 미션 투어 운영…지역 소비에 최대 3만원 지급

### 4. 한화플러스제5호스팩 (498390)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **58.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **41.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 6, success rate: 0.00%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -1.87%
- Next close return data: -0.19%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 4. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 16일 주식시장 주요공시 | 한화플러스제5호스팩 합병 임시주총 11월 12일로 연기 | 벤처투자부터 스팩 합병까지…창업투자 업종 매수세 확산

### 5. 한화플러스제5호스팩 (498390)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **58.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **41.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 6, success rate: 0.00%, avg next close: -0.74%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -1.87%
- Next close return data: -0.19%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 4. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 16일 주식시장 주요공시 | 한화플러스제5호스팩 합병 임시주총 11월 12일로 연기 | 벤처투자부터 스팩 합병까지…창업투자 업종 매수세 확산

### 6. 고려제강 (002240)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.00**
- Adjusted recommendation score: **49.03**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.61%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -2.98%
- Next close return data: -1.61%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 시몬스, 롯데몰 김포공항점 팝업 오픈…온라인 전용 매트리스도 전시 | 고려제강 홍석표 지분 20.57%로 확대 | 미쉐린 키 받은 특급호텔, 시몬스 침대 쓴다

### 7. 고려제강 (002240)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.00**
- Adjusted recommendation score: **49.03**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.61%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -2.98%
- Next close return data: -1.61%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 시몬스, 롯데몰 김포공항점 팝업 오픈…온라인 전용 매트리스도 전시 | 고려제강 홍석표 지분 20.57%로 확대 | 미쉐린 키 받은 특급호텔, 시몬스 침대 쓴다

### 8. 고려제강 (002240)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.00**
- Adjusted recommendation score: **49.03**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.61%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -2.98%
- Next close return data: -1.61%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 시몬스, 롯데몰 김포공항점 팝업 오픈…온라인 전용 매트리스도 전시 | 고려제강 홍석표 지분 20.57%로 확대 | 미쉐린 키 받은 특급호텔, 시몬스 침대 쓴다

### 9. 송우인포텍 (0203K0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **76.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **65.83**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -1. Negative keyword count is 3. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 송우인포텍 LH 계약 종료일 2027년 10월로 변경 | AI 위조 잡고 실적까지 터졌다… 라온시큐어로 쏠린 시장 매수세 뚜렷 | 거래소, '코스닥 데이' 마련…정책·산업 전망·기업 촘촘한 IR

### 10. 글로본 (019660)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.12**
- Adjusted recommendation score: **72.95**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.55%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -4.54%
- Next close return data: 0.58%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 5. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 16일 주식시장 주요공시 | 아모레퍼시픽, 화장품 상장기업 브랜드평판 1위…LG생활건강 맹추격 | 글로본, 필리핀 인산·황산 계약 종료일 11월 말로 변경

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
