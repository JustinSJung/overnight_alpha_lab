# Daily Stock Candidate Report - 2026-10-30

Generated at: 2026-10-30 02:32:21

ML dataset: `data/processed/ml_dataset_20261030.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1303 | 970 | 57.42% | 0.53% | 3.00 |
| lawsuit | 497 | 376 | 56.12% | -0.38% | 3.00 |
| paid_in_capital_increase | 2482 | 1962 | 57.95% | -0.18% | 3.00 |
| spin_off | 117 | 85 | 51.76% | 1.61% | 2.00 |
| investment_decision | 439 | 324 | 52.78% | -0.09% | 0.00 |
| disclosure_violation | 189 | 119 | 42.86% | -0.27% | -3.00 |
| bond_with_warrant | 145 | 133 | 39.85% | 0.23% | -3.00 |
| bonus_issue | 105 | 102 | 41.18% | -0.58% | -3.00 |
| major_shareholder_change | 2427 | 1794 | 38.02% | -0.78% | -3.00 |
| earnings_guidance | 62 | 58 | 25.86% | 0.17% | -6.00 |
| merger | 591 | 495 | 33.54% | 0.01% | -6.00 |
| supply_contract | 1465 | 1139 | 31.61% | -0.77% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2482 | 1137 | 825 | 520 | 1.29 |
| convertible_bond | 1303 | 557 | 413 | 333 | 1.19 |
| lawsuit | 497 | 211 | 165 | 121 | 1.13 |
| disclosure_violation | 189 | 51 | 68 | 70 | 0.27 |
| bond_with_warrant | 145 | 53 | 80 | 12 | 0.17 |
| investment_decision | 439 | 171 | 153 | 115 | -0.49 |
| spin_off | 117 | 44 | 41 | 32 | -0.57 |
| bonus_issue | 105 | 42 | 60 | 3 | -1.16 |
| supply_contract | 1465 | 360 | 779 | 326 | -1.17 |
| earnings_guidance | 62 | 15 | 43 | 4 | -1.26 |

## Positive Candidates

### 1. 네이블 (153460)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **155.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **150.33**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.36%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.21%
- Next close return data: 0.21%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 29일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 30일] 美 증시, 알파벳 실적 충격에 일제히 ... | 네이블, SK텔레콤에 19억2000만원 규모 공급

### 2. 아센디오 (012170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **140.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.59**
- Adjusted recommendation score: **135.42**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 80.00%, avg next close: -3.36%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -3.86%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.59 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 29일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 30일] 美 증시, 알파벳 실적 충격에 일제히 ... | 아센디오, 글로벌 유통사에 화장품 5억5564만원 공급

### 3. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **119.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.25**
- Adjusted recommendation score: **119.08**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 10, success rate: 90.00%, avg next close: 2.44%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -2.55%
- Next close return data: -9.30%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.25 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 29일 주식시장 주요공시 | 페로타임즈 손바닥뉴스 10월30일(금) | 에이치브이엠, 해외 우주항공 금속 유통사와 190억 규모 특수합금 공급...

### 4. 다스코 (058730)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.18**
- Adjusted recommendation score: **106.65**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 50.00%, avg next close: -0.71%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.74%
- Next close return data: -1.67%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.18 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 29일 주식시장 주요공시 | 다스코, 60억원 사모 BW 발행 결정…채무 상환 목적 | 한솔테크닉스 11% 상승랠리…태양광 관련주 무슨 호재 있나

### 5. 다스코 (058730)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.18**
- Adjusted recommendation score: **106.65**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 50.00%, avg next close: -0.71%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.74%
- Next close return data: -1.67%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.18 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 29일 주식시장 주요공시 | 다스코, 60억원 사모 BW 발행 결정…채무 상환 목적 | 한솔테크닉스 11% 상승랠리…태양광 관련주 무슨 호재 있나

### 6. 다스코 (058730)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.18**
- Adjusted recommendation score: **106.65**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 50.00%, avg next close: -0.71%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.74%
- Next close return data: -1.67%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.18 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 29일 주식시장 주요공시 | 다스코, 60억원 사모 BW 발행 결정…채무 상환 목적 | 한솔테크닉스 11% 상승랠리…태양광 관련주 무슨 호재 있나

### 7. 다스코 (058730)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.18**
- Adjusted recommendation score: **106.65**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 50.00%, avg next close: -0.71%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.74%
- Next close return data: -1.67%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.18 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 29일 주식시장 주요공시 | 다스코, 60억원 사모 BW 발행 결정…채무 상환 목적 | 한솔테크닉스 11% 상승랠리…태양광 관련주 무슨 호재 있나

### 8. 계룡건설산업 (013580)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **109.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.94**
- Adjusted recommendation score: **105.77**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 57.14%, avg next close: 2.12%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.64%
- Next close return data: -3.82%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.94 points. Stock pattern label is relatively_positive_history.
- Related news examples: 서울 입주물량 감소 전망, 연말 신규 분양 '정비사업 중심' | [한국 건설, 80년의 기록]⑯ 아파트로 쌓아 올린 48년…제일건설, 이제 ... | [N2 모닝 경제 브리핑-10월 30일] 美 증시, 알파벳 실적 충격에 일제히 ...

## Volatile Watchlist

### 1. 콜마비앤에이치 (200130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.49**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.51**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 15, success rate: 100.00%, avg next close: 3.14%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -1.17%
- Next close return data: -2.21%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes subtracted 2.49 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 콜마비앤에이치, 3Q 영업益 12.4%↑… 누적 317억원·HNG 흡수합병 추진 | ‘취임 1년’ 이승화 콜마비앤에이치 대표, ‘선택과 집중’ 통했다 | "영업익 33%↑·영업이익률 8.8%"…콜마BNH, 해외 ODM 성장에 수익성 개선

### 2. 콜마비앤에이치 (200130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.49**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.51**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 15, success rate: 100.00%, avg next close: 3.14%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -1.17%
- Next close return data: -2.21%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes subtracted 2.49 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 콜마비앤에이치, 3Q 영업益 12.4%↑… 누적 317억원·HNG 흡수합병 추진 | ‘취임 1년’ 이승화 콜마비앤에이치 대표, ‘선택과 집중’ 통했다 | "영업익 33%↑·영업이익률 8.8%"…콜마BNH, 해외 ODM 성장에 수익성 개선

### 3. 콜마비앤에이치 (200130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.49**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.51**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 15, success rate: 100.00%, avg next close: 3.14%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -1.17%
- Next close return data: -2.21%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes subtracted 2.49 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 콜마비앤에이치, 3Q 영업益 12.4%↑… 누적 317억원·HNG 흡수합병 추진 | ‘취임 1년’ 이승화 콜마비앤에이치 대표, ‘선택과 집중’ 통했다 | "영업익 33%↑·영업이익률 8.8%"…콜마BNH, 해외 ODM 성장에 수익성 개선

### 4. 콜마비앤에이치 (200130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-2.49**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **97.51**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 15, success rate: 100.00%, avg next close: 3.14%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: -1.17%
- Next close return data: -2.21%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 13. Negative keyword count is 1. Historical error notes subtracted 2.49 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 콜마비앤에이치, 3Q 영업益 12.4%↑… 누적 317억원·HNG 흡수합병 추진 | ‘취임 1년’ 이승화 콜마비앤에이치 대표, ‘선택과 집중’ 통했다 | "영업익 33%↑·영업이익률 8.8%"…콜마BNH, 해외 ODM 성장에 수익성 개선

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 한국정밀기계 (101680)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.94**
- Adjusted recommendation score: **97.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -3.38%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -6.09%
- Next close return data: -8.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 29일 주식시장 주요공시 | 한국정밀기계 씨에스베어링 계약 종료일 2028년 2월로 변경 | 한국정밀기계, 베트남 공급 'Turning Machine' 계약 기간 2028년 2월로 연...

### 2. 현대건설 (000720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.64**
- Adjusted recommendation score: **101.19**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 12, success rate: 33.33%, avg next close: -2.40%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.98%
- Next close return data: -4.61%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.64 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 현대차그룹, 새만금 AI 데이터센터 내년 착공…9조원 투자 속도 | 현대차그룹, 새만금 9조원 AI 밸리 투자 '속도' … 2030년 데이터센터 가... | 현대차그룹, 새만금 AI 센터 내년 3월 착공…“목표는 2030년 초 가동”

### 3. 퀄리타스반도체 (432720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.58**
- Adjusted recommendation score: **101.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 16.67%, avg next close: -3.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.69%
- Next close return data: -6.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.58 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 29일 주식시장 주요공시 | 생체현미경 국산화·해외 진출 성과···아이빔테크놀로지 '유공 표창' | HBM부터 후공정까지… 반도체와반도체장비 관련주 옥석 가리기 본격화

### 4. 퀄리타스반도체 (432720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.58**
- Adjusted recommendation score: **101.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 16.67%, avg next close: -3.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.69%
- Next close return data: -6.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.58 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 29일 주식시장 주요공시 | 생체현미경 국산화·해외 진출 성과···아이빔테크놀로지 '유공 표창' | HBM부터 후공정까지… 반도체와반도체장비 관련주 옥석 가리기 본격화

### 5. 퀄리타스반도체 (432720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.58**
- Adjusted recommendation score: **101.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 16.67%, avg next close: -3.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.69%
- Next close return data: -6.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.58 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 29일 주식시장 주요공시 | 생체현미경 국산화·해외 진출 성과···아이빔테크놀로지 '유공 표창' | HBM부터 후공정까지… 반도체와반도체장비 관련주 옥석 가리기 본격화

### 6. 퀄리타스반도체 (432720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.58**
- Adjusted recommendation score: **101.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 16.67%, avg next close: -3.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.69%
- Next close return data: -6.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.58 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 29일 주식시장 주요공시 | 생체현미경 국산화·해외 진출 성과···아이빔테크놀로지 '유공 표창' | HBM부터 후공정까지… 반도체와반도체장비 관련주 옥석 가리기 본격화

### 7. 퀄리타스반도체 (432720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.58**
- Adjusted recommendation score: **101.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 16.67%, avg next close: -3.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.69%
- Next close return data: -6.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.58 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 29일 주식시장 주요공시 | 생체현미경 국산화·해외 진출 성과···아이빔테크놀로지 '유공 표창' | HBM부터 후공정까지… 반도체와반도체장비 관련주 옥석 가리기 본격화

### 8. 퀄리타스반도체 (432720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.58**
- Adjusted recommendation score: **101.25**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 16.67%, avg next close: -3.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.69%
- Next close return data: -6.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.58 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 29일 주식시장 주요공시 | 생체현미경 국산화·해외 진출 성과···아이빔테크놀로지 '유공 표창' | HBM부터 후공정까지… 반도체와반도체장비 관련주 옥석 가리기 본격화

### 9. 동부건설 (005960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-5.44**
- Adjusted recommendation score: **102.39**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 14.29%, avg next close: -0.91%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.53%
- Next close return data: -4.21%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 5.44 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 홍지선 국토장관 “중계동서 5년 살았다”…상계2구역 찾아 재개발 속도... | 홍지선, 재개발 현장 상계2구역서 “조기 착공 땐 세제 혜택” | [영상] 디에이치·자이·르엘 한꺼번에···방배동 재건축 벨트

### 10. 우원개발 (046940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **118.00**
- Error-note adjustment score: **-1.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.40**
- Adjusted recommendation score: **103.43**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -1.81%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.60%
- Next close return data: -4.37%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 4. Historical error notes subtracted 1.17 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.40 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 신고가 2개 , 신저가 169개... 코스피 3%대 하락 | 10월 29일 주식시장 주요공시 | 우원개발 강릉~제진 4공구 계약액 547억원으로 증액

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
