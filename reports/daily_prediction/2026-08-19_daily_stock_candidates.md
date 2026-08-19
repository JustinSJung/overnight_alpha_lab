# Daily Stock Candidate Report - 2026-08-19

Generated at: 2026-08-19 22:48:42

ML dataset: `data/processed/ml_dataset_20260819.csv`

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
| 407400 | 꿈비 | 2 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | N/A | Not available | 0.00 |
| bonus_issue | 3 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 160 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 39 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| investment_decision | 87 | 0 | N/A | Not available | 0.00 |
| lawsuit | 85 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 289 | 0 | N/A | Not available | 0.00 |
| merger | 48 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 167 | 0 | N/A | Not available | 0.00 |
| spin_off | 10 | 0 | N/A | Not available | 0.00 |
| supply_contract | 159 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bond_with_warrant | 10 | 0 | 0 | 10 | 0.00 |
| bonus_issue | 3 | 0 | 0 | 3 | 0.00 |
| convertible_bond | 160 | 0 | 0 | 160 | 0.00 |
| disclosure_violation | 39 | 0 | 0 | 39 | 0.00 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| investment_decision | 87 | 0 | 0 | 87 | 0.00 |
| lawsuit | 85 | 0 | 0 | 85 | 0.00 |
| major_shareholder_change | 289 | 0 | 0 | 289 | 0.00 |
| merger | 48 | 0 | 0 | 48 | 0.00 |
| paid_in_capital_increase | 167 | 0 | 0 | 167 | 0.00 |

## Positive Candidates

### 1. IPARK현대산업개발 (294870)

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
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 IR] HEM파마·실리콘투·위메이드맥스 등 | 서준오 노원구청장 “태릉CC 개발땐 교통망 확충 필수… ‘미래 경제 도... | “안 싸우는 게 상책”…목동 재건축, 수주전 실종

### 2. IPARK현대산업개발 (294870)

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
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [오늘의 IR] HEM파마·실리콘투·위메이드맥스 등 | 서준오 노원구청장 “태릉CC 개발땐 교통망 확충 필수… ‘미래 경제 도... | “안 싸우는 게 상책”…목동 재건축, 수주전 실종

### 3. 코오롱글로벌 (003070)

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
- Related news examples: [Who Is ?] 최신원 SK네트웍스 명예회장 | 이연제약, 상반기 외부 임원 4명 영입…충주공장 사업화 속도 | 중국 Z세대 사로잡은 K패션… 인디 브랜드로 무한 영토 확장

### 4. 티에스아이 (277880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **114.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 화재 위험 낮추고 주행거리 늘린다…전고체 배터리株에 쏠린 시선 | 2차전지 공정 핵심 쥐었다… 티이엠씨씨엔에스, 소재·부품 쌍끌이 승부... | 2차전지 배터리 대장주 살아나나… 삼성SDI·LG엔솔 상승세 속 테마 온기...

### 5. 코오롱 (002020)

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
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '스마트 셔츠' 만든 한인과학자, 美국방부 4억8천만달러 프로젝트 이끈... | 의류쇼핑 줄었는데…6개 패션기업 일제히 반등, 왜? | 초저전력 AI 반도체 기업, 520억 시리즈A 투자 유치 [VC 브리핑]

### 6. 삼성물산 (028260)

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
- Related news examples: 의류쇼핑 줄었는데…6개 패션기업 일제히 반등, 왜? | AI 데이터센터 뛰어드는 건설사들…전력 확보가 관건 | “안 싸우는 게 상책”…목동 재건축, 수주전 실종

## Volatile Watchlist

### 1. 코퍼스코리아 (322780)

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
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 코퍼스코리아, 250억원 수혈로 새 출발…정상화 로드맵은 아직 | 코퍼스코리아, 250억 규모 투자금 조달...새 경영체제 구축 본격화 | 아티스트스튜디오, M83에 25억 지분투자…'원스톱' 제작 생태계 완성

### 2. SJG세종 (033530)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **34.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **34.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 이랜시스, 차세대 감속기 라인업 확대로 밸류에이션 재평가 | 울산 상장사 29곳 중 20곳 상반기 영업익 개선 | 로봇 대전환기 맞아 몸값 뛰었다… 하이젠알앤엠, 핵심 부품 독주 체제

### 3. SJG세종 (033530)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **34.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **34.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 이랜시스, 차세대 감속기 라인업 확대로 밸류에이션 재평가 | 울산 상장사 29곳 중 20곳 상반기 영업익 개선 | 로봇 대전환기 맞아 몸값 뛰었다… 하이젠알앤엠, 핵심 부품 독주 체제

### 4. 유안타증권 (003470)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **34.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **34.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [금융투자 상반기 실적]토스증권, 대형사급 이익...해외주식이 99% | 금감원, 비청산 장외파생상품거래 가이드라인 1년 연장 | [더벨][하우스 분석 | 유안타증권] 리테일·홀세일 날았다…반기 영업익...

