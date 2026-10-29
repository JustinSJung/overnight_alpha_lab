# Daily Stock Candidate Report - 2026-10-23

Generated at: 2026-10-23 01:25:43

ML dataset: `data/processed/ml_dataset_20261023.csv`

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
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 18 | 18 | 94.44% | 14.50% | relatively_positive_history | 8.90 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 006980 | 우성 | 15 | 9 | 100.00% | 8.46% | relatively_positive_history | 8.60 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 15 | 11 | 81.82% | 2.91% | 8.00 |
| lawsuit | 440 | 319 | 55.17% | -0.62% | 3.00 |
| paid_in_capital_increase | 2272 | 1752 | 57.82% | -0.00% | 3.00 |
| convertible_bond | 1145 | 812 | 51.11% | 1.02% | 2.00 |
| spin_off | 113 | 81 | 50.62% | 1.76% | 2.00 |
| investment_decision | 421 | 306 | 51.96% | -0.24% | 0.00 |
| bonus_issue | 103 | 100 | 42.00% | -0.37% | -3.00 |
| disclosure_violation | 182 | 112 | 43.75% | -0.36% | -3.00 |
| bond_with_warrant | 117 | 105 | 23.81% | 0.47% | -6.00 |
| major_shareholder_change | 2182 | 1549 | 34.93% | -0.65% | -6.00 |
| merger | 447 | 352 | 19.89% | 0.27% | -6.00 |
| supply_contract | 1314 | 988 | 30.57% | -0.70% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 15 | 9 | 2 | 4 | 2.07 |
| paid_in_capital_increase | 2272 | 1013 | 739 | 520 | 1.25 |
| lawsuit | 440 | 176 | 143 | 121 | 1.02 |
| convertible_bond | 1145 | 415 | 397 | 333 | 0.77 |
| disclosure_violation | 182 | 49 | 63 | 70 | 0.31 |
| investment_decision | 421 | 159 | 147 | 115 | -0.56 |
| spin_off | 113 | 41 | 40 | 32 | -0.66 |
| bond_with_warrant | 117 | 25 | 80 | 12 | -0.98 |
| bonus_issue | 103 | 42 | 58 | 3 | -1.09 |
| supply_contract | 1314 | 302 | 686 | 326 | -1.18 |

## Positive Candidates

### 1. 삼성E&A (028050)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **2.07**
- Event-type performance adjustment score: **8.00**
- Stock-specific pattern adjustment score: **1.44**
- Adjusted recommendation score: **125.51**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 50.00%, avg next close: 1.20%, pattern: not_enough_data
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 0.36%
- Next close return data: 4.99%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes added 2.07 points. Event-type performance added 8.00 points. Stock-specific history added 1.44 points. Stock pattern label is not_enough_data.
- Related news examples: 코스피, 메타發 AI 우려 5400선 이탈… 삼전닉스 동반 약세 | 삼성E&A, 깜짝 실적에 증권가 목표가 줄상향…3거래일째 강세[특징주] | NH투자증권, 삼성E&A 목표주가 8만6000원으로 상향…"수주 호조·주주환...

### 2. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.14**
- Adjusted recommendation score: **115.96**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 66.67%, avg next close: 3.11%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.96%
- Next close return data: 2.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.14 points. Stock pattern label is relatively_positive_history.
- Related news examples: 안양시노사민정협의회 산재예방 상생협약 체결 | 계룡건설 새만금 공사 계약액 1115억원으로 늘어 | 올 ‘BIM 어워즈’ 수상작 26점…간삼건축, 비전상 영예 안았다

### 3. 워트 (396470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **109.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.67**
- Adjusted recommendation score: **100.15**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -1.04%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.87%
- Next close return data: -2.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.67 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 22일 주식시장 주요공시 | 수출 실무도 AI로…무협 대경본부, 대구서 'AI 통상 솔루션' 세미나 | 특허 검색에서 기업 업무 전환으로… 워트인텔리전스, LESI에서 'IP-AX' 전...

### 4. 예스티 (122640)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.08**
- Adjusted recommendation score: **97.90**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 4.72%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -3.84%
- Next close return data: -4.51%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.08 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 22일 주식시장 주요공시 | 넥썸, 반도체 냉각유체 관리에서 정밀 온도제어 장비까지 | [코스닥 기관] 코세스·심텍 담고 에코프로·에코프로비엠 팔았다

### 5. 세보엠이씨 (011560)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **89.00**
- Error-note adjustment score: **-1.18**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.30**
- Adjusted recommendation score: **87.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 0.52%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.25%
- Next close return data: -2.25%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.18 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.30 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 22일 주식시장 주요공시 | 세보엠이씨 용인 공사 계약액 2억5588만원 줄어 | [공시] 10월 23일, 코스닥 상장사 80개 종목 자사주 매수 신청

## Volatile Watchlist

### 1. 신풍제약 (019170)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **62.00**
- Error-note adjustment score: **-0.56**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **1.00**
- Adjusted recommendation score: **62.44**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -1.52%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (급성 허혈성 뇌졸중 치료제 SP8203 임상 3상 시험변경계획 승인)
- Next open return data: 9.16%
- Next close return data: 2.32%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.56 points. Event-type performance did not change the score. Stock-specific history added 1.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 제약주 장 초반 상승랠리 뚜렷…삼성바이오로직스·신풍제약이 주도 | 10월 22일 주식시장 주요공시 | 신풍제약 애드마일스, 약국 20여곳 입점…유통망 확대

### 2. 피스피스스튜디오 (0117P0)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.00**
- Adjusted recommendation score: **51.37**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -2.65%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 0.51%
- Next close return data: -2.65%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 피스피스스튜디오, 자회사 월스 흡수합병 결정 | 피스피스스튜디오, 자회사 월스 흡수합병 결정 | 10월 22일 주식시장 주요공시

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 주성코퍼레이션 (109070)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **57.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.79**
- Adjusted recommendation score: **41.58**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 79, success rate: 6.33%, avg next close: -0.19%, pattern: weak_historical_reaction
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 2.56%
- Next close return data: -3.08%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.79 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [개장 시황] 코스피, 하락 출발…대형주들 2~3%대 낙폭 기록 중 | 10월 22일 주식시장 주요공시 | [개장 전 주요 공시] SK하이닉스·대덕·엘리스·교보증권·롯데지주 등

### 2. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 3. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 4. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 5. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 6. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 7. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 8. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 9. IBKS제25호스팩 (0099X0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **61.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.35**
- Adjusted recommendation score: **45.02**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 34, success rate: 5.88%, avg next close: -0.56%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.92%
- Next close return data: -0.92%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 3. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.35 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 22일 주식시장 주요공시 | 스팩으로 IPO 활로 찾는 중소형證…거래 확보 넘어 수익화 과제 | ‘우유 검사 강자’ 셀트릭스, 동물진단·수출로 성장판 넓힌다[상장人...

### 10. 에스엠국일 (078130)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **62.00**
- Error-note adjustment score: **-3.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.29**
- Adjusted recommendation score: **46.08**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 12, success rate: 8.33%, avg next close: -0.04%, pattern: weak_historical_reaction
- Disclosure title: 기타경영사항(자율공시)              (소규모합병 승인 이사회 결의(주주총회 갈음) 결과보고)
- Next open return data: 0.00%
- Next close return data: -0.14%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 3.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.29 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 에스엠국일, ESS 장비 전문 기업 '대진기계' 인수 우선협상대상자 선정 | 10월 22일 주식시장 주요공시 | 에스엠국일, 대진기계 인수 우협 선정..."이차전지 장비사업 진출 추진...

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
