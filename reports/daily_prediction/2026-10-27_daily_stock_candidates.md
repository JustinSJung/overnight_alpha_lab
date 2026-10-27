# Daily Stock Candidate Report - 2026-10-27

Generated at: 2026-10-27 02:03:12

ML dataset: `data/processed/ml_dataset_20261027.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 044380 | 주연테크 | 18 | 13 | 92.31% | 6.24% | relatively_positive_history | 8.58 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 21 | 17 | 88.24% | 4.25% | 10.00 |
| paid_in_capital_increase | 2351 | 1831 | 57.29% | -0.04% | 3.00 |
| spin_off | 114 | 82 | 50.00% | 1.75% | 2.00 |
| convertible_bond | 1158 | 825 | 51.39% | 0.97% | 0.00 |
| lawsuit | 466 | 345 | 53.04% | -0.21% | 0.00 |
| investment_decision | 435 | 320 | 52.50% | -0.06% | 0.00 |
| bonus_issue | 104 | 101 | 41.58% | -0.49% | -3.00 |
| disclosure_violation | 182 | 112 | 43.75% | -0.36% | -3.00 |
| bond_with_warrant | 117 | 105 | 23.81% | 0.47% | -6.00 |
| major_shareholder_change | 2270 | 1637 | 34.70% | -0.63% | -6.00 |
| merger | 520 | 425 | 23.29% | 0.43% | -6.00 |
| supply_contract | 1386 | 1060 | 32.55% | -0.64% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 21 | 15 | 2 | 4 | 2.90 |
| paid_in_capital_increase | 2351 | 1049 | 782 | 520 | 1.23 |
| lawsuit | 466 | 183 | 162 | 121 | 0.92 |
| convertible_bond | 1158 | 424 | 401 | 333 | 0.79 |
| disclosure_violation | 182 | 49 | 63 | 70 | 0.31 |
| investment_decision | 435 | 168 | 152 | 115 | -0.51 |
| spin_off | 114 | 41 | 41 | 32 | -0.72 |
| bond_with_warrant | 117 | 25 | 80 | 12 | -0.98 |
| supply_contract | 1386 | 345 | 715 | 326 | -1.08 |
| bonus_issue | 104 | 42 | 59 | 3 | -1.14 |

## Positive Candidates

### 1. 지아이텍 (382480)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.08**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **130.42**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.76%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.76%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.08 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 지아이텍, 초정밀 부품·장비→자동차 분야 검사장비 시장 진출 | 10월 26일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 27일] 美 증시, 앤트로픽 IPO 기대감에 기술...

### 2. 서남 (294630)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.08**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.17**
- Adjusted recommendation score: **128.09**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 8.55%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.05%
- Next close return data: 1.74%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.08 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: 독감 예방접종 쪽방촌·노숙인 1200여명 찾아간다 | 새로운 황금을 품을지 선택의 시간이 왔다 | 서남, 초전도 선재 對美 수출 계약 체결

### 3. 텔콘RF제약 (200230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.08**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.05**
- Adjusted recommendation score: **127.97**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 3.44%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.25%
- Next close return data: 4.18%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.08 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.05 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 26일 주식시장 주요공시 | 10월 27일 개장 전 주요 공시 | [HIT알공] 에스엘에스바이오, 상장폐지 가처분 신청…정리매매 보류

### 4. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **2.90**
- Event-type performance adjustment score: **10.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **126.22**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 26, success rate: 69.23%, avg next close: 3.32%, pattern: relatively_positive_history
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 1.57%
- Next close return data: 6.71%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 7. Historical error notes added 2.90 points. Event-type performance added 10.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [건설업계 동향] 삼성물산ㆍ현대건설ㆍIPARK현대산업개발 (10.27) | IPARK현대산업개발·두산건설, 목동 아이파크 라운지 오픈·두산위브더... | IPARK현대산업개발, '목동 아파트 재건축 청사진'…신개념 라운지 11월 ...

### 5. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **2.90**
- Event-type performance adjustment score: **10.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **126.22**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 26, success rate: 69.23%, avg next close: 3.32%, pattern: relatively_positive_history
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 1.57%
- Next close return data: 6.71%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 7. Historical error notes added 2.90 points. Event-type performance added 10.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [건설업계 동향] 삼성물산ㆍ현대건설ㆍIPARK현대산업개발 (10.27) | IPARK현대산업개발·두산건설, 목동 아이파크 라운지 오픈·두산위브더... | IPARK현대산업개발, '목동 아파트 재건축 청사진'…신개념 라운지 11월 ...

### 6. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **2.90**
- Event-type performance adjustment score: **10.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **126.22**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 26, success rate: 69.23%, avg next close: 3.32%, pattern: relatively_positive_history
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 1.57%
- Next close return data: 6.71%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 7. Historical error notes added 2.90 points. Event-type performance added 10.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [건설업계 동향] 삼성물산ㆍ현대건설ㆍIPARK현대산업개발 (10.27) | IPARK현대산업개발·두산건설, 목동 아이파크 라운지 오픈·두산위브더... | IPARK현대산업개발, '목동 아파트 재건축 청사진'…신개념 라운지 11월 ...

### 7. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **2.90**
- Event-type performance adjustment score: **10.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **126.22**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 26, success rate: 69.23%, avg next close: 3.32%, pattern: relatively_positive_history
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 1.57%
- Next close return data: 6.71%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 7. Historical error notes added 2.90 points. Event-type performance added 10.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [건설업계 동향] 삼성물산ㆍ현대건설ㆍIPARK현대산업개발 (10.27) | IPARK현대산업개발·두산건설, 목동 아이파크 라운지 오픈·두산위브더... | IPARK현대산업개발, '목동 아파트 재건축 청사진'…신개념 라운지 11월 ...

### 8. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **2.90**
- Event-type performance adjustment score: **10.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **126.22**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 26, success rate: 69.23%, avg next close: 3.32%, pattern: relatively_positive_history
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 1.57%
- Next close return data: 6.71%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 7. Historical error notes added 2.90 points. Event-type performance added 10.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [건설업계 동향] 삼성물산ㆍ현대건설ㆍIPARK현대산업개발 (10.27) | IPARK현대산업개발·두산건설, 목동 아이파크 라운지 오픈·두산위브더... | IPARK현대산업개발, '목동 아파트 재건축 청사진'…신개념 라운지 11월 ...

### 9. IPARK현대산업개발 (294870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **neutral_positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **2.90**
- Event-type performance adjustment score: **10.00**
- Stock-specific pattern adjustment score: **8.32**
- Adjusted recommendation score: **126.22**
- Risk level: **LOW**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 26, success rate: 69.23%, avg next close: 3.32%, pattern: relatively_positive_history
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 1.57%
- Next close return data: 6.71%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 7. Historical error notes added 2.90 points. Event-type performance added 10.00 points. Stock-specific history added 8.32 points. Stock pattern label is relatively_positive_history.
- Related news examples: [건설업계 동향] 삼성물산ㆍ현대건설ㆍIPARK현대산업개발 (10.27) | IPARK현대산업개발·두산건설, 목동 아이파크 라운지 오픈·두산위브더... | IPARK현대산업개발, '목동 아파트 재건축 청사진'…신개념 라운지 11월 ...

### 10. 베노티앤알 (206400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-1.08**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.82**
- Adjusted recommendation score: **122.10**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 53.57%, avg next close: -4.07%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 1.08 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.82 points. Stock pattern label is relatively_positive_history.
- Related news examples: 베노티앤알, 글로벌 배터리 제조사향 美 생산시설 프로젝트 수주 | 베노티앤알, 반도체사업부 신설 후 첫 수주…美 배터리 프로젝트 52억 규... | 베노티앤알, 반도체사업부 신설 후 첫 수주…북미 배터리 생산시설 참여

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 일성건설 (013360)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.08**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.21**
- Adjusted recommendation score: **125.71**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 20.00%, avg next close: -1.25%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.09%
- Next close return data: 0.23%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.08 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.21 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 26일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 27일] 美 증시, 앤트로픽 IPO 기대감에 기술... | 기업공시 [10월 26일]

### 2. 디와이피엔에프 (104460)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.08**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **128.04**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -5.38%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -6.00%
- Next close return data: -5.38%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.08 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 디와이피엔에프-하나머티리얼즈, 실리콘 음극재 양산공장 EPC 계약 체결 | 디와이피엔에프, 하나머티리얼즈와 약 480억원 규모 실리콘 음극재 양산... | 디와이피엔에프, 하나머티리얼즈 실리콘 음극재 양산공장 EPC 사업 수주

### 3. HD현대마린엔진 (071970)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **150.00**
- Error-note adjustment score: **-1.08**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.40**
- Adjusted recommendation score: **137.52**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 20.00%, avg next close: -0.64%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.88%
- Next close return data: 4.77%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Historical error notes subtracted 1.08 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.40 points. Stock pattern label is weak_historical_reaction.
- Related news examples: HD현대마린솔루션, 핵심사업 견조…주가 조정 과도 | 신한證 “HD현대마린솔루션, 3분기 일회성에 주춤… 쌓이는 이익 구조는... | NH證 "HD현대마린솔루션, 영업이익률 26%…기업 가치 저평가"

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
