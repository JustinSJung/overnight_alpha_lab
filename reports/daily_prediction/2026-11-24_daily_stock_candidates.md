# Daily Stock Candidate Report - 2026-11-24

Generated at: 2026-11-24 06:54:34

ML dataset: `data/processed/ml_dataset_20261124.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 052460 | 아이크래프트 | 12 | 12 | 100.00% | 3.50% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 10 | 10 | 100.00% | 16.52% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 248170 | 샘표식품 | 22 | 22 | 95.45% | 26.45% | relatively_positive_history | 8.89 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 914 | 818 | 46.09% | 4.89% | 4.00 |
| convertible_bond | 1693 | 1360 | 59.49% | 0.24% | 3.00 |
| paid_in_capital_increase | 3125 | 2604 | 57.10% | -0.21% | 3.00 |
| bonus_issue | 120 | 117 | 47.86% | 0.36% | 0.00 |
| investment_decision | 655 | 540 | 51.67% | 0.16% | 0.00 |
| lawsuit | 668 | 547 | 51.74% | -0.45% | 0.00 |
| disclosure_violation | 230 | 160 | 43.75% | -0.91% | -3.00 |
| bond_with_warrant | 163 | 151 | 41.72% | 0.04% | -3.00 |
| spin_off | 158 | 122 | 39.34% | 0.83% | -3.00 |
| major_shareholder_change | 3389 | 2755 | 40.18% | -0.81% | -3.00 |
| supply_contract | 1986 | 1660 | 35.54% | -0.70% | -3.00 |
| earnings_guidance | 96 | 92 | 26.09% | -1.87% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1693 | 809 | 551 | 333 | 1.41 |
| paid_in_capital_increase | 3125 | 1487 | 1117 | 521 | 1.31 |
| lawsuit | 668 | 283 | 264 | 121 | 0.93 |
| disclosure_violation | 230 | 70 | 90 | 70 | 0.35 |
| bond_with_warrant | 163 | 63 | 88 | 12 | 0.31 |
| bonus_issue | 120 | 56 | 61 | 3 | -0.46 |
| investment_decision | 655 | 279 | 261 | 115 | -0.66 |
| supply_contract | 1986 | 590 | 1070 | 326 | -1.02 |
| merger | 914 | 377 | 441 | 96 | -1.32 |
| earnings_guidance | 96 | 24 | 68 | 4 | -1.54 |

## Positive Candidates

### 1. 기가비스 (420770)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.14**
- Adjusted recommendation score: **141.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 54.55%, avg next close: 0.23%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.92%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 0.14 points. Stock pattern label is relatively_positive_history.
- Related news examples: AI 데이터센터가 바꾸는 반도체 공급망…이수페타시스·대덕전자· 코리... | AI 반도체가 키운 유리 기판 시장…삼성전기·SKC에 '쏠린 시선' | 11월 23일 주식시장 주요공시

### 2. 아인스팩씨엔에스 (206400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.88**
- Adjusted recommendation score: **130.10**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 30, success rate: 50.00%, avg next close: -3.99%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -9.99%
- Next close return data: -2.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.88 points. Stock pattern label is not_enough_data.
- Related news examples: 협동로봇 넘어 물류 자동화까지… 현대무벡스·클로봇도 '함박웃음' | 11월 23일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 24일] 美 증시, 젠슨 황 복귀에 엔비디아 31%...

### 3. 아인스팩씨엔에스 (206400)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.88**
- Adjusted recommendation score: **130.10**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 30, success rate: 50.00%, avg next close: -3.99%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -9.99%
- Next close return data: -2.90%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.88 points. Stock pattern label is not_enough_data.
- Related news examples: 협동로봇 넘어 물류 자동화까지… 현대무벡스·클로봇도 '함박웃음' | 11월 23일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 24일] 美 증시, 젠슨 황 복귀에 엔비디아 31%...

### 4. 오브젠 (417860)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **125.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **123.48**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.98%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 7.00%
- Next close return data: 0.98%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 휴림로봇·LG전자 '불기둥'…피지컬 AI가 바꾸는 로봇 산업 | 오브젠, 신한카드 46억원 규모 사업 수주 | 11월 23일 주식시장 주요공시

### 5. HD현대 (267250)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **7.15**
- Adjusted recommendation score: **118.13**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 28, success rate: 85.71%, avg next close: 2.23%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.74%
- Next close return data: 5.40%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 7.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: [오피셜]시민구단 늘어나는 K리그, 정작 팬 친화 마케팅 우수 구단은 기... | 서부발전, 뷔나·CIP와 태안해상풍력 현안 점검…“안정적 추진” | 부산 북구, 대한민국 지방자치 혁신대상 최우수상 수상

### 6. 한국항공우주 (047810)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **1.58**
- Adjusted recommendation score: **117.56**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 2.17%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.74%
- Next close return data: 5.26%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 1.58 points. Stock pattern label is not_enough_data.
- Related news examples: [방산외교 ①] 무기 수출을 넘어 국가전략으로…K-방산, 외교의 새로운... | 무보·방산진흥회, K-방산 중소기업 수출 지원 맞손 | KAI, 국방품질경영상 단체부문 '대통령표창' 수상

### 7. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.14**
- Adjusted recommendation score: **110.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 19, success rate: 57.89%, avg next close: 1.19%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.47%
- Next close return data: 4.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.14 points. Stock pattern label is relatively_positive_history.
- Related news examples: HD건설기계 자사주 609억 소각에 최대주주 지분율↑ | 인도 조선산업 육성위해 5개 주에 초대형단지 추진… HD현대 등 글로벌... | HD현대, 판교 R&D센터 안전성 입증… '공간안전인증' 획득

### 8. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.14**
- Adjusted recommendation score: **110.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 19, success rate: 57.89%, avg next close: 1.19%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.47%
- Next close return data: 4.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.14 points. Stock pattern label is relatively_positive_history.
- Related news examples: HD건설기계 자사주 609억 소각에 최대주주 지분율↑ | 인도 조선산업 육성위해 5개 주에 초대형단지 추진… HD현대 등 글로벌... | HD현대, 판교 R&D센터 안전성 입증… '공간안전인증' 획득

### 9. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.14**
- Adjusted recommendation score: **110.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 19, success rate: 57.89%, avg next close: 1.19%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 0.47%
- Next close return data: 4.66%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.14 points. Stock pattern label is relatively_positive_history.
- Related news examples: HD건설기계 자사주 609억 소각에 최대주주 지분율↑ | 인도 조선산업 육성위해 5개 주에 초대형단지 추진… HD현대 등 글로벌... | HD현대, 판교 R&D센터 안전성 입증… '공간안전인증' 획득

### 10. 핑거스토리 (417180)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **85.00**
- Error-note adjustment score: **-0.46**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **8.75**
- Adjusted recommendation score: **93.29**
- Risk level: **LOW**
- Event type: `bonus_issue`
- Stock-specific evaluated cases: 14, success rate: 85.71%, avg next close: 6.93%, pattern: relatively_positive_history
- Disclosure title: 권리락              (무상증자)
- Next open return data: 5.80%
- Next close return data: -2.17%
- Reason: Event type is bonus_issue. Initial direction is positive. Event score is 60. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 0.46 points. Event-type performance did not change the score. Stock-specific history added 8.75 points. Stock pattern label is relatively_positive_history.
- Related news examples: 위메이드부터 컴투스홀딩스까지… NFT 관련 게임주에 '시선 집중' | 오늘의 메모[11월 25일] | [52주] 최저가 63개, 최고가 2개... 코스피 5%대 반등

## Volatile Watchlist

### 1. IPARK현대산업개발 (294870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-0.66**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **4.18**
- Adjusted recommendation score: **83.52**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 31, success rate: 61.29%, avg next close: 2.78%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.00%
- Next close return data: 0.86%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.66 points. Event-type performance did not change the score. Stock-specific history added 4.18 points. Stock pattern label is relatively_positive_history.
- Related news examples: IPARK현대산업개발, 영등포 노후 담장에 벽화 그리기 봉사…지역주민과... | [아파트, 생활을 분양하다] 집이 답하고 로봇이 배달… 건설사 ‘사는 ... | IPARK현대산업개발, 영등포 노후 담장에 국화 벽화…주민 40여명 참여

### 2. IPARK현대산업개발 (294870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-0.66**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **4.18**
- Adjusted recommendation score: **83.52**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 31, success rate: 61.29%, avg next close: 2.78%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.00%
- Next close return data: 0.86%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.66 points. Event-type performance did not change the score. Stock-specific history added 4.18 points. Stock pattern label is relatively_positive_history.
- Related news examples: IPARK현대산업개발, 영등포 노후 담장에 벽화 그리기 봉사…지역주민과... | [아파트, 생활을 분양하다] 집이 답하고 로봇이 배달… 건설사 ‘사는 ... | IPARK현대산업개발, 영등포 노후 담장에 국화 벽화…주민 40여명 참여

### 3. IPARK현대산업개발 (294870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-0.66**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **4.18**
- Adjusted recommendation score: **83.52**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 31, success rate: 61.29%, avg next close: 2.78%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.00%
- Next close return data: 0.86%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.66 points. Event-type performance did not change the score. Stock-specific history added 4.18 points. Stock pattern label is relatively_positive_history.
- Related news examples: IPARK현대산업개발, 영등포 노후 담장에 벽화 그리기 봉사…지역주민과... | [아파트, 생활을 분양하다] 집이 답하고 로봇이 배달… 건설사 ‘사는 ... | IPARK현대산업개발, 영등포 노후 담장에 국화 벽화…주민 40여명 참여

### 4. IPARK현대산업개발 (294870)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **80.00**
- Error-note adjustment score: **-0.66**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **4.18**
- Adjusted recommendation score: **83.52**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 31, success rate: 61.29%, avg next close: 2.78%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.00%
- Next close return data: 0.86%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.66 points. Event-type performance did not change the score. Stock-specific history added 4.18 points. Stock pattern label is relatively_positive_history.
- Related news examples: IPARK현대산업개발, 영등포 노후 담장에 벽화 그리기 봉사…지역주민과... | [아파트, 생활을 분양하다] 집이 답하고 로봇이 배달… 건설사 ‘사는 ... | IPARK현대산업개발, 영등포 노후 담장에 국화 벽화…주민 40여명 참여

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 삼영이엔씨 (065570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.08**
- Adjusted recommendation score: **87.90**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 36, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.08 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 23일 주식시장 주요공시 | 삼영이엔씨, 방위사업청 '단파통신체계' 공급계약 금액 132억 4,889만 원으... | 11월 16일 주식시장 주요공시

### 2. 삼영이엔씨 (065570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.08**
- Adjusted recommendation score: **87.90**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 36, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.08 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 23일 주식시장 주요공시 | 삼영이엔씨, 방위사업청 '단파통신체계' 공급계약 금액 132억 4,889만 원으... | 11월 16일 주식시장 주요공시

### 3. 삼영이엔씨 (065570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.08**
- Adjusted recommendation score: **87.90**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 36, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.08 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 23일 주식시장 주요공시 | 삼영이엔씨, 방위사업청 '단파통신체계' 공급계약 금액 132억 4,889만 원으... | 11월 16일 주식시장 주요공시

### 4. 삼영이엔씨 (065570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **98.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.08**
- Adjusted recommendation score: **87.90**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 36, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.08 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 23일 주식시장 주요공시 | 삼영이엔씨, 방위사업청 '단파통신체계' 공급계약 금액 132억 4,889만 원으... | 11월 16일 주식시장 주요공시

### 5. 엔알비 (475230)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-7.09**
- Adjusted recommendation score: **92.89**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 11, success rate: 9.09%, avg next close: -2.03%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.83%
- Next close return data: 4.55%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 7.09 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 23일 주식시장 주요공시 | LH, 건설사·제조사·학계 참여 '모듈러주택 안정적 생태계 구축을 위한... | ‘이틀에 3개층 완성’ 모듈러 주택, 공급 속도전 해법 될까

### 6. 대우건설 (047040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.70**
- Adjusted recommendation score: **94.28**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 24, success rate: 33.33%, avg next close: -2.34%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.11%
- Next close return data: 6.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.70 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [아유경제_재건축] 대우건설, 목동8단지 재건축 홍보관 개관… '써밋디... | 순천대·경국대 의대 신설 확정···인근 아파트 공급 잇따라 | 삼성물산은 미래사업·코오롱글로벌은 내실…새 수장 선임에 담긴 생존...

### 7. 한진중공업홀딩스 (003480)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **95.98**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.41%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: -2.58%
- Next close return data: 1.41%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 23일 주식시장 주요공시 | 배당·자사주 소각 기대에도 지주사株 약세…실적이 가를 희비 | 주주환원 기대감도 지주사주 차익 매물 앞에 주춤… 한진칼·AK홀딩스 웃...

### 8. LS (006260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.50**
- Adjusted recommendation score: **103.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 42.86%, avg next close: 0.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 3.90%
- Next close return data: 5.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [젠슨 황 복귀] ④ 코스피, AI 투심 회복인가 일시적 반등인가...'방심은... | LS증권 "첨단 본딩 시장, HBM 넘어 로직으로 확장" | 서부발전, 뷔나·CIP와 태안해상풍력 현안 점검…“안정적 추진”

### 9. LS (006260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.50**
- Adjusted recommendation score: **103.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 42.86%, avg next close: 0.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 3.90%
- Next close return data: 5.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [젠슨 황 복귀] ④ 코스피, AI 투심 회복인가 일시적 반등인가...'방심은... | LS증권 "첨단 본딩 시장, HBM 넘어 로직으로 확장" | 서부발전, 뷔나·CIP와 태안해상풍력 현안 점검…“안정적 추진”

### 10. LS (006260)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **-1.02**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.50**
- Adjusted recommendation score: **103.48**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 42.86%, avg next close: 0.37%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 3.90%
- Next close return data: 5.06%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.02 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [젠슨 황 복귀] ④ 코스피, AI 투심 회복인가 일시적 반등인가...'방심은... | LS증권 "첨단 본딩 시장, HBM 넘어 로직으로 확장" | 서부발전, 뷔나·CIP와 태안해상풍력 현안 점검…“안정적 추진”

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
