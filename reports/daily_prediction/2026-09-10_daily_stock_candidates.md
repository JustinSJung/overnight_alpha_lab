# Daily Stock Candidate Report - 2026-09-10

Generated at: 2026-09-10 00:54:35

ML dataset: `data/processed/ml_dataset_20260910.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 12 | 12 | 100.00% | 5.43% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 14 | 9 | 100.00% | 7.29% | relatively_positive_history | 8.64 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 223310 | 사토시홀딩스 | 53 | 36 | 75.00% | 4.14% | relatively_positive_history | 8.38 |
| 336260 | 두산퓨얼셀 | 7 | 4 | 75.00% | 11.15% | relatively_positive_history | 8.32 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 288980 | 모아데이타 | 24 | 17 | 88.24% | 2.16% | relatively_positive_history | 7.00 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 006840 | AK홀딩스 | 3 | 3 | 100.00% | -0.53% | relatively_positive_history | 6.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 541 | 268 | 55.22% | 2.73% | 5.00 |
| lawsuit | 188 | 91 | 79.12% | -2.70% | 4.00 |
| investment_decision | 196 | 95 | 62.11% | -0.63% | 3.00 |
| paid_in_capital_increase | 942 | 639 | 63.38% | 0.66% | 3.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 65 | 15 | 6.67% | 0.68% | -6.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| major_shareholder_change | 1058 | 575 | 27.65% | -0.64% | -6.00 |
| merger | 149 | 71 | 14.08% | 0.69% | -6.00 |
| spin_off | 54 | 32 | 21.88% | -0.22% | -6.00 |
| supply_contract | 602 | 340 | 26.47% | -0.87% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| lawsuit | 188 | 72 | 19 | 97 | 1.61 |
| paid_in_capital_increase | 942 | 405 | 234 | 303 | 1.40 |
| convertible_bond | 541 | 148 | 120 | 273 | 0.70 |
| investment_decision | 196 | 59 | 36 | 101 | 0.22 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| disclosure_violation | 65 | 1 | 14 | 50 | -0.57 |
| supply_contract | 602 | 90 | 250 | 262 | -1.05 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 1058 | 159 | 416 | 483 | -2.00 |
| merger | 149 | 10 | 61 | 78 | -2.53 |

## Positive Candidates

### 1. 인텍플러스 (064290)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **147.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.25**
- Adjusted recommendation score: **141.20**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 2.82%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.67%
- Next close return data: 7.68%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Negative keyword count is 1. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.25 points. Stock pattern label is not_enough_data.
- Related news examples: [코스피·코스닥,대우건설 코스메카코리아 샘표 넥사다이내믹스 유진테... | [N2 모닝 경제 브리핑-9월 10일] 美 증시, 유가·국채금리 상승에 일제히... | [주요공시] 코스메카코리아, 넥사다이내믹스, 신세계, 한국가스공사, 금...

### 2. 에이디테크놀로지 (200710)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **128.95**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.81%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.62%
- Next close return data: 1.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 메모리·비메모리 다 잡는다... SFA반도체, AI 반도체 물량 증가로 턴어... | AI 서버에서 단말기로 확산… 온디바이스 AI 관련주 화색도네 | 온디바이스 AI 인프라 확산…에이디테크놀로지, 시스템반도체 수주 확대...

### 3. 금양그린파워 (282720)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.17**
- Adjusted recommendation score: **127.78**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.60%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 0.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.17 points. Stock pattern label is not_enough_data.
- Related news examples: 버려지는 태양광 전력 잡는다... HD현대에너지솔루션, 고효율 ESS 융합 기... | 해저케이블부터 전력기기까지... LS, 글로벌 신재생 에너지 수주 모멘텀... | 빅테크도 원전 전력 확보 나선다…원자력발전 관련주에 매수 유입 '촉각...

### 4. 일양약품 (007570)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.00**
- Adjusted recommendation score: **118.95**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.36%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약해지              
- Next open return data: 0.97%
- Next close return data: 0.36%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주요공시] 코스메카코리아, 넥사다이내믹스, 신세계, 한국가스공사, 금... | [9월10일자] 비즈니스포스트 아침의 주요기사 | [HIT알공] '상폐 위기' 이오플로우, 거래소에 이의신청

### 5. HEM파마 (376270)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.06**
- Adjusted recommendation score: **103.01**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.64%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.34%
- Next close return data: 0.14%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.06 points. Stock pattern label is not_enough_data.
- Related news examples: 마이크로바이옴 '확장' 택한 HEM파마…사업화 승부수 | [주식] 국내 신약 44호 허가됐는데...지엘팜텍 14%↓ | [의료기기업계 소식] 9월 9일

### 6. 특수건설 (026150)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **88.57**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -1.85%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -1.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 지중선 파손에 정전 피해…책임공방·보상 지연에 아파트 주민 반발 | 지중선 파손에 정전피해…책임공방·보상지연에 아파트주민 반발 | 5G-R 시대까지 잇는다... 우리넷, 공공 통신 인프라 시장서 존재감 부각

## Volatile Watchlist

### 1. 보로노이 (310210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.22**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **4.31**
- Adjusted recommendation score: **47.53**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 13, success rate: 92.31%, avg next close: -2.95%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획자진취하등)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: -4.65%
- Next close return data: -3.03%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes added 0.22 points. Event-type performance added 3.00 points. Stock-specific history added 4.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, CMO에 '30조·M&A' 조건 스톡옵션 부여 | 보로노이, CMO에 258억 옵션…기업가치 30조 조건 | 보로노이, CMO에 조건부 스톡옵션…“기업가치 30조·경영권 변동 연계...

### 2. 보로노이 (310210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.22**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **4.31**
- Adjusted recommendation score: **47.53**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 13, success rate: 92.31%, avg next close: -2.95%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획자진취하등)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: -4.65%
- Next close return data: -3.03%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes added 0.22 points. Event-type performance added 3.00 points. Stock-specific history added 4.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, CMO에 '30조·M&A' 조건 스톡옵션 부여 | 보로노이, CMO에 258억 옵션…기업가치 30조 조건 | 보로노이, CMO에 조건부 스톡옵션…“기업가치 30조·경영권 변동 연계...

### 3. 보로노이 (310210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.22**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **4.31**
- Adjusted recommendation score: **47.53**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 13, success rate: 92.31%, avg next close: -2.95%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획자진취하등)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: -4.65%
- Next close return data: -3.03%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes added 0.22 points. Event-type performance added 3.00 points. Stock-specific history added 4.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, CMO에 '30조·M&A' 조건 스톡옵션 부여 | 보로노이, CMO에 258억 옵션…기업가치 30조 조건 | 보로노이, CMO에 조건부 스톡옵션…“기업가치 30조·경영권 변동 연계...

### 4. 보로노이 (310210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.22**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **4.31**
- Adjusted recommendation score: **47.53**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 13, success rate: 92.31%, avg next close: -2.95%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(임상시험계획자진취하등)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: -4.65%
- Next close return data: -3.03%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes added 0.22 points. Event-type performance added 3.00 points. Stock-specific history added 4.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, CMO에 '30조·M&A' 조건 스톡옵션 부여 | 보로노이, CMO에 258억 옵션…기업가치 30조 조건 | 보로노이, CMO에 조건부 스톡옵션…“기업가치 30조·경영권 변동 연계...

### 5. 보로노이 (310210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.22**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **4.31**
- Adjusted recommendation score: **47.53**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 13, success rate: 92.31%, avg next close: -2.95%, pattern: relatively_positive_history
- Disclosure title: [기재정정]투자판단관련주요경영사항(임상시험계획변경승인신청)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: -4.65%
- Next close return data: -3.03%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes added 0.22 points. Event-type performance added 3.00 points. Stock-specific history added 4.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, CMO에 '30조·M&A' 조건 스톡옵션 부여 | 보로노이, CMO에 258억 옵션…기업가치 30조 조건 | 보로노이, CMO에 조건부 스톡옵션…“기업가치 30조·경영권 변동 연계...

### 6. 보로노이 (310210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.22**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **4.31**
- Adjusted recommendation score: **47.53**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 13, success rate: 92.31%, avg next close: -2.95%, pattern: relatively_positive_history
- Disclosure title: [기재정정]투자판단관련주요경영사항(임상시험계획변경승인신청)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: -4.65%
- Next close return data: -3.03%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes added 0.22 points. Event-type performance added 3.00 points. Stock-specific history added 4.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, CMO에 '30조·M&A' 조건 스톡옵션 부여 | 보로노이, CMO에 258억 옵션…기업가치 30조 조건 | 보로노이, CMO에 조건부 스톡옵션…“기업가치 30조·경영권 변동 연계...

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 한화오션 (042660)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **0.22**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **-2.62**
- Adjusted recommendation score: **60.60**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 10, success rate: 40.00%, avg next close: -0.38%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: -1.93%
- Next close return data: -1.70%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes added 0.22 points. Event-type performance added 3.00 points. Stock-specific history subtracted 2.62 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 거제시의회, '양대 조선소 설계인력 부산 확대 재검토 결의안' | 현대엔지니어링, '힐스테이트 거제시그니처' 10월 공급...1963가구 규모 | 거제 최대규모 랜드마크 단지, '힐스테이트 거제시그니처'가 주목받는 ...

### 2. 까뮤이앤씨 (013700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.94**
- Adjusted recommendation score: **79.01**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 14, success rate: 0.00%, avg next close: 0.07%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -0.18%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [건설 인당 생산성] 까뮤이앤씨, 직원보다 더 높았던 '매출 증가율' | 건설업계 안전불감증 '여전'…더 강한 규제 나오나 | [더벨][Company Watch] 'PC 전문' 까뮤이앤씨, SK하이닉스향 수주 릴레이

### 3. 현대건설 (000720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **85.70**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -2.86%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.37%
- Next close return data: -3.89%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [굿모닝! 9일 건설업계 소식] 대우건설·IPARK현대산업개발·BS그룹·현대... | 현대건설, 평택 '힐스테이트 고덕엘리스트' 9월 분양 | 한화 건설부문, 도시정비 수주 질주…'포레나' 외연 넓힌다

### 4. SG (255220)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.70**
- Adjusted recommendation score: **90.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 26, success rate: 0.00%, avg next close: 3.66%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.49%
- Next close return data: -0.25%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.70 points. Stock pattern label is weak_historical_reaction.
- Related news examples: SG워너비 김진호, 1년 9개월 만에 단독 공연 '할머니가 손주의 찢어진 옷... | SG워너비 김진호, 단독 콘서트 개최…팬들과 만남 | SG워너비 김진호, 1년 9개월 만에 단독 공연…10월 서울서 개최

### 5. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.60**
- Adjusted recommendation score: **94.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -3.01%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.83%
- Next close return data: -2.47%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대우건설, 164개 혁신기술 평가해 스타트업 9곳과 스마트건설 협업 | 대우건설, 스타트업 협업 확대… AI·로봇 등 스마트건설기술 발굴 | 대우건설 '오픈 이노베이션 데이'…스타트업과 협업 본격화

### 6. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.60**
- Adjusted recommendation score: **94.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -3.01%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.83%
- Next close return data: -2.47%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대우건설, 164개 혁신기술 평가해 스타트업 9곳과 스마트건설 협업 | 대우건설, 스타트업 협업 확대… AI·로봇 등 스마트건설기술 발굴 | 대우건설 '오픈 이노베이션 데이'…스타트업과 협업 본격화

### 7. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.60**
- Adjusted recommendation score: **94.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -3.01%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.83%
- Next close return data: -2.47%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대우건설, 164개 혁신기술 평가해 스타트업 9곳과 스마트건설 협업 | 대우건설, 스타트업 협업 확대… AI·로봇 등 스마트건설기술 발굴 | 대우건설 '오픈 이노베이션 데이'…스타트업과 협업 본격화

### 8. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.60**
- Adjusted recommendation score: **94.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -3.01%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.83%
- Next close return data: -2.47%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대우건설, 164개 혁신기술 평가해 스타트업 9곳과 스마트건설 협업 | 대우건설, 스타트업 협업 확대… AI·로봇 등 스마트건설기술 발굴 | 대우건설 '오픈 이노베이션 데이'…스타트업과 협업 본격화

### 9. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.60**
- Adjusted recommendation score: **94.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -3.01%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.83%
- Next close return data: -2.47%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대우건설, 164개 혁신기술 평가해 스타트업 9곳과 스마트건설 협업 | 대우건설, 스타트업 협업 확대… AI·로봇 등 스마트건설기술 발굴 | 대우건설 '오픈 이노베이션 데이'…스타트업과 협업 본격화

### 10. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.05**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.60**
- Adjusted recommendation score: **94.35**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -3.01%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -2.83%
- Next close return data: -2.47%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.05 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 대우건설, 164개 혁신기술 평가해 스타트업 9곳과 스마트건설 협업 | 대우건설, 스타트업 협업 확대… AI·로봇 등 스마트건설기술 발굴 | 대우건설 '오픈 이노베이션 데이'…스타트업과 협업 본격화

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
