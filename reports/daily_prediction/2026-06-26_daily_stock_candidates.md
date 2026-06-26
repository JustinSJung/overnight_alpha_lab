# Daily Stock Candidate Report - 2026-06-26

Generated at: 2026-06-26 07:57:08

ML dataset: `data/processed/ml_dataset_20260626.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 005960 | 동부건설 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 006570 | 대림통상 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 006740 | 블루산업개발 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 012630 | HDC | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 013580 | 계룡건설산업 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 023770 | 플레이위드 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 045390 | 대아티아이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 109960 | 앱토크롬 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 138360 | 앤로보틱스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 179530 | 애드바이오텍 | 16 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 187660 | 페니트리움바이오 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 361610 | SK아이이테크놀로지 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 17 | 0 | N/A | Not available | 0.00 |
| investment_decision | 2 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 5 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 6 | 0 | N/A | Not available | 0.00 |
| supply_contract | 4 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | 0 | 1 | 0.00 |
| convertible_bond | 17 | 0 | 0 | 17 | 0.00 |
| investment_decision | 2 | 0 | 0 | 2 | 0.00 |
| major_shareholder_change | 5 | 0 | 0 | 5 | 0.00 |
| paid_in_capital_increase | 6 | 0 | 0 | 6 | 0.00 |
| supply_contract | 4 | 0 | 0 | 4 | 0.00 |

## Positive Candidates

### 1. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **105.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 신계용 과천시장 "철도 시민 일상과 직결되는 핵심 교통 인프라" | 하반기 수주시장 ‘공공주택ㆍ철도’에 달렸다 | [르포]사천 빈 들판 위 '우주항공청 신청사' 표지…2030년 우주항공 수도...

### 2. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **105.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 신계용 과천시장 "철도 시민 일상과 직결되는 핵심 교통 인프라" | 하반기 수주시장 ‘공공주택ㆍ철도’에 달렸다 | [르포]사천 빈 들판 위 '우주항공청 신청사' 표지…2030년 우주항공 수도...

### 3. 동부건설 (005960)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **102.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [분양 소식] '더샵'은 완판 행진, '윤슬'은 이름 승부···아파트 시장... | HD현대중공업, 7800억에 군산조선소 매각…12월31일 소유권 이전 | 동부건설, '센트레빌 아스테리움 거제' 7월 분양…1307가구 대단지 공급

### 4. 대아티아이 (045390)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **97.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [데이터 뉴스룸] 에너지 업체 영업益 10%대 상승에 방긋…한전·가스공... | K-철도 해외 진출 쾌거 속 "속도보다 안전" 강조한 철도의 날 | [N2 모닝 경제 브리핑-6월 25일] 美 증시, 혼조세로 마감…마이크론 경계...

### 5. 알지노믹스 (476830)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **92.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 권리락              (무상증자)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스닥 외국인] 주성엔지니어링 파두 대한광통신 에코프로 에코프로비... | 생물공학 업종 약세… 에이비엘바이오·펩트론· 휴젤· 크로넥스 동반... | 상반기 무상증자 잇따라…엠앤씨솔루션, 200% 무상증자 추진

## Volatile Watchlist

### 1. 대림통상 (006570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **70.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **70.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 11. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 대림통상 "'한국카본' 신기술사업금융사와 글로벌 신사업 공조" | 대림통상 "'한국카본' 신기술사업금융사와 미주 거점 활용 글로벌 신사... | 대림통상, 한국카본과 글로벌 신사업 공조

### 2. 대림통상 (006570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **70.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **70.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 11. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 대림통상 "'한국카본' 신기술사업금융사와 글로벌 신사업 공조" | 대림통상 "'한국카본' 신기술사업금융사와 미주 거점 활용 글로벌 신사... | 대림통상, 한국카본과 글로벌 신사업 공조

### 3. 대림통상 (006570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **70.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **70.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 11. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 대림통상 "'한국카본' 신기술사업금융사와 글로벌 신사업 공조" | 대림통상 "'한국카본' 신기술사업금융사와 미주 거점 활용 글로벌 신사... | 대림통상, 한국카본과 글로벌 신사업 공조

### 4. HDC (012630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **27.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **27.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [라이즈 선도대학을 가다/한국골프과학기술대학교] 강원의 미래를 잇는... | 건설주 희비 교차…정책 수혜주는 급등, 대형주는 숨고르기 | [산업소식] 카카오, 4대 과기원과 맞손..청소년 유니콘 창업가 발굴

### 5. HDC (012630)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **27.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **27.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [라이즈 선도대학을 가다/한국골프과학기술대학교] 강원의 미래를 잇는... | 건설주 희비 교차…정책 수혜주는 급등, 대형주는 숨고르기 | [산업소식] 카카오, 4대 과기원과 맞손..청소년 유니콘 창업가 발굴

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 2. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 3. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 4. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 5. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 6. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 7. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 8. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 9. 애드바이오텍 (179530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-41.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-41.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 10. 블루산업개발 (006740)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-35.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 국방부, '50만 드론 전사' 시대 연다…AI 군집드론·K-LUCAS 대거 전력화 | 국립부경대, ‘부산형 앵커사업 평가’ 부산 유일 S등급 | 모빌리티 플랫폼은 차세대 게임 마켓이 될 수 있을까?

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
