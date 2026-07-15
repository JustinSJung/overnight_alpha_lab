# Daily Stock Candidate Report - 2026-07-15

Generated at: 2026-07-15 23:15:48

ML dataset: `data/processed/ml_dataset_20260715.csv`

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
| 002880 | 디와이에이 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003060 | 에이프로젠바이오로직스 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003070 | 코오롱글로벌 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |
| 003350 | 한국화장품제조 | 1 | 0 | N/A | Not available | mostly_pending | 0.00 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | N/A | Not available | 0.00 |
| convertible_bond | 63 | 0 | N/A | Not available | 0.00 |
| disclosure_violation | 12 | 0 | N/A | Not available | 0.00 |
| earnings_guidance | 2 | 0 | N/A | Not available | 0.00 |
| investment_decision | 31 | 0 | N/A | Not available | 0.00 |
| lawsuit | 39 | 0 | N/A | Not available | 0.00 |
| major_shareholder_change | 74 | 0 | N/A | Not available | 0.00 |
| merger | 16 | 0 | N/A | Not available | 0.00 |
| paid_in_capital_increase | 49 | 0 | N/A | Not available | 0.00 |
| spin_off | 1 | 0 | N/A | Not available | 0.00 |
| supply_contract | 75 | 0 | N/A | Not available | 0.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| bonus_issue | 1 | 0 | 0 | 1 | 0.00 |
| convertible_bond | 63 | 0 | 0 | 63 | 0.00 |
| disclosure_violation | 12 | 0 | 0 | 12 | 0.00 |
| earnings_guidance | 2 | 0 | 0 | 2 | 0.00 |
| investment_decision | 31 | 0 | 0 | 31 | 0.00 |
| lawsuit | 39 | 0 | 0 | 39 | 0.00 |
| major_shareholder_change | 74 | 0 | 0 | 74 | 0.00 |
| merger | 16 | 0 | 0 | 16 | 0.00 |
| paid_in_capital_increase | 49 | 0 | 0 | 49 | 0.00 |
| spin_off | 1 | 0 | 0 | 1 | 0.00 |

## Positive Candidates

### 1. 효성중공업 (298040)

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
- Related news examples: 효성중공업, 고점 대비 조정된 주가는 펀더멘털 훼손 아닌 수급 이슈-SK | [인프라, 건설에서 교체로]⑩"노후 SOC 교체 적극 참여할 것"…기업들은... | [이넷뉴스 브랜드평판] 두산에너빌리티, 원자력발전 상장기업 7월 1위.....

### 2. 티엘비 (356860)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **97.00**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 권리락              (무상증자)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 티엘비, 16일 무상증자 권리락…기준가 4만4000원 | 티엘비 주가, 7월 15일 87,500원 20.35% 상승 마감

### 3. 효성 (004800)

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
- Related news examples: "문과생만 모십니다"…창사 첫 인문계만 뽑는 대기업 '어디' | 효성중공업, 고점 대비 조정된 주가는 펀더멘털 훼손 아닌 수급 이슈-SK | [인프라, 건설에서 교체로]⑩"노후 SOC 교체 적극 참여할 것"…기업들은...

## Volatile Watchlist

### 1. 강스템바이오텍 (217730)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **100.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **100.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (기술도입 계약 체결)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 13. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | 1.6조 기술수출 경험한 큐라클... MT-103 잇는 다음 타자는 | 강스템바이오텍, 서울대와 특허출원 기술 도입 계약 체결

### 2. 이노에이엑스 (296640)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **69.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **69.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 합병등종료보고서(자산양수도)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 도면 분석부터 예지보전까지…마키나락스, 제조·방산 AI 확산 수혜 예고 | [52주] 최고가 4개, 최저가 92개... 시장 약세 지속 | 애자일소다 덕에 농협은행과 밀접해진 이노에이엑스

### 3. 스페코 (013810)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 스페코, 최대주주 넥사코리아로 변경…지분 33.55% 인수

### 4. 스페코 (013810)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 스페코, 최대주주 넥사코리아로 변경…지분 33.55% 인수

### 5. 엔켐 (348370)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 회사합병결정(종속회사의주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(15일) 주요공시...비비안, 주당 1.0주 무상증자... | [주요공시] 서진시스템, 한화오션, 남양유업, 신성이엔지, 이수페타시스...

### 6. 엔켐 (348370)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 회사합병결정(종속회사의주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(15일) 주요공시...비비안, 주당 1.0주 무상증자... | [주요공시] 서진시스템, 한화오션, 남양유업, 신성이엔지, 이수페타시스...

### 7. 엔켐 (348370)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 회사합병결정(종속회사의주요경영사항)              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | 코스피·코스닥 전 거래일(15일) 주요공시...비비안, 주당 1.0주 무상증자... | [주요공시] 서진시스템, 한화오션, 남양유업, 신성이엔지, 이수페타시스...

### 8. 에임드바이오 (0009K0)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]투자판단관련주요경영사항(임상시험계획승인신청)              (BI 4060107 (ODS025)의 제 1상 임상시험계획 승인 신청)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [속보] 에임드바이오, 프랑스 ANSM에 BI 4060107(ODS025) 1상 임상시험계... | HLB 상한가 직행에 바이젠셀·에이프릴바이오 동반 폭등… 면역항암제 ... | [2026 상반기 VC 리그테이블] [④ 회수] 인터베스트가 회수 1위한 비결…...

### 9. 스페코 (013810)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 스페코, 최대주주 넥사코리아로 변경…지분 33.55% 인수

### 10. 스페코 (013810)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **67.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **67.00**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 7월 16일 개장 전 주요 공시 | [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 스페코, 최대주주 넥사코리아로 변경…지분 33.55% 인수

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 에스아이리소스 (065420)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (대표이사 및 사내이사에 대한 횡령·배임 고소 접수)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is -2. Negative keyword count is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 에스아이리소스, 풍문 등 조회결과→주권매매거래 7월 16일 해제 | 에스아이리소스, 임시주총 결의 효력정지…대표·사외이사 직무도 정지

### 2. 에스아이리소스 (065420)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (대표이사 및 사내이사에 대한 횡령·배임 고소 접수)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is -2. Negative keyword count is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 에스아이리소스, 풍문 등 조회결과→주권매매거래 7월 16일 해제 | 에스아이리소스, 임시주총 결의 효력정지…대표·사외이사 직무도 정지

### 3. 에스아이리소스 (065420)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (대표이사 및 사내이사에 대한 횡령·배임 고소 접수)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is -2. Negative keyword count is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 에스아이리소스, 풍문 등 조회결과→주권매매거래 7월 16일 해제 | 에스아이리소스, 임시주총 결의 효력정지…대표·사외이사 직무도 정지

### 4. 에스아이리소스 (065420)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (대표이사 및 사내이사에 대한 횡령·배임 고소 접수)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is -2. Negative keyword count is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 에스아이리소스, 풍문 등 조회결과→주권매매거래 7월 16일 해제 | 에스아이리소스, 임시주총 결의 효력정지…대표·사외이사 직무도 정지

### 5. 에스아이리소스 (065420)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **7.00**
- Error-note adjustment score: **0.00**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **7.00**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              (대표이사 및 사내이사에 대한 횡령·배임 고소 접수)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is -2. Negative keyword count is 6. Historical error notes did not change the score. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [N2 모닝 경제 브리핑-7월 16일] 美 증시, 물가 안정 기대에 일제히 상승... | 에스아이리소스, 풍문 등 조회결과→주권매매거래 7월 16일 해제 | 에스아이리소스, 임시주총 결의 효력정지…대표·사외이사 직무도 정지

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
