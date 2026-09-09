# Daily Stock Candidate Report - 2026-09-09

Generated at: 2026-09-09 00:53:50

ML dataset: `data/processed/ml_dataset_20260909.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 12 | 12 | 100.00% | 5.43% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 006980 | 우성 | 12 | 6 | 100.00% | 15.55% | relatively_positive_history | 8.50 |
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 288980 | 모아데이타 | 22 | 15 | 86.67% | 3.05% | relatively_positive_history | 8.45 |
| 223310 | 사토시홀딩스 | 53 | 36 | 75.00% | 4.14% | relatively_positive_history | 8.38 |
| 336260 | 두산퓨얼셀 | 7 | 4 | 75.00% | 11.15% | relatively_positive_history | 8.32 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 389260 | 대명에너지 | 4 | 4 | 100.00% | -0.19% | relatively_positive_history | 6.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| lawsuit | 168 | 72 | 73.61% | -0.92% | 6.00 |
| investment_decision | 164 | 63 | 46.03% | 3.31% | 4.00 |
| convertible_bond | 502 | 229 | 61.14% | 0.02% | 3.00 |
| paid_in_capital_increase | 893 | 590 | 63.39% | 0.46% | 3.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| spin_off | 37 | 15 | 40.00% | -0.17% | -3.00 |
| merger | 135 | 57 | 14.04% | 1.34% | -4.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| disclosure_violation | 65 | 15 | 6.67% | 0.68% | -6.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| major_shareholder_change | 1024 | 541 | 27.54% | -0.64% | -6.00 |
| supply_contract | 579 | 317 | 26.18% | -0.89% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 893 | 374 | 216 | 303 | 1.37 |
| lawsuit | 168 | 53 | 19 | 96 | 1.24 |
| convertible_bond | 502 | 140 | 89 | 273 | 0.86 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| disclosure_violation | 65 | 1 | 14 | 50 | -0.57 |
| investment_decision | 164 | 29 | 34 | 101 | -0.57 |
| spin_off | 37 | 6 | 9 | 22 | -0.89 |
| supply_contract | 579 | 83 | 234 | 262 | -1.06 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| major_shareholder_change | 1024 | 149 | 392 | 483 | -1.95 |

## Positive Candidates

### 1. EG (037370)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **128.94**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.93%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 1.10%
- Next close return data: 1.93%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 8일 주식시장 주요공시 | [코스피·코스닥, HMM GS글로벌 한화솔루션 코오롱글로벌 진흥기업 우양... | Mamdani Accuses Former N.Y.C. Leaders of Lying About 9/11 Air Quality

### 2. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.95**
- Adjusted recommendation score: **113.89**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 21, success rate: 100.00%, avg next close: 3.09%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.22%
- Next close return data: 4.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.95 points. Stock pattern label is relatively_positive_history.
- Related news examples: 정기선 HD현대 회장, 필리핀 해군 현대화 협력 | 아시안컵서 겪은 최악의 부진에 팬들은 기대감 제로인데…이영표·설기... | 울산 남구 1521가구 대단지 나온다…'그랑라크 에일린의 뜰' 14일 청약

### 3. 세미파이브 (490470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **103.44**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.76%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.00%
- Next close return data: 2.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 8일 주식시장 주요공시 | [아주증시포커스] 상폐 대신 코넥스 이전 '탈출구'…코스닥 상장사 43곳... | 세미파이브, 삼성 4나노 기반 LLM AI 추론 가속기 '베르다' 첫 대규모 양...

### 4. 코오롱 (002020)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.30**
- Adjusted recommendation score: **103.24**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 85.71%, avg next close: 0.34%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.39%
- Next close return data: 0.59%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.30 points. Stock pattern label is relatively_positive_history.
- Related news examples: 대기업 오너일가 주식가치 331조원…삼성 101조원 최대 | 트리플 역세권·직주근접 갖춘 마곡…주거형 오피스텔 부상 | 신규 공급 뜸한 전주 완산구…'삼천 하늘채 라비엘' 9월 분양

### 5. 대명에너지 (389260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.00**
- Adjusted recommendation score: **97.94**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 100.00%, avg next close: -0.19%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.46%
- Next close return data: 2.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 8일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 9일] 美 증시, 중동 긴장·유가 상승에 3대 지... | [이넷뉴스 브랜드평판] 비에이치아이, 에너지장비 상장기업 9월 1위... 씨...

## Volatile Watchlist

### 1. 대창솔루션 (096350)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **57.00**
- Error-note adjustment score: **-0.57**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **69.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 3.60%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (특허권 취득(보론을 함유하는 스테인리스강 제조 방법))
- Next open return data: 4.86%
- Next close return data: 3.60%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 0.57 points. Event-type performance added 4.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 8일 주식시장 주요공시 | [개장 전 주요 공시] 한화오션·넥사다이내믹스·원풍물산·한화솔루션... | 9월 9일 개장 전 주요 공시

### 2. 대창솔루션 (096350)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **57.00**
- Error-note adjustment score: **-0.57**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **69.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 3.60%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (특허권 취득(보론을 함유하는 스테인리스강 제조 방법))
- Next open return data: 4.86%
- Next close return data: 3.60%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 0.57 points. Event-type performance added 4.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 8일 주식시장 주요공시 | [개장 전 주요 공시] 한화오션·넥사다이내믹스·원풍물산·한화솔루션... | 9월 9일 개장 전 주요 공시

### 3. 대창솔루션 (096350)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **57.00**
- Error-note adjustment score: **-0.57**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **69.43**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 3.60%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (특허권 취득(보론을 함유하는 스테인리스강 제조 방법))
- Next open return data: 4.86%
- Next close return data: 3.60%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 0.57 points. Event-type performance added 4.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 8일 주식시장 주요공시 | [개장 전 주요 공시] 한화오션·넥사다이내믹스·원풍물산·한화솔루션... | 9월 9일 개장 전 주요 공시

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.64**
- Adjusted recommendation score: **46.41**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 22, success rate: 9.09%, avg next close: -0.51%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.21%
- Next close return data: -0.21%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.64 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [게시판] 유안타증권 MEGA센터분당점, 14일 투자설명회 개최 | 유안타증권, MEGA센터분당점 투자설명회 개최 | SK텔레콤, AIDC 확장에 배당 기대까지…"14만원 간다"[애널리스트의 시각...

### 2. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.64**
- Adjusted recommendation score: **46.41**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 22, success rate: 9.09%, avg next close: -0.51%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.21%
- Next close return data: -0.21%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.64 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [게시판] 유안타증권 MEGA센터분당점, 14일 투자설명회 개최 | 유안타증권, MEGA센터분당점 투자설명회 개최 | SK텔레콤, AIDC 확장에 배당 기대까지…"14만원 간다"[애널리스트의 시각...

### 3. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.64**
- Adjusted recommendation score: **46.41**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 22, success rate: 9.09%, avg next close: -0.51%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.21%
- Next close return data: -0.21%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.64 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [게시판] 유안타증권 MEGA센터분당점, 14일 투자설명회 개최 | 유안타증권, MEGA센터분당점 투자설명회 개최 | SK텔레콤, AIDC 확장에 배당 기대까지…"14만원 간다"[애널리스트의 시각...

### 4. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.64**
- Adjusted recommendation score: **46.41**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 22, success rate: 9.09%, avg next close: -0.51%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.21%
- Next close return data: -0.21%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.64 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [게시판] 유안타증권 MEGA센터분당점, 14일 투자설명회 개최 | 유안타증권, MEGA센터분당점 투자설명회 개최 | SK텔레콤, AIDC 확장에 배당 기대까지…"14만원 간다"[애널리스트의 시각...

### 5. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.64**
- Adjusted recommendation score: **46.41**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 22, success rate: 9.09%, avg next close: -0.51%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.21%
- Next close return data: -0.21%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.64 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [게시판] 유안타증권 MEGA센터분당점, 14일 투자설명회 개최 | 유안타증권, MEGA센터분당점 투자설명회 개최 | SK텔레콤, AIDC 확장에 배당 기대까지…"14만원 간다"[애널리스트의 시각...

### 6. 바이오인프라 (199730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-2.24**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **49.26**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -1.21%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 4.93%
- Next close return data: -1.21%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 2.24 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 이재용·구자은·조현준, 프랑스서 AI·전력망 등 첨단산업 협력 모색 | 강원·인천·충북, 국제양자산업대전서 양자바이오 공동관 운영 | 이동석 충주시장, 이장섭 청주시장 누르고 K-브랜드지수 충북 지자체장...

### 7. 바이오인프라 (199730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-2.24**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **49.26**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -1.21%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 4.93%
- Next close return data: -1.21%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 2.24 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 이재용·구자은·조현준, 프랑스서 AI·전력망 등 첨단산업 협력 모색 | 강원·인천·충북, 국제양자산업대전서 양자바이오 공동관 운영 | 이동석 충주시장, 이장섭 청주시장 누르고 K-브랜드지수 충북 지자체장...

### 8. 대신증권 (003540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.94**
- Adjusted recommendation score: **51.11**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.45%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.38%
- Next close return data: 1.13%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [모닝 리포트] "티엘비, 올 3분기 호실적 예상…소캠2 수혜 본격화" | "계좌 개설하고 거래하면 6만원"…대신증권, 크레온 신규 고객 이벤트 | 대신증권 "심텍, 하반기 영업익 122% 증가.. 반도체 기판 최선호주"

### 9. 대신증권 (003540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.94**
- Adjusted recommendation score: **51.11**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.45%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.38%
- Next close return data: 1.13%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [모닝 리포트] "티엘비, 올 3분기 호실적 예상…소캠2 수혜 본격화" | "계좌 개설하고 거래하면 6만원"…대신증권, 크레온 신규 고객 이벤트 | 대신증권 "심텍, 하반기 영업익 122% 증가.. 반도체 기판 최선호주"

### 10. 대신증권 (003540)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.95**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.94**
- Adjusted recommendation score: **51.11**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.45%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.38%
- Next close return data: 1.13%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.95 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [모닝 리포트] "티엘비, 올 3분기 호실적 예상…소캠2 수혜 본격화" | "계좌 개설하고 거래하면 6만원"…대신증권, 크레온 신규 고객 이벤트 | 대신증권 "심텍, 하반기 영업익 122% 증가.. 반도체 기판 최선호주"

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