### 5. 듀오백 (073190)

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
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시]듀오백, 정관영 대표 부고 후 주권매매거래 정지 | 듀오백, 대표이사 변경 | 거래소 "듀오백, 20일부터 주권매매거래 정지"

### 6. 듀오백 (073190)

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
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시]듀오백, 정관영 대표 부고 후 주권매매거래 정지 | 듀오백, 대표이사 변경 | 거래소 "듀오백, 20일부터 주권매매거래 정지"

### 7. 듀오백 (073190)

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
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시]듀오백, 정관영 대표 부고 후 주권매매거래 정지 | 듀오백, 대표이사 변경 | 거래소 "듀오백, 20일부터 주권매매거래 정지"

### 8. 듀오백 (073190)

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
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시]듀오백, 정관영 대표 부고 후 주권매매거래 정지 | 듀오백, 대표이사 변경 | 거래소 "듀오백, 20일부터 주권매매거래 정지"

### 9. 비투엔 (307870)

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
- Disclosure title: [기재정정]최대주주변경을수반하는주식양수도계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시] 애니메디솔루션·혜인 '거래정지 예고', 성호전자·저스템 '투자... | 비투엔, 최대주주 스트레지1호조합으로 변경 | 비투엔, 쌍방울 체제서 스트레지1호로 최대주주 변경

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 캔버스엔 (210120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '그래, 이혼하자' 오늘 이혼 전쟁 | '그래 이혼하자' 이민정 오열, 무슨 일?…방송 시간·인물관계도·몇부... | 캔버스엔, 20일 주권매매거래 정지 해제

### 2. 캔버스엔 (210120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '그래, 이혼하자' 오늘 이혼 전쟁 | '그래 이혼하자' 이민정 오열, 무슨 일?…방송 시간·인물관계도·몇부... | 캔버스엔, 20일 주권매매거래 정지 해제

### 3. 캔버스엔 (210120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '그래, 이혼하자' 오늘 이혼 전쟁 | '그래 이혼하자' 이민정 오열, 무슨 일?…방송 시간·인물관계도·몇부... | 캔버스엔, 20일 주권매매거래 정지 해제

### 4. 캔버스엔 (210120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '그래, 이혼하자' 오늘 이혼 전쟁 | '그래 이혼하자' 이민정 오열, 무슨 일?…방송 시간·인물관계도·몇부... | 캔버스엔, 20일 주권매매거래 정지 해제

### 5. 캔버스엔 (210120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '그래, 이혼하자' 오늘 이혼 전쟁 | '그래 이혼하자' 이민정 오열, 무슨 일?…방송 시간·인물관계도·몇부... | 캔버스엔, 20일 주권매매거래 정지 해제

### 6. 캔버스엔 (210120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '그래, 이혼하자' 오늘 이혼 전쟁 | '그래 이혼하자' 이민정 오열, 무슨 일?…방송 시간·인물관계도·몇부... | 캔버스엔, 20일 주권매매거래 정지 해제

### 7. 캔버스엔 (210120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-68.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-68.00**
- Risk level: **HIGH**
- Event type: `convertible_bond`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(전환사채권발행결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is -1. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: '그래, 이혼하자' 오늘 이혼 전쟁 | '그래 이혼하자' 이민정 오열, 무슨 일?…방송 시간·인물관계도·몇부... | 캔버스엔, 20일 주권매매거래 정지 해제

### 8. 아시아나항공 (020560)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **negative**
- Base recommendation score: **-66.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **-66.00**
- Risk level: **HIGH**
- Event type: `lawsuit`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 소송등의제기ㆍ신청(일정금액이상의청구)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is lawsuit. Initial direction is negative. Event score is -75. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 진에어, 적자에도 몸집 키워…'통합 LCC' 출범 승부수 | 800도 견디는 '배터리 방화팩'…기내 화재 구원투수 될까 | 통합 앞두고 마일리지 부채 첫 4조원 돌파…승인 지연에 적립·사용 혼선

### 9. 플레이그램 (009810)

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
- Related news examples: 친아빠, 빚 수십억 떠넘기고 이혼…사실 ‘재혼가정’이라고 털어놓은... | 배우 김민규, 집에서 전한 편안한 근황…청춘 배우의 성장 행보 | 로시, 'Sweetest' 콘셉트 포토로 몽환 비주얼…FLAT 프로젝트 세 번째 이...

### 10. 신테카바이오 (226330)

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
- Disclosure title: 주요사항보고서(자기전환사채만기전취득결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is convertible_bond. Initial direction is negative. Event score is -60. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주가] 8월 19일 주요 제약·바이오·기기 5% 변동 현황 - 바이오니아 상... | [아주쉬운 재무제표] 반기보고서 '시즌 마감'…문제된 기업들은 이곳 | 실적 급상승 레메디 23%↑…中 진출 바이오솔루션도 주목[바이오맥짚기...

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
