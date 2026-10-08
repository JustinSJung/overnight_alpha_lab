# Daily Stock Candidate Report - 2026-10-08

Generated at: 2026-10-08 04:06:02

ML dataset: `data/processed/ml_dataset_20261008.csv`

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
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
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
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 366 | 249 | 56.63% | -0.52% | 3.00 |
| paid_in_capital_increase | 1791 | 1385 | 58.70% | 0.35% | 3.00 |
| convertible_bond | 931 | 633 | 53.08% | 1.05% | 2.00 |
| bonus_issue | 93 | 90 | 45.56% | 0.40% | 0.00 |
| disclosure_violation | 132 | 77 | 49.35% | -0.12% | 0.00 |
| investment_decision | 364 | 251 | 52.19% | 0.09% | 0.00 |
| bond_with_warrant | 76 | 65 | 9.23% | 0.07% | -6.00 |
| major_shareholder_change | 1747 | 1182 | 34.01% | -0.68% | -6.00 |
| merger | 355 | 264 | 19.70% | 0.59% | -6.00 |
| spin_off | 85 | 55 | 32.73% | 0.50% | -6.00 |
| supply_contract | 1024 | 724 | 29.01% | -0.72% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1791 | 813 | 572 | 406 | 1.31 |
| lawsuit | 366 | 141 | 108 | 117 | 1.04 |
| convertible_bond | 931 | 336 | 297 | 298 | 0.85 |
| disclosure_violation | 132 | 38 | 39 | 55 | 0.55 |
| investment_decision | 364 | 131 | 120 | 113 | -0.51 |
| bonus_issue | 93 | 41 | 49 | 3 | -0.58 |
| supply_contract | 1024 | 210 | 514 | 300 | -1.23 |
| bond_with_warrant | 76 | 6 | 59 | 11 | -1.93 |
| major_shareholder_change | 1747 | 402 | 780 | 565 | -1.97 |

## Positive Candidates

### 1. 윤성에프앤씨 (372170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **152.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **148.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.78%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.86%
- Next close return data: 2.78%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시 Pick] 윤성에프앤씨, 이틀 연속 美 2차전지 장비 수주 공시에 상승... | 2차전지 장비 테마 신바람… 전문가 "수주 잔고 탄탄한 기업에 올라타라... | 윤성에프앤씨, 美 2차전지 믹싱시스템 수주…134억 규모

### 2. HD건설기계 (267270)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.88**
- Adjusted recommendation score: **139.89**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -4.35%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.18%
- Next close return data: -6.16%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.88 points. Stock pattern label is not_enough_data.
- Related news examples: HD현대, 사장단 인사로 조선·안전경영 재정비…신사업 확대 속도 | HD건설기계, 美서 3879억 규모 가스 발전용 엔진 롱블럭 수주 | [카드] HD건설기계, 미국 데이터센터 발전용 엔진 수주

### 3. 아이에스티이 (212710)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.12**
- Adjusted recommendation score: **132.89**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.07%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 1.22%
- Next close return data: 0.68%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: HBM·고성능 반도체 수요 폭발…반도체 장비주, 기술주 주도속 매수 봇... | [N2 모닝 경제 브리핑-10월 8일] 美 증시, 사상 최고 찍고 반락…S&P500 0... | 아이에스티이, SK하이닉스에 16억원 세정장비 공급

