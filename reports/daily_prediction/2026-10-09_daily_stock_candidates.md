# Daily Stock Candidate Report - 2026-10-09

Generated at: 2026-10-09 02:47:51

ML dataset: `data/processed/ml_dataset_20261009.csv`

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
| lawsuit | 369 | 249 | 56.63% | -0.52% | 3.00 |
| paid_in_capital_increase | 1903 | 1385 | 58.70% | 0.35% | 3.00 |
| convertible_bond | 965 | 633 | 53.08% | 1.05% | 2.00 |
| bonus_issue | 93 | 90 | 45.56% | 0.40% | 0.00 |
| disclosure_violation | 147 | 77 | 49.35% | -0.12% | 0.00 |
| investment_decision | 366 | 251 | 52.19% | 0.09% | 0.00 |
| bond_with_warrant | 77 | 65 | 9.23% | 0.07% | -6.00 |
| major_shareholder_change | 1815 | 1182 | 34.01% | -0.68% | -6.00 |
| merger | 359 | 264 | 19.70% | 0.59% | -6.00 |
| spin_off | 87 | 55 | 32.73% | 0.50% | -6.00 |
| supply_contract | 1050 | 724 | 29.01% | -0.72% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1903 | 813 | 572 | 518 | 1.23 |
| lawsuit | 369 | 141 | 108 | 120 | 1.03 |
| convertible_bond | 965 | 336 | 297 | 332 | 0.82 |
| disclosure_violation | 147 | 38 | 39 | 70 | 0.50 |
| investment_decision | 366 | 131 | 120 | 115 | -0.51 |
| bonus_issue | 93 | 41 | 49 | 3 | -0.58 |
| supply_contract | 1050 | 210 | 514 | 326 | -1.20 |
| major_shareholder_change | 1815 | 402 | 780 | 633 | -1.90 |
| bond_with_warrant | 77 | 6 | 59 | 12 | -1.91 |

## Positive Candidates

### 1. 피엠티 (147760)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **142.80**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [속보] 피엠티, 삼성전자와 72억9250만원 규모 반도체 검사장치 공급계... | AI 반도체 호황에 장비株 주목… HBM 공급망 수혜주 '출렁' | AI 반도체 투자 재개 기대…에프엔에스테크·미코 등 반도체株 '불기둥...

### 2. 윤성에프앤씨 (372170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **138.30**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.78%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 기업 공시[10월 8일] | PCB부터 3D 검사장비까지…전자장비와기기株 매수 열기 확산 | [공시 Pick] 윤성에프앤씨, 이틀 연속 美 2차전지 장비 수주 공시에 상승...

### 3. 영진약품 (003520)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.50**
- Adjusted recommendation score: **128.30**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -1.05%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 영진약품, 프랑스 아테나와 소아 설사치료제 도입 계약 | [제약 레이더] 동아제약 여성문학 후원…시지바이오 임상, 영진약품 제... | 영진약품, 급성설사치료제 시장 강화...'라세카도트릴' 라인업

### 4. 다스코 (058730)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.56**
- Adjusted recommendation score: **104.36**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 2.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.56 points. Stock pattern label is relatively_positive_history.
- Related news examples: 방음터널ㆍ빌딩외벽ㆍ창문까지 전기 직접생산…발전소 변신 | 대주전자재료 주가 폭등랠리...무슨 호재 있나 | 데이터센터 전력 수요 폭증… 태양광에너지 테마 상승 동력 확보

### 5. 자연과환경 (043910)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.08**
- Adjusted recommendation score: **92.72**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.93%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.08 points. Stock pattern label is not_enough_data.
- Related news examples: 아역배우 박소이, ‘날씨의 아이들’을 만나다 (다큐 인사이드) | 포스뱅크·자연과환경 주가 '방긋'… 포스 장비 및 환경 복원 수혜주에... | 구리시, 동구릉서 야외도서관 '왕릉책마당' 운영

### 6. 자연과환경 (043910)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.08**
- Adjusted recommendation score: **92.72**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.93%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.08 points. Stock pattern label is not_enough_data.
- Related news examples: 아역배우 박소이, ‘날씨의 아이들’을 만나다 (다큐 인사이드) | 포스뱅크·자연과환경 주가 '방긋'… 포스 장비 및 환경 복원 수혜주에... | 구리시, 동구릉서 야외도서관 '왕릉책마당' 운영

