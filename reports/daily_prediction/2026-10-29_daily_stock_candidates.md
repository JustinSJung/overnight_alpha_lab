# Daily Stock Candidate Report - 2026-10-29

Generated at: 2026-10-29 02:25:50

ML dataset: `data/processed/ml_dataset_20261029.csv`

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
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 12 | 12 | 100.00% | 4.48% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 295310 | 에이치브이엠 | 9 | 9 | 100.00% | 3.75% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2407 | 1887 | 58.51% | -0.16% | 3.00 |
| lawsuit | 493 | 372 | 56.45% | -0.37% | 3.00 |
| spin_off | 117 | 85 | 51.76% | 1.61% | 2.00 |
| convertible_bond | 1205 | 872 | 54.01% | 0.69% | 0.00 |
| investment_decision | 436 | 321 | 52.65% | -0.07% | 0.00 |
| major_shareholder_change | 2396 | 1763 | 37.32% | -0.77% | -3.00 |
| bonus_issue | 105 | 102 | 41.18% | -0.58% | -3.00 |
| disclosure_violation | 188 | 118 | 43.22% | -0.27% | -3.00 |
| bond_with_warrant | 117 | 105 | 23.81% | 0.47% | -6.00 |
| earnings_guidance | 50 | 46 | 32.61% | 0.97% | -6.00 |
| merger | 584 | 488 | 32.58% | 0.05% | -6.00 |
| supply_contract | 1411 | 1085 | 32.63% | -0.67% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2407 | 1104 | 783 | 520 | 1.32 |
| lawsuit | 493 | 210 | 162 | 121 | 1.14 |
| convertible_bond | 1205 | 471 | 401 | 333 | 0.96 |
| disclosure_violation | 188 | 51 | 67 | 70 | 0.29 |
| investment_decision | 436 | 169 | 152 | 115 | -0.50 |
| spin_off | 117 | 44 | 41 | 32 | -0.57 |
| earnings_guidance | 50 | 15 | 31 | 4 | -0.84 |
| bond_with_warrant | 117 | 25 | 80 | 12 | -0.98 |
| supply_contract | 1411 | 354 | 731 | 326 | -1.09 |
| bonus_issue | 105 | 42 | 60 | 3 | -1.16 |

## Positive Candidates

### 1. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 2. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 3. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 4. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 5. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 6. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 7. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 8. 에이치브이엠 (295310)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **157.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **158.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 3.75%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.58%
- Next close return data: 2.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 14. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동... | [주요공시] SK하이닉스, 삼성전자, 에이치브이엠, 기가비스, 레인보우로...

