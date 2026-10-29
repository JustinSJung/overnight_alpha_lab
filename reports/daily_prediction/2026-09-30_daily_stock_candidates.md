# Daily Stock Candidate Report - 2026-09-30

Generated at: 2026-09-30 02:55:44

ML dataset: `data/processed/ml_dataset_20260930.csv`

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
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |
| 290690 | 아리바이오홀딩스 | 20 | 20 | 80.00% | 7.78% | relatively_positive_history | 8.54 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| bonus_issue | 77 | 74 | 55.41% | 0.75% | 3.00 |
| lawsuit | 335 | 222 | 57.21% | -0.47% | 3.00 |
| paid_in_capital_increase | 1610 | 1239 | 56.34% | 0.46% | 3.00 |
| convertible_bond | 863 | 575 | 52.35% | 0.80% | 0.00 |
| disclosure_violation | 127 | 72 | 52.78% | -0.17% | 0.00 |
| investment_decision | 344 | 238 | 51.26% | 0.28% | 0.00 |
| merger | 246 | 166 | 24.70% | 1.46% | -4.00 |
| bond_with_warrant | 74 | 63 | 9.52% | 0.01% | -6.00 |
| major_shareholder_change | 1623 | 1084 | 32.93% | -0.92% | -6.00 |
| spin_off | 75 | 51 | 31.37% | 0.56% | -6.00 |
| supply_contract | 931 | 653 | 29.40% | -0.65% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1610 | 698 | 541 | 371 | 1.16 |
| lawsuit | 335 | 127 | 95 | 113 | 1.04 |
| convertible_bond | 863 | 301 | 274 | 288 | 0.79 |
| disclosure_violation | 127 | 38 | 34 | 55 | 0.69 |
| bonus_issue | 77 | 41 | 33 | 3 | 0.03 |
| investment_decision | 344 | 122 | 116 | 106 | -0.59 |
| supply_contract | 931 | 192 | 461 | 278 | -1.21 |
| bond_with_warrant | 74 | 6 | 57 | 11 | -1.91 |
| major_shareholder_change | 1623 | 357 | 727 | 539 | -2.04 |

## Positive Candidates

### 1. 세아제강 (306200)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **160.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **158.29**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 4.78%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 7.17%
- Next close return data: 4.78%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주] 美 알래스카 LNG 투자 기대에 강관주 강세 | 美 50% 고관세 불구 한국산 철강수출 52% 증가 | [특징주] 금강철강, 알래스카 LNG 사업 투자 기대감에 급등세

### 2. 피델릭스 (032580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **152.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.06**
- Adjusted recommendation score: **144.85**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.06%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.42%
- Next close return data: 2.07%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history added 0.06 points. Stock pattern label is not_enough_data.
- Related news examples: 9월 29일 주식시장 주요공시 | [N2 모닝 경제 브리핑-9월 30일] 美 증시, 장기금리 급등에 일제히 하락... | 피델릭스, 190억 규모 메모리반도체 공급계약

### 3. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

### 4. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

### 5. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

### 6. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

### 7. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

### 8. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

### 9. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

### 10. 프로티아 (303360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **0.03**
- Event-type performance adjustment score: **3.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **142.53**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 1.73%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (무상증자)
- Next open return data: 0.00%
- Next close return data: 1.73%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes added 0.03 points. Event-type performance added 3.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 29일 주식시장 주요공시 | [전일 주요공시] SK온·한미반도체·삼성전기 등 | [코스피·코스닥, SK온 셀트리온 삼성전기 셀비온 한미반도체한국가스공...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 세아제강지주 (003030)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **162.00**
- Error-note adjustment score: **-1.21**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.00**
- Adjusted recommendation score: **150.79**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 25.00%, avg next close: 1.10%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 9.19%
- Next close return data: 8.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Negative keyword count is 1. Historical error notes subtracted 1.21 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주] TCC 스틸, 알래스카 LNG사업 발표 소식에 기대…14%대 강세 | [특징주] 트럼프, 韓 알래스카 LNG 투자 발표 가능성…강관·철강株 급등 | [특징주] 세아제강, 알래스카 LNG 사업 수혜 기대감에 7%대 급등

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
