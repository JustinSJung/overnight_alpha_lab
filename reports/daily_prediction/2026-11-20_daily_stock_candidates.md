# Daily Stock Candidate Report - 2026-11-20

Generated at: 2026-11-20 04:02:22

ML dataset: `data/processed/ml_dataset_20261120.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 10 | 10 | 100.00% | 16.52% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 895 | 799 | 45.43% | 5.01% | 4.00 |
| convertible_bond | 1676 | 1343 | 59.57% | 0.17% | 3.00 |
| paid_in_capital_increase | 3012 | 2491 | 56.08% | -0.10% | 3.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| investment_decision | 625 | 510 | 50.78% | 0.22% | 0.00 |
| lawsuit | 645 | 524 | 50.76% | -0.43% | 0.00 |
| disclosure_violation | 228 | 158 | 44.30% | -0.93% | -3.00 |
| bond_with_warrant | 162 | 150 | 42.00% | 0.03% | -3.00 |
| spin_off | 158 | 122 | 39.34% | 0.83% | -3.00 |
| major_shareholder_change | 3286 | 2652 | 37.97% | -0.72% | -3.00 |
| supply_contract | 1910 | 1584 | 35.92% | -0.62% | -3.00 |
| earnings_guidance | 96 | 92 | 26.09% | -1.87% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1676 | 800 | 543 | 333 | 1.41 |
| paid_in_capital_increase | 3012 | 1397 | 1094 | 521 | 1.23 |
| lawsuit | 645 | 266 | 258 | 121 | 0.86 |
| disclosure_violation | 228 | 70 | 88 | 70 | 0.38 |
| bond_with_warrant | 162 | 63 | 87 | 12 | 0.33 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 625 | 259 | 251 | 115 | -0.74 |
| supply_contract | 1910 | 569 | 1015 | 326 | -0.95 |
| merger | 895 | 363 | 436 | 96 | -1.38 |
| earnings_guidance | 96 | 24 | 68 | 4 | -1.54 |

## Positive Candidates

### 1. 씨에스윈드 (112610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.54**
- Adjusted recommendation score: **148.59**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 57.14%, avg next close: -0.70%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -3.01%
- Next close return data: -5.29%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.54 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 19일 주식시장 주요공시 | [이넷뉴스 브랜드평판] 두산에너빌리티, 풍력에너지 상장기업 11월 1위·... | [N2 모닝 경제 브리핑-11월 20일] 美 증시, 다우 5만선 붕괴 ‘검은 목요...

## Volatile Watchlist

### 1. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (합병)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 2. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (합병)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 3. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 4. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 5. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 6. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 7. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (합병)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 8. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (합병)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 9. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (합병)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

### 10. HLB생명과학 (067630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **-1.38**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **8.81**
- Adjusted recommendation score: **78.43**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 88.89%, avg next close: 15.59%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 5.03%
- Next close return data: 17.51%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.38 points. Event-type performance added 4.00 points. Stock-specific history added 8.81 points. Stock pattern label is relatively_positive_history.
- Related news examples: HLB 합병 재추진…매수청구 해제 기준 200억원으로 낮춰 | 제약사 50곳의 현금 성적표…흑자에도 돈이 마른 기업들 | HLB, HLB생명과학 흡수합병 재추진∙∙∙매수청구 200억 원이 성패 가른...

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. HS화성 (002460)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.66**
- Adjusted recommendation score: **90.39**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 15, success rate: 20.00%, avg next close: -0.97%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.03%
- Next close return data: -1.41%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.66 points. Stock pattern label is weak_historical_reaction.
- Related news examples: HS화성, 건설안전관리 평가 최고 등급 'SA1' 획득 | HS화성, '건설안전관리 평가' 950점 획득…최고 등급 'SA1 취득' | 팔레트 찾고 엘리베이터 타는 로봇…삼성물산 'AI 네이티브 건설사' 속...

### 2. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.74**
- Adjusted recommendation score: **104.31**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 23, success rate: 30.43%, avg next close: -2.72%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -5.30%
- Next close return data: -7.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.74 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [카드] 대우건설 "푸르지오에 현대적 한국미를 담다" | 대우건설, 푸르지오 조경 시그니처 '가든 에세이' 개발…하늘·숲·비 담... | 대우건설, 푸르지오 조경 시그니처 공간 개발

### 3. 나노실리칸첨단소재 (286750)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-4.39**
- Adjusted recommendation score: **105.66**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 44.44%, avg next close: -1.97%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.00%
- Next close return data: -0.60%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 4.39 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 화학주도 옥석 가리기…정밀화학 웃고 범용 석유화학은 부진 | 나노실리칸첨단소재, 한-중동 포럼서 의약품 위조방지 성과 공유 | 첨단 보안기술로 중동 보건 재정 1억 달러 절감…나노실리칸첨단소재, ...

### 4. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.65**
- Adjusted recommendation score: **108.40**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.04%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.41%
- Next close return data: -2.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.65 points. Stock pattern label is weak_historical_reaction.
- Related news examples: ‘김건희 어좌’ 사진 공개한 측근 “안 말려놓고…악마화” 주장 | 11월 19일 주식시장 주요공시 | [개장 전 주요 공시] LG유플러스·LG전자·HLB·엘앤에프·CJ CGV 등

### 5. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.65**
- Adjusted recommendation score: **108.40**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.04%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.41%
- Next close return data: -2.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.65 points. Stock pattern label is weak_historical_reaction.
- Related news examples: ‘김건희 어좌’ 사진 공개한 측근 “안 말려놓고…악마화” 주장 | 11월 19일 주식시장 주요공시 | [개장 전 주요 공시] LG유플러스·LG전자·HLB·엘앤에프·CJ CGV 등

### 6. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.65**
- Adjusted recommendation score: **108.40**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.04%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.41%
- Next close return data: -2.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.65 points. Stock pattern label is weak_historical_reaction.
- Related news examples: ‘김건희 어좌’ 사진 공개한 측근 “안 말려놓고…악마화” 주장 | 11월 19일 주식시장 주요공시 | [개장 전 주요 공시] LG유플러스·LG전자·HLB·엘앤에프·CJ CGV 등

### 7. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.65**
- Adjusted recommendation score: **108.40**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.04%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.41%
- Next close return data: -2.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.65 points. Stock pattern label is weak_historical_reaction.
- Related news examples: ‘김건희 어좌’ 사진 공개한 측근 “안 말려놓고…악마화” 주장 | 11월 19일 주식시장 주요공시 | [개장 전 주요 공시] LG유플러스·LG전자·HLB·엘앤에프·CJ CGV 등

### 8. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.65**
- Adjusted recommendation score: **108.40**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.04%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.41%
- Next close return data: -2.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.65 points. Stock pattern label is weak_historical_reaction.
- Related news examples: ‘김건희 어좌’ 사진 공개한 측근 “안 말려놓고…악마화” 주장 | 11월 19일 주식시장 주요공시 | [개장 전 주요 공시] LG유플러스·LG전자·HLB·엘앤에프·CJ CGV 등

### 9. 한국주강 (025890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-8.00**
- Adjusted recommendation score: **112.05**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -1.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.69%
- Next close return data: -2.62%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 8.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [지분View] 한국정밀기계, 하종식 대표 지분 확대 | 11월 19일 주식시장 주요공시 | 한국주강, 25억 계약 종료일 2027년 2월 28일로 연장

### 10. 일성건설 (013360)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-0.95**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.79**
- Adjusted recommendation score: **112.26**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 35.29%, avg next close: -3.04%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.67%
- Next close return data: -4.83%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 0.95 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.79 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 19일 주식시장 주요공시 | [오늘의 증시일정] KB금융·이앤플러스·제넥신 등 | [N2 모닝 경제 브리핑-11월 20일] 美 증시, 다우 5만선 붕괴 ‘검은 목요...

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
