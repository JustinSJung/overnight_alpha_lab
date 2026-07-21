# Daily Stock Candidate Report - 2026-07-21

Generated at: 2026-07-21 23:15:41

ML dataset: `data/processed/ml_dataset_20260721.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 000500 | 가온전선 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 0009K0 | 에임드바이오 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001470 | 삼부토건 | 13 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001840 | 이화공영 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002020 | 코오롱 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002070 | 비비안 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002210 | 동성제약 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002780 | 진흥기업 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002810 | 삼영무역 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002880 | 디와이에이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003060 | 에이프로젠바이오로직스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 2 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 75 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 20 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 36 | 0 | N/A | Not available | 0.00 |
| lawsuit | 42 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 85 | 0 | N/A | Not available | 0.00 |
| merger | 23 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 76 | 0 | N/A | Not available | 0.00 |
| spin_off | 2 | 0 | N/A | Not available | 0.00 |
| supply_contract | 84 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 2 | 0 | 0 | 2 | 0.00 |
| convertible_bond | 75 | 0 | 0 | 75 | 0.00 |
| disclosure_violation | 20 | 0 | 0 | 20 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 36 | 0 | 0 | 36 | 0.00 |
| lawsuit | 42 | 0 | 0 | 42 | 0.00 |
| major_shareholder_change | 85 | 0 | 0 | 85 | 0.00 |
| merger | 23 | 0 | 0 | 23 | 0.00 |
| paid_in_capital_increase | 76 | 0 | 0 | 76 | 0.00 |
| spin_off | 2 | 0 | 0 | 2 | 0.00 |

## Positive Candidates

### 1. 웹케시 (053580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **145.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 웹케시, 87억 2천만 원 규모 IBK디지털뱅킹 계약→외주생산 추진 | 웹케시, 87억 2천만 원 공급계약→디지털뱅킹 사업 확대 | 자연어 명령으로 AI-외부데이터 연결…쿠콘 ‘AI 에이전트’ 고도화

### 2. 지엔씨에너지 (119850)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **140.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 지엔씨에너지, '3대 메가프로젝트 핵심' 데이터센터 비상발전기 독점적... | 소외 받는 코스닥, 이젠 'AI 데이터센터'로 재도약 노린다 | 북미·아세안 러브콜… LS ELECTRIC, 핵심 전력기기 사업 경쟁력 부각

### 3. 부스타 (008470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **100.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 권리락              (무상증자)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [특징주] 부스타, 100% 무상증자 권리락 실시…1대1 신주 배정에 주가 강... | [특징주] 부스타, 22 무상증자 권리락 실시… 1대1 신주 배정 | 겨울 테마 조정…실적 경쟁력이 주가 가른다

## Volatile Watchlist

### 1. 제이알글로벌리츠 (348950)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **55.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [더벨][건설부동산 풍향계] 리츠업계, '재투자 준비금' 도입 필요 한목... | 홈플러스·중앙 사태 후폭풍…하이일드펀드 석달간 3445억 순유출 | JR리츠, ETF 의결권 행사 모범 사례될까…"1~2곳 소액주주 힘 실었다"

### 2. 에이프릴바이오 (397030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **49.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **49.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (기술도입 계약 체결)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [아주증시포커스] 6월 이후 하락률 1위 K-증시…한달 새 100조 자금 빠져... | 에이프릴바이오 "플랫폼 직접, 기술은 협력"… 모달리티 확장 지속 | [주요공시] 에이프릴바이오, 효성ITX, SNT에너지, 고려아연, 전진건설로...

### 3. 갤럭시아에스엠 (011420)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **37.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **37.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 엔화·가상자산도 폰으로 결제…다날, 디지털자산 플랫폼 사업에 가속도 | 신한지주, 주주환원 확대·STO 인프라 선점 기대감에 강세 | 효성 조현준 회장 장남 조재현, 갤럭시아에스엠 지분 매입 배경은?

### 4. 가온전선 (000500)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **22.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **22.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주요공시] 삼성바이오로직스, 대덕전자, 테크윙, 코오롱티슈진, 파두,... | LS그룹 가온전선, 상반기 영업이익 640억…"AI 데이터센터·미국 전력 투... | 전력 인프라 수요 업고 전선업계 수주랠리…증설 속도전

### 5. 가온전선 (000500)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **22.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **22.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주요공시] 삼성바이오로직스, 대덕전자, 테크윙, 코오롱티슈진, 파두,... | LS그룹 가온전선, 상반기 영업이익 640억…"AI 데이터센터·미국 전력 투... | 전력 인프라 수요 업고 전선업계 수주랠리…증설 속도전

### 6. 가온전선 (000500)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **22.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **22.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주요공시] 삼성바이오로직스, 대덕전자, 테크윙, 코오롱티슈진, 파두,... | LS그룹 가온전선, 상반기 영업이익 640억…"AI 데이터센터·미국 전력 투... | 전력 인프라 수요 업고 전선업계 수주랠리…증설 속도전

### 7. 가온전선 (000500)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **22.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **22.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주요공시] 삼성바이오로직스, 대덕전자, 테크윙, 코오롱티슈진, 파두,... | LS그룹 가온전선, 상반기 영업이익 640억…"AI 데이터센터·미국 전력 투... | 전력 인프라 수요 업고 전선업계 수주랠리…증설 속도전

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 코아스 (071950)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-126.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-126.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -7. Negative keyword count is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 20일 주식시장 주요공시 | [특징주] 제이케이시냅스, 30억 유상증자에 휴림로봇 최대주주 변경…재... | [특징주] 제이케이시냅스, 30억 유상증자…최대주주 휴림로봇 변경

### 2. 씨엑스아이 (900120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-100.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -3. Negative keyword count is 5. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 씨엑스아이, 최대주주 유증·장내매수 추진…"상장유지 의지" | [속보] 씨엑스아이, 480억원 규모 제3자배정 유상증자 결정…운영자금 ... | 씨엑스아이, 3,700,000주 유상증자→3자배정 통한 자금확보

### 3. 씨엑스아이 (900120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-100.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -3. Negative keyword count is 5. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 씨엑스아이, 최대주주 유증·장내매수 추진…"상장유지 의지" | [속보] 씨엑스아이, 480억원 규모 제3자배정 유상증자 결정…운영자금 ... | 씨엑스아이, 3,700,000주 유상증자→3자배정 통한 자금확보

### 4. 씨엑스아이 (900120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-100.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -3. Negative keyword count is 5. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 씨엑스아이, 최대주주 유증·장내매수 추진…"상장유지 의지" | [속보] 씨엑스아이, 480억원 규모 제3자배정 유상증자 결정…운영자금 ... | 씨엑스아이, 3,700,000주 유상증자→3자배정 통한 자금확보

### 5. 씨엑스아이 (900120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-100.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -3. Negative keyword count is 5. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 씨엑스아이, 최대주주 유증·장내매수 추진…"상장유지 의지" | [속보] 씨엑스아이, 480억원 규모 제3자배정 유상증자 결정…운영자금 ... | 씨엑스아이, 3,700,000주 유상증자→3자배정 통한 자금확보

### 6. 제주은행 (006220)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-73.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-73.00**
- Risk level: **HIGH**
- Event type: `disclosure_violation`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 불성실공시법인지정              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is disclosure_violation. Initial direction is negative. Event score is -80. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 증시일정] LG디스플레이·제주은행·엔젠바이오 등 | [브랜드평판] 미래에셋자산운용, 연금 7월 1위.... 하나은행, 신한은행 ... | 제주은행, 불성실공시법인 지정→8백만원 제재 부과

### 7. 아이로보틱스 (066430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-63.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-63.00**
- Risk level: **HIGH**
- Event type: `lawsuit`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 소송등의제기ㆍ신청(경영권분쟁소송)              (주주총회결의 취소 등의 소)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is lawsuit. Initial direction is negative. Event score is -75. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 새 간판 걸고 띄운 스팩…iM증권 IPO 재시동 [이슈 더보기] | [ICT 종합] 인텔 및 비피엠지 소식 외 | [주식마감] '로봇주' 강세에 코스모로보틱스 상한가... 에브리봇, 스모...

### 8. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-61.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-61.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 하이트진로, 음료 상장기업 브랜드평판 1위…롯데칠성 제치고 정상 지켜 | [브랜드평판] 하이로진로, 음료 상장기업 7월 1위... 롯데칠성, 보해양조... | 한울앤제주, 전환사채 전환 주식 8만 7천주 추가상장→유통주식수 확대

### 9. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-61.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-61.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 하이트진로, 음료 상장기업 브랜드평판 1위…롯데칠성 제치고 정상 지켜 | [브랜드평판] 하이로진로, 음료 상장기업 7월 1위... 롯데칠성, 보해양조... | 한울앤제주, 전환사채 전환 주식 8만 7천주 추가상장→유통주식수 확대

### 10. 에코글로우 (159910)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-58.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-58.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 중소·중견기업 547개 ‘혁신 프리미어’ 선정…정책금융 우대 집중 지... | '유소년 청룡 결승 대진 완성!' 휘문아카데미-세종시 격돌…마이데일리... | CU 맥그리거 흑맥주, 에코 골프, 롯데GRS ‘한식미관’ 外 [똑똑한소비]

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
