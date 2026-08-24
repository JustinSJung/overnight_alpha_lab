# Daily Stock Candidate Report - 2026-08-24

Generated at: 2026-08-24 22:51:41

ML dataset: `data/processed/ml_dataset_20260824.csv`

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
| 000950 | 전방 | 5 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 0009K0 | 에임드바이오 | 3 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001040 | CJ | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001060 | JW중외제약 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001260 | 남광토건 | 4 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001340 | PKC | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 001420 | 태원물산 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 212 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 41 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| investment_decision | 87 | 0 | N/A | Not available | 0.00 |
| lawsuit | 87 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 309 | 0 | N/A | Not available | 0.00 |
| merger | 49 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 191 | 0 | N/A | Not available | 0.00 |
| spin_off | 12 | 0 | N/A | Not available | 0.00 |
| supply_contract | 173 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 212 | 0 | 0 | 212 | 0.00 |
| disclosure_violation | 41 | 0 | 0 | 41 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 87 | 0 | 0 | 87 | 0.00 |
| lawsuit | 87 | 0 | 0 | 87 | 0.00 |
| major_shareholder_change | 309 | 0 | 0 | 309 | 0.00 |
| merger | 49 | 0 | 0 | 49 | 0.00 |
| paid_in_capital_increase | 191 | 0 | 0 | 191 | 0.00 |

## Positive Candidates

### 1. 세미파이브 (490470)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **147.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **147.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-8월 25일] 美 증시, 국채금리 하락에도 AI주 매도…... | [마감시황]코스닥, 1.42% 올라 813.33 마감…2차전지 강세에 반등 | 삼성 파운드리 훈풍 타고…국내 DSP 5곳, 반년만에 작년 매출 70% 채웠다

### 2. 에스비비테크 (389500)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **129.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **129.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-8월 25일] 美 증시, 국채금리 하락에도 AI주 매도…... | "일본산 넘어선다"…에스비비테크, 하모닉 감속기 국산화로 승부 | 에스비비테크, 국내 로봇 제조회사와 휴머노이드 로봇용 정밀 감속기 공...

### 3. 코오롱글로벌 (003070)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **125.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 포항 도시정비사업 '공사비·미분양' 이중고…시공사 선정·착공은 하세... | 씨지인사이드, 아라미드 공정 '비전 AI 계측' 국책과제 선정 | [기자의눈] 훈풍 올라탄 K-바이오…'팔로워' 넘어 '리더'로

### 4. 코오롱글로벌 (003070)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **125.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 포항 도시정비사업 '공사비·미분양' 이중고…시공사 선정·착공은 하세... | 씨지인사이드, 아라미드 공정 '비전 AI 계측' 국책과제 선정 | [기자의눈] 훈풍 올라탄 K-바이오…'팔로워' 넘어 '리더'로

### 5. 코오롱글로벌 (003070)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **125.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 포항 도시정비사업 '공사비·미분양' 이중고…시공사 선정·착공은 하세... | 씨지인사이드, 아라미드 공정 '비전 AI 계측' 국책과제 선정 | [기자의눈] 훈풍 올라탄 K-바이오…'팔로워' 넘어 '리더'로

### 6. 코오롱글로벌 (003070)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **125.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 포항 도시정비사업 '공사비·미분양' 이중고…시공사 선정·착공은 하세... | 씨지인사이드, 아라미드 공정 '비전 AI 계측' 국책과제 선정 | [기자의눈] 훈풍 올라탄 K-바이오…'팔로워' 넘어 '리더'로

### 7. HS화성 (002460)

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
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 대구 태왕이앤씨, 건설 불황 못넘고 결국 회생절차 | 대구 3대 건설사 태왕 결국 법정관리…지역 건설업계 ‘충격’ | [BBS PLAZA]HS화성 자원봉사단, 치매 어르신 시설 찾아 환경개선 봉사…...

### 8. 엔시스 (333620)

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
- Related news examples: [공시] 25일, 코스닥 상장사 78개 종목 자사주 매수 신청 | 지주사 할인 해제되나… 솔브레인홀딩스, 알짜 계열사 지분 가치 부각 | [공시] 브이티·에스티오·씨유테크 등...24일 코스닥 76개 종목 '자사주...

### 9. 동부건설 (005960)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **100.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 기술형입찰 설계심의 ‘슈퍼 위크’ | 포항 도시정비사업 '공사비·미분양' 이중고…시공사 선정·착공은 하세... | 동부건설 '로얄캐닌 김제공장' 공사기간 또 연장..10월 말까지

