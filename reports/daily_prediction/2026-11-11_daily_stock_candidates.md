# Daily Stock Candidate Report - 2026-11-11

Generated at: 2026-11-11 06:03:14

ML dataset: `data/processed/ml_dataset_20261111.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 248170 | 샘표식품 | 21 | 21 | 100.00% | 27.77% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1502 | 1169 | 57.74% | 0.35% | 3.00 |
| paid_in_capital_increase | 2819 | 2298 | 56.14% | -0.18% | 3.00 |
| merger | 821 | 725 | 43.86% | 5.15% | 1.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| investment_decision | 575 | 460 | 52.17% | 0.25% | 0.00 |
| lawsuit | 576 | 455 | 51.87% | -0.46% | 0.00 |
| disclosure_violation | 212 | 142 | 40.85% | -0.31% | -3.00 |
| bond_with_warrant | 146 | 134 | 40.30% | 0.21% | -3.00 |
| spin_off | 152 | 116 | 37.93% | 0.98% | -3.00 |
| major_shareholder_change | 2892 | 2258 | 39.95% | -0.81% | -3.00 |
| supply_contract | 1729 | 1403 | 35.85% | -0.64% | -3.00 |
| earnings_guidance | 68 | 64 | 25.00% | -0.17% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1502 | 675 | 494 | 333 | 1.26 |
| paid_in_capital_increase | 2819 | 1290 | 1008 | 521 | 1.22 |
| lawsuit | 576 | 236 | 219 | 121 | 0.91 |
| bond_with_warrant | 146 | 54 | 80 | 12 | 0.21 |
| disclosure_violation | 212 | 58 | 84 | 70 | 0.18 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 575 | 240 | 220 | 115 | -0.59 |
| supply_contract | 1729 | 503 | 900 | 326 | -0.94 |
| earnings_guidance | 68 | 16 | 48 | 4 | -1.41 |
| merger | 821 | 318 | 407 | 96 | -1.53 |

## Positive Candidates

### 1. 케이씨텍 (281820)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **146.56**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 12.32%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.79%
- Next close return data: 12.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 반도체 소재·부품주 매수세 봇물…HBM 공정 고도화 기대 커졌다 | 글로벌 반도체 설비 투자 확대…반도체 장비 관련주 무더기 '휘파람' | 11월 10일 주식시장 주요공시

### 2. 플리토 (300080)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.61**
- Adjusted recommendation score: **127.67**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: -0.58%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.78%
- Next close return data: 0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.61 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 10일 주식시장 주요공시 | 플리토 AI 데이터 계약액 193억원으로 정정 | "출판물 무단 학습 안 된다"…출협, AI 기업 5곳과 맞손

### 3. 플리토 (300080)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.61**
- Adjusted recommendation score: **127.67**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: -0.58%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.78%
- Next close return data: 0.65%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.61 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 10일 주식시장 주요공시 | 플리토 AI 데이터 계약액 193억원으로 정정 | "출판물 무단 학습 안 된다"…출협, AI 기업 5곳과 맞손

### 4. 지엠비코리아 (013870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.00**
- Adjusted recommendation score: **124.06**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 100.00%, avg next close: 0.30%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 0.40%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 10일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 11일] 美 증시, 물가 쇼크에 3대 지수 일제히... | 동남권 주력산업 업체 시총 저평가…기업가치 제고 ‘험로’

### 5. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.26**
- Adjusted recommendation score: **114.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 64.29%, avg next close: -1.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.63%
- Next close return data: 0.72%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.26 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 부산 벡스코 제3전시장 838억원 공사계약 체결 | HD현대중공업·HD한국조선해양 2%대 하락…미국·이란 전쟁 변수 속 조선... | [유캐스트 IPO] 기술은 軍에서, 돈은 民에서…2년래 이익률 40% 승부

### 6. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.26**
- Adjusted recommendation score: **114.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 64.29%, avg next close: -1.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.63%
- Next close return data: 0.72%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.26 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 부산 벡스코 제3전시장 838억원 공사계약 체결 | HD현대중공업·HD한국조선해양 2%대 하락…미국·이란 전쟁 변수 속 조선... | [유캐스트 IPO] 기술은 軍에서, 돈은 民에서…2년래 이익률 40% 승부

### 7. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.26**
- Adjusted recommendation score: **114.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 64.29%, avg next close: -1.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.63%
- Next close return data: 0.72%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.26 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 부산 벡스코 제3전시장 838억원 공사계약 체결 | HD현대중공업·HD한국조선해양 2%대 하락…미국·이란 전쟁 변수 속 조선... | [유캐스트 IPO] 기술은 軍에서, 돈은 民에서…2년래 이익률 40% 승부

### 8. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.26**
- Adjusted recommendation score: **114.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 64.29%, avg next close: -1.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.63%
- Next close return data: 0.72%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.26 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 부산 벡스코 제3전시장 838억원 공사계약 체결 | HD현대중공업·HD한국조선해양 2%대 하락…미국·이란 전쟁 변수 속 조선... | [유캐스트 IPO] 기술은 軍에서, 돈은 民에서…2년래 이익률 40% 승부

### 9. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.26**
- Adjusted recommendation score: **114.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 64.29%, avg next close: -1.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.63%
- Next close return data: 0.72%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.26 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 부산 벡스코 제3전시장 838억원 공사계약 체결 | HD현대중공업·HD한국조선해양 2%대 하락…미국·이란 전쟁 변수 속 조선... | [유캐스트 IPO] 기술은 軍에서, 돈은 民에서…2년래 이익률 40% 승부

### 10. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.26**
- Adjusted recommendation score: **114.32**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 64.29%, avg next close: -1.79%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.63%
- Next close return data: 0.72%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.26 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 부산 벡스코 제3전시장 838억원 공사계약 체결 | HD현대중공업·HD한국조선해양 2%대 하락…미국·이란 전쟁 변수 속 조선... | [유캐스트 IPO] 기술은 軍에서, 돈은 民에서…2년래 이익률 40% 승부

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 레이저쎌 (412350)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **134.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.69**
- Adjusted recommendation score: **124.37**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 25.00%, avg next close: -0.24%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.97%
- Next close return data: 5.29%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 2. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 글로벌 반도체 설비 투자 확대…반도체 장비 관련주 무더기 '휘파람' | 마이크로 LED·첨단 패키징 투자 확대…장비株 들썩이네 | 11월 10일 주식시장 주요공시

### 2. 스피어 (347700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **165.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.59**
- Adjusted recommendation score: **158.47**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 41.18%, avg next close: 0.33%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.07%
- Next close return data: 7.28%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 15. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.59 points. Stock pattern label is weak_historical_reaction.
- Related news examples: DB증권, 스피어 랩스와 디지털자산 사업 협력 | 스피어, 누적 수주 2.1억달러...성장 잠재력 증명-교보 | DB증권, 스피어랩스와 STO·RWA 사업화 추진

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
