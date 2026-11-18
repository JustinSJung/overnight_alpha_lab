# Daily Stock Candidate Report - 2026-11-18

Generated at: 2026-11-18 04:51:00

ML dataset: `data/processed/ml_dataset_20261118.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 870 | 774 | 45.87% | 5.00% | 4.00 |
| convertible_bond | 1639 | 1306 | 58.58% | 0.34% | 3.00 |
| paid_in_capital_increase | 2955 | 2434 | 55.46% | -0.19% | 3.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| investment_decision | 607 | 492 | 51.02% | 0.22% | 0.00 |
| lawsuit | 630 | 509 | 49.90% | -0.33% | 0.00 |
| disclosure_violation | 218 | 148 | 41.22% | -0.38% | -3.00 |
| bond_with_warrant | 162 | 150 | 42.00% | 0.03% | -3.00 |
| spin_off | 156 | 120 | 39.17% | 0.87% | -3.00 |
| major_shareholder_change | 3229 | 2595 | 38.07% | -0.72% | -3.00 |
| supply_contract | 1866 | 1540 | 36.10% | -0.58% | -3.00 |
| earnings_guidance | 96 | 92 | 26.09% | -1.87% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1639 | 765 | 541 | 333 | 1.34 |
| paid_in_capital_increase | 2955 | 1350 | 1084 | 521 | 1.18 |
| lawsuit | 630 | 254 | 255 | 121 | 0.80 |
| bond_with_warrant | 162 | 63 | 87 | 12 | 0.33 |
| disclosure_violation | 218 | 61 | 87 | 70 | 0.20 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 607 | 251 | 241 | 115 | -0.71 |
| supply_contract | 1866 | 556 | 984 | 326 | -0.93 |
| merger | 870 | 355 | 419 | 96 | -1.33 |
| earnings_guidance | 96 | 24 | 68 | 4 | -1.54 |

## Positive Candidates

### 1. 코오롱글로벌 (003070)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.63**
- Adjusted recommendation score: **135.70**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 32, success rate: 56.25%, avg next close: 0.71%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.72%
- Next close return data: -3.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.63 points. Stock pattern label is relatively_positive_history.
- Related news examples: 구미상의소·iM뱅크, 제42회 CEO포럼 개최…AI 시대 산업 변화 조망 | 주요 공시(17일)-삼성바이오로직스 등 | 원가 개선·합병 효과 톡톡…코오롱글로벌, 3분기 수익성·외형↑

### 2. 코오롱글로벌 (003070)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.63**
- Adjusted recommendation score: **135.70**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 32, success rate: 56.25%, avg next close: 0.71%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.72%
- Next close return data: -3.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.63 points. Stock pattern label is relatively_positive_history.
- Related news examples: 구미상의소·iM뱅크, 제42회 CEO포럼 개최…AI 시대 산업 변화 조망 | 주요 공시(17일)-삼성바이오로직스 등 | 원가 개선·합병 효과 톡톡…코오롱글로벌, 3분기 수익성·외형↑

### 3. 아센디오 (012170)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.48**
- Adjusted recommendation score: **130.55**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 72.73%, avg next close: -3.66%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.15%
- Next close return data: -6.64%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.48 points. Stock pattern label is relatively_positive_history.
- Related news examples: 주요 공시(17일)-삼성바이오로직스 등 | 11월 17일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 18일] 美 증시, 엔비디아 실적 앞두고 AI 불안...

### 4. 미래컴퍼니 (049950)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **117.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.31**
- Adjusted recommendation score: **118.38**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.82%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.40%
- Next close return data: 2.99%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 1. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.31 points. Stock pattern label is relatively_positive_history.
- Related news examples: 주요 공시(17일)-삼성바이오로직스 등 | 전고체 배터리 관련주 상승세…삼성전기 6.23%·이수스페셜티케미컬 1.1... | AI 반도체 패키징 판 바꿀 유리 기판… 삼성전기·태성 '신바람'

### 5. 코오롱 (002020)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.67**
- Adjusted recommendation score: **103.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 34, success rate: 91.18%, avg next close: 0.76%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.94%
- Next close return data: 0.17%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.67 points. Stock pattern label is relatively_positive_history.
- Related news examples: 레저용품 2026년 11월 브랜드평판...데카트론, 스노우피크, 노스페이스 ... | 구미상의소·iM뱅크, 제42회 CEO포럼 개최…AI 시대 산업 변화 조망 | 대기업 계열사 3개월 새 5곳 감소…SK 11곳 줄이고 한화 6곳 늘려

### 6. 코오롱 (002020)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **102.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.67**
- Adjusted recommendation score: **103.74**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 34, success rate: 91.18%, avg next close: 0.76%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.94%
- Next close return data: 0.17%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 1. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.67 points. Stock pattern label is relatively_positive_history.
- Related news examples: 레저용품 2026년 11월 브랜드평판...데카트론, 스노우피크, 노스페이스 ... | 구미상의소·iM뱅크, 제42회 CEO포럼 개최…AI 시대 산업 변화 조망 | 대기업 계열사 3개월 새 5곳 감소…SK 11곳 줄이고 한화 6곳 늘려

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 2. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 3. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 4. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 5. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 6. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 7. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 8. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 9. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

### 10. 싸이버원 (356890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.93**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **103.57**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.65%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.26%
- Next close return data: -0.45%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.93 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 싸이버원, 국가고용전산망 보안관제 41억원 수주 | 주요 공시(17일)-삼성바이오로직스 등 | 싸이버원, 한국고용정보원 국가고용전산망 보안관제 운영지원 사업 수주

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