### 10. 동부건설 (005960)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **100.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 기술형입찰 설계심의 ‘슈퍼 위크’ | 포항 도시정비사업 '공사비·미분양' 이중고…시공사 선정·착공은 하세... | 동부건설 '로얄캐닌 김제공장' 공사기간 또 연장..10월 말까지

## Volatile Watchlist

### 1. 케이바이오랩스 (038530)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **52.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **52.00**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주권매매거래정지              (주식의 병합, 분할 등 전자등록 변경, 말소)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 케이바이오랩스, 주식병합에 따른 주권매매거래 정지 결정 | 진단키트·백신 개발사 수급 쏠림…셀리드·신풍제약 폭등랠리 주목 | '글로벌 빅파마' 눈독… 셀리드, 자체 백신 기술이전 대박 터지나

### 2. 유안타증권 (003470)

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
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 에코프로비엠, 헝가리공장 개조 착수…유럽 완성차에 양극재 공급 | [Invest]증시 랠리에 PB만 웃은 줄 알았더니…'연봉킹' 꿰찬 IB맨들 | “SK하이닉스 성과급 안 부러워”… ‘극단의 성과주의’에 MZ들 은행보...

### 3. 삼성물산 (028260)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **19.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **19.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 엇갈린 그룹주…‘주주환원’ 삼성 울고 2차전지 훈풍 포스코 웃었다 [... | [Who Is ?] 김영대 대성산업 회장 | ‘핫플’ 넘어 핵심 업무지구로…강남·판교 기업 끌어당기는 성수동 [...

### 4. 케이씨 (029460)

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
- Related news examples: [거버넌스워치] ‘주식 부호’ 케이씨 맏딸 고유현, 비상장 KC이앤씨株... | [거버넌스워치] 케이씨그룹 활동 반경 넓히는 딸과 사위…분가 구도는? | 횡성케이씨 도축장에 '전자출하시스템' 도입

### 5. 원림 (005820)

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
- Related news examples: [공시]원림 최대주주 일가 지분 승계 본격화 | 폭우 피해 거제에 온정 이어진다···유통업계, 구호물품 지원 잇따라 | 원림, 거제시 수해복구에 산업용 포장백 1만 장 지원

### 6. 원림 (005820)

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
- Related news examples: [공시]원림 최대주주 일가 지분 승계 본격화 | 폭우 피해 거제에 온정 이어진다···유통업계, 구호물품 지원 잇따라 | 원림, 거제시 수해복구에 산업용 포장백 1만 장 지원

### 7. 원림 (005820)

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
- Related news examples: [공시]원림 최대주주 일가 지분 승계 본격화 | 폭우 피해 거제에 온정 이어진다···유통업계, 구호물품 지원 잇따라 | 원림, 거제시 수해복구에 산업용 포장백 1만 장 지원

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 넥사다이내믹스 (351320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-49.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-49.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(자기전환사채만기전취득결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, HD한국조선해양 셀트리온 에코프로에이치엔 한미약품... | 코스피·코스닥지수, 주요 기업 공시 잇따라…대규모 유증부터 조선 수... | [공시] 인바이츠바이오코아 '거래정지', 네오이뮨텍·안지오랩 '투자경...

### 2. 넥사다이내믹스 (351320)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-49.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-49.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(자기전환사채만기전취득결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [코스피·코스닥, HD한국조선해양 셀트리온 에코프로에이치엔 한미약품... | 코스피·코스닥지수, 주요 기업 공시 잇따라…대규모 유증부터 조선 수... | [공시] 인바이츠바이오코아 '거래정지', 네오이뮨텍·안지오랩 '투자경...

### 3. 컴투스엔 (291230)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-36.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-36.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (전환사채 인수계약 조건 일부 변경)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [속보] 컴투스엔 주가, 합병 승계 전환사채 조건 변경 | [속보] 컴투스엔, 전환사채 인수계약 조건 일부 변경…만기보장수익률... | [공시] 인바이츠바이오코아·좋은사람들·탑코미디어 '투자경고' 등...7...

### 4. 모아데이타 (288980)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **8.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **8.00**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시] 인바이츠바이오코아 '거래정지', 네오이뮨텍·안지오랩 '투자경... | 모아데이타, 단일계좌 거래량 상위 종목으로 투자주의종목 지정 | [주식마감] 코로나19 재확산 우려에 '제약주' 강세... 신풍제약, 셀리드...

### 5. 비츠로시스 (054220)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **13.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **13.00**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식담보제공계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 4. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: AI 전력 수요 늘어나는데 스마트그리드주는 왜 밀리나 | 비츠로셀, 차세대 특수전지 경쟁력으로 밸류에이션 재평가 | 전력망부터 신호·건설까지... 철도 인프라 밸류체인 전반 매수 온기 확...

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
