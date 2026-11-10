# Daily Stock Candidate Report - 2026-11-10

Generated at: 2026-11-10 05:37:13

ML dataset: `data/processed/ml_dataset_20261110.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 248170 | 샘표식품 | 21 | 21 | 100.00% | 27.77% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1463 | 1130 | 57.17% | 0.36% | 3.00 |
| paid_in_capital_increase | 2767 | 2246 | 56.10% | -0.23% | 3.00 |
| merger | 798 | 702 | 44.87% | 5.29% | 1.00 |
| investment_decision | 566 | 451 | 52.77% | 0.25% | 0.00 |
| lawsuit | 566 | 445 | 51.69% | -0.46% | 0.00 |
| disclosure_violation | 211 | 141 | 41.13% | -0.31% | -3.00 |
| bond_with_warrant | 146 | 134 | 40.30% | 0.21% | -3.00 |
| bonus_issue | 107 | 104 | 42.31% | -0.51% | -3.00 |
| spin_off | 152 | 116 | 37.93% | 0.98% | -3.00 |
| major_shareholder_change | 2857 | 2223 | 39.81% | -0.80% | -3.00 |
| supply_contract | 1706 | 1380 | 35.07% | -0.67% | -3.00 |
| earnings_guidance | 66 | 62 | 25.81% | -0.08% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1463 | 646 | 484 | 333 | 1.22 |
| paid_in_capital_increase | 2767 | 1260 | 986 | 521 | 1.21 |
| lawsuit | 566 | 230 | 215 | 121 | 0.89 |
| bond_with_warrant | 146 | 54 | 80 | 12 | 0.21 |
| disclosure_violation | 211 | 58 | 83 | 70 | 0.19 |
| investment_decision | 566 | 238 | 213 | 115 | -0.53 |
| supply_contract | 1706 | 484 | 896 | 326 | -0.99 |
| bonus_issue | 107 | 44 | 60 | 3 | -1.05 |
| earnings_guidance | 66 | 16 | 46 | 4 | -1.24 |
| merger | 798 | 315 | 387 | 96 | -1.42 |

## Positive Candidates

### 1. 에스와이스틸텍 (365330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **170.00**
- Error-note adjustment score: **-0.99**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **171.51**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 7.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.07%
- Next close return data: 7.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 16. Historical error notes subtracted 0.99 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 9일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 10일] 美 증시, 저가 매수세에 3대 지수 급등... | 에스와이스틸텍, 삼성물산서 94억 원 수주…데크플레이트 사업 경쟁력 ...

### 2. 다스코 (058730)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-0.99**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.45**
- Adjusted recommendation score: **130.46**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 57.14%, avg next close: -0.53%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.58%
- Next close return data: 2.31%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.99 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.45 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 9일 주식시장 주요공시 | [개장 전 주요 공시] 삼성화재·GS건설·더블유게임즈·DL·피노 등 | [박정식의 국내 주식시황] 美 반도체 6.9% 급등…코스피 5000선 딛고 반등...

### 3. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-0.99**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.98**
- Adjusted recommendation score: **111.99**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 55.56%, avg next close: 2.22%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.71%
- Next close return data: 5.14%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 0.99 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.98 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 벡스코 제3전시장 공사 838억원 계약 | 계룡건설산업, 838억원 규모 벡스코 제3전시장 공사 수주 | 계룡건설 참여 인천 검암 S-2BL, AI 통합 안전시스템 도입 추진

### 4. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-0.99**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.02**
- Adjusted recommendation score: **111.03**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 50.00%, avg next close: 0.57%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 2.34%
- Next close return data: 3.29%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 0.99 points. Event-type performance subtracted 3.00 points. Stock-specific history added 0.02 points. Stock pattern label is not_enough_data.
- Related news examples: 코스피·코스닥 전 거래일(9일) 주요공시 | 도크 꽉 찬 K-조선…中 '선 건조' 전략에 주춤 | LNG선 발주 4.5배 늘었는데...선가는 왜 내렸나

### 5. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-0.99**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.43**
- Adjusted recommendation score: **107.44**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 50.00%, avg next close: 1.28%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 2.83%
- Next close return data: 5.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.99 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.43 points. Stock pattern label is not_enough_data.
- Related news examples: 윤지영 시의원, 340억 투입 스마트양식 사업 공공성 집중 점검 | GS건설, 겨울철 콘크리트 품질 관리 강화…레미콘 공장 전수 검증 실시 | GS건설, 동절기 내한 콘크리트 공급 전 품질 검증

## Volatile Watchlist

### 1. IPARK현대산업개발 (294870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **85.00**
- Error-note adjustment score: **-0.53**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **8.31**
- Adjusted recommendation score: **92.78**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 28, success rate: 67.86%, avg next close: 3.19%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 1.51%
- Next close return data: 5.59%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 0.53 points. Event-type performance did not change the score. Stock-specific history added 8.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: "정비사업 2.7조원 돌파" IPARK현대산업개발, 추가 수주 '속도' | [특징주] 현대건설 10% 급등·DL이앤씨 대우건설도 강세…건설주 동반 상... | [굿모닝! 10일 건설업계 소식] DL이앤씨·대우건설·IPARK현대산업개발

### 2. DL (000210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-1.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.91**
- Adjusted recommendation score: **77.04**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 7, success rate: 85.71%, avg next close: 1.92%, pattern: relatively_positive_history
- Disclosure title: 회사분할결정(종속회사의주요경영사항)              
- Next open return data: -0.11%
- Next close return data: 0.44%
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.91 points. Stock pattern label is relatively_positive_history.
- Related news examples: DL이앤씨, 성수2지구 수주 목전…‘아크로 성수’ 홍보관 개관 | 성수2지구 수주 노리는 DL이앤씨 홍보관 개관 | DL이앤씨 성수2지구 조합원 표심 잡기

### 3. 삼성물산 (028260)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **-0.53**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **5.33**
- Adjusted recommendation score: **39.80**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 31, success rate: 74.19%, avg next close: 0.77%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 5.98%
- Next close return data: 3.08%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 0.53 points. Event-type performance did not change the score. Stock-specific history added 5.33 points. Stock pattern label is relatively_positive_history.
- Related news examples: 삼성물산, 목동 첫 '래미안' 선보인다…양천구 목동13단지 재건축 시공... | [더벨][Company Watch] 신세계 백화점부문, 이석구 사장 앞세워 관리체계... | [부고] 김경한(전 대전MBC 상무)씨 별세

### 4. 동양건설산업 (005900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.27**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등의주식보유변동
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 시흥·안산 생활권 공유 ‘시흥 거모 아테라’ 11월 공급 | [더벨]라인그룹 EG건설, 파주운정 업무복합용지 확보 | '도봉 재건축 선발' 쌍문한양1차, 현설 유찰…연내 시공사 선정 불투명

### 5. 노을 (376930)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **15.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **8.42**
- Adjusted recommendation score: **18.69**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 24.49%, pattern: relatively_positive_history
- Disclosure title: 최대주주변경              
- Next open return data: 4.23%
- Next close return data: 21.77%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history added 8.42 points. Stock pattern label is relatively_positive_history.
- Related news examples: 에녹, 신곡 '미치도록 사랑해'로 깊어진 가을 감성 전한다 | 보은군, 지체장애인의 날 기념행사 열려 | [여행을 떠나요] 김포, 서해 노을에 하루를 물들이다

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 유유제약 (000220)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **21.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **13.27**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 0.94%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.27%
- Next close return data: 0.94%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 중앙대 약제학실 '약제반의 날' 50주년…장학금 1억2000만원 약정 | [HIT알공] 셀리드, 110만주 신주발행 무효 소송 피소 | 글로벌 임상·기술수출 기대… 제약업체주 옥석 가리기 본격화

### 2. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.09**
- Adjusted recommendation score: **14.18**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 49, success rate: 4.08%, avg next close: 0.97%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.73%
- Next close return data: 1.42%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.09 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김정관 산업장관 "정부가 기업보다 더 절박해야"...과감한 규제 완화 필... | 설화수, '카카오톡 기프트X'와 홀리데이 특별 선물 제안 | 자동차·가전·김장재료·패션까지…끝나지 않은 '코그페' 할인은 '쭈욱...

### 3. DB손해보험 (005830)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **18.77**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -1.00%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.79%
- Next close return data: -1.50%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼성화재, 英 캐노피우스 경영권 확보···글로벌 영토 확장 '승부수' | 금융권, 고향사랑기부제·고객 혜택 확대 | [보험 Pick] 보험사들, 의료·아동·지역사회 지원 잇따라

### 4. SNT에너지 (100840)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **16.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **8.71**
- Adjusted recommendation score: **19.98**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 6, success rate: 83.33%, avg next close: 9.07%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 3.23%
- Next close return data: 12.90%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 3. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history added 8.71 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 전력 수요에 원전주 들썩…디케이락·두산에너빌리티에 탑승할까 | SNT홀딩스, SNT에너지 주식 10만6000주 장내매수 | 삼성증권, 11월 첫째주 CJ ENM 등 49종목 매수 추천

### 5. 남광토건 (001260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-0.53**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-5.81**
- Adjusted recommendation score: **25.66**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 24, success rate: 8.33%, avg next close: -0.73%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 1.22%
- Next close return data: 1.90%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes subtracted 0.53 points. Event-type performance did not change the score. Stock-specific history subtracted 5.81 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 동아지질 주가 폭풍랠리... 무슨 호재 있나 | "분양가상한제 아파트에 청약통장 몰린다"… '부천대장 하우스토리 디센... | 11월 9일 주식시장 주요공시

### 6. 아이티센피엔에스 (232830)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.42**
- Event-type performance adjustment score: **1.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **28.58**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.98%, pattern: weak_historical_reaction
- Disclosure title: 회사합병결정(종속회사의주요경영사항)              
- Next open return data: 0.05%
- Next close return data: 0.98%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes subtracted 1.42 points. Event-type performance added 1.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 9일 주식시장 주요공시 | 씨플랫폼, 투케이엠시스템즈 흡수합병 결정 | [더벨][i-point] 아이티센피엔에스, AI 기반 선제 보안 대응역량 강화

### 7. 넥센타이어 (002350)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **28.77**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 1.17%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.17%
- Next close return data: 1.17%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 넥센타이어, 현대차 투싼 신차용 타이어 공급 | 美 공장 없는 넥센타이어, 영업익 61% 급감…현지 생산 격차 커지나 | 넥센타이어, 현대차 '디 올 뉴 투싼'에 OE 공급…"브랜드 인지도 강화"

### 8. CS홀딩스 (000590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **33.77**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 1.24%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.10%
- Next close return data: 1.24%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: AI 데이터센터 전력 수요 확대… 스마트그리드株 '신바람' | 지능형 전력망 투자 확대… LS ELECTRIC·일진전기 노려볼까 | CS홀딩스 장원영 대표, 5거래일간 1144주 매수

### 9. 인제니아테라퓨틱스 (950260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **38.00**
- Error-note adjustment score: **-0.53**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **46.47**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.04%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (IGT-302 연구개발 협약 관련 녹내장 적응증 옵션 미행사 공문 수령)
- Next open return data: 4.82%
- Next close return data: 5.72%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes subtracted 0.53 points. Event-type performance did not change the score. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: MSD, 인제니아 녹내장 신약 옵션 미행사…"기술반환 아냐" | MSD가 놓은 녹내장 신약…인제니아, 136억 들여 독자 임상 승부 | [Stock tracking] 인제니아테라퓨틱스 주가, IGT-302 옵션 미행사 소식에...

### 10. NH투자증권 (005940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-1.73**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.87**
- Adjusted recommendation score: **47.40**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 78, success rate: 44.87%, avg next close: -0.51%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 3.17%
- Next close return data: 3.39%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.73 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.87 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 피엔티, 동박부터 LFP 배터리까지 신사업 전략 공개 | [증권街] NH투자증권·미래에셋자산운용·삼성증권·신한투자증권 | 삼성화재, 캐노피우스 인수에 2.3조 투입…“신종자본증권 발행 계획 없...

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
