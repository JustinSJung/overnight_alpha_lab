# Daily Stock Candidate Report - 2026-09-29

Generated at: 2026-09-29 03:32:23

ML dataset: `data/processed/ml_dataset_20260929.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |
| 003060 | 에이프로젠바이오로직스 | 16 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.08 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 318 | 205 | 55.12% | -0.51% | 3.00 |
| paid_in_capital_increase | 1569 | 1198 | 57.10% | 0.45% | 3.00 |
| bonus_issue | 65 | 62 | 46.77% | 0.56% | 0.00 |
| convertible_bond | 858 | 570 | 52.28% | 0.81% | 0.00 |
| disclosure_violation | 126 | 71 | 53.52% | -0.17% | 0.00 |
| investment_decision | 333 | 227 | 52.86% | 0.31% | 0.00 |
| bond_with_warrant | 74 | 63 | 9.52% | 0.01% | -6.00 |
| major_shareholder_change | 1584 | 1045 | 33.21% | -0.98% | -6.00 |
| merger | 200 | 120 | 20.83% | 0.81% | -6.00 |
| spin_off | 73 | 49 | 30.61% | 0.30% | -6.00 |
| supply_contract | 899 | 621 | 28.18% | -0.71% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1569 | 684 | 514 | 371 | 1.20 |
| lawsuit | 318 | 113 | 92 | 113 | 0.91 |
| convertible_bond | 858 | 298 | 272 | 288 | 0.79 |
| disclosure_violation | 126 | 38 | 33 | 55 | 0.72 |
| investment_decision | 333 | 120 | 107 | 106 | -0.45 |
| bonus_issue | 65 | 29 | 33 | 3 | -0.89 |
| supply_contract | 899 | 175 | 446 | 278 | -1.27 |
| bond_with_warrant | 74 | 6 | 57 | 11 | -1.91 |
| major_shareholder_change | 1584 | 347 | 698 | 539 | -1.99 |

## Positive Candidates

### 1. 테라뷰 (950250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **148.23**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 27.22%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.90%
- Next close return data: 27.22%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주] 테라뷰, 美 기업과 14억 규모 반도체 검사장비 공급계약에 24%... | 테라뷰 주가, 9월 29일 장중 4,180원 24.78% 상승 | 테라뷰 주가, 급등세... 왜?

### 2. RF머트리얼즈 (327260)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **135.23**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 8.68%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.22%
- Next close return data: 8.68%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 29일] 美 증시, 금리·유가 급등에 일제히 하... | [코스닥 기관] 파두·에코프로비엠· 솔브레인· ISC· 올릭스 쓸어 담았...

### 3. SFA넥셀 (222080)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.12**
- Adjusted recommendation score: **129.85**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.48%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.18%
- Next close return data: -3.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: 9월 28일 주식시장 주요공시 | ESS·배터리 공급망 다변화 기대…전기차 관련주 동반 상승랠리 | AI 시대 전력저장 뜬다… ESS 관련주 장중 상승세 확산

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 2. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 3. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 4. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 5. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 6. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 7. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 8. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 9. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

### 10. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.27**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **122.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 0.00%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.23%
- Next close return data: -0.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.27 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 28일 주식시장 주요공시 | 삼성·SK HBM 증설 본격화…후공정 생태계 수혜 주목 | [특징주] 엑시콘, AI 서버 확대와 CXL 2.0 테스터 양산 공급 기대감에 급...

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
