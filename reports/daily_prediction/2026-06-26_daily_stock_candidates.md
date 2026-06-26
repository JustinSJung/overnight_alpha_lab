# Daily Stock Candidate Report - 2026-06-26

Generated at: 2026-06-26 16:11:03

ML dataset: `data/processed/ml_dataset_20260626.csv`

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
| 073640 | 테라사이언스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 074610 | 이엔플러스 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 079900 | 전진건설로봇 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 082740 | 한화엔진 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 083790 | CG인바이츠 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 090350 | 노루페인트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 096240 | 크레버스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 097780 | 에코볼트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 105550 | 엣지파운드리 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 123690 | 한국화장품 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 1 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 12 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 6 | 0 | N/A | Not available | 0.00 |
| investment_decision | 5 | 0 | N/A | Not available | 0.00 |
| lawsuit | 4 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 17 | 0 | N/A | Not available | 0.00 |
| merger | 3 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 8 | 0 | N/A | Not available | 0.00 |
| spin_off | 2 | 0 | N/A | Not available | 0.00 |
| supply_contract | 12 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 1 | 0 | 0 | 1 | 0.00 |
| convertible_bond | 12 | 0 | 0 | 12 | 0.00 |
| disclosure_violation | 6 | 0 | 0 | 6 | 0.00 |
| investment_decision | 5 | 0 | 0 | 5 | 0.00 |
| lawsuit | 4 | 0 | 0 | 4 | 0.00 |
| major_shareholder_change | 17 | 0 | 0 | 17 | 0.00 |
| merger | 3 | 0 | 0 | 3 | 0.00 |
| paid_in_capital_increase | 8 | 0 | 0 | 8 | 0.00 |
| spin_off | 2 | 0 | 0 | 2 | 0.00 |
| supply_contract | 12 | 0 | 0 | 12 | 0.00 |

## Positive Candidates

### 1. 한화엔진 (082740)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **127.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 기업공시 [6월 26일] | 한주에이알티, 리퍼 플랫폼 'TTM' 인수 완료 | 조선·엔진주 일제히 조정… 장기 성장성은 여전

### 2. 한성크린텍 (066980)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **89.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **89.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 위지트, '자회사 가치'가 시가총액 추월…반도체 소부장 리레이팅 시동 | 위지트, 반도체 소부장 기업으로의 재평가 시점…"자회사 지분가치, 시... | 밸류파인더 "위지트, 반도체 소부장 리레이팅 기대…해외 매출 확대 기...

## Volatile Watchlist

### 1. 젠큐릭스 (229000)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **85.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **85.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 10. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 젠큐릭스, 제노픽스와 합병 추진…"암 진단 R&D 강화" | 젠큐릭스, 제노픽스와 전략적 합병 추진…시장확대·R&D 역량 강화 | 젠큐릭스, 제노픽스 흡수합병 결정..암 진단 포트폴리오 확대 [공시록]

### 2. 노루페인트 (090350)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **55.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 8. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 노루페인트, 아파트 외벽 시안이 5분 만에…재도장 시장 흔든 AI 혁명 | 외벽 틈 막아 빗물 차단…'큐피트마스터'로 아파트 수명 지킨다 | 건설경기 회복 기대감에 건축자재주 강세…KCC·서산 신바람 났네

### 3. 코웨이 (021240)

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
- Related news examples: [문화 트렌드] 유니세프 한국위원회-티모넷, 기후위기 속 어린이 현실 ... | LG전자, 말레이 구독 브랜드샵 130호점 돌파 | LG전자, 말레이 구독 브랜드샵 130호점 돌파…‘K-구독’ 영토 빠르게 확...

### 4. 한익스프레스 (014130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **15.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **15.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 반복할수록 강해졌다...정부 사이버 모의훈련 효과 확인 | 해킹 메일 10명 중 4명 열람…디도스 대응에 24분 걸려 | 임직원 10명 중 4명 해킹메일 열었다…12.7%는 악성코드 감염

