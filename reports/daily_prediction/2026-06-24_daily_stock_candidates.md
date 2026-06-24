# Daily Stock Candidate Report - 2026-06-24

Generated at: 2026-06-24 22:05:55

ML dataset: `data/processed/ml_dataset_20260624.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001470 | 삼부토건 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 068270 | 셀트리온 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 071850 | 캐스텍코리아 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 073640 | 테라사이언스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 074610 | 이엔플러스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 079900 | 전진건설로봇 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 083790 | CG인바이츠 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 096240 | 크레버스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 097780 | 에코볼트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 105550 | 엣지파운드리 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 123690 | 한국화장품 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 10 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 6 | 0 | N/A | Not available | 0.00 |
| investment_decision | 5 | 0 | N/A | Not available | 0.00 |
| lawsuit | 3 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 9 | 0 | N/A | Not available | 0.00 |
| merger | 2 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 8 | 0 | N/A | Not available | 0.00 |
| spin_off | 1 | 0 | N/A | Not available | 0.00 |
| supply_contract | 10 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 10 | 0 | 0 | 10 | 0.00 |
| disclosure_violation | 6 | 0 | 0 | 6 | 0.00 |
| investment_decision | 5 | 0 | 0 | 5 | 0.00 |
| lawsuit | 3 | 0 | 0 | 3 | 0.00 |
| major_shareholder_change | 9 | 0 | 0 | 9 | 0.00 |
| merger | 2 | 0 | 0 | 2 | 0.00 |
| paid_in_capital_increase | 8 | 0 | 0 | 8 | 0.00 |
| spin_off | 1 | 0 | 0 | 1 | 0.00 |
| supply_contract | 10 | 0 | 0 | 10 | 0.00 |

## Positive Candidates

No candidates in this section.

## Volatile Watchlist

### 1. 에코볼트 (097780)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **80.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [춘추세평] 순환의 미학, 쓰레기가 예술과 일상이 되는 시대 | [신상브리핑] GS25, 버즈니, 크림, 비어커, 모두투어, 쿠쿠, 이디야커피... | [투자전략] 2차전지, 미국 ESS 성장 본격화…LG엔솔·삼성SDI 주목

### 2. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 3. 감성코퍼레이션 (036620)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **65.00**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(회사분할결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 제2의 코인 불장 오나…위지트, 가상화폐 인프라 확장으로 영토 넓힌다 | 6월 23일 주식시장 주요공시 | [뷰티 새소식] 플라워노즈, 나이트 유니콘 컬렉션 기념 더현대 서울 팝...

### 4. 한화갤러리아 (452260)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **40.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 한화갤러리아, 서울 순화빌딩 2135억원에 인수 추진 | 한화갤러리아, 순화빌딩 매입 가시화...2135억원에 MOU 체결 | [아주경제 오늘의 뉴스 종합] SK하이닉스, 美 나스닥 ADR 상장 추진 外

### 5. 한국화장품제조 (003350)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **30.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: K뷰티…내일은 더 맑다 | [단독] 에버코스 회생절차 돌입 불똥…LG생활건강 공급망 흔들리는 까닭 | K-뷰티 강세 속 효성티앤씨 급등…패션주는 종목별 차별화

### 6. 성호전자 (043260)

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
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스닥 외국인] 알테오젠 서진시스템 파두 성호전자 집중매수...제주반... | 성호전자 주가, 6월 24일 장중 31,650원 0.80% 상승 | 지구온난화의 역설… 오텍, 전 세계 탄소중립 흐름 타고 역대급 호황 예...

### 7. 한국화장품 (123690)

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
- Related news examples: K뷰티…내일은 더 맑다 | [제약바이오 브리프] 메디톡스·신라젠·셀트리온제약·지씨셀·GC·종근... | 메디톡스, 히알루론산 필러 '아띠에르' 도미니카공화국 허가 획득…중남...

### 8. 비투엔 (307870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **14.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **14.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]최대주주변경을수반하는주식양수도계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주식마감] 美 자회사, 나스닥 상장 임박에 로킷헬스케어 '上'... 금호건... | [EBN 데이터센터] 24일 상승 종목 30選…중소형 개별주 '불기둥' | 6월 22일 주식시장 주요공시

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 아모텍 (052710)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-90.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-90.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 권리락              (유상증자)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -1. Negative keyword count is 5. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 아모텍, 25일 권리락 발생 | 코스닥도 '급등'...알테오젠 · HLB · 삼천당제약 · 펩트론 '껑충' | 삼성전기 삼화콘덴서 폭등, MLCC가 뭐길래 / 전자산업의 쌀, 판도를 바꾸...

### 2. CG인바이츠 (083790)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `disclosure_violation`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 불성실공시법인지정              (공시변경)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is disclosure_violation. Initial direction is negative. Event score is -80. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: CG인바이츠, 불성실공시법인 지정→공시위반제재금 부과 | [CG인바이츠 분쟁]①조중명 사비도 한계…'아이발티노스타트' 임상 중단... | 인바이츠바이오코아 "내년 3분기 코스닥 이전 상장 완료할 것"

### 3. 워트 (396470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **101.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 워트, 8억 5천7백만 원 공급계약→삼성전자와 초정밀항온항습장치 납품 | AI 반도체 폭발에 심장 거머쥔 한미반도체…차세대 TC본더로 시장 장악 | '2분기 흑자 전환' 워트, '국산화 THC'의 반도체 증설 수혜

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
