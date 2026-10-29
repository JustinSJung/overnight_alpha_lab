# Daily Stock Candidate Report - 2026-10-05

Generated at: 2026-10-05 01:19:30

ML dataset: `data/processed/ml_dataset_20261005.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 3 | 3 | 100.00% | 9.98% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 010950 | S-Oil | 9 | 9 | 88.89% | 5.68% | relatively_positive_history | 8.72 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 348 | 231 | 58.87% | -0.61% | 3.00 |
| paid_in_capital_increase | 1704 | 1299 | 57.81% | 0.33% | 3.00 |
| bonus_issue | 79 | 76 | 53.95% | 0.64% | 0.00 |
| convertible_bond | 887 | 589 | 53.48% | 0.69% | 0.00 |
| disclosure_violation | 129 | 74 | 51.35% | -0.13% | 0.00 |
| investment_decision | 353 | 240 | 51.25% | 0.26% | 0.00 |
| merger | 277 | 186 | 26.88% | 1.34% | -4.00 |
| bond_with_warrant | 74 | 63 | 9.52% | 0.01% | -6.00 |
| major_shareholder_change | 1685 | 1120 | 34.11% | -0.86% | -6.00 |
| spin_off | 83 | 53 | 30.19% | 0.50% | -6.00 |
| supply_contract | 974 | 674 | 29.82% | -0.65% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1704 | 751 | 548 | 405 | 1.24 |
| lawsuit | 348 | 136 | 95 | 117 | 1.14 |
| convertible_bond | 887 | 315 | 274 | 298 | 0.85 |
| disclosure_violation | 129 | 38 | 36 | 55 | 0.64 |
| bonus_issue | 79 | 41 | 35 | 3 | -0.05 |
| investment_decision | 353 | 123 | 117 | 113 | -0.58 |
| supply_contract | 974 | 201 | 473 | 300 | -1.16 |
| bond_with_warrant | 74 | 6 | 57 | 11 | -1.91 |
| major_shareholder_change | 1685 | 382 | 738 | 565 | -1.93 |

## Positive Candidates

### 1. 오픈엣지테크놀로지 (394280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **114.84**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 한미반도체 등 일부 HBM 관련주 '빨간불'…와이씨·윈팩 5%대 강세 | 반도체 IP 업계, 'K-온디바이스 국책 과제' 수혜 시작 | 오픈엣지테크놀로지, AI 반도체 기업과 67억 규모 계약 체결

### 2. 티에스아이 (277880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.17**
- Adjusted recommendation score: **112.67**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: -0.13%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.17 points. Stock pattern label is not_enough_data.
- Related news examples: 롯데에너지머티리얼즈 18%대 급등…대주전자재료·SK이노베이션 등 전고... | 이차전지·글라스기판 모멘텀… 전자장비주 동반 상승랠리 | 2차전지 장비업계, 수주 모멘텀 속 체질 개선 집중… 투자 전략은?

### 3. 티와이홀딩스 (363280)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.83**
- Adjusted recommendation score: **111.67**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.24%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: 태영건설, PF 보증채무 선제적 출자전환…재무구조 개선 '속도' | 9월 30일 주식시장 주요공시 | [개장 전 주요 공시] LS·한화솔루션·한화투자증권·한화생명 등

### 4. DL (000210)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.20**
- Adjusted recommendation score: **111.04**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.42%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.20 points. Stock pattern label is relatively_positive_history.
- Related news examples: [이슈] 산업 국감 '초읽기'…대미투자·반도체·석유화학 쟁점은 | 163㎞ 뚫었다! 밀워키, 샌디에이고에 9회말 2아웃 역전 끝내기 승리…밀... | [기획] 목동 재건축 시공사 윤곽…남은 수주전은?

### 5. DL (000210)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.20**
- Adjusted recommendation score: **111.04**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.42%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.20 points. Stock pattern label is relatively_positive_history.
- Related news examples: [이슈] 산업 국감 '초읽기'…대미투자·반도체·석유화학 쟁점은 | 163㎞ 뚫었다! 밀워키, 샌디에이고에 9회말 2아웃 역전 끝내기 승리…밀... | [기획] 목동 재건축 시공사 윤곽…남은 수주전은?

### 6. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.39**
- Adjusted recommendation score: **109.23**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 1.47%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 건설사, 로봇 기술 확보 속도전…단지 서비스부터 현장·신사업까지 | [기획] 목동 재건축 시공사 윤곽…남은 수주전은? | 대형 건설사 막판 정비사업 수주 총력, 2위 쟁탈 치열

### 7. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.39**
- Adjusted recommendation score: **109.23**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 1.47%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 건설사, 로봇 기술 확보 속도전…단지 서비스부터 현장·신사업까지 | [기획] 목동 재건축 시공사 윤곽…남은 수주전은? | 대형 건설사 막판 정비사업 수주 총력, 2위 쟁탈 치열

### 8. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.39**
- Adjusted recommendation score: **109.23**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 50.00%, avg next close: 1.47%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.39 points. Stock pattern label is not_enough_data.
- Related news examples: 건설사, 로봇 기술 확보 속도전…단지 서비스부터 현장·신사업까지 | [기획] 목동 재건축 시공사 윤곽…남은 수주전은? | 대형 건설사 막판 정비사업 수주 총력, 2위 쟁탈 치열

### 9. 태영건설 (009410)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.55**
- Adjusted recommendation score: **108.39**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: -0.02%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.55 points. Stock pattern label is relatively_positive_history.
- Related news examples: [증시 UP&DOWN]코스피 '칠천피' 분수령…실적주 압축 대응 필요 | 태영건설 '서부산의료원' 건립공사 수주…965억원 규모 | [2026 국감 레이더⑪] 코오롱글로벌_김영범 대표이사 사장, 하자판정 상...

### 10. 삼성바이오로직스 (207940)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.71**
- Adjusted recommendation score: **106.55**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 30, success rate: 70.00%, avg next close: -1.77%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.71 points. Stock pattern label is relatively_positive_history.
- Related news examples: 수주부터 기술수출까지…K-제약·바이오, CPHI서 해외 파트너 찾는다 | “밀라노·요코하마·샌디에이고로”…K-바이오, 10월 ‘3주 수주전’ | 美 의약품 관세 발효…삼성에피스, 테바와 시밀러 동맹 확대 [바이오 주...

## Volatile Watchlist

### 1. 듀켐바이오 (176750)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **64.00**
- Error-note adjustment score: **-2.53**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **57.47**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 2.53 points. Event-type performance subtracted 4.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 시흥에 투자하는 기업에 최대 6억원 보조금…공격적 투자유치 | [주식] HLB, '재료 소멸'에 차익실현 매물 출회...10% 급락 | 기업공시 [10월 2일]

### 2. 이노인스트루먼트 (215790)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **54.00**
- Error-note adjustment score: **-2.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **45.84**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주권매매거래정지              (주식의 병합, 분할 등 전자등록 변경, 말소)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 2.16 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 엑셈 등 3개사, 주식병합으로 8일부터 거래정지 | 통신장비주, 5G·6G 고도화 바람 타고 폭등랠리 | "통신망 다시 깐다"…AI 데이터센터에 통신장비주 '신바람'

### 3. CJ (001040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **45.00**
- Error-note adjustment score: **-0.58**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.05**
- Adjusted recommendation score: **44.47**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.61%, pattern: not_enough_data
- Disclosure title: 투자판단관련주요경영사항(자회사의 주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 0.58 points. Event-type performance did not change the score. Stock-specific history added 0.05 points. Stock pattern label is not_enough_data.
- Related news examples: 토스·CJ대한통운, 온·오프라인 묶어 생활물류 진출…결제 매장이 택배... | CJ제일제당이 만든 프리미엄 술 'jari', 뉴욕에 이어 LA까지..."美 공략 ... | 전라도 올리브영 매출 72% 뛰었다…무슨 일이

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 동아쏘시오홀딩스 (000640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-2.53**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-5.60**
- Adjusted recommendation score: **52.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.40%, pattern: weak_historical_reaction
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 2.53 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 5.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "인재 모셔라"…제약바이오, 임원급 영입 줄이어 | 동아오츠카, 낙동강생물자원관과 광려천 담수생물다양성 모니터링 | 동아제약 합병 마무리…피노라인 직접 자회사로

### 2. 동아쏘시오홀딩스 (000640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-2.53**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-5.60**
- Adjusted recommendation score: **52.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.40%, pattern: weak_historical_reaction
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 2.53 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 5.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "인재 모셔라"…제약바이오, 임원급 영입 줄이어 | 동아오츠카, 낙동강생물자원관과 광려천 담수생물다양성 모니터링 | 동아제약 합병 마무리…피노라인 직접 자회사로

### 3. 동아쏘시오홀딩스 (000640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-2.53**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-5.60**
- Adjusted recommendation score: **52.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.40%, pattern: weak_historical_reaction
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 2.53 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 5.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "인재 모셔라"…제약바이오, 임원급 영입 줄이어 | 동아오츠카, 낙동강생물자원관과 광려천 담수생물다양성 모니터링 | 동아제약 합병 마무리…피노라인 직접 자회사로

### 4. 동아쏘시오홀딩스 (000640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-2.53**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-5.60**
- Adjusted recommendation score: **52.87**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: -0.40%, pattern: weak_historical_reaction
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 2.53 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 5.60 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "인재 모셔라"…제약바이오, 임원급 영입 줄이어 | 동아오츠카, 낙동강생물자원관과 광려천 담수생물다양성 모니터링 | 동아제약 합병 마무리…피노라인 직접 자회사로

### 5. 메드팩토 (235980)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **-0.58**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-6.40**
- Adjusted recommendation score: **65.02**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 28, success rate: 0.00%, avg next close: 0.98%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항(임상시험계획승인신청등결정)              (MP2021 호주 임상1상 시험 계획 승인)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 0.58 points. Event-type performance did not change the score. Stock-specific history subtracted 6.40 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [주가] 10월 1일 주요 제약·바이오·기기 5% 변동 현황 - 41곳 증가 | 비만 치료제 장기지속형 제형 선점… 지투지바이오, 글로벌 빅파마 눈독 | 3세대 항암제 시장 커진다…이중항체·ADC 관련주 동반 상승랠리

### 6. 금화피에스시 (036190)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **65.59**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -0.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 5. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 원전주 엇갈려…두산에너빌리티 약세·우리기술 상승, 연휴 이후 흐름 ... | [이넷뉴스 브랜드평판] 두산에너빌리티, 전력설비 상장기업 10월 1위··... | AI 시대 전력 확보가 관건…원전 설계·기자재·시공주 불기둥

### 7. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.80**
- Adjusted recommendation score: **77.04**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: -2.02%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.80 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 서희건설, 9년 분쟁 진주아파트 '전액 상환' 합의로 푼다 | 추석 하도급대금 조기지급 2.2조 전년比 22%↓...계룡건설 1위 | [아유경제_재건축] 인천부평건우 소규모재건축, 시공권 서희건설 품으로...

### 8. 한국종합기술 (023350)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.38**
- Adjusted recommendation score: **87.46**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -2.09%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 4. News sentiment score is 2. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.38 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [굿모닝퓨처] 에너지는 지속가능한가: 한국 사회의 에너지 전환 | 로보락, KCSI 로봇청소기 '2년 연속 1위'…만족도 93.7점 | 현대자동차 아반떼N TCR, 월드투어 한국 경기 2년 연속 석권

### 9. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.72**
- Adjusted recommendation score: **88.12**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 15, success rate: 46.67%, avg next close: -1.68%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.72 points. Stock pattern label is weak_historical_reaction.
- Related news examples: SK하이닉스·삼성전자 204조…9월 일평균 거래대금 18% 감소 | 보험사 M&A, 계륵에서 화수분으로…‘시간 운용’ 능력이 관건 | 2년 뒤 금호타이어 함평시대 연다…세수확충·인구유입 기대

### 10. 텔콘RF제약 (200230)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.16**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.19**
- Adjusted recommendation score: **104.65**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 2.71%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.16 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.19 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 텔콘RF제약, KT와 23억원 5G 자재 계약 | [HIT알공] 삼성바이오로직스 '한건 더'…935억 규모 위탁계약 | 텔콘RF제약, KT와 23억원 규모 5G 무선장비 공급계약

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
