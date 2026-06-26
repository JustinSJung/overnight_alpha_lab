# Daily Stock Candidate Report - 2026-06-26

Generated at: 2026-06-26 16:39:48

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
| 214150 | 클래시스 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 079900 | 전진건설로봇 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 083790 | CG인바이츠 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 096240 | 크레버스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 097780 | 에코볼트 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 105550 | 엣지파운드리 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 105560 | KB금융 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 123690 | 한국화장품 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 138360 | 앤로보틱스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 142760 | 모아라이프플러스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 186230 | 그린플러스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 13 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 6 | 0 | N/A | Not available | 0.00 |
| investment_decision | 5 | 0 | N/A | Not available | 0.00 |
| lawsuit | 3 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 13 | 0 | N/A | Not available | 0.00 |
| merger | 2 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 16 | 0 | N/A | Not available | 0.00 |
| spin_off | 1 | 0 | N/A | Not available | 0.00 |
| supply_contract | 15 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | 0 | 1 | 0.00 |
| convertible_bond | 13 | 0 | 0 | 13 | 0.00 |
| disclosure_violation | 6 | 0 | 0 | 6 | 0.00 |
| investment_decision | 5 | 0 | 0 | 5 | 0.00 |
| lawsuit | 3 | 0 | 0 | 3 | 0.00 |
| major_shareholder_change | 13 | 0 | 0 | 13 | 0.00 |
| merger | 2 | 0 | 0 | 2 | 0.00 |
| paid_in_capital_increase | 16 | 0 | 0 | 16 | 0.00 |
| spin_off | 1 | 0 | 0 | 1 | 0.00 |
| supply_contract | 15 | 0 | 0 | 15 | 0.00 |

## Positive Candidates

### 1. 금양그린파워 (282720)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **124.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 한화솔루션·씨에스윈드 급락…에너지 테마 투자심리 얼어붙었다 | [52주] 최고가 2개, 최저가 726개 ... 지수 하락 | 금양그린파워, AI 데이터센터발 전력 대란 속 '신재생 EPC' 핵심 부상

### 2. 케일럼 (258610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **124.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 조선·에너지 다 잘한다…SK오션플랜트, 해양플랜트 노하우로 몸값 재평... | 폴더블폰 시장 다시 달아오른다… 수혜주 어디가 뜰까 | [이넷뉴스 브랜드평판] 삼성중공업, 액화천연가스 LNG 6월 1위···HD한국...

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

### 4. 그린플러스 (186230)

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
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 네이버, AI탭 정식 출시…그린닷 대신 AI 검색 전면에 | [재계 투데이] 삼성전자 감사페스티벌, 소비자 막바지 관심 고조 外 | 네이버, 대화형 검색 ‘AI탭’ 정식 출시

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

### 1. 유안타증권 (003470)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **47.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [더벨][Market Watch] 기지개 켜는 롱숏 하우스…리테일 관심 증가세 | 한화, 한화솔루션 유증 앞두고 자구안 잇달아 실행...재무구조 개선 가... | LG CNS, 엔비디아와 '파주 AIDC' 투입 로봇 훈련·제어 맡나

### 2. 클래시스 (214150)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **20.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **20.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스닥 외국인] 주성엔지니어링 파두 대한광통신 에코프로 에코프로비... | 의료기기 상장기업 2026년 6월 브랜드평판...리가켐바이오, 파마리서치... | 리가켐바이오, 6월 의료기기 상장기업 브랜드평판 1위…파마리서치·클...

### 3. 클래시스 (214150)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **20.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **20.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스닥 외국인] 주성엔지니어링 파두 대한광통신 에코프로 에코프로비... | 의료기기 상장기업 2026년 6월 브랜드평판...리가켐바이오, 파마리서치... | 리가켐바이오, 6월 의료기기 상장기업 브랜드평판 1위…파마리서치·클...

