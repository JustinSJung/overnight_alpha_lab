# Daily Stock Candidate Report - 2026-07-09

Generated at: 2026-07-09 23:41:02

ML dataset: `data/processed/ml_dataset_20260709.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 000520 | 삼일제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001470 | 삼부토건 | 13 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002020 | 코오롱 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002070 | 비비안 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002780 | 진흥기업 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 002880 | 디와이에이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003060 | 에이프로젠바이오로직스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003070 | 코오롱글로벌 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003350 | 한국화장품제조 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003470 | 유안타증권 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003490 | 대한항공 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 004440 | 삼일씨엔에스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 25 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 7 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 17 | 0 | N/A | Not available | 0.00 |
| lawsuit | 26 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 51 | 0 | N/A | Not available | 0.00 |
| merger | 9 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 38 | 0 | N/A | Not available | 0.00 |
| spin_off | 1 | 0 | N/A | Not available | 0.00 |
| supply_contract | 68 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 25 | 0 | 0 | 25 | 0.00 |
| disclosure_violation | 7 | 0 | 0 | 7 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 17 | 0 | 0 | 17 | 0.00 |
| lawsuit | 26 | 0 | 0 | 26 | 0.00 |
| major_shareholder_change | 51 | 0 | 0 | 51 | 0.00 |
| merger | 9 | 0 | 0 | 9 | 0.00 |
| paid_in_capital_increase | 38 | 0 | 0 | 38 | 0.00 |
| spin_off | 1 | 0 | 0 | 1 | 0.00 |
| supply_contract | 68 | 0 | 0 | 68 | 0.00 |

## Positive Candidates

### 1. 동신건설 (025950)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **180.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **180.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 18. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [이 시각 시황] 코스피 7,500선 붕괴…화장품·AI 강세 속 증시 조정 지... | 남화토건, 굳건한 토목·건축 경쟁력으로 정책 수혜 정조준 | [특징주] '4800조 메가 프로젝트' 기대감에 진흥기업·일성건설 '上'

### 2. 에이스토리 (241840)

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
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 10일 개장 전 주요 공시 | [특징주] 에이스토리, 스튜디오드래곤과 12부작 신작 계약…글로벌 판권... | [특징주] 에이스토리, 스튜디오드래곤과 '수성궁밀회록' 12부작 공급계약

### 3. 코오롱글로벌 (003070)

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
- Related news examples: [코스피·코스닥, 코오롱글로벌  HD현대중공업 신테카바이오 한진 TJ미디... | 코오롱생명과학 "ESG 고도화·온실가스 감축" | [N2 모닝 경제 브리핑-7월 10일] 美 증시, AI 반도체 훈풍 속 3대지수 상...

### 4. 코오롱 (002020)

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
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '중학생 강연서-15발 만발 박정윤' 韓 여자 컴파운드 대표팀, 중국 꺾고... | [코스피·코스닥, 코오롱글로벌  HD현대중공업 신테카바이오 한진 TJ미디... | [역사속 오늘·7.10] 당포해전 승리(1592)·한국전쟁 휴전회담 시작(1951)...

### 5. 다스코 (058730)

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
- Related news examples: [26.7.9 증시 인싸잇] 오늘의 특징주 - 증시 급락 속 호남 반도체 메가 ... | 다스코 주가, 7월 9일 장중 5,320원 2.31% 상승 | [서울데이터랩]코스피 거래상위 종목 혼조…한성기업 상한가·금호건설...

### 6. 다스코 (058730)

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
- Related news examples: [26.7.9 증시 인싸잇] 오늘의 특징주 - 증시 급락 속 호남 반도체 메가 ... | 다스코 주가, 7월 9일 장중 5,320원 2.31% 상승 | [서울데이터랩]코스피 거래상위 종목 혼조…한성기업 상한가·금호건설...

## Volatile Watchlist

### 1. 프로티나 (468530)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **85.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **85.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (항체 바이오베터 공동기술개발 및 기술이전 옵션 계약 체결)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 10. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [프리마켓 포커스] SK하이닉스 'IPO 대박'·뉴욕증시 훈풍에 개장 전 3% ... | 삼성바이오에피스, 프로티나와 AI 항체 신약개발 '속도' | 삼성바이오에피스-프로티나, AI 항체 신약 개발 후속계약 체결

### 2. 젠큐릭스 (229000)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **55.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [의료기기업계 소식] 7월 7일 | 젠큐릭스 "복지부 '저출산 극복 기술개발' 선정…차세대 산전진단 개발... | 젠큐릭스, 경영권 매각 '없다'…공식 부인

### 3. 유안타증권 (003470)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **42.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: "브로커리지 넘어 WM까지"…유안타증권 '체질 개선' 속도 | 미래에셋증권, 증권사 브랜드평판 2026년 7월...1위 | 은행보다 돈 많은 하이닉스…미래에셋 1.26조 CP 인수

### 4. 아틀라스링크 (297570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **12.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **12.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 10일 개장 전 주요 공시 | 저궤도 위성 경쟁 치열, 국내 개발 상황은? | 아틀라스링크, 최대주주 변경…미래산업 주식회사 등

### 5. 아틀라스링크 (297570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **12.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **12.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 10일 개장 전 주요 공시 | 저궤도 위성 경쟁 치열, 국내 개발 상황은? | 아틀라스링크, 최대주주 변경…미래산업 주식회사 등

### 6. 아틀라스링크 (297570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **12.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **12.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 10일 개장 전 주요 공시 | 저궤도 위성 경쟁 치열, 국내 개발 상황은? | 아틀라스링크, 최대주주 변경…미래산업 주식회사 등

### 7. 아틀라스링크 (297570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **12.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **12.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 10일 개장 전 주요 공시 | 저궤도 위성 경쟁 치열, 국내 개발 상황은? | 아틀라스링크, 최대주주 변경…미래산업 주식회사 등

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 2. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 3. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 4. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 5. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 6. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 7. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 8. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 9. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

### 10. 한울앤제주 (276730)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-29.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 10. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 경기 불황 뚫는 70년 관록… '주정 대장' 풍국주정, 안정적 실적 기대감... | 냉동김밥 수출 기대감에 김밥주 강세…한성기업 주가 파죽지세 | 지구온난화 장기화에 멈추지 않는 랠리... 여름 테마 '슈퍼 사이클' 진입...

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