### 4. 성도이엔지 (037350)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **100.27**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.48%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.07%
- Next close return data: 0.48%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: HBM·고성능 반도체 수요 폭발…반도체 장비주, 기술주 주도속 매수 봇... | [코스피·코스닥, 삼성전자 HD건설기계 한미약품 LG전자 윤성에프앤씨 ... | [N2 모닝 경제 브리핑-10월 8일] 美 증시, 사상 최고 찍고 반락…S&P500 0...

### 5. 빅텍 (065450)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **87.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.17**
- Adjusted recommendation score: **84.94**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.41%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.17%
- Next close return data: 0.34%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: 잘 나가던 방산株 일제히 조정…우주·드론주는 엇갈려 | 한화에어로스페이스, 우주항공국방 상장기업 2026년 10월 브랜드평판 1위 | 우주항공국방 상장기업 브랜드평판 2026년 10월 빅데이터 분석결과…1위...

## Volatile Watchlist

### 1. 빅텐츠 (210120)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **-0.51**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **6.99**
- Adjusted recommendation score: **58.48**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 22, success rate: 77.27%, avg next close: 2.02%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (경영지배인 선임)
- Next open return data: 0.05%
- Next close return data: 23.49%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 0.51 points. Event-type performance did not change the score. Stock-specific history added 6.99 points. Stock pattern label is relatively_positive_history.
- Related news examples: 빅텐츠 주가, 상한가... 무슨 회사길래? | [오늘의 증시일정] 한국유니온제약·일양약품·에이비온 등 | 지상파·수목 드라마 편성 확대... 스튜디오드래곤 주가 상승 재점화

### 2. 넥사다이내믹스 (351320)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.35**
- Adjusted recommendation score: **54.38**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 96, success rate: 76.04%, avg next close: -4.83%, pattern: relatively_positive_history
- Disclosure title: 기타시장안내              (최대주주의 의무보유 이행 관련)
- Next open return data: 2.77%
- Next close return data: -1.04%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.35 points. Stock pattern label is relatively_positive_history.
- Related news examples: 예선테크·선익시스템 주가 방긋…디스플레이 장비주 투자심리 개선 | [9월 주가상승률]상위 50개 중 46개 교체…상승폭은 둔화 | 씨싸이트 75%·윈팩 67% 상승…HLB 계열주 눈길

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 대양금속 (009190)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **24.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.99**
- Adjusted recommendation score: **19.02**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 11, success rate: 45.45%, avg next close: 3.95%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경              
- Next open return data: 0.76%
- Next close return data: -0.15%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.99 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 글로벌 광물 확보전 치열… 니켈 밸류체인 실적 향방은? | [전일 주요공시] 모나미·형지엘리트·한미사이언스·BGF·SGC에너지·SK디... | 동양고속 30%·천일고속 29.99%…20% 이상 상승 11개

### 2. 파라택시스이더리움 (290560)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **38.00**
- Error-note adjustment score: **-1.99**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.55**
- Adjusted recommendation score: **22.46**
- Risk level: **HIGH**
- Event type: `spin_off`
- Stock-specific evaluated cases: 17, success rate: 5.88%, avg next close: -2.04%, pattern: weak_historical_reaction
- Disclosure title: 주권매매거래정지              (주식의 병합, 분할 등 전자등록 변경, 말소)
- Next open return data: -2.32%
- Next close return data: -6.33%
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes subtracted 1.99 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.55 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [주요공시] HLB, 모비릭스, 영원무역, 포스코퓨처엠, 하나투어, 알테오젠... | 소프트웨어株 상승세 꺾였다… 안랩 급락에 보안주도 '휘청' | [더벨]파라택시스ETH, 코리아 합병 철회 '현금 유출 부담'

### 3. 동원모빌리티 (018500)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.12**
- Adjusted recommendation score: **25.91**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -0.53%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.83%
- Next close return data: -0.53%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.97 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [금융家] BNK부산은행 ⑥ㅣ 지역 상생·산업금융 확대에 '잰걸음'…해킹... | "전남·광주 묶자 100개 조직 들썩"… NH농협금융지주, 서남권 메가시티... | [Who Is ?] 정일택 금호타이어 대표이사 사장

### 4. 한미약품 (128940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **34.00**
- Error-note adjustment score: **-0.51**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-6.83**
- Adjusted recommendation score: **26.66**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 25.00%, avg next close: -1.78%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (에페오토인젝터주(에페글레나타이드) 식품의약품안전처 품목허가 승인)
- Next open return data: -1.50%
- Next close return data: -7.16%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 0.51 points. Event-type performance did not change the score. Stock-specific history subtracted 6.83 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [금융권 이모저모]한국투자신탁운용, ACE 주주가치 ETF 6개월 비교지수... | 한미약품, 토종 비만약 '에페' 식약처 허가…국산 45호 신약 | 기술반환 굴욕 딛고 '45호 신약'으로…한미약품 '에페', 10년 와신상담 ...

### 5. 선도전기 (007610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **77.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **63.27**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.78%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.66%
- Next close return data: -1.78%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 6. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 8일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-10월 8일] 美 증시, 사상 최고 찍고 반락…S&P500 0... | AI 전력 수요는 늘어나는데…전기장비株는 차익실현에 '휘청'

### 6. 주연테크 (044380)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **63.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.58**
- Adjusted recommendation score: **64.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 92.31%, avg next close: 6.24%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -3. Negative keyword count is 4. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.58 points. Stock pattern label is relatively_positive_history.
- Related news examples: 거래소 '시총 미달' 상장폐지 유예에 관리종목 줄줄이 '上' | 거래소 '시총 미달' 상폐 절차 유예에 관련주 줄줄이 급등 | [특징주] 법원 '시총 미달' 상장폐지 제동에…형지I&C 등 관리종목 줄상...

### 7. HJ중공업 (097230)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.57**
- Adjusted recommendation score: **75.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 0.00%, avg next close: -1.43%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.27%
- Next close return data: -2.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.57 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [2026 국감] 현대건설, 철근누락 책임 연장…대우건설, 가덕도 공사비 증... | KLPGA '변형 스테이블포드' HJ중공업·동부건설 챔피언십 관전포인트…... | [오늘의 주요일정·8일] 노동부, 일자리 전담반(TF) 개최

### 8. HS화성 (002460)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.23**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.21**
- Adjusted recommendation score: **90.56**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 16.67%, avg next close: -1.04%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.23 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.21 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대구보호관찰소, '범죄예방플랫폼'...HS화성(주)협력사업 업무협약 체결 | 【데일리 ESG 정책 브리핑】디스플레이 규제개선·원전수출 지원 확대 | 화학 상장기업 2026년 10월 브랜드평판...에코프로, LG화학, 포스코퓨처...

### 9. 알파칩스 (117670)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-0.58**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-5.75**
- Adjusted recommendation score: **90.67**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -0.67%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.90%
- Next close return data: -0.67%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 0.58 points. Event-type performance did not change the score. Stock-specific history subtracted 5.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [코스피·코스닥, 삼성전자 HD건설기계 한미약품 LG전자 윤성에프앤씨 ... | 코스피·코스닥 전 거래일(7일) 주요공시는?...에피소드컴퍼니, 140억원... | [N2 모닝 경제 브리핑-10월 8일] 美 증시, 사상 최고 찍고 반락…S&P500 0...

### 10. 알파칩스 (117670)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-0.58**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-5.75**
- Adjusted recommendation score: **90.67**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -0.67%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 0.90%
- Next close return data: -0.67%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 0.58 points. Event-type performance did not change the score. Stock-specific history subtracted 5.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [코스피·코스닥, 삼성전자 HD건설기계 한미약품 LG전자 윤성에프앤씨 ... | 코스피·코스닥 전 거래일(7일) 주요공시는?...에피소드컴퍼니, 140억원... | [N2 모닝 경제 브리핑-10월 8일] 美 증시, 사상 최고 찍고 반락…S&P500 0...

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
