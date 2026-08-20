# Daily Stock Candidate Report - 2026-08-20

Generated at: 2026-08-20 22:50:33

ML dataset: `data/processed/ml_dataset_20260820.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950220 | 네오이뮨텍 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000210 | DL | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000500 | 가온전선 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000660 | SK하이닉스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 419540 | 비스토스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 418620 | E8 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 407400 | 꿈비 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 403490 | 우듬지팜 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 397030 | 에이프릴바이오 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 396470 | 워트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 389680 | 유디엠텍 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 174 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 39 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| investment_decision | 87 | 0 | N/A | Not available | 0.00 |
| lawsuit | 86 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 301 | 0 | N/A | Not available | 0.00 |
| merger | 49 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 175 | 0 | N/A | Not available | 0.00 |
| spin_off | 11 | 0 | N/A | Not available | 0.00 |
| supply_contract | 161 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 174 | 0 | 0 | 174 | 0.00 |
| disclosure_violation | 39 | 0 | 0 | 39 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 87 | 0 | 0 | 87 | 0.00 |
| lawsuit | 86 | 0 | 0 | 86 | 0.00 |
| major_shareholder_change | 301 | 0 | 0 | 301 | 0.00 |
| merger | 49 | 0 | 0 | 49 | 0.00 |
| paid_in_capital_increase | 175 | 0 | 0 | 175 | 0.00 |

## Positive Candidates

### 1. 디와이피엔에프 (104460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **94.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **94.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 8월 19일 주식시장 주요공시 | 기계 상장기업 브랜드평판 8월 빅데이터 분석... 1위 두산에너빌리티, ... | [52주] 신저가만 517개 ... 지수 하락 반전

### 2. 엠앤씨솔루션 (484870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **92.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 한화에어로는 버티는데 현대로템·한화시스템 '휘청'…방산주 희비 뚜렷 | [오늘의 IR] 카카오게임즈·삼양식품·레드캡투어 등 | 의약품 공장 증축·실시간 공정…휴온스그룹, 전방위 제조 혁신

## Volatile Watchlist

### 1. 코스맥스 (192820)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **75.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: K뷰티 성장세 지속…ODM업계 수혜 확대 | “화장품 회사는 뭘 잘해야 들어가죠?”…하반기에도 줄줄이 채용한다 | 이 티켓 뭐길래 48초 만에 매진…올영 긴장하고 있다

### 2. 덴티스 (261200)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **60.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 그래피, 부산대 치의학전문대학원과 산학협력 협약 체결 | 그래피·오스테오닉 주가 방긋… 글로벌 임플란트 및 치과 소재 모멘텀... | [그래피 줌업] 시가의 115% 프리미엄? 레이 인수 뭘 봤나⑤

### 3. 덴티스 (261200)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **60.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 9. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 그래피, 부산대 치의학전문대학원과 산학협력 협약 체결 | 그래피·오스테오닉 주가 방긋… 글로벌 임플란트 및 치과 소재 모멘텀... | [그래피 줌업] 시가의 115% 프리미엄? 레이 인수 뭘 봤나⑤

### 4. 유안타증권 (003470)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **44.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **44.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 유안타證 “SK, 자회사 실적 회복은 시작 단계⋯주주환원 내년부터가 진... | 신성이엔지, 반도체 투자 확대에 수주잔고↑…실적개선 기대-유안타 | "진영이형, 무조건 사라더니"…주가 24% 빠지자 '부글부글' [종목+]

### 5. 나인앤컴퍼니 (366030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **35.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 일동제약·나인앤컴퍼니 "합작법인 설립" | 일동제약, 패션기업과 손잡고 뷰티·헬스케어 확장…합작법인 추진 | 뷰티에서 헬스케어까지…일동제약&나인앤컴퍼니, 새 성장축 '맞손'

### 6. 나인앤컴퍼니 (366030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **35.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 일동제약·나인앤컴퍼니 "합작법인 설립" | 일동제약, 패션기업과 손잡고 뷰티·헬스케어 확장…합작법인 추진 | 뷰티에서 헬스케어까지…일동제약&나인앤컴퍼니, 새 성장축 '맞손'

### 7. 나인앤컴퍼니 (366030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **35.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 일동제약·나인앤컴퍼니 "합작법인 설립" | 일동제약, 패션기업과 손잡고 뷰티·헬스케어 확장…합작법인 추진 | 뷰티에서 헬스케어까지…일동제약&나인앤컴퍼니, 새 성장축 '맞손'

### 8. 나인앤컴퍼니 (366030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **35.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 일동제약·나인앤컴퍼니 "합작법인 설립" | 일동제약, 패션기업과 손잡고 뷰티·헬스케어 확장…합작법인 추진 | 뷰티에서 헬스케어까지…일동제약&나인앤컴퍼니, 새 성장축 '맞손'

### 9. 나인앤컴퍼니 (366030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **35.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 일동제약·나인앤컴퍼니 "합작법인 설립" | 일동제약, 패션기업과 손잡고 뷰티·헬스케어 확장…합작법인 추진 | 뷰티에서 헬스케어까지…일동제약&나인앤컴퍼니, 새 성장축 '맞손'

### 10. 나인앤컴퍼니 (366030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **35.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 일동제약·나인앤컴퍼니 "합작법인 설립" | 일동제약, 패션기업과 손잡고 뷰티·헬스케어 확장…합작법인 추진 | 뷰티에서 헬스케어까지…일동제약&나인앤컴퍼니, 새 성장축 '맞손'

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