### 7. 씨이랩 (189330)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **82.80**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 씨이랩, 건설안전박람회 참가 | “GPU·전력 다음은 메모리”…SK하이퍼 정석근, ‘AI 토큰 팩토리’ 시... | 씨이랩, 한국건설·안전박람회서 '비전 AI·디지털 트윈' 안전 솔루션 선...

### 8. 티사이언티픽 (057680)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **89.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **81.80**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: AI 열풍에도 IT서비스株 줄줄이 하락… 대형주 실적 우려 부각 | IT 경기 회복 및 보안 사고 여파… 보안 테마주에 뭉칫돈 유입 | 5G부터 AI·핀테크까지… IT서비스 업종에 매수세 몰렸다

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 동아쏘시오홀딩스 (000640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **77.00**
- Error-note adjustment score: **-1.90**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.26**
- Adjusted recommendation score: **63.84**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.40%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes subtracted 1.90 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.26 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [HIT알공]에이프로젠바이오로직스, 에이프로젠 630억 담보 연장 | 동아제약, '제44회 마로니에 여성 백일장' 성료 | 동아쏘시오그룹, 협력사 ESG 관리 역량 강화···공급망 교육 실시

### 2. 삼성SDI (006400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-1.90**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **64.85**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.19%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.90 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼성SDI 3분기 영업익 2575억원 전망…본업 흑자 전환 확인 | 원료부터 소재까지···공급망 재편 나선 K배터리 | "CATL 1GWh 시험선 vs 韓 삼전·에코프로 연합"… 전고체 상용화에 배터...

### 3. KC코트렐 (119650)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **73.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **65.80**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -1. Negative keyword count is 4. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [데이터 뉴스룸] 기계 업체 50곳 매출 하락에 울상…HD건설기계 매출 20... | 9월 4일 개장 전 주요 공시 | 신재생에너지 관련주 장중 혼조…유니테스트 강세

### 4. 아이쓰리시스템 (214430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **87.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.06**
- Adjusted recommendation score: **74.74**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -6.71%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.06 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 잘 나가던 방산株 일제히 조정…우주·드론주는 엇갈려 | 한화에어로스페이스, 우주항공국방 상장기업 2026년 10월 브랜드평판 1위 | 우주항공국방 상장기업 브랜드평판 2026년 10월 빅데이터 분석결과…1위...

### 5. 동부건설 (005960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.55**
- Adjusted recommendation score: **77.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.46%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.55 points. Stock pattern label is weak_historical_reaction.
- Related news examples: HJ중공업과 동부건설 소속 선수들 중에서 살아남는 선수는 누가 될까?..... | 공격 골프로 무장한 김민솔..1점 차 공동 3위 출발 | 리더보드로 돌아온 박현경의 농반진반 “주말 골프가 목표 됐네요”

### 6. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **80.55**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -1.19%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, '향남역 그로브 스위첸' 견본주택 개관 | KCC건설 ‘향남역 그로브 스위첸’ 견본주택, 흥행 열기에 야간 개장 | KCC건설 ‘향남역 그로브 스위첸’ 견본주택 운영시간 연장… 오후 7시...

### 7. KCC건설 (021320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **80.55**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -1.19%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KCC건설, '향남역 그로브 스위첸' 견본주택 개관 | KCC건설 ‘향남역 그로브 스위첸’ 견본주택, 흥행 열기에 야간 개장 | KCC건설 ‘향남역 그로브 스위첸’ 견본주택 운영시간 연장… 오후 7시...

### 8. 파두 (440110)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.67**
- Adjusted recommendation score: **85.13**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -6.72%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.67 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼성전자 영업익 100조원 시대…진짜 수혜주는 따로 있다 | 리사 수와 방한한 AMD 잭 후인, 노타AI 본사도 찾았다 | 파두 주가, 10월 8일 애프터마켓 83,000원 0.85% 상승

### 9. 파두 (440110)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.67**
- Adjusted recommendation score: **85.13**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -6.72%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.67 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼성전자 영업익 100조원 시대…진짜 수혜주는 따로 있다 | 리사 수와 방한한 AMD 잭 후인, 노타AI 본사도 찾았다 | 파두 주가, 10월 8일 애프터마켓 83,000원 0.85% 상승

### 10. 파두 (440110)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.67**
- Adjusted recommendation score: **85.13**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -6.72%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.20 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.67 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼성전자 영업익 100조원 시대…진짜 수혜주는 따로 있다 | 리사 수와 방한한 AMD 잭 후인, 노타AI 본사도 찾았다 | 파두 주가, 10월 8일 애프터마켓 83,000원 0.85% 상승

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
