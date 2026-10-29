# Daily Stock Candidate Report - 2026-10-20

Generated at: 2026-10-20 01:45:27

ML dataset: `data/processed/ml_dataset_20261020.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 9 | 9 | 100.00% | 8.27% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 4 | 4 | 100.00% | 6.91% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 002720 | 국제약품 | 10 | 8 | 100.00% | 27.30% | relatively_positive_history | 8.80 |
| 109670 | 씨싸이트 | 4 | 3 | 100.00% | 29.99% | relatively_positive_history | 8.75 |
| 373170 | 엠아이큐브솔루션 | 10 | 10 | 80.00% | 23.51% | relatively_positive_history | 8.65 |
| 006980 | 우성 | 15 | 9 | 100.00% | 8.46% | relatively_positive_history | 8.60 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 100.00% | 1.92% | 8.00 |
| lawsuit | 413 | 292 | 58.22% | -0.78% | 3.00 |
| paid_in_capital_increase | 2196 | 1676 | 57.58% | 0.18% | 3.00 |
| spin_off | 112 | 80 | 51.25% | 1.80% | 2.00 |
| investment_decision | 394 | 279 | 54.84% | -0.23% | 0.00 |
| disclosure_violation | 168 | 98 | 48.98% | -0.46% | 0.00 |
| convertible_bond | 1087 | 755 | 52.45% | 0.89% | 0.00 |
| bonus_issue | 102 | 99 | 41.41% | -0.40% | -3.00 |
| major_shareholder_change | 2120 | 1487 | 35.31% | -0.67% | -3.00 |
| bond_with_warrant | 117 | 105 | 23.81% | 0.47% | -6.00 |
| merger | 418 | 323 | 19.50% | 0.35% | -6.00 |
| supply_contract | 1231 | 905 | 29.83% | -0.84% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 8 | 4 | 0 | 4 | 2.50 |
| paid_in_capital_increase | 2196 | 965 | 711 | 520 | 1.23 |
| lawsuit | 413 | 170 | 122 | 121 | 1.17 |
| convertible_bond | 1087 | 396 | 359 | 332 | 0.83 |
| disclosure_violation | 168 | 48 | 50 | 70 | 0.54 |
| investment_decision | 394 | 153 | 126 | 115 | -0.30 |
| spin_off | 112 | 41 | 39 | 32 | -0.61 |
| bond_with_warrant | 117 | 25 | 80 | 12 | -0.98 |
| bonus_issue | 102 | 41 | 58 | 3 | -1.15 |
| supply_contract | 1231 | 270 | 635 | 326 | -1.19 |

## Positive Candidates

### 1. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 2. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 3. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 4. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 5. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 6. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 7. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 8. 비나텍 (126340)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **139.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **9.00**
- Adjusted recommendation score: **140.81**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 100.00%, avg next close: 8.27%, pattern: relatively_positive_history
- Disclosure title: 주권매매거래정지              (단일판매공급계약)
- Next open return data: 20.73%
- Next close return data: 9.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 9.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [특징주]비나텍, 대만 ACBEL과 1천230억 원 슈퍼커패시터 계약에 11.09% 오... | 국내증시 개장부터 '휘청'…코스피·코스닥 동반 하락 출발 | [특징주] 비나텍, 슈퍼커패시터 공급 계약…주가 13%↑

### 9. 비아트론 (141000)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.38**
- Adjusted recommendation score: **118.43**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -2.32%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.96%
- Next close return data: -6.95%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.38 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 19일 주식시장 주요공시 | 바이오인프라 105%·삼기에너지솔루션즈 96%…회전율 상위권 | "GIST '반도체 혁신기술' 2종, 소부장 기업들 러브콜 기대"

### 10. S-Oil (010950)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **8.45**
- Adjusted recommendation score: **113.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 72.73%, avg next close: 3.27%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.48%
- Next close return data: -7.58%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history added 8.45 points. Stock pattern label is relatively_positive_history.
- Related news examples: China Sets Licensing and Registration Rules for Tunnel Boring Exports | 전남광주특별시, 10월의 친환경농산물에 해남 명랑농원 ‘유기농 오디’... | 10월 19일 주식시장 주요공시

## Volatile Watchlist

### 1. DL (000210)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-0.30**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **83.70**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 4, success rate: 100.00%, avg next close: -1.41%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항(자회사의 주요경영사항)              
- Next open return data: -1.45%
- Next close return data: -2.68%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.30 points. Event-type performance did not change the score. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 국민연금, 포트폴리오 대수술..석유화학·건설 ‘담고’ 반도체·조선방... | [빅데이터투데이] 건설회사 2026년 10월 브랜드평판 랭킹... 1위 현대건설... | SCL사이언스, 베트남 국립 '후에중앙병원'과 MOU 체결…해외 매출 신호탄

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 에스트래픽 (234300)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.31**
- Adjusted recommendation score: **77.50**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -1.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.17%
- Next close return data: -2.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.31 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, ITS 세계총회서 K-MaaS 구축·운영..."교통 플랫폼 역량 확...

### 2. 에스트래픽 (234300)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.31**
- Adjusted recommendation score: **77.50**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -1.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.17%
- Next close return data: -2.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.31 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, ITS 세계총회서 K-MaaS 구축·운영..."교통 플랫폼 역량 확...

### 3. 에스트래픽 (234300)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.31**
- Adjusted recommendation score: **77.50**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -1.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.17%
- Next close return data: -2.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.31 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, ITS 세계총회서 K-MaaS 구축·운영..."교통 플랫폼 역량 확...

### 4. 에스트래픽 (234300)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.31**
- Adjusted recommendation score: **77.50**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 0.00%, avg next close: -1.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.17%
- Next close return data: -2.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.31 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, '2026 강릉 ITS 세계총회' K-MaaS 총괄 | 에스트래픽, ITS 세계총회서 K-MaaS 구축·운영..."교통 플랫폼 역량 확...

### 5. 디바이스 (187870)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.88**
- Adjusted recommendation score: **87.93**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -10.26%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -2.24%
- Next close return data: -10.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.88 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 엑스와이지, 엔비디아 교육에 휴머노이드 '듀스' 10대 공급 | 임팩티브AI, 노타와 전략적 MOU 체결…공급망·제조 AI 혁신 가속 | 앳홈, 日 굿 디자인 어워드서 4개 제품 수상…사용 편의성 강조

### 6. 일성건설 (013360)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.55**
- Adjusted recommendation score: **89.26**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 0.00%, avg next close: -1.62%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.08%
- Next close return data: -2.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.55 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [빅데이터투데이] 건설회사 2026년 10월 브랜드평판 랭킹... 1위 현대건설... | 현대건설, 건설회사 브랜드평판 10월 빅데이터 1위... 롯데·대우건설 순 | 10월 19일 주식시장 주요공시

### 7. 스피어 (347700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.13**
- Adjusted recommendation score: **93.68**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 13, success rate: 38.46%, avg next close: -1.33%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.91%
- Next close return data: -3.86%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.13 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 알바몬, AI 기반 채용 솔루션 '스마트픽' 선봬…맞춤형 채용 서비스 확... | 1.6조 낭비한 '공공 AI데이터'…스타트업은 현장서 이미 답 찾았다 | 알바몬, AI 채용 서비스 '스마트픽' 도입…클릭당 과금 적용

### 8. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-1.69**
- Adjusted recommendation score: **98.12**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 17, success rate: 47.06%, avg next close: -1.49%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.34%
- Next close return data: -6.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 1.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [빅데이터투데이] 건설회사 2026년 10월 브랜드평판 랭킹... 1위 현대건설... | 현대건설, 건설회사 브랜드평판 10월 빅데이터 1위... 롯데·대우건설 순 | 10월 19일 주식시장 주요공시

### 9. 동아지질 (028100)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **106.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-0.15**
- Adjusted recommendation score: **98.66**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 8, success rate: 50.00%, avg next close: -0.97%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.62%
- Next close return data: -2.31%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 3. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 0.15 points. Stock pattern label is not_enough_data.
- Related news examples: 10월 19일 주식시장 주요공시 | [공시] 10월 20일, 코스피 상장사 50개 종목 자사주 매수 신청 | 철도 관련주 일제히 요동…정책 기대와 실제 수주 구분해야

### 10. 미래산업 (025560)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.75**
- Adjusted recommendation score: **101.06**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 22.22%, avg next close: -1.87%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.89%
- Next close return data: -6.54%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.19 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.75 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 이준형 서울시의회 기획경제위원장, '2026 서울투자서밋' 개막식 참석 | 고려대 강형엽·김영근 교수, 과기정통부 'AI최고급신진연구자지원사업... | 파주시, 평화경제특구 지정 총력전…푸드테크 기업 유치까지 '투트랙 전...

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
