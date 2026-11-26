# Daily Stock Candidate Report - 2026-11-26

Generated at: 2026-11-26 05:02:13

ML dataset: `data/processed/ml_dataset_20261126.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 10 | 10 | 100.00% | 16.52% | relatively_positive_history | 9.00 |
| 010170 | 대한광통신 | 45 | 45 | 100.00% | 3.06% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 1008 | 912 | 51.10% | 4.76% | 4.00 |
| convertible_bond | 1721 | 1388 | 59.87% | 0.15% | 3.00 |
| paid_in_capital_increase | 3189 | 2668 | 56.15% | -0.23% | 3.00 |
| bonus_issue | 132 | 129 | 52.71% | 0.58% | 0.00 |
| investment_decision | 667 | 552 | 51.09% | 0.19% | 0.00 |
| lawsuit | 679 | 558 | 51.61% | -0.43% | 0.00 |
| disclosure_violation | 233 | 163 | 42.94% | -0.80% | -3.00 |
| bond_with_warrant | 163 | 151 | 41.72% | 0.04% | -3.00 |
| spin_off | 159 | 123 | 39.02% | 0.81% | -3.00 |
| major_shareholder_change | 3453 | 2819 | 39.94% | -0.77% | -3.00 |
| supply_contract | 2030 | 1704 | 36.27% | -0.63% | -3.00 |
| earnings_guidance | 100 | 96 | 29.17% | -1.54% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1721 | 831 | 557 | 333 | 1.44 |
| paid_in_capital_increase | 3189 | 1498 | 1170 | 521 | 1.25 |
| lawsuit | 679 | 288 | 270 | 121 | 0.93 |
| bond_with_warrant | 163 | 63 | 88 | 12 | 0.31 |
| disclosure_violation | 233 | 70 | 93 | 70 | 0.30 |
| bonus_issue | 132 | 68 | 61 | 3 | 0.04 |
| investment_decision | 667 | 282 | 270 | 115 | -0.72 |
| merger | 1008 | 466 | 446 | 96 | -0.79 |
| supply_contract | 2030 | 618 | 1086 | 326 | -0.97 |
| earnings_guidance | 100 | 28 | 68 | 4 | -1.28 |

## Positive Candidates

### 1. 로체시스템즈 (071280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **146.53**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 5.99%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 5.73%
- Next close return data: 5.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 25일 주식시장 주요공시 | [박정식의 국내 주식시황] 엔비디아 신용등급 강등 경고·美 관세 압박…... | [개장 전 주요 공시] SK하이닉스·삼성전기·한국전력공사·아시아나항...

### 2. 나라스페이스테크놀로지 (478340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **8.38**
- Adjusted recommendation score: **136.41**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 3.85%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 6.20%
- Next close return data: 14.46%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 8.38 points. Stock pattern label is relatively_positive_history.
- Related news examples: 하나에어로·나노팀 30% 안팎 급등…코스닥 종목 강세 | [ET특징주] 나라스페이스테크놀로지, 수자원공사와 101억 규모 공급 계약... | “반도체 인재, 대학원 아닌 취업 선택…이러다 일본 전철”

### 3. 지엔씨에너지 (119850)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.12**
- Adjusted recommendation score: **130.15**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 2.97%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 5.34%
- Next close return data: 12.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.12 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 25일 주식시장 주요공시 | [전일 주요공시] SK하이닉스ㆍLG화학ㆍ현대건설ㆍ삼성전기 등 | [이넷뉴스 브랜드평판] HD현대일렉트릭, 전기장비 상장기업 11월 1위... ...

### 4. 지엔씨에너지 (119850)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.12**
- Adjusted recommendation score: **130.15**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 2.97%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 5.34%
- Next close return data: 12.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.12 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 25일 주식시장 주요공시 | [전일 주요공시] SK하이닉스ㆍLG화학ㆍ현대건설ㆍ삼성전기 등 | [이넷뉴스 브랜드평판] HD현대일렉트릭, 전기장비 상장기업 11월 1위... ...

### 5. 서진시스템 (178320)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.86**
- Adjusted recommendation score: **129.89**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 96, success rate: 67.71%, avg next close: -2.08%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.75%
- Next close return data: 0.18%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.86 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터·6G·위성망 투자 삼박자 맞았다…센서뷰·RFHIC·인텔리안... | AI·차세대 망 투자가 불 지폈다…센서뷰·AP위성·RFHIC 주가 기세등등 | [특징주] 엘티씨, 고체산화물 연료전지(SOFC) 테마 강세에 15%대 급등

### 6. 대성하이텍 (129920)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.64**
- Adjusted recommendation score: **126.67**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 85.71%, avg next close: -0.67%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 5.55%
- Next close return data: 12.34%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.64 points. Stock pattern label is relatively_positive_history.
- Related news examples: 대성하이텍 주가, 급등세... 왜? | [특징주] 대성하이텍, 반도체·로봇 모멘텀에 매수세 유입…정밀기계·... | [N2 증시 풍향계] 반도체·2차전지주 동반 반등…스페이스X·보안 테마도...

### 7. 액트로 (290740)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.04**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **119.54**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 2.77%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 5.86%
- Next close return data: 2.77%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes added 0.04 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 25일 주식시장 주요공시 | [전일 주요공시] SK하이닉스ㆍLG화학ㆍ현대건설ㆍ삼성전기 등 | [코스피·코스닥,현대건설 한화오션 카카오뱅크로체시스템즈 삼성전기...

### 8. 액트로 (290740)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.04**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **119.54**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 2.77%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 5.86%
- Next close return data: 2.77%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes added 0.04 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 25일 주식시장 주요공시 | [전일 주요공시] SK하이닉스ㆍLG화학ㆍ현대건설ㆍ삼성전기 등 | [코스피·코스닥,현대건설 한화오션 카카오뱅크로체시스템즈 삼성전기...

### 9. 액트로 (290740)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.04**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **119.54**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 2.77%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 5.86%
- Next close return data: 2.77%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes added 0.04 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 25일 주식시장 주요공시 | [전일 주요공시] SK하이닉스ㆍLG화학ㆍ현대건설ㆍ삼성전기 등 | [코스피·코스닥,현대건설 한화오션 카카오뱅크로체시스템즈 삼성전기...

### 10. 액트로 (290740)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **0.04**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **119.54**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 2.77%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(무상증자결정)
- Next open return data: 5.86%
- Next close return data: 2.77%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes added 0.04 points. Event-type performance did not change the score. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 25일 주식시장 주요공시 | [전일 주요공시] SK하이닉스ㆍLG화학ㆍ현대건설ㆍ삼성전기 등 | [코스피·코스닥,현대건설 한화오션 카카오뱅크로체시스템즈 삼성전기...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. STX엔진 (077970)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **133.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.25**
- Adjusted recommendation score: **128.78**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.87%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 3.75%
- Next close return data: 0.94%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 4. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.25 points. Stock pattern label is not_enough_data.
- Related news examples: 페로타임즈 손바닥뉴스 11월26일(목) | 11월 25일 주식시장 주요공시 | 경남 내년 조선업 전망 '매우 맑음'

### 2. 네오셈 (253590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-0.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.18**
- Adjusted recommendation score: **138.85**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 5.56%, avg next close: -1.53%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 5.01%
- Next close return data: 5.11%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 0.97 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.18 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 25일 주식시장 주요공시 | [코스피·코스닥,현대건설 한화오션 카카오뱅크로체시스템즈 삼성전기... | [N2 모닝 경제 브리핑-11월 26일] 美 증시, 물가 충격에 반도체주 또 ‘...

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
