# Daily Stock Candidate Report - 2026-09-17

Generated at: 2026-09-17 01:41:28

ML dataset: `data/processed/ml_dataset_20260917.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 14 | 9 | 100.00% | 7.29% | relatively_positive_history | 8.64 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 003060 | 에이프로젠바이오로직스 | 4 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.31 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |
| 003850 | 보령 | 6 | 6 | 100.00% | 2.48% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| investment_decision | 258 | 157 | 65.61% | 0.08% | 6.00 |
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| paid_in_capital_increase | 1322 | 1019 | 60.45% | 0.26% | 3.00 |
| lawsuit | 227 | 129 | 64.34% | -0.62% | 3.00 |
| convertible_bond | 660 | 387 | 54.01% | 1.50% | 2.00 |
| bonus_issue | 64 | 61 | 47.54% | 0.59% | 0.00 |
| disclosure_violation | 115 | 65 | 50.77% | -0.08% | 0.00 |
| merger | 170 | 92 | 22.83% | 1.14% | -4.00 |
| bond_with_warrant | 27 | 17 | 5.88% | -0.11% | -6.00 |
| spin_off | 66 | 43 | 30.23% | 0.19% | -6.00 |
| supply_contract | 752 | 490 | 28.57% | -0.77% | -6.00 |
| major_shareholder_change | 1395 | 912 | 33.99% | -1.17% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1322 | 616 | 403 | 303 | 1.42 |
| lawsuit | 227 | 83 | 46 | 98 | 1.22 |
| convertible_bond | 660 | 209 | 178 | 273 | 0.77 |
| disclosure_violation | 115 | 33 | 32 | 50 | 0.60 |
| investment_decision | 258 | 103 | 54 | 101 | 0.53 |
| bonus_issue | 64 | 29 | 32 | 3 | -0.86 |
| supply_contract | 752 | 140 | 350 | 262 | -1.14 |
| bond_with_warrant | 27 | 1 | 16 | 10 | -1.59 |
| major_shareholder_change | 1395 | 310 | 602 | 483 | -1.91 |

## Positive Candidates

### 1. 빅텍 (065450)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.25**
- Adjusted recommendation score: **119.61**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.45%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.88%
- Next close return data: 1.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.25 points. Stock pattern label is not_enough_data.
- Related news examples: 우주항공·방산주 일제히 날았다…나라스페이스 29%↑·켄코아 26%↑ | 9월 16일 주식시장 주요공시 | 유진투자증권 “한화시스템, 레이저 무기 ‘천광’ 새 성장축…목표가...

### 2. 비에이치아이 (083650)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.14**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.42**
- Adjusted recommendation score: **103.28**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.64%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.58%
- Next close return data: 3.63%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.14 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.42 points. Stock pattern label is relatively_positive_history.
- Related news examples: 비에이치아이, 경남 고용우수기업 선정…발전산업 인재·지역 고용 확대 | 비에이치아이, '경남 고용우수기업' 선정 | ﻿비에이치아이, 경남 고용우수기업 선정…발전산업 전문인재 육성 고용...

## Volatile Watchlist

### 1. 올릭스 (226950)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **0.53**
- Event-type performance adjustment score: **6.00**
- Stock-specific pattern adjustment score: **1.25**
- Adjusted recommendation score: **49.78**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 2.47%, pattern: not_enough_data
- Disclosure title: 투자판단관련주요경영사항(임상시험계획승인신청)              
- Next open return data: 1.35%
- Next close return data: 4.33%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes added 0.53 points. Event-type performance added 6.00 points. Stock-specific history added 1.25 points. Stock pattern label is not_enough_data.
- Related news examples: “경쟁사는 자체 개발”…올릭스 비만약 기술이전 가치 부각 [Why 바이오... | 올릭스, '황반변성 치료제' 호주 2a상 승인 신청 | 올릭스, 황반변성치료제 호주 2a상 신청

### 2. 보령 (003850)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **45.00**
- Error-note adjustment score: **-2.20**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.50**
- Adjusted recommendation score: **44.30**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 2.48%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사분할결정)
- Next open return data: 1.14%
- Next close return data: -2.39%
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 2.20 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 김준의 어촌정담 漁村情談 103. 유네스코도 인정한 갯벌어업의 전통지식... | [9월 17일 충청권 날씨] "구름 조금, 쾌청한 초가을" | 염홍철 충청U대회 위원장, “대전엑스포처럼 기억될 대회 만들겠다” 각...

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 2. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 3. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 4. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 5. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 6. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 7. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 8. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 9. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.91**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **35.21**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.76%
- Next close return data: 1.52%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.91 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 아모레퍼시픽그룹, 협력사에 거래 대금 649억원 조기 지급 | K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 아모레퍼시픽 그룹, 600여 개 협력사에 총 649억원 거래 대금 조기 지급

### 10. 에이피알 (278470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **56.00**
- Error-note adjustment score: **-2.31**
- Event-type performance adjustment score: **-4.00**
- Stock-specific pattern adjustment score: **-7.81**
- Adjusted recommendation score: **41.88**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 13, success rate: 7.69%, avg next close: -1.50%, pattern: weak_historical_reaction
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: 0.86%
- Next close return data: 3.28%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 3. Historical error notes subtracted 2.31 points. Event-type performance subtracted 4.00 points. Stock-specific history subtracted 7.81 points. Stock pattern label is weak_historical_reaction.
- Related news examples: K뷰티 수출 훈풍에 화장품주 들썩… 제이투케이바이오·네오팜 화색 가... | 9월 16일 주식시장 주요공시 | [비즈 인사이트] 화장품 빅6 순이익 모두 늘었다…에이피알 영업익 3428...

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
