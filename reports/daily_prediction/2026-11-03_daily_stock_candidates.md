# Daily Stock Candidate Report - 2026-11-03

Generated at: 2026-11-03 04:09:34

ML dataset: `data/processed/ml_dataset_20261103.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 248170 | 샘표식품 | 21 | 21 | 100.00% | 27.77% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 754 | 658 | 47.26% | 5.70% | 4.00 |
| convertible_bond | 1350 | 1017 | 57.52% | 0.43% | 3.00 |
| lawsuit | 504 | 383 | 56.14% | -0.48% | 3.00 |
| paid_in_capital_increase | 2555 | 2034 | 57.33% | -0.17% | 3.00 |
| spin_off | 117 | 85 | 51.76% | 1.61% | 2.00 |
| investment_decision | 508 | 393 | 49.87% | -0.13% | 0.00 |
| bond_with_warrant | 145 | 133 | 39.85% | 0.23% | -3.00 |
| bonus_issue | 105 | 102 | 41.18% | -0.58% | -3.00 |
| disclosure_violation | 202 | 132 | 40.15% | -0.26% | -3.00 |
| major_shareholder_change | 2584 | 1951 | 39.47% | -0.76% | -3.00 |
| earnings_guidance | 63 | 59 | 27.12% | 0.28% | -6.00 |
| supply_contract | 1584 | 1258 | 34.42% | -0.65% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2555 | 1166 | 868 | 521 | 1.26 |
| convertible_bond | 1350 | 585 | 432 | 333 | 1.21 |
| lawsuit | 504 | 215 | 168 | 121 | 1.13 |
| bond_with_warrant | 145 | 53 | 80 | 12 | 0.17 |
| disclosure_violation | 202 | 53 | 79 | 70 | 0.14 |
| spin_off | 117 | 44 | 41 | 32 | -0.57 |
| investment_decision | 508 | 196 | 197 | 115 | -0.79 |
| supply_contract | 1584 | 433 | 825 | 326 | -1.03 |
| bonus_issue | 105 | 42 | 60 | 3 | -1.16 |
| earnings_guidance | 63 | 16 | 43 | 4 | -1.16 |

## Positive Candidates

### 1. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **160.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.49**
- Adjusted recommendation score: **151.48**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 19, success rate: 52.63%, avg next close: -2.79%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.06%
- Next close return data: -0.57%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.49 points. Stock pattern label is relatively_positive_history.
- Related news examples: 방산주, 글로벌 국방비 증액 기대…휴니드 주가 폭풍질주 | HJ중공업의 질주···'수빅의 교훈' 속 지속 가능성 시험대 | 美 군함 수주 첫발 뗀 K-조선… 한미 조선협력 물꼬 텄다

### 2. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 3. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 4. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 5. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 6. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 7. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 8. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 9. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

### 10. 녹십자 (006280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **131.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 100.00%, avg next close: 4.07%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.52%
- Next close return data: 4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: GC녹십자웰빙, 의료기기 GMP 공장 착공… "필러·스킨부스터 생산 내재화... | 국민성장펀드, GC녹십자 '차세대 혈액제제' 1700억 저리대출 승인 | 코스피 의약품업종 개인, 3Q 1.1조 순매도 전환…대형주 집중

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 선도전기 (007610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.03**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.54**
- Adjusted recommendation score: **135.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 14.29%, avg next close: -1.13%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.88%
- Next close return data: -5.16%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.03 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.54 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 2일 주식시장 주요공시 | 기업공시 [11월 2일] | 선도전기, 국가철도공단서 63억 철도설비 수주

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
