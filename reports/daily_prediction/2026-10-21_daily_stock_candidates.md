# Daily Stock Candidate Report - 2026-10-21

Generated at: 2026-10-21 01:15:49

ML dataset: `data/processed/ml_dataset_20261021.csv`

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
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 10 | 10 | 90.00% | 8.18% | relatively_positive_history | 8.82 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 006980 | 우성 | 15 | 9 | 100.00% | 8.46% | relatively_positive_history | 8.60 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 100.00% | 1.92% | 8.00 |
| lawsuit | 416 | 295 | 58.31% | -0.79% | 3.00 |
| paid_in_capital_increase | 2206 | 1686 | 57.30% | 0.19% | 3.00 |
| spin_off | 113 | 81 | 50.62% | 1.76% | 2.00 |
| investment_decision | 402 | 287 | 54.70% | -0.21% | 0.00 |
| disclosure_violation | 169 | 99 | 48.48% | -0.42% | 0.00 |
| convertible_bond | 1097 | 765 | 52.03% | 0.90% | 0.00 |
| bonus_issue | 103 | 100 | 42.00% | -0.37% | -3.00 |
| major_shareholder_change | 2142 | 1509 | 35.19% | -0.66% | -3.00 |
| bond_with_warrant | 117 | 105 | 23.81% | 0.47% | -6.00 |
| merger | 418 | 323 | 19.50% | 0.35% | -6.00 |
| supply_contract | 1247 | 921 | 30.73% | -0.79% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 0 | 4 | 2.50 |
| paid_in_capital_increase | 2206 | 966 | 720 | 520 | 1.21 |
| lawsuit | 416 | 172 | 123 | 121 | 1.18 |
| convertible_bond | 1097 | 398 | 367 | 332 | 0.81 |
| disclosure_violation | 169 | 48 | 51 | 70 | 0.51 |
| investment_decision | 402 | 157 | 130 | 115 | -0.31 |
| spin_off | 113 | 41 | 40 | 32 | -0.66 |
| bond_with_warrant | 117 | 25 | 80 | 12 | -0.98 |
| bonus_issue | 103 | 42 | 58 | 3 | -1.09 |
| supply_contract | 1247 | 283 | 638 | 326 | -1.13 |

## Positive Candidates

### 1. 코닉오토메이션 (391710)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **138.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 4.64%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 1.20%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 20일 주식시장 주요공시 | [코스피·코스닥,S-Oil 한화생명  HD현대중공업 에이플러스에셋 사람인... | [N2 모닝 경제 브리핑-10월 21일] 美 증시, 기술주 숨고르기 속 혼조…다...

