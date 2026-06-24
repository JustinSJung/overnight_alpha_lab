# Daily Stock Candidate Report - 2026-06-24

Generated at: 2026-06-24 17:45:49

ML dataset: `data/processed/ml_dataset_20260624.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments from advanced error notes, and event-type performance adjustments based on historical success rates and returns.

## Event-Type Success Rate Adjustment

The recommender now applies a direct event-type performance adjustment. Event types with stronger historical success rates or positive average next-day returns can receive a small positive adjustment. Event types with weak success rates or negative average returns can receive a conservative penalty.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Success Adj | Return Adj | Total Adj |
|---|---:|---:|---:|---:|---:|---:|---:|
| bonus_issue | 15 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| convertible_bond | 18 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| disclosure_violation | 5 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| investment_decision | 4 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| lawsuit | 16 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| major_shareholder_change | 17 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| merger | 5 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| paid_in_capital_increase | 46 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| spin_off | 2 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |
| supply_contract | 14 | 0 | N/A | Not available | 0.00 | 0.00 | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 15 | 0 | 0 | 15 | 0.00 |
| convertible_bond | 18 | 0 | 0 | 18 | 0.00 |
| disclosure_violation | 5 | 0 | 0 | 5 | 0.00 |
| investment_decision | 4 | 0 | 0 | 4 | 0.00 |
| lawsuit | 16 | 0 | 0 | 16 | 0.00 |
| major_shareholder_change | 17 | 0 | 0 | 17 | 0.00 |
| merger | 5 | 0 | 0 | 5 | 0.00 |
| paid_in_capital_increase | 46 | 0 | 0 | 46 | 0.00 |
| spin_off | 2 | 0 | 0 | 2 | 0.00 |
| supply_contract | 14 | 0 | 0 | 14 | 0.00 |

## Positive Candidates

### 1. HEM파마 (376270)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **127.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: HEM파마, 46억 3천만 원대 공급계약→매출 기반 확대 기대 | [속보] HEM파마, 46.3억원 규모 프로바이오틱스 공급계약 체결…전년 연... | [주가] 6월 24일 주요 제약·바이오·기기 5% 변동 현황 - 38개사 증가

### 2. 솔디펜스 (215090)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **125.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: [52주] 최고가 3개, 최저가 693개 ... 지수는 반등 | [52주] 신고가 9개, 신저가 451개... 지수 낙폭 키워 | [52주] 최고가 7개, 최저가 124개... 지수 상승

### 3. 서호전기 (065710)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **125.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: [속보] 서호전기, 1079억원 규모 크레인 제어시스템 공급계약 체결 | 서호전기, 1,078억 7천만 원 크레인 시스템 공급계약→중공업 수주 확대... | 김병훈-최진민-김창수-이성엽은 재벌총수 못잖게 배당-연봉 챙겨

### 4. 원티드랩 (376980)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **110.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: 유동성공급계약의체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: [52주] 최고가 3개, 최저가 693개 ... 지수는 반등 | ‘삼전·하이닉스 직행’ 반도체 계약학과, 서울대 자연계 넘었다 | AI 다음은 양자컴퓨터…빅테크 승부 시작

### 5. DL이앤씨 (375500)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **110.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 시공사 뽑고 이주하고…'양재천 벨트' 재건축 잰걸음 | 호반건설 박철희 사장 '서울 드림' 빛 봤지만 안심 멀었다, 2026년 도시정... | DL이앤씨 주가 20% 끌어내린 사우디 8500억 세금…"근거 없는 위법 과세...

## Volatile Watchlist

### 1. 에코볼트 (097780)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **90.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **90.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 11. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: [신상브리핑] GS25, 버즈니, 크림, 비어커, 모두투어, 쿠쿠, 이디야커피... | [투자전략] 2차전지, 미국 ESS 성장 본격화…LG엔솔·삼성SDI 주목 | 전기차 성장 기대 흔들리나…자동차 부품주 전반 조정, 옥석 가리기 시...

### 2. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [첨부정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 3. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [첨부정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 4. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [첨부정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 5. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [첨부정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 6. 감성코퍼레이션 (036620)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **65.00**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(회사분할결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 제2의 코인 불장 오나…위지트, 가상화폐 인프라 확장으로 영토 넓힌다 | 6월 23일 주식시장 주요공시 | [뷰티 새소식] 플라워노즈, 나이트 유니콘 컬렉션 기념 더현대 서울 팝...

### 7. 인베니아 (079950)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **52.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: 최대주주변경을수반하는주식담보제공계약해제ㆍ취소등              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 6월 23일 주식시장 주요공시 | [코스피·코스닥,SK바이오사이언스 현대건설 브이엠 BGF리테일  경남제... | 인베니아, BOE에 드라이에처 공급

### 8. 유안타증권 (003470)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **50.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 유안타·LS·DB·현대차證, AI 대전환 시대 맞아 생존 전략 '각양각색' | '30돌' 축제 못 즐기는 코스닥…지수 정체 속 '동전주 구조조정' 시험대 | 올해 상승분 다 반납한 코스닥…“반도체 쏠림 완화돼야 반등”

### 9. 한국화장품 (123690)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **40.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: [단독] 에버코스 회생절차 돌입 불똥…LG생활건강 공급망 흔들리는 까닭 | K-뷰티 강세 속 효성티앤씨 급등…패션주는 종목별 차별화 | [제약+] 메디톡스, HA필러 아띠에르 도미니카공화국 허가 획득 外

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 토비스 (051360)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **66.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **66.00**
- Risk level: **HIGH**
- Event type: `spin_off`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: 주권매매거래정지              (주식의 병합, 분할 등 전자등록 변경, 말소)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 토비스, 주식 전자등록 변경 정지→인적분할 후 거래 재개 | 업황 회복 기대 vs 차익실현 충돌…디스플레이株 방향성 탐색 국면 | [데이터 뉴스룸] 전자업체 1분기 영업益 900% 육박 상승에 함박웃음…증...

### 2. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 3. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 4. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 5. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 6. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 7. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 8. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 9. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

### 10. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Adjusted recommendation score: **68.00**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Event-type evaluated cases: 0, success rate: N/A, avg next close: Not available
- Disclosure title: [기재정정]주요사항보고서(유무상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score.
- Related news examples: 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸... | 코스닥도 '추락'...반도체 소부장·로봇·광통신주 등 '와르르'

## Data Readiness

At this stage, candidates are still generated using rule-based scoring. The system now also uses historical error-note patterns and event-type performance statistics as conservative confidence adjustment layers. These adjustments will become more meaningful after enough evaluated event-reaction samples are accumulated.

## How to Read This Report

- Positive Candidates: relatively favorable event and news conditions.
- Volatile Watchlist: potentially important events with uncertain direction.
- General Watchlist: events worth monitoring but not strong enough for positive classification.
- Risk / Avoid Review List: negative or high-risk events such as capital increases, CB/BW, lawsuits, or disclosure violations.
- Error-note adjustment score: learning signal from previous advanced error notes.
- Event-type performance adjustment score: success-rate and average-return based adjustment.

## Next Step

The next step is to add stock-specific historical reaction patterns, so the system can distinguish between event-type level behavior and stock-level behavior.
