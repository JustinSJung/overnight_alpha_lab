# Daily Stock Candidate Report - 2026-07-16

Generated at: 2026-07-16 23:14:10

ML dataset: `data/processed/ml_dataset_20260716.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
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
| 003070 | 코오롱글로벌 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 63 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 13 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 33 | 0 | N/A | Not available | 0.00 |
| lawsuit | 40 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 76 | 0 | N/A | Not available | 0.00 |
| merger | 18 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 57 | 0 | N/A | Not available | 0.00 |
| spin_off | 2 | 0 | N/A | Not available | 0.00 |
| supply_contract | 76 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | 0 | 1 | 0.00 |
| convertible_bond | 63 | 0 | 0 | 63 | 0.00 |
| disclosure_violation | 13 | 0 | 0 | 13 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 33 | 0 | 0 | 33 | 0.00 |
| lawsuit | 40 | 0 | 0 | 40 | 0.00 |
| major_shareholder_change | 76 | 0 | 0 | 76 | 0.00 |
| merger | 18 | 0 | 0 | 18 | 0.00 |
| paid_in_capital_increase | 57 | 0 | 0 | 57 | 0.00 |
| spin_off | 2 | 0 | 0 | 2 | 0.00 |

## Positive Candidates

### 1. HJ중공업 (097230)

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
- Related news examples: HJ중공업, 폭염 현장 안전 강화...협력사 근무환경도 개선 | 수박 300통 들고 현장으로…혹서기 직원 격려 나선 HJ중공업 | HJ중공업 현장 경영…협력사와 ‘수박 소통’

## Volatile Watchlist

### 1. 삼영무역 (002810)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **50.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [리스트] 국내 고배당주 30선 | 단순히 디스플레이 소재 기업인 줄 알았는데…한솔케미칼, AI 반도체 핵... | 화학 상장기업 브랜드평판 7월 빅데이터 분석... 1위 에코프로, 2위 LG화...

### 2. 삼영무역 (002810)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **50.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [리스트] 국내 고배당주 30선 | 단순히 디스플레이 소재 기업인 줄 알았는데…한솔케미칼, AI 반도체 핵... | 화학 상장기업 브랜드평판 7월 빅데이터 분석... 1위 에코프로, 2위 LG화...

### 3. 아진전자부품 (009320)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **40.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 영흥, 철강 넘어 미래차 소재 기업 도약… 고부가가치 선재 공급망 풀가... | 자동차부품 브랜드 1위 현대모비스…한온시스템·한국타이어앤테크놀로... | 시총 4조6천억원 증발, 전북 증시 '20조 방어선' 붕괴

### 4. 진원생명과학 (011000)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **29.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [HIT알공] 진원생명과학, 자회사 생산 중단에 8월 7일까지 거래정지 | [속보] 진원생명과학 "VGXI CDMO 상반기 생산 유보…CDMO 매출 0원" | 진원생명과학 핵심 자회사 VGXI 생산 멈췄나…거래소, 상반기 매출까지...

### 5. 진원생명과학 (011000)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **29.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **29.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [HIT알공] 진원생명과학, 자회사 생산 중단에 8월 7일까지 거래정지 | [속보] 진원생명과학 "VGXI CDMO 상반기 생산 유보…CDMO 매출 0원" | 진원생명과학 핵심 자회사 VGXI 생산 멈췄나…거래소, 상반기 매출까지...

### 6. 동일산업 (004890)

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
- Related news examples: 중소형 철강주 펄펄 끓는다…건설·인프라 투자 기대 반영 | 올 상반기 산재사망 253명…통계 작성 이후 최저 | 상반기 산업재해 사망 253명…역대 최대 감소에도 대형 제조업서↑

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 씨씨에스 (066790)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-116.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-116.00**
- Risk level: **HIGH**
- Event type: `lawsuit`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 소송등의판결ㆍ결정              (이사 해임 등 청구의 소)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is lawsuit. Initial direction is negative. Event score is -75. News attention score is 5. News sentiment score is -4. Negative keyword count is 7. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 증시일정] 엔피·위지웍스튜디오·한국제지·동원금속 등 | 충청권 상장사 불성실공시 잇따라…신뢰성 높일 유인책 필요 | 7월 8일 주식시장 주요공시

### 2. 이상네트웍스 (080010)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-91.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-91.00**
- Risk level: **HIGH**
- Event type: `disclosure_violation`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 불성실공시법인미지정              (지정유예)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is disclosure_violation. Initial direction is negative. Event score is -80. News attention score is 5. News sentiment score is -1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 이상네트웍스, 불성실공시법인 지정유예→6개월간 재발 시 지정전환 | 탄산, 산소 등 공급부족 따른 대책 논의 | 티플랙스, 희귀금속·STS 절삭가공 독주…반도체·조선 훈풍에 실적 '가...

### 3. 시선AI (340810)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: ‘300만닉스’ 첫 칸 맞췄다…SK하이닉스, TSMC 훈풍에도 엇갈린 전망 | [허아은의 편한숏] 영화관에서 보는 영화의 쓸모, '호프' | [AI 10년 전 오늘] 영동고속도로 봉평터널서 6중 추돌…20명 사상 참사

### 4. 상지건설 (042940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-65.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-65.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 혈연 아닌 후배에게 경영 ‘바통’…상지건축 신뢰의 승계 | 국군사관학교가 바꿀 자운대 미래지도 | 여경협 강원지회 창립27주년 기념행사…여성경제인 능력 제고·경쟁력 ...

### 5. 우성머티리얼스 (011300)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-54.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-54.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 원가 절감과 고부가가치 제품 다변화…섬유·의류 업종 재평가 국면 | 코스피, 외국인·기관 순매수에 6.85% 급등…7천선 재탈환 성공 | [EBN 데이터센터] 14일 상승 종목 30選…애국매수에 모나미·한성기업 강...

### 6. 우성머티리얼스 (011300)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-54.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-54.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 원가 절감과 고부가가치 제품 다변화…섬유·의류 업종 재평가 국면 | 코스피, 외국인·기관 순매수에 6.85% 급등…7천선 재탈환 성공 | [EBN 데이터센터] 14일 상승 종목 30選…애국매수에 모나미·한성기업 강...

### 7. 한울반도체 (320000)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-40.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-40.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 인사 : 7월 16일] KBS·오늘경제·서울대병원·연세대학교 의료... | [인사] 의정부시, 부산시, 충남 당진시 외 | 한울반도체 주가, 7월 16일 13,080원 10.75% 상승 마감

### 8. 한울반도체 (320000)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-40.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-40.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 인사 : 7월 16일] KBS·오늘경제·서울대병원·연세대학교 의료... | [인사] 의정부시, 부산시, 충남 당진시 외 | 한울반도체 주가, 7월 16일 13,080원 10.75% 상승 마감

### 9. 한울반도체 (320000)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-40.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-40.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 인사 : 7월 16일] KBS·오늘경제·서울대병원·연세대학교 의료... | [인사] 의정부시, 부산시, 충남 당진시 외 | 한울반도체 주가, 7월 16일 13,080원 10.75% 상승 마감

### 10. 한울반도체 (320000)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-40.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-40.00**
- Risk level: **HIGH**
- Event type: `paid_in_capital_increase`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(유상증자결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is paid_in_capital_increase. Initial direction is negative. Event score is -70. News attention score is 5. News sentiment score is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 인사 : 7월 16일] KBS·오늘경제·서울대병원·연세대학교 의료... | [인사] 의정부시, 부산시, 충남 당진시 외 | 한울반도체 주가, 7월 16일 13,080원 10.75% 상승 마감

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
