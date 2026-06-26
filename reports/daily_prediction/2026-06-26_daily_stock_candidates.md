# Daily Stock Candidate Report - 2026-06-26

Generated at: 2026-06-26 08:30:38

ML dataset: `data/processed/ml_dataset_20260626.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 007460 | 에이프로젠 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 009730 | 이렘 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 012510 | 더존비즈온 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 012630 | HDC | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 013580 | 계룡건설산업 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 013700 | 까뮤이앤씨 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 023770 | 플레이위드 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 043260 | 성호전자 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 045390 | 대아티아이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 054930 | 유신 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 085660 | 차바이오텍 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 179530 | 애드바이오텍 | 8 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 1 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 11 | 0 | N/A | Not available | 0.00 |
| investment_decision | 2 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 3 | 0 | N/A | Not available | 0.00 |
| merger | 2 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 3 | 0 | N/A | Not available | 0.00 |
| supply_contract | 6 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 1 | 0 | 0 | 1 | 0.00 |
| convertible_bond | 11 | 0 | 0 | 11 | 0.00 |
| investment_decision | 2 | 0 | 0 | 2 | 0.00 |
| major_shareholder_change | 3 | 0 | 0 | 3 | 0.00 |
| merger | 2 | 0 | 0 | 2 | 0.00 |
| paid_in_capital_increase | 3 | 0 | 0 | 3 | 0.00 |
| supply_contract | 6 | 0 | 0 | 6 | 0.00 |

## Positive Candidates

### 1. 까뮤이앤씨 (013700)

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
- Related news examples: [데이터 뉴스룸] 건설業, 1분기 영업성적에 희비 교차…대우건설 웃고 ... | "PF 리스크 없다"...남화토건, 독보적 대금 회수력으로 '저평가 탈출' 시... | 일성건설 주가 파죽지세… 건설주 혼조세 속 투자 기회는 어디?

### 2. 에이직랜드 (445090)

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
- Related news examples: 반도체 업종 7% 가까이 급등…하반기 슈퍼사이클 기대 커진다 | [인터뷰] 퇴임 앞둔 강기정 시장 “‘고생하셨어요’ 시민 한마디에 모... | 강기정, “대기업 설계·생산 반도체 종합세트 광주에 올 것”

### 3. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **110.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 계룡건설산업, 1,442억 3천만 원 공동주택 신축공사 계약→매출 기반 확... | 신계용 과천시장 "철도 시민 일상과 직결되는 핵심 교통 인프라" | 하반기 수주시장 ‘공공주택ㆍ철도’에 달렸다

### 4. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **110.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 계룡건설산업, 1,442억 3천만 원 공동주택 신축공사 계약→매출 기반 확... | 신계용 과천시장 "철도 시민 일상과 직결되는 핵심 교통 인프라" | 하반기 수주시장 ‘공공주택ㆍ철도’에 달렸다

### 5. 대아티아이 (045390)

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

### 6. 유신 (054930)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **95.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: "만해 스님 가르침 따라 세상 속으로 들어가야" | 정명희 “대심도 개선공사 연내 착공… 금곡과선교는 내년 6월 준공 목... | 인혁당 사형수 서도원 열사 아내 배수자 여사 별세

## Volatile Watchlist

### 1. 휴온스 (243070)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **62.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **62.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제약사 간편식, 밀키트서 '맞춤 영양식'으로…실적 존재감은 아직 | [제약 뉴스브리핑] 한미사이언스, 완전두유 '굿스파이크' 캠페인 진행 | "CDMO·AI 앞세웠다"…BIO USA서 K-바이오 존재감 입증

### 2. 휴온스 (243070)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **62.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **62.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제약사 간편식, 밀키트서 '맞춤 영양식'으로…실적 존재감은 아직 | [제약 뉴스브리핑] 한미사이언스, 완전두유 '굿스파이크' 캠페인 진행 | "CDMO·AI 앞세웠다"…BIO USA서 K-바이오 존재감 입증

### 3. HDC (012630)

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

### 5. 더존비즈온 (012510)

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
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 사설 데이터 1만건 현미경 분석... '언론사유화'를 폭로하다 | 삼성전자, 4000억 상당 온누리상품권 푼다 | 기회균형전형 선발 축소…합격 문 더 좁아진다

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
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
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
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
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
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
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
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 6월 26일 주요 제약·바이오·기기 5% 변동 현황 - 75곳 감소 | 코스닥 제약지수 3.13% 하락, 1만선 위협 | [주가] 6월 25일 주요 제약·바이오·기기 5% 변동 현황 - 비엘팜텍 상한...

### 10. 애드바이오텍 (179530)

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
