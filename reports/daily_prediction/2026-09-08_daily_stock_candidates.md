# Daily Stock Candidate Report - 2026-09-08

Generated at: 2026-09-08 01:05:25

ML dataset: `data/processed/ml_dataset_20260908.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 12 | 12 | 100.00% | 5.43% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 21 | 20 | 100.00% | 3.04% | relatively_positive_history | 8.95 |
| 006980 | 우성 | 12 | 6 | 100.00% | 15.55% | relatively_positive_history | 8.50 |
| 044380 | 주연테크 | 10 | 5 | 100.00% | 18.53% | relatively_positive_history | 8.50 |
| 288980 | 모아데이타 | 21 | 14 | 85.71% | 3.33% | relatively_positive_history | 8.43 |
| 223310 | 사토시홀딩스 | 53 | 36 | 75.00% | 4.14% | relatively_positive_history | 8.38 |
| 336260 | 두산퓨얼셀 | 7 | 4 | 75.00% | 11.15% | relatively_positive_history | 8.32 |
| 326030 | 에스케이바이오팜 | 3 | 3 | 100.00% | 2.29% | relatively_positive_history | 7.50 |
| 161000 | 애경케미칼 | 3 | 3 | 100.00% | -0.64% | relatively_positive_history | 6.00 |
| 006840 | AK홀딩스 | 3 | 3 | 100.00% | -0.53% | relatively_positive_history | 6.00 |
| 003920 | 남양유업 | 10 | 9 | 100.00% | -0.86% | relatively_positive_history | 5.90 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 836 | 533 | 66.79% | 0.01% | 6.00 |
| lawsuit | 165 | 69 | 76.81% | -0.99% | 6.00 |
| convertible_bond | 488 | 215 | 64.19% | -1.19% | 1.00 |
| investment_decision | 160 | 59 | 44.07% | 3.35% | 1.00 |
| earnings_guidance | 4 | 0 | N/A | Not available | 0.00 |
| spin_off | 34 | 12 | 41.67% | 0.11% | -3.00 |
| merger | 123 | 45 | 17.78% | 1.88% | -4.00 |
| bond_with_warrant | 26 | 16 | 6.25% | -0.16% | -6.00 |
| disclosure_violation | 65 | 15 | 6.67% | 0.68% | -6.00 |
| bonus_issue | 41 | 38 | 31.58% | 0.37% | -6.00 |
| major_shareholder_change | 996 | 513 | 29.04% | -0.68% | -6.00 |
| supply_contract | 565 | 303 | 24.42% | -0.98% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 836 | 356 | 177 | 303 | 1.49 |
| lawsuit | 165 | 53 | 16 | 96 | 1.32 |
| convertible_bond | 488 | 138 | 77 | 273 | 0.94 |
| earnings_guidance | 4 | 0 | 0 | 4 | 0.00 |
| disclosure_violation | 65 | 1 | 14 | 50 | -0.57 |
| investment_decision | 160 | 26 | 33 | 101 | -0.63 |
| spin_off | 34 | 5 | 7 | 22 | -0.71 |
| supply_contract | 565 | 74 | 229 | 262 | -1.13 |
| bond_with_warrant | 26 | 1 | 15 | 10 | -1.54 |
| merger | 123 | 8 | 37 | 78 | -1.78 |

## Positive Candidates

### 1. 씨에스윈드 (112610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **135.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.71%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.84%
- Next close return data: 0.71%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 페로타임즈 손바닥뉴스 9월8일(화) | 씨에스윈드, 美 베스타스에 풍력타워 1510억 원 공급 | [N2 모닝 경제 브리핑-9월 8일] 美 증시, 노동절 맞아 휴장…주요 공시 ...

### 2. 씨에스윈드 (112610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **135.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.71%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.84%
- Next close return data: 0.71%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 페로타임즈 손바닥뉴스 9월8일(화) | 씨에스윈드, 美 베스타스에 풍력타워 1510억 원 공급 | [N2 모닝 경제 브리핑-9월 8일] 美 증시, 노동절 맞아 휴장…주요 공시 ...

### 3. 제너셈 (217190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **126.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.17%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.16%
- Next close return data: 2.17%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 7일 주식시장 주요공시 | [EBN 데이터센터] AI 연산 수요 기대에 HBM주 질주 | [오늘의 주요공시] 한화에어로스페이스·LG전자·한국카본 등

### 4. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **120.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.31%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.47%
- Next close return data: 0.31%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 7일 주식시장 주요공시 | [코스피·코스닥, 셀트리온 LG전자 나우로보틱스 비나텍파 인디앤씨 제... | [N2 모닝 경제 브리핑-9월 8일] 美 증시, 노동절 맞아 휴장…주요 공시 ...

### 5. DL (000210)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **119.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.33**
- Adjusted recommendation score: **115.20**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 2.42%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.74%
- Next close return data: 2.42%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.33 points. Stock pattern label is relatively_positive_history.
- Related news examples: 서전기전·오르비텍 나란히 상한가 근접…원전株 무더기 폭등랠이 왜? | 조절 불충분 T2DM에 아나글립틴 대안...“식후·TIR 개선” | 삼성물산, 2.4조 목동13단지 재건축 단독 응찰…수의계약 가능성

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **1.00**
- Stock-specific pattern adjustment score: **-5.86**
- Adjusted recommendation score: **49.51**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP51(키트루다 바이오시밀러) 미국 임상 3상 시험계획 변경신청 승인)
- Next open return data: 0.64%
- Next close return data: -0.54%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.63 points. Event-type performance added 1.00 points. Stock-specific history subtracted 5.86 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 셀트리온, 日 최대 바이오 클러스터와 유망 스타트업 키운다 | 셀트리온, 日 고베 바이오클러스터와 오픈이노베이션…“유망 바이오 기... | 셀트리온, 일본 KBIC와 바이오 스타트업 육성 프로그램 출범

### 2. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **1.00**
- Stock-specific pattern adjustment score: **-5.86**
- Adjusted recommendation score: **49.51**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP51(키트루다 바이오시밀러) 미국 임상 3상 시험계획 변경신청 승인)
- Next open return data: 0.64%
- Next close return data: -0.54%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.63 points. Event-type performance added 1.00 points. Stock-specific history subtracted 5.86 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 셀트리온, 日 최대 바이오 클러스터와 유망 스타트업 키운다 | 셀트리온, 日 고베 바이오클러스터와 오픈이노베이션…“유망 바이오 기... | 셀트리온, 일본 KBIC와 바이오 스타트업 육성 프로그램 출범

### 3. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **1.00**
- Stock-specific pattern adjustment score: **-5.86**
- Adjusted recommendation score: **49.51**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP51(키트루다 바이오시밀러) 미국 임상 3상 시험계획 변경신청 승인)
- Next open return data: 0.64%
- Next close return data: -0.54%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.63 points. Event-type performance added 1.00 points. Stock-specific history subtracted 5.86 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 셀트리온, 日 최대 바이오 클러스터와 유망 스타트업 키운다 | 셀트리온, 日 고베 바이오클러스터와 오픈이노베이션…“유망 바이오 기... | 셀트리온, 일본 KBIC와 바이오 스타트업 육성 프로그램 출범

### 4. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **1.00**
- Stock-specific pattern adjustment score: **-5.86**
- Adjusted recommendation score: **49.51**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP51(키트루다 바이오시밀러) 미국 임상 3상 시험계획 변경신청 승인)
- Next open return data: 0.64%
- Next close return data: -0.54%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.63 points. Event-type performance added 1.00 points. Stock-specific history subtracted 5.86 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 셀트리온, 日 최대 바이오 클러스터와 유망 스타트업 키운다 | 셀트리온, 日 고베 바이오클러스터와 오픈이노베이션…“유망 바이오 기... | 셀트리온, 일본 KBIC와 바이오 스타트업 육성 프로그램 출범

### 5. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **1.00**
- Stock-specific pattern adjustment score: **-5.86**
- Adjusted recommendation score: **49.51**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP51(키트루다 바이오시밀러) 미국 임상 3상 시험계획 변경신청 승인)
- Next open return data: 0.64%
- Next close return data: -0.54%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.63 points. Event-type performance added 1.00 points. Stock-specific history subtracted 5.86 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 셀트리온, 日 최대 바이오 클러스터와 유망 스타트업 키운다 | 셀트리온, 日 고베 바이오클러스터와 오픈이노베이션…“유망 바이오 기... | 셀트리온, 일본 KBIC와 바이오 스타트업 육성 프로그램 출범

### 6. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **1.00**
- Stock-specific pattern adjustment score: **-5.86**
- Adjusted recommendation score: **49.51**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP51(키트루다 바이오시밀러) 미국 임상 3상 시험계획 변경신청 승인)
- Next open return data: 0.64%
- Next close return data: -0.54%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.63 points. Event-type performance added 1.00 points. Stock-specific history subtracted 5.86 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 셀트리온, 日 최대 바이오 클러스터와 유망 스타트업 키운다 | 셀트리온, 日 고베 바이오클러스터와 오픈이노베이션…“유망 바이오 기... | 셀트리온, 일본 KBIC와 바이오 스타트업 육성 프로그램 출범

### 7. DB증권 (016610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-1.81**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **67.69**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: 0.58%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.00%
- Next close return data: 0.40%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.81 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: DB하이텍, 4%대 강세…"中 수요에 8인치 파운드리 공급 부족" | DB손보, 질적 성장 전환… 해외사업 수익 기반 확대 | [애널픽] DB하이텍, 中 AIDC·로봇 성장 수혜…목표가 20만원

### 8. DB증권 (016610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-1.81**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **67.69**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: 0.58%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.00%
- Next close return data: 0.40%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.81 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: DB하이텍, 4%대 강세…"中 수요에 8인치 파운드리 공급 부족" | DB손보, 질적 성장 전환… 해외사업 수익 기반 확대 | [애널픽] DB하이텍, 中 AIDC·로봇 성장 수혜…목표가 20만원

### 9. DB증권 (016610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-1.81**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **67.69**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: 0.58%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.00%
- Next close return data: 0.40%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.81 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: DB하이텍, 4%대 강세…"中 수요에 8인치 파운드리 공급 부족" | DB손보, 질적 성장 전환… 해외사업 수익 기반 확대 | [애널픽] DB하이텍, 中 AIDC·로봇 성장 수혜…목표가 20만원

### 10. DB증권 (016610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-1.81**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **67.69**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: 0.58%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.00%
- Next close return data: 0.40%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.81 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: DB하이텍, 4%대 강세…"中 수요에 8인치 파운드리 공급 부족" | DB손보, 질적 성장 전환… 해외사업 수익 기반 확대 | [애널픽] DB하이텍, 中 AIDC·로봇 성장 수혜…목표가 20만원

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
