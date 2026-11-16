# Daily Stock Candidate Report - 2026-11-16

Generated at: 2026-11-16 02:53:25

ML dataset: `data/processed/ml_dataset_20261116.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 248170 | 샘표식품 | 22 | 22 | 95.45% | 26.45% | relatively_positive_history | 8.89 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 862 | 766 | 46.21% | 5.01% | 4.00 |
| convertible_bond | 1569 | 1236 | 56.47% | 0.52% | 3.00 |
| investment_decision | 599 | 484 | 50.83% | 0.21% | 0.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| paid_in_capital_increase | 2906 | 2385 | 54.88% | -0.12% | 0.00 |
| lawsuit | 613 | 492 | 48.58% | -0.26% | 0.00 |
| disclosure_violation | 217 | 147 | 41.50% | -0.48% | -3.00 |
| bond_with_warrant | 161 | 149 | 42.28% | 0.01% | -3.00 |
| spin_off | 155 | 119 | 39.50% | 0.89% | -3.00 |
| major_shareholder_change | 3158 | 2524 | 37.84% | -0.67% | -3.00 |
| supply_contract | 1786 | 1460 | 36.44% | -0.57% | -3.00 |
| earnings_guidance | 90 | 86 | 23.26% | -1.74% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1569 | 698 | 538 | 333 | 1.20 |
| paid_in_capital_increase | 2906 | 1309 | 1076 | 521 | 1.14 |
| lawsuit | 613 | 239 | 253 | 121 | 0.71 |
| bond_with_warrant | 161 | 63 | 86 | 12 | 0.35 |
| disclosure_violation | 217 | 61 | 86 | 70 | 0.22 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 599 | 246 | 238 | 115 | -0.73 |
| supply_contract | 1786 | 532 | 928 | 326 | -0.90 |
| merger | 862 | 354 | 412 | 96 | -1.29 |
| earnings_guidance | 90 | 20 | 66 | 4 | -1.71 |

## Positive Candidates

### 1. 아티스트컴퍼니 (321820)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.00**
- Adjusted recommendation score: **97.10**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 0.21%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 1.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 데이원드림, 스튜디오힘과 사업 확장…STO 토큰도 공략 | 데이원드림, 스튜디오힘 결합...음악·드라마·배우 IP 사업 확대 | 한국타이어, 캐리어로 소비자 접점 넓혀..리드볼트 협업 제품 오프라인...

### 2. 아티스트컴퍼니 (321820)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.00**
- Adjusted recommendation score: **97.10**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 100.00%, avg next close: 0.21%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 1.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 데이원드림, 스튜디오힘과 사업 확장…STO 토큰도 공략 | 데이원드림, 스튜디오힘 결합...음악·드라마·배우 IP 사업 확대 | 한국타이어, 캐리어로 소비자 접점 넓혀..리드볼트 협업 제품 오프라인...

### 3. DL (000210)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.75**
- Adjusted recommendation score: **92.85**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 75.00%, avg next close: 1.39%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.30%
- Next close return data: -2.36%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.75 points. Stock pattern label is relatively_positive_history.
- Related news examples: LH, 하반기 공공주택 9000가구 민간참여 공모…"내년 착공 목표" | '美 항공대란' 사흘째 현지 결항·지연 여전…인천발 환승객도 불편 | LH, 남양주왕숙 등 민간참여 공공주택 9000호 공모 … 내년 첫 삽

## Volatile Watchlist

### 1. 진에어 (272450)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.29**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **1.00**
- Adjusted recommendation score: **53.71**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -2.06%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.51%
- Next close return data: -2.06%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.29 points. Event-type performance added 4.00 points. Stock-specific history added 1.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: "통합 LCC 제2허브는 실효성 없는 생색내기" | [비즈뉴스룸] 진에어·제주항공·세아제강·대한전선·현대로템·OCI 등 ... | 대한항공 정보 유출에 美 공항 마비까지 … 항공업계 덮친 '불안 경고등...

### 2. 진에어 (272450)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.29**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **1.00**
- Adjusted recommendation score: **53.71**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: -2.06%, pattern: relatively_positive_history
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -0.51%
- Next close return data: -2.06%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.29 points. Event-type performance added 4.00 points. Stock-specific history added 1.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: "통합 LCC 제2허브는 실효성 없는 생색내기" | [비즈뉴스룸] 진에어·제주항공·세아제강·대한전선·현대로템·OCI 등 ... | 대한항공 정보 유출에 美 공항 마비까지 … 항공업계 덮친 '불안 경고등...

### 3. 삼성전자 (005930)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.93**
- Adjusted recommendation score: **40.96**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 78.57%, avg next close: -1.76%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.20%
- Next close return data: -4.19%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.93 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주목 e-기업] '제2의 캐시카우' 부상 건물관리 '에스원'…"매출 9천억?... | 엔비디아 열풍 뒤에 숨은 빚더미… 월가가 경고한 2800조원 채권 폭탄 | '수능 D-3' 삼성전자·LG전자도 비상... "시험장 냉난방 설비 점검"

### 4. 삼성전자 (005930)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.93**
- Adjusted recommendation score: **40.96**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 78.57%, avg next close: -1.76%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.20%
- Next close return data: -4.19%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.93 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주목 e-기업] '제2의 캐시카우' 부상 건물관리 '에스원'…"매출 9천억?... | 엔비디아 열풍 뒤에 숨은 빚더미… 월가가 경고한 2800조원 채권 폭탄 | '수능 D-3' 삼성전자·LG전자도 비상... "시험장 냉난방 설비 점검"

### 5. 삼성전자 (005930)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.93**
- Adjusted recommendation score: **40.96**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 78.57%, avg next close: -1.76%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.20%
- Next close return data: -4.19%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.93 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주목 e-기업] '제2의 캐시카우' 부상 건물관리 '에스원'…"매출 9천억?... | 엔비디아 열풍 뒤에 숨은 빚더미… 월가가 경고한 2800조원 채권 폭탄 | '수능 D-3' 삼성전자·LG전자도 비상... "시험장 냉난방 설비 점검"

### 6. 삼성전자 (005930)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.93**
- Adjusted recommendation score: **40.96**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 78.57%, avg next close: -1.76%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.20%
- Next close return data: -4.19%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.93 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주목 e-기업] '제2의 캐시카우' 부상 건물관리 '에스원'…"매출 9천억?... | 엔비디아 열풍 뒤에 숨은 빚더미… 월가가 경고한 2800조원 채권 폭탄 | '수능 D-3' 삼성전자·LG전자도 비상... "시험장 냉난방 설비 점검"

### 7. 삼성전자 (005930)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.93**
- Adjusted recommendation score: **40.96**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 78.57%, avg next close: -1.76%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.20%
- Next close return data: -4.19%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.93 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주목 e-기업] '제2의 캐시카우' 부상 건물관리 '에스원'…"매출 9천억?... | 엔비디아 열풍 뒤에 숨은 빚더미… 월가가 경고한 2800조원 채권 폭탄 | '수능 D-3' 삼성전자·LG전자도 비상... "시험장 냉난방 설비 점검"

### 8. 삼성전자 (005930)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-1.97**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.93**
- Adjusted recommendation score: **40.96**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 78.57%, avg next close: -1.76%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.20%
- Next close return data: -4.19%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.97 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.93 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주목 e-기업] '제2의 캐시카우' 부상 건물관리 '에스원'…"매출 9천억?... | 엔비디아 열풍 뒤에 숨은 빚더미… 월가가 경고한 2800조원 채권 폭탄 | '수능 D-3' 삼성전자·LG전자도 비상... "시험장 냉난방 설비 점검"

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 아시아나항공 (020560)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-1.29**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-5.21**
- Adjusted recommendation score: **52.50**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: 0.22%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]회사합병결정(종속회사의주요경영사항)              
- Next open return data: 0.24%
- Next close return data: 1.67%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.29 points. Event-type performance added 4.00 points. Stock-specific history subtracted 5.21 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주] 아시아나IDT 주가, 10%대 급등... 이유는? | 일본서 한국 오는 국제선 항공권, 유류할증료 산정 기간 다르다…항공유... | 美 항공대란 여파 사흘째…국내 영향은 제한적

### 2. SK디스커버리 (006120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **51.00**
- Error-note adjustment score: **-0.73**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **5.22**
- Adjusted recommendation score: **55.49**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 7, success rate: 71.43%, avg next close: -0.94%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.00%
- Next close return data: -6.70%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 0.73 points. Event-type performance did not change the score. Stock-specific history added 5.22 points. Stock pattern label is relatively_positive_history.
- Related news examples: SK디스커버리, SK에코플랜트 PRS 7년 만에 정산 | '군살 뺀' SK, AI 서비스로 보폭 확장 | SK㈜ 완전자회사·중복상장 해소…SK디스커버리 5355억 확보

### 3. SK디스커버리 (006120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **51.00**
- Error-note adjustment score: **-0.73**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **5.22**
- Adjusted recommendation score: **55.49**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 7, success rate: 71.43%, avg next close: -0.94%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.00%
- Next close return data: -6.70%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 0.73 points. Event-type performance did not change the score. Stock-specific history added 5.22 points. Stock pattern label is relatively_positive_history.
- Related news examples: SK디스커버리, SK에코플랜트 PRS 7년 만에 정산 | '군살 뺀' SK, AI 서비스로 보폭 확장 | SK㈜ 완전자회사·중복상장 해소…SK디스커버리 5355억 확보

### 4. 에어부산 (298690)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-1.29**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **66.21**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 1.12%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: 0.06%
- Next close return data: 1.12%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.29 points. Event-type performance added 4.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "통합 LCC 제2허브는 실효성 없는 생색내기" | 진에어·에어서울·에어부산, 내년 3월 17일 '진에어'로 합친다 | 한진칼 “LCC 3사 통합 시너지 연 260억…주주가치 제고 기대”

### 5. 탑선 (180060)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.12**
- Adjusted recommendation score: **71.98**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 6. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [공시셀렉트] 대신증권, 공정위 과징금에 3분기 순손실 1338억으로…시너... | 대동금속 90.77%·한진칼 58.27% 상승…코스피 급락 속 강세 | 솔리다임發 유탄 맞은 SK에코플랜트 "중복상장 가이드라인 세부사항 검...

### 6. 탑선 (180060)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.12**
- Adjusted recommendation score: **71.98**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 6. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [공시셀렉트] 대신증권, 공정위 과징금에 3분기 순손실 1338억으로…시너... | 대동금속 90.77%·한진칼 58.27% 상승…코스피 급락 속 강세 | 솔리다임發 유탄 맞은 SK에코플랜트 "중복상장 가이드라인 세부사항 검...

### 7. 탑선 (180060)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.12**
- Adjusted recommendation score: **71.98**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 6. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [공시셀렉트] 대신증권, 공정위 과징금에 3분기 순손실 1338억으로…시너... | 대동금속 90.77%·한진칼 58.27% 상승…코스피 급락 속 강세 | 솔리다임發 유탄 맞은 SK에코플랜트 "중복상장 가이드라인 세부사항 검...

### 8. 탑선 (180060)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.12**
- Adjusted recommendation score: **71.98**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 6. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [공시셀렉트] 대신증권, 공정위 과징금에 3분기 순손실 1338억으로…시너... | 대동금속 90.77%·한진칼 58.27% 상승…코스피 급락 속 강세 | 솔리다임發 유탄 맞은 SK에코플랜트 "중복상장 가이드라인 세부사항 검...

### 9. 디티앤씨알오 (383930)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **88.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-4.28**
- Adjusted recommendation score: **79.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 5.88%, avg next close: 1.05%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 6.17%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 4. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 4.28 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월13일 주식시장 주요공시 | 디티앤씨알오 3분기 흑자 전환…누적 영업손실 97억원 | 바이오 연구장비株도 희비… 생명과학도구 업종서 무슨 일?

### 10. 디티앤씨알오 (383930)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **88.00**
- Error-note adjustment score: **-0.90**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-4.28**
- Adjusted recommendation score: **79.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 5.88%, avg next close: 1.05%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 6.17%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 4. Historical error notes subtracted 0.90 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 4.28 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월13일 주식시장 주요공시 | 디티앤씨알오 3분기 흑자 전환…누적 영업손실 97억원 | 바이오 연구장비株도 희비… 생명과학도구 업종서 무슨 일?

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