### 4. 클래시스 (214150)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **20.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **20.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스닥 외국인] 주성엔지니어링 파두 대한광통신 에코프로 에코프로비... | 의료기기 상장기업 2026년 6월 브랜드평판...리가켐바이오, 파마리서치... | 리가켐바이오, 6월 의료기기 상장기업 브랜드평판 1위…파마리서치·클...

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 페니트리움바이오 (187660)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-94.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-94.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 권리락              (유상증자)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -3. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 페니트리움바이오, "최대주주 거래 없다" 반복…금감원 '이해상충' 우려... | 류마티스 권위자 파이어스타인 교수, AI 항암 신약 '페니트리움' 임상 합... | 파이어스타인 교수, 생성형 AI 기반 항암 신약후보 '페니트리움' 임상 합...

### 2. SK아이이테크놀로지 (361610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-91.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-91.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 유상증자결정(종속회사의주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 0. Negative keyword count is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 2차전지주 급락에 전기제품 업종 약세…LG에너지솔루션·삼성SDI 하락세... | 증시 활황에 주식 계좌도 폭증…올해만 1000만개 넘게 늘었다 | 2차전지 관련주 혼조세…삼성SDI 선방, 소재·장비주는 차익실현

### 3. KB금융 (105560)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-84.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-84.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 유상증자결정(자회사의 주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is -1. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: KB증권, 1조원 규모 주주배정 유상증자 결정 | KB증권, 1조원 규모 유상증자…KB금융, 생산적 금융 박차 | KB증권 1조원 유상증자 단행…"IB·트레이딩 경쟁력 강화"

### 4. 케이비증권 (003450)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-53.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-53.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 코스피200 변동성지수 급등, '한국형 공포지수' 사상 최고 근접 | '포스코 관심' 하안주공3·4단지, 시공자 수의계약 입찰 | 스페이스X 시총 2.5조$? 미 증시, ‘광기 국면’ 진입했나

### 5. 제이에스코퍼레이션 (194370)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-50.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 섬유의류 상장기업 2026년 6월 브랜드평판...한섬, 영원무역, F&F 順 | 한섬 독주 체제 강화…소통지수 상승이 만든 결과 | [브랜드평판] 한섬, 섬유의류 상장기업 6월 1위···영원무역·F&F 뒤쫓...

### 6. 앤로보틱스 (138360)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-46.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-46.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 증권발행결과(자율공시)              (제3자배정 유상증자)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 서암기계공업 계양전기 주가 폭등랠리… AI 시대 로봇주 폭발, 다음 주인... | 스마트팩토리 대전환 수혜…씨피시스템, 산업용 로봇 보호 시스템 독점... | AMAT도 반했네…티로보틱스, 자율주행 물류로봇 '돌풍'

### 7. 블루산업개발 (006740)

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
- Related news examples: 모빌리티 플랫폼은 차세대 게임 마켓이 될 수 있을까? | 국립부경대, 부산 앵커사업 1차 연차평가 부산 유일 S등급 1위 | 한국형 장거리 자폭 드론 전력화 추진…50만 드론 전사 양성

### 8. 블루산업개발 (006740)

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
- Related news examples: 모빌리티 플랫폼은 차세대 게임 마켓이 될 수 있을까? | 국립부경대, 부산 앵커사업 1차 연차평가 부산 유일 S등급 1위 | 한국형 장거리 자폭 드론 전력화 추진…50만 드론 전사 양성

### 9. 블루산업개발 (006740)

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
- Related news examples: 모빌리티 플랫폼은 차세대 게임 마켓이 될 수 있을까? | 국립부경대, 부산 앵커사업 1차 연차평가 부산 유일 S등급 1위 | 한국형 장거리 자폭 드론 전력화 추진…50만 드론 전사 양성

### 10. 티에스아이 (277880)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **96.00**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 증시일정] 현대홈쇼핑ㆍYTN 등 | 2차전지 관련주 혼조세…삼성SDI 선방, 소재·장비주는 차익실현 | 메모리 호황 올라탄 심텍, HPC 시장 성장세에 실적 턴어라운드 본격화

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
