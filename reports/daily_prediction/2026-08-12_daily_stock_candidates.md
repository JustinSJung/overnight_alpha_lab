# Daily Stock Candidate Report - 2026-08-12

Generated at: 2026-08-12 23:06:38

ML dataset: `data/processed/ml_dataset_20260812.csv`

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
| 403490 | 우듬지팜 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 397030 | 에이프릴바이오 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 396470 | 워트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 389680 | 유디엠텍 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 383800 | LX홀딩스 | 16 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 380540 | 옵티코어 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 378800 | 샤페론 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 376270 | HEM파마 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 137 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 35 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| investment_decision | 83 | 0 | N/A | Not available | 0.00 |
| lawsuit | 76 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 273 | 0 | N/A | Not available | 0.00 |
| merger | 46 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 148 | 0 | N/A | Not available | 0.00 |
| spin_off | 8 | 0 | N/A | Not available | 0.00 |
| supply_contract | 147 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 137 | 0 | 0 | 137 | 0.00 |
| disclosure_violation | 35 | 0 | 0 | 35 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 83 | 0 | 0 | 83 | 0.00 |
| lawsuit | 76 | 0 | 0 | 76 | 0.00 |
| major_shareholder_change | 273 | 0 | 0 | 273 | 0.00 |
| merger | 46 | 0 | 0 | 46 | 0.00 |
| paid_in_capital_increase | 148 | 0 | 0 | 148 | 0.00 |

## Positive Candidates

### 1. 영진약품 (003520)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **130.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [아주증시포커스] '스페이스X' 투자 효과? 미래에셋 2분기 순이익 2조원... | "알약으로 쉽게 먹는다"…아토목세틴, 정제 출시 잇따라 | 영진약품, 中서 '세프카펜 세립' 허가…현지 공략 본격화

### 2. 예스티 (122640)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **115.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 예스티, 日 요나타와 합작사 설립 MOU…검사 장비 시장 진출 | 코스닥 '상승'...에코프로비엠·원익IPS·실리콘투 '껑충' | 외산 의존 끊고 발광층 선점… 한켐, 차세대 소재 수주 모멘텀 본격화

## Volatile Watchlist

### 1. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 2. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 3. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 4. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 5. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 6. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 7. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 8. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 9. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

### 10. 에이전트AI (060900)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **25.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 기타시장안내(최대주주의의무보유관련)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 데이터 중심으로 기술 모으는 오라클의 AI 전략 [테크리포트] | "내 기사 읽더니 내 문체로 초안까지"…'아마존 퀵' 직접 써보니 | 앱 여는 스마트폰 끝나나… 구글 픽셀11, '알아서 행동하는 AI폰' 승부수

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

No candidates in this section.

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