### 5. 한익스프레스 (014130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **15.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **15.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 반복할수록 강해졌다...정부 사이버 모의훈련 효과 확인 | 해킹 메일 10명 중 4명 열람…디도스 대응에 24분 걸려 | 임직원 10명 중 4명 해킹메일 열었다…12.7%는 악성코드 감염

### 6. 크래프톤 (259960)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [게임 레이더] 컴투스·크래프톤·넷마블, 신작 사전예약·e스포츠 개막... | 낙폭 커진 인터넷·게임주...증권가 "지금이 매수 기회" | 배틀그라운드 세계 최강자전…서울서 '최후의 치킨' 겨룬다

### 7. 크래프톤 (259960)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [게임 레이더] 컴투스·크래프톤·넷마블, 신작 사전예약·e스포츠 개막... | 낙폭 커진 인터넷·게임주...증권가 "지금이 매수 기회" | 배틀그라운드 세계 최강자전…서울서 '최후의 치킨' 겨룬다

### 8. 크래프톤 (259960)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [게임 레이더] 컴투스·크래프톤·넷마블, 신작 사전예약·e스포츠 개막... | 낙폭 커진 인터넷·게임주...증권가 "지금이 매수 기회" | 배틀그라운드 세계 최강자전…서울서 '최후의 치킨' 겨룬다

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 이엔플러스 (074610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-98.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-98.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -4. Negative keyword count is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 6월 19일 주식시장 주요공시 | 이엔플러스, 상폐 위기 속 경영권 분쟁…'경영진 교체' 요구 | 6월 18일 주식시장 주요공시

### 2. 더코디 (224060)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-62.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-62.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(자기전환사채매도결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 2. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 2차전지주 급락에 전기제품 업종 약세…LG에너지솔루션·삼성SDI 하락세... | [상한가 종목] 씨에스윈드-화신 이어 화신정공-씨에스베어링 등 마감 | [주식마감] 트럼프 풍력 규제 후퇴에 씨에스윈드 상한가… 씨에스베어링...

### 3. 블루엠텍 (439580)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-61.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-61.00**
- Risk level: **HIGH**
- Event type: `bond_with_warrant`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(신주인수권부사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bond_with_warrant. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [딜리셔스 IPO] 몸값 대신 상장 완주 택했다…FI도 손실 감수 | [주가] 6월 24일 주요 제약·바이오·기기 5% 변동 현황 - 38개사 증가 | 글로벌 시장 사로잡은 바이오 기술…HEM파마, 해외 매출 잭팟 터졌다

### 4. 하이즈항공 (221840)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-35.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-35.00**
- Risk level: **HIGH**
- Event type: `lawsuit`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 소송등의판결ㆍ결정              (회계장부 등 열람등사 신청)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is lawsuit. Initial direction is negative. Event score is -75. News attention score is 5. News sentiment score is 8. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 우주항공·국방주 차익실현 본격화…지금이 매수 기회일까 | 유동주식 실종된 일정실업, 자산총액 대조군 대비 '극단적 저평가' 부각 | K-UAM 상용화의 열쇠…파이버프로, 차세대 모빌리티 필수재로 수혜 기대

### 5. 체시스 (033250)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **11.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **11.00**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 신종 감염병 우려에 진단키트株 꿈틀…수혜주 찾아라 | [공시] 가이아코퍼레이션·보해양조 '거래정지 예고', 비씨엔씨·팸텍 등... | 체시스, 소수계좌 거래집중 지정→투자주의 경고

### 6. 큐라티스 (348080)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **38.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **38.00**
- Risk level: **HIGH**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주권매매거래정지              (주식의 병합, 분할 등 전자등록 변경, 말소)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 큐라티스, 내달 1일부터 주권매매거래 정지 | 큐라티스, 주식 병합 및 분할→주권매매거래 정지 결정 | 바이오 생태계 확장 수혜…인바이츠바이오코아, 독보적 플랫폼 가치 재...

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