### 9. 기가비스 (420770)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **136.53**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 50.00%, avg next close: -1.21%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -1.47%
- Next close return data: -6.81%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 28일 주식시장 주요공시 | [코스피·코스닥, SK하이닉스 우진아이엔에스 LG전자 HD현대중공업 농협... | [N2 모닝 경제 브리핑-10월 29일] 美 증시, 연준 금리 동결에 3대 지수 동...

### 10. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **1.05**
- Adjusted recommendation score: **105.96**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 55.56%, avg next close: -2.91%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.41%
- Next close return data: -4.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 1.05 points. Stock pattern label is relatively_positive_history.
- Related news examples: [52주] 신고가 7개, 신저가 71개...지수 보합 | 10월 28일 주식시장 주요공시 | HJ중공업 등 4개사, 군산에 해상풍력 클러스터 구축…조선업 새 성장동...

## Volatile Watchlist

### 1. 콜마비앤에이치 (200130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **89.00**
- Error-note adjustment score: **-2.58**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **89.42**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 12, success rate: 100.00%, avg next close: 4.48%, pattern: relatively_positive_history
- Disclosure title: 주요사항보고서(회사합병결정)
- Next open return data: 11.80%
- Next close return data: 4.48%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 12. Negative keyword count is 2. Historical error notes subtracted 2.58 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 콜마비앤에이치, 3Q 영업익 12.4%↑…에치엔지 흡수합병도 추진 | 콜마비앤에이치, 3분기 별도 매출 감소에도 영업이익 12.4% 증가 | 콜마비앤에이치, 3분기 누적 영업익 32.6% 증가

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 우리기술 (032820)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **106.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.94**
- Adjusted recommendation score: **89.97**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.15%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.65%
- Next close return data: -8.14%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: LS그룹, 협력사 80곳과 '동반성장' 머리 맞댔다… AI 전환·글로벌 불확... | 조승래 의원, 우주항공·로봇·방위산업·조선 국가전략기술 추가 조특... | LS그룹, 협력사와 미래 성장전략 모색… 공급망 경쟁력 강화 '한뜻'

### 2. 우리기술 (032820)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **106.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.94**
- Adjusted recommendation score: **89.97**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 0.00%, avg next close: -5.15%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.65%
- Next close return data: -8.14%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: LS그룹, 협력사 80곳과 '동반성장' 머리 맞댔다… AI 전환·글로벌 불확... | 조승래 의원, 우주항공·로봇·방위산업·조선 국가전략기술 추가 조특... | LS그룹, 협력사와 미래 성장전략 모색… 공급망 경쟁력 강화 '한뜻'

### 3. 신원종합개발 (017000)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **108.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-8.94**
- Adjusted recommendation score: **91.97**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -3.18%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -3.09%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 4. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 8.94 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 28일 주식시장 주요공시 | "국내 분양 경기 침체 부담"… 건설 관련주, 숨고르기 장세 뚜렷 | 건설주 일제히 들썩…삼성E&A 13% 급등, 해외 수주 기대 커졌다

### 4. 엑시온그룹 (069920)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **101.00**
- Error-note adjustment score: **-1.09**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.45**
- Adjusted recommendation score: **96.36**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 25, success rate: 88.00%, avg next close: -4.43%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.05%
- Next close return data: 5.92%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 3. Historical error notes subtracted 1.09 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.45 points. Stock pattern label is relatively_positive_history.
- Related news examples: 10월 28일 주식시장 주요공시 | [기획] 왜 본업보다 부동산인가…'오래 가진 땅'이 효자된 이유 | 루닛 상한가·노을 29.94%…주식 상승률 상위권 강세

### 5. 한세실업 (105630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-0.84**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **97.91**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -1.81%, pattern: weak_historical_reaction
- Disclosure title: 연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 0.12%
- Next close return data: -1.81%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.84 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한세예스24그룹, 배당 40%와 매출 6조원 청사진 | 10월 28일 주식시장 주요공시 | 한세예스24 “2032년 매출 6조…AI 투자·중미 생산 확대”

### 6. 한세실업 (105630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-0.84**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **97.91**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -1.81%, pattern: weak_historical_reaction
- Disclosure title: 연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 0.12%
- Next close return data: -1.81%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.84 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한세예스24그룹, 배당 40%와 매출 6조원 청사진 | 10월 28일 주식시장 주요공시 | 한세예스24 “2032년 매출 6조…AI 투자·중미 생산 확대”

### 7. 한세실업 (105630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-0.84**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **97.91**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -1.81%, pattern: weak_historical_reaction
- Disclosure title: 영업실적등에대한전망(공정공시)              
- Next open return data: 0.12%
- Next close return data: -1.81%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.84 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한세예스24그룹, 배당 40%와 매출 6조원 청사진 | 10월 28일 주식시장 주요공시 | 한세예스24 “2032년 매출 6조…AI 투자·중미 생산 확대”

### 8. 한세실업 (105630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-0.84**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **97.91**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -1.81%, pattern: weak_historical_reaction
- Disclosure title: 영업실적등에대한전망(공정공시)              
- Next open return data: 0.12%
- Next close return data: -1.81%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.84 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한세예스24그룹, 배당 40%와 매출 6조원 청사진 | 10월 28일 주식시장 주요공시 | 한세예스24 “2032년 매출 6조…AI 투자·중미 생산 확대”

### 9. 한세실업 (105630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-0.84**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **97.91**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -1.81%, pattern: weak_historical_reaction
- Disclosure title: 영업실적등에대한전망(공정공시)              
- Next open return data: 0.12%
- Next close return data: -1.81%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.84 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한세예스24그룹, 배당 40%와 매출 6조원 청사진 | 10월 28일 주식시장 주요공시 | 한세예스24 “2032년 매출 6조…AI 투자·중미 생산 확대”

### 10. 한세실업 (105630)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-0.84**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.25**
- Adjusted recommendation score: **97.91**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -1.81%, pattern: weak_historical_reaction
- Disclosure title: 연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: 0.12%
- Next close return data: -1.81%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.84 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한세예스24그룹, 배당 40%와 매출 6조원 청사진 | 10월 28일 주식시장 주요공시 | 한세예스24 “2032년 매출 6조…AI 투자·중미 생산 확대”

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
