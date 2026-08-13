# Daily Stock Candidate Report - 2026-08-13

Generated at: 2026-08-13 23:08:11

ML dataset: `data/processed/ml_dataset_20260813.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950220 | 네오이뮨텍 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000210 | DL | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000500 | 가온전선 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000660 | SK하이닉스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000950 | 전방 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 0009K0 | 에임드바이오 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001040 | CJ | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001060 | JW중외제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001260 | 남광토건 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001340 | PKC | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001420 | 태원물산 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 150 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 35 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| investment_decision | 85 | 0 | N/A | Not available | 0.00 |
| lawsuit | 82 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 275 | 0 | N/A | Not available | 0.00 |
| merger | 46 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 150 | 0 | N/A | Not available | 0.00 |
| spin_off | 8 | 0 | N/A | Not available | 0.00 |
| supply_contract | 148 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 150 | 0 | 0 | 150 | 0.00 |
| disclosure_violation | 35 | 0 | 0 | 35 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 85 | 0 | 0 | 85 | 0.00 |
| lawsuit | 82 | 0 | 0 | 82 | 0.00 |
| major_shareholder_change | 275 | 0 | 0 | 275 | 0.00 |
| merger | 46 | 0 | 0 | 46 | 0.00 |
| paid_in_capital_increase | 150 | 0 | 0 | 150 | 0.00 |

## Positive Candidates

### 1. 삼성E&A (028050)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **117.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: ‘AI 인프라’ 특화 속도…신성장 모터 장착하는 전통 제조사들 [biz-플... | 철강·석화 ‘AI·반도체 특수’로 불황 뚫었다 | 첨단산업 성장세 탄 삼성E&A…연간 실적 목표 순항

## Volatile Watchlist

### 1. 한국금융지주 (071050)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **65.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 김남구의 보험업 확장 구상 현실화…한국투자금융지주, KDB생명 품는다 | 8월 14일 개장 전 주요 공시

### 2. SIMPAC (009160)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **57.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **57.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: SIMPAC 주가, 8월 11일 4,900원 0.61% 하락 마감 | 구리·아연 솟구치자 비철금속주 폭발…고려아연·에이치브이엠 주가 신... | [특징주] 비철금속 업종 11% 급등…구리 가격 상승 전망 부각

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 2. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 3. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 4. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 5. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 6. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 7. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 8. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 9. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

### 10. 성호전자 (043260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, 한국금융지주 삼성생명 LG 이마트 스타벅스 차바이오... | 8월 14일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(13일) 주요공시... 모아데이타, 20억원 제3자배...

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
