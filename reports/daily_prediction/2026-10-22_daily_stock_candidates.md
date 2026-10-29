# Daily Stock Candidate Report - 2026-10-22

Generated at: 2026-10-22 01:26:01

ML dataset: `data/processed/ml_dataset_20261022.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
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
| earnings_guidance | 10 | 6 | 66.67% | 1.18% | 8.00 |
| lawsuit | 434 | 313 | 56.23% | -0.77% | 3.00 |
| paid_in_capital_increase | 2233 | 1713 | 57.21% | 0.17% | 3.00 |
| spin_off | 113 | 81 | 50.62% | 1.76% | 2.00 |
| investment_decision | 410 | 295 | 53.22% | -0.24% | 0.00 |
| convertible_bond | 1127 | 795 | 51.82% | 0.89% | 0.00 |
| bonus_issue | 103 | 100 | 42.00% | -0.37% | -3.00 |
| disclosure_violation | 182 | 112 | 43.75% | -0.36% | -3.00 |
| bond_with_warrant | 117 | 105 | 23.81% | 0.47% | -6.00 |
| major_shareholder_change | 2160 | 1527 | 34.91% | -0.64% | -6.00 |
| merger | 419 | 324 | 19.44% | 0.35% | -6.00 |
| supply_contract | 1299 | 973 | 30.83% | -0.67% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2233 | 980 | 733 | 520 | 1.21 |
| lawsuit | 434 | 176 | 137 | 121 | 1.08 |
| convertible_bond | 1127 | 412 | 383 | 332 | 0.81 |
| earnings_guidance | 10 | 4 | 2 | 4 | 0.60 |
| disclosure_violation | 182 | 49 | 63 | 70 | 0.31 |
| investment_decision | 410 | 157 | 138 | 115 | -0.44 |
| spin_off | 113 | 41 | 40 | 32 | -0.66 |
| bond_with_warrant | 117 | 25 | 80 | 12 | -0.98 |
| bonus_issue | 103 | 42 | 58 | 3 | -1.09 |
| supply_contract | 1299 | 300 | 673 | 326 | -1.16 |

## Positive Candidates

### 1. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **148.34**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 3.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.40%
- Next close return data: 6.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [전일 주요공시] 삼성바이오로직스ㆍLS일렉트릭ㆍCJ대한통운ㆍ비나텍 등 | [코스피·코스닥, SK하이닉스 삼성바이오 IPARK현대산업개발 LS마린솔루... | [아주증시포커스]널뛰는 삼전·하이닉스 목표가에 투자자 '혼란'…증권...

### 2. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **148.34**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 3.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.40%
- Next close return data: 6.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [전일 주요공시] 삼성바이오로직스ㆍLS일렉트릭ㆍCJ대한통운ㆍ비나텍 등 | [코스피·코스닥, SK하이닉스 삼성바이오 IPARK현대산업개발 LS마린솔루... | [아주증시포커스]널뛰는 삼전·하이닉스 목표가에 투자자 '혼란'…증권...

### 3. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

### 4. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

### 5. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

### 6. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

### 7. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

### 8. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

### 9. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

### 10. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.90**
- Adjusted recommendation score: **133.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 94.44%, avg next close: 14.50%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 13.94%
- Next close return data: 22.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.90 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터 전력난에 SOFC주 요동…비나텍 주가 '폭등쇼' | 코스피 5,700선 붕괴에도 급등주 속출…엇갈린 증시 | 나스닥 훈풍에도 코스닥 1.07% 하락… 하락 종목 1102개

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 유니테스트 (086390)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.75**
- Adjusted recommendation score: **134.09**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.96%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.88%
- Next close return data: -1.96%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 21일 주식시장 주요공시 | [코스피·코스닥, SK하이닉스 삼성바이오 IPARK현대산업개발 LS마린솔루... | [N2 모닝 경제 브리핑-10월 22일] 美 증시, 스페이스X·슈퍼마이크로 호...

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