### 2. 엑세스바이오 (950130)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **131.87**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.45%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.73%
- Next close return data: 1.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 20일 주식시장 주요공시 | [코스피·코스닥,S-Oil 한화생명  HD현대중공업 에이플러스에셋 사람인... | [N2 모닝 경제 브리핑-10월 21일] 美 증시, 기술주 숨고르기 속 혼조…다...

### 3. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.94**
- Adjusted recommendation score: **129.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 71.43%, avg next close: 1.12%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 2.98%
- Next close return data: 1.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.94 points. Stock pattern label is relatively_positive_history.
- Related news examples: HMM, HD현대에 컨테이너선 8척 발주…1조9196억원 규모 | HD현대, 미국서 무인수상함 자율운항 시연…안두릴과 기술 검증 | 10월 20일 주식시장 주요공시

### 4. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.94**
- Adjusted recommendation score: **129.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 71.43%, avg next close: 1.12%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 2.98%
- Next close return data: 1.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.94 points. Stock pattern label is relatively_positive_history.
- Related news examples: HMM, HD현대에 컨테이너선 8척 발주…1조9196억원 규모 | HD현대, 미국서 무인수상함 자율운항 시연…안두릴과 기술 검증 | 10월 20일 주식시장 주요공시

### 5. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.94**
- Adjusted recommendation score: **129.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 71.43%, avg next close: 1.12%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 2.98%
- Next close return data: 1.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.94 points. Stock pattern label is relatively_positive_history.
- Related news examples: HMM, HD현대에 컨테이너선 8척 발주…1조9196억원 규모 | HD현대, 미국서 무인수상함 자율운항 시연…안두릴과 기술 검증 | 10월 20일 주식시장 주요공시

### 6. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **6.94**
- Adjusted recommendation score: **129.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 71.43%, avg next close: 1.12%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 2.98%
- Next close return data: 1.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 6.94 points. Stock pattern label is relatively_positive_history.
- Related news examples: HMM, HD현대에 컨테이너선 8척 발주…1조9196억원 규모 | HD현대, 미국서 무인수상함 자율운항 시연…안두릴과 기술 검증 | 10월 20일 주식시장 주요공시

### 7. 티에스아이 (277880)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **124.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **119.37**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 0.31%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.38%
- Next close return data: 2.10%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 20일 주식시장 주요공시 | 티에스아이 321억원 믹싱시스템 계약 3개월 연장 | 코세스·에이치와이티씨 상승에도…2차전지 장비주 매도 우위 '촉각'

### 8. 디바이스 (187870)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.42**
- Adjusted recommendation score: **111.45**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -2.40%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 3.10%
- Next close return data: 5.46%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.42 points. Stock pattern label is not_enough_data.
- Related news examples: [IT라운지] '에이전트고' GS 1등급·'보이스 알프' 출시·트레이스위브 ... | K팝부터 편의점까지…일상 파고드는 K뷰티 | 시스템반도체株 불붙었다... 무슨 호재? 눈여겨볼 종목은

### 9. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.39**
- Adjusted recommendation score: **107.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 95.83%, avg next close: 2.58%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 2.19%
- Next close return data: 0.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.39 points. Stock pattern label is relatively_positive_history.
- Related news examples: 석유화학 사업재편 1호 H&L어드밴스드, 통합 후 첫 신입 공채 … 경영관... | HMM, HD현대에 컨테이너선 8척 발주…1조9196억원 규모 | [속보] 엔비디아·마이크론 하락에도 효성중공업·HD현대일렉트릭 상승...

### 10. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.39**
- Adjusted recommendation score: **107.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 95.83%, avg next close: 2.58%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 2.19%
- Next close return data: 0.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.39 points. Stock pattern label is relatively_positive_history.
- Related news examples: 석유화학 사업재편 1호 H&L어드밴스드, 통합 후 첫 신입 공채 … 경영관... | HMM, HD현대에 컨테이너선 8척 발주…1조9196억원 규모 | [속보] 엔비디아·마이크론 하락에도 효성중공업·HD현대일렉트릭 상승...

## Volatile Watchlist

### 1. 삼성물산 (028260)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-0.31**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **5.45**
- Adjusted recommendation score: **52.14**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 21, success rate: 80.95%, avg next close: 0.79%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 2.39%
- Next close return data: 5.88%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 0.31 points. Event-type performance did not change the score. Stock-specific history added 5.45 points. Stock pattern label is relatively_positive_history.
- Related news examples: “외국인들 돌아오나요?”…코스피 3%대 상승, 전날 급락 폭 회복 중 | 삼성물산·롯데건설, 스마트빌딩플랫폼 '바인드' 파트너스 데이 개최·마... | 코스피, 장중 3% 올라 5700 돌파...스페이스X 호실적에 美 기술주 애프터...

### 2. 성창기업지주 (000180)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **39.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 2.00%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 3.05%
- Next close return data: 3.47%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.96 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 일광개발, 성창기업지주 10만2886주 장내매수 | [주요공시] 플리토, HD현대중공업, S-Oil, 메가스터디교육, 대원화성, 다... | 재개장 기약 없는 국내 1호 민간식물원 [존폐 기로에 선 금강식물원]

### 3. 성창기업지주 (000180)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **39.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 2.00%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 3.05%
- Next close return data: 3.47%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.96 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 일광개발, 성창기업지주 10만2886주 장내매수 | [주요공시] 플리토, HD현대중공업, S-Oil, 메가스터디교육, 대원화성, 다... | 재개장 기약 없는 국내 1호 민간식물원 [존폐 기로에 선 금강식물원]

### 4. 성창기업지주 (000180)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **39.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 5, success rate: 60.00%, avg next close: 2.00%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 3.05%
- Next close return data: 3.47%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.96 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 일광개발, 성창기업지주 10만2886주 장내매수 | [주요공시] 플리토, HD현대중공업, S-Oil, 메가스터디교육, 대원화성, 다... | 재개장 기약 없는 국내 1호 민간식물원 [존폐 기로에 선 금강식물원]

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. DB증권 (016610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **44.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **32.54**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 49, success rate: 0.00%, avg next close: 0.63%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.48%
- Next close return data: 1.05%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 시스템반도체株 불붙었다... 무슨 호재? 눈여겨볼 종목은 | 은행 퇴직연금 5조원 감소…7년 만에 첫 '역성장' | [마켓+] 손보사 3분기 실적 기대치 낮추는 증권가, 왜?

### 2. DB증권 (016610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **44.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **32.54**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 49, success rate: 0.00%, avg next close: 0.63%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.48%
- Next close return data: 1.05%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 시스템반도체株 불붙었다... 무슨 호재? 눈여겨볼 종목은 | 은행 퇴직연금 5조원 감소…7년 만에 첫 '역성장' | [마켓+] 손보사 3분기 실적 기대치 낮추는 증권가, 왜?

### 3. DB증권 (016610)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **44.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **32.54**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 49, success rate: 0.00%, avg next close: 0.63%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.48%
- Next close return data: 1.05%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 시스템반도체株 불붙었다... 무슨 호재? 눈여겨볼 종목은 | 은행 퇴직연금 5조원 감소…7년 만에 첫 '역성장' | [마켓+] 손보사 3분기 실적 기대치 낮추는 증권가, 왜?

### 4. 보로노이 (310210)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-0.31**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **4.15**
- Adjusted recommendation score: **43.84**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 16, success rate: 87.50%, avg next close: -1.22%, pattern: relatively_positive_history
- Disclosure title: [기재정정]투자판단관련주요경영사항(임상시험계획변경승인)              (VRN110755의 제 1/2상 임상시험)
- Next open return data: 2.73%
- Next close return data: 8.27%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Negative keyword count is 5. Historical error notes subtracted 0.31 points. Event-type performance did not change the score. Stock-specific history added 4.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 보로노이, 신약 후보의 유럽 임상 변경 승인국가 추가에 7%대 강세 | 보로노이 VRN110755 임상 변경승인에 프랑스·스페인 추가 | [HIT알공] 이오플로우, 인슐렛 소송전서 791억원 배상명령 받아

### 5. 심플랫폼 (444530)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **57.00**
- Error-note adjustment score: **-0.31**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-4.50**
- Adjusted recommendation score: **52.19**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -1.73%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (국책과제 선정  충북청주 첨단 반도체패키징분야 AX 실증산단 구축사업)
- Next open return data: 0.62%
- Next close return data: -1.73%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 0.31 points. Event-type performance did not change the score. Stock-specific history subtracted 4.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 심플랫폼, 말레이시아 제조업 AI 전환 협력 모델 제시 | 10월 20일 주식시장 주요공시 | 심플랫폼, 말레이서 제조업 AX 협력 모델 제시

### 6. 다우기술 (023590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-0.31**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-4.17**
- Adjusted recommendation score: **55.52**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: 2.24%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 2.42%
- Next close return data: 1.67%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 0.31 points. Event-type performance did not change the score. Stock-specific history subtracted 4.17 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 20일 주식시장 주요공시 | [코스피·코스닥,S-Oil 한화생명  HD현대중공업 에이플러스에셋 사람인... | “신생 재단이라 가능한 실험”…예강희망키움재단이 사각지대를 찾아...

### 7. 다우기술 (023590)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **60.00**
- Error-note adjustment score: **-0.31**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-4.17**
- Adjusted recommendation score: **55.52**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: 2.24%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 2.42%
- Next close return data: 1.67%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 0.31 points. Event-type performance did not change the score. Stock-specific history subtracted 4.17 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 20일 주식시장 주요공시 | [코스피·코스닥,S-Oil 한화생명  HD현대중공업 에이플러스에셋 사람인... | “신생 재단이라 가능한 실험”…예강희망키움재단이 사각지대를 찾아...

### 8. 알파칩스 (117670)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **82.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.62**
- Adjusted recommendation score: **72.29**
- Risk level: **HIGH**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 13, success rate: 7.69%, avg next close: -0.48%, pattern: weak_historical_reaction
- Disclosure title: 권리락              (무상증자)
- Next open return data: 2.14%
- Next close return data: 1.84%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.62 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 시스템반도체株 불붙었다... 무슨 호재? 눈여겨볼 종목은 | 알파칩스 무상증자 권리락…기준가 6950원 | "기업이 먼저 찾는 AI 반도체 인재 양성"... 대한상공회의소 서울기술교...

### 9. 싸이토젠 (217330)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.67**
- Adjusted recommendation score: **88.20**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: 0.16%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.00%
- Next close return data: 0.18%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.67 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 20일 주식시장 주요공시 | 싸이토젠 장비 납품기한 12월 4일로 변경 | 글로벌 웰니스 시장 커진다… 건강기능식품·바이오 기업 노려라

### 10. 삼일기업공사 (002290)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.13**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **90.37**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.31%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.16%
- Next close return data: 0.31%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 5. Historical error notes subtracted 1.13 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 20일 주식시장 주요공시 | 건국대병원 증축공사 계약금 249억원…삼일기업공사 정정 | 부동산 경기 회복 더딘데 원가 부담까지…중소형 건설주 '휘청'

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
