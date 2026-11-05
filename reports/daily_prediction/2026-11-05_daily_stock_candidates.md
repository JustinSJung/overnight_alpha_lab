# Daily Stock Candidate Report - 2026-11-05

Generated at: 2026-11-05 03:22:34

ML dataset: `data/processed/ml_dataset_20261105.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 248170 | 샘표식품 | 21 | 21 | 100.00% | 27.77% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 760 | 664 | 46.99% | 5.65% | 4.00 |
| convertible_bond | 1387 | 1054 | 57.78% | 0.43% | 3.00 |
| paid_in_capital_increase | 2600 | 2079 | 57.14% | -0.15% | 3.00 |
| spin_off | 124 | 88 | 50.00% | 1.62% | 2.00 |
| lawsuit | 537 | 416 | 52.40% | -0.41% | 0.00 |
| investment_decision | 523 | 408 | 50.00% | 0.07% | 0.00 |
| bond_with_warrant | 146 | 134 | 40.30% | 0.21% | -3.00 |
| bonus_issue | 105 | 102 | 41.18% | -0.58% | -3.00 |
| disclosure_violation | 209 | 139 | 40.29% | -0.28% | -3.00 |
| major_shareholder_change | 2669 | 2036 | 39.10% | -0.77% | -3.00 |
| earnings_guidance | 63 | 59 | 27.12% | 0.28% | -6.00 |
| supply_contract | 1609 | 1283 | 34.06% | -0.67% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2600 | 1188 | 891 | 521 | 1.26 |
| convertible_bond | 1387 | 609 | 445 | 333 | 1.23 |
| lawsuit | 537 | 218 | 198 | 121 | 0.92 |
| bond_with_warrant | 146 | 54 | 80 | 12 | 0.21 |
| disclosure_violation | 209 | 56 | 83 | 70 | 0.15 |
| spin_off | 124 | 44 | 44 | 36 | -0.71 |
| investment_decision | 523 | 204 | 204 | 115 | -0.78 |
| supply_contract | 1609 | 437 | 846 | 326 | -1.06 |
| bonus_issue | 105 | 42 | 60 | 3 | -1.16 |
| earnings_guidance | 63 | 16 | 43 | 4 | -1.16 |

## Positive Candidates

### 1. 코미팜 (041960)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **119.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **114.44**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.83%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.56%
- Next close return data: 1.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 2. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 진단 수요 확대 기대 커지나…백신·방역 관련주 희비 | 코미팜 조달청 백신 계약 104억원…품목 14종 | 백신 플랫폼부터 동물용 의약품까지… 바이오 관련주 매수세 봇물

### 2. 컨텍 (451760)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.88**
- Adjusted recommendation score: **97.06**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -7.29%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: -0.46%
- Next close return data: -8.58%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.88 points. Stock pattern label is not_enough_data.
- Related news examples: LG유플러스, AIDC 매출 27.7% 달성 '성장세 지속'…자회사 매출 감소에 ... | [리스트] MVP 상위 20선...달바글로벌, 휴젤 등 - 5일 | [포토] 레이싱모델 오은담 '심쿵 아이컨텍'

## Volatile Watchlist

### 1. 고려아연 (010130)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **-0.78**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **3.15**
- Adjusted recommendation score: **74.37**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 15, success rate: 53.33%, avg next close: 3.37%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 1.76%
- Next close return data: 8.15%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 0.78 points. Event-type performance did not change the score. Stock-specific history added 3.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 고려아연 주가 장중 8%대 상승, 자사주 소각과 주식분할 재추진 결의 | 고려아연, 자사주 51% 소각·액면분할 재추진 "주주가치 제고 노력 계속... | [특징주] 고려아연, 자사주 소각·액면분할 재추진에 8%대 강세

### 2. 아이엘 (307180)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-1.19**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **4.50**
- Adjusted recommendation score: **62.31**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 7, success rate: 100.00%, avg next close: -2.37%, pattern: relatively_positive_history
- Disclosure title: [첨부정정]주요사항보고서(회사합병결정)
- Next open return data: 1.16%
- Next close return data: -5.71%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.19 points. Event-type performance added 4.00 points. Stock-specific history added 4.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 아이엘, 최대주주·경영진 잇따라 자사주 매입…피지컬AI 성장 자신감 | 아이엘, 최대주주 이어 그룹 임원 9명도 자사주 매입…책임경영 강화 | "피지컬 AI 선점하자" 로보월드서 기술력 알리는 중기

### 3. 메지온 (140410)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **57.00**
- Error-note adjustment score: **-0.78**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **61.72**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 6.74%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (유데나필의 호주 특허권 양도 계약 체결)
- Next open return data: 3.19%
- Next close return data: 6.74%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 0.78 points. Event-type performance did not change the score. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 모닝 경제 브리핑-11월 5일] 美 증시, 민주당 압승에 다우 3% 급등…... | 아리바이오홀딩스·대명에너지 등 5개 종목 29%대 급등 | 코스닥 '활짝'...주성엔지니어링·심텍·에코프로비엠 '훨훨'

### 4. 현대홈쇼핑 (057050)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-0.71**
- Event-type performance adjustment score: **2.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **43.29**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(회사분할결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 0.71 points. Event-type performance added 2.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 농공상융합형 중소기업 34곳 신규 지정 | 콘서트 열고 매장 차리고…화면 밖으로 나오는 홈쇼핑 | 현대홈쇼핑 인적분할 일정 변경…기일 12월 14일

### 5. 현대홈쇼핑 (057050)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-0.71**
- Event-type performance adjustment score: **2.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **43.29**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]회사분할결정
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 0.71 points. Event-type performance added 2.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 농공상융합형 중소기업 34곳 신규 지정 | 콘서트 열고 매장 차리고…화면 밖으로 나오는 홈쇼핑 | 현대홈쇼핑 인적분할 일정 변경…기일 12월 14일

### 6. 현대홈쇼핑 (057050)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-0.71**
- Event-type performance adjustment score: **2.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **43.29**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]회사분할결정
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 0.71 points. Event-type performance added 2.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 농공상융합형 중소기업 34곳 신규 지정 | 콘서트 열고 매장 차리고…화면 밖으로 나오는 홈쇼핑 | 현대홈쇼핑 인적분할 일정 변경…기일 12월 14일

### 7. 현대홈쇼핑 (057050)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-0.71**
- Event-type performance adjustment score: **2.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **43.29**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]주요사항보고서(회사분할결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 0.71 points. Event-type performance added 2.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 농공상융합형 중소기업 34곳 신규 지정 | 콘서트 열고 매장 차리고…화면 밖으로 나오는 홈쇼핑 | 현대홈쇼핑 인적분할 일정 변경…기일 12월 14일

### 8. 세아제강 (306200)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.00**
- Adjusted recommendation score: **31.24**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 4, success rate: 100.00%, avg next close: -0.63%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.16%
- Next close return data: -2.43%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: [미르의 글로벌 레이더]美 국내 강관 반덤핑 최종판정…휴스틸 0%·현대... | [단독] 美, 현대제철 강관 반덤핑 4.20% 확정…휴스틸은 0% | 이마트 등 151개 기업 '저PBR 꼬리표'붙여 공개 망신주기

### 9. 에스케이바이오팜 (326030)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **24.00**
- Error-note adjustment score: **-0.78**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **6.73**
- Adjusted recommendation score: **29.95**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 10, success rate: 70.00%, avg next close: 1.07%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              (뇌전증 치료제 세노바메이트의 일차성 전신강직간대발작 적응증 미국 FDA 허가 신청)
- Next open return data: 3.07%
- Next close return data: 13.37%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is -1. Negative keyword count is 2. Historical error notes subtracted 0.78 points. Event-type performance did not change the score. Stock-specific history added 6.73 points. Stock pattern label is relatively_positive_history.
- Related news examples: [오늘의 IR] 카카오ㆍCJ ENMㆍ에코프로 등 | [N2 모닝 경제 브리핑-11월 5일] 美 증시, 민주당 압승에 다우 3% 급등…... | ‘2026 수출 붐업코리아’ 성료… 5366건 상담, 149건 체결

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 한진칼 (180640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **18.74**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.22%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경              
- Next open return data: 2.08%
- Next close return data: 0.27%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주]한진칼우, 호반건설 최대주주 등극에 20.62% 올라…한진칼 지분... | 대동금속 이틀 연속 상한가...한진칼 경영권 경쟁·기업 구조개편주도 ... | 곽규택 “산은, 대한항공이 통합 LCC 부산 설립 거부시 호반지원해야”

### 2. 한진칼 (180640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **18.74**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.22%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서(최대주주변경시)              
- Next open return data: 2.08%
- Next close return data: 0.27%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주]한진칼우, 호반건설 최대주주 등극에 20.62% 올라…한진칼 지분... | 대동금속 이틀 연속 상한가...한진칼 경영권 경쟁·기업 구조개편주도 ... | 곽규택 “산은, 대한항공이 통합 LCC 부산 설립 거부시 호반지원해야”

### 3. 한진칼 (180640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **18.74**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.22%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서(최대주주변경시)              
- Next open return data: 2.08%
- Next close return data: 0.27%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주]한진칼우, 호반건설 최대주주 등극에 20.62% 올라…한진칼 지분... | 대동금속 이틀 연속 상한가...한진칼 경영권 경쟁·기업 구조개편주도 ... | 곽규택 “산은, 대한항공이 통합 LCC 부산 설립 거부시 호반지원해야”

### 4. 한진칼 (180640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **18.74**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.22%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경              
- Next open return data: 2.08%
- Next close return data: 0.27%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주]한진칼우, 호반건설 최대주주 등극에 20.62% 올라…한진칼 지분... | 대동금속 이틀 연속 상한가...한진칼 경영권 경쟁·기업 구조개편주도 ... | 곽규택 “산은, 대한항공이 통합 LCC 부산 설립 거부시 호반지원해야”

### 5. 한진칼 (180640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **18.74**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.22%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경              
- Next open return data: 2.08%
- Next close return data: 0.27%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주]한진칼우, 호반건설 최대주주 등극에 20.62% 올라…한진칼 지분... | 대동금속 이틀 연속 상한가...한진칼 경영권 경쟁·기업 구조개편주도 ... | 곽규택 “산은, 대한항공이 통합 LCC 부산 설립 거부시 호반지원해야”

### 6. 한진칼 (180640)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **30.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **18.74**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 10, success rate: 0.00%, avg next close: 0.22%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경              
- Next open return data: 2.08%
- Next close return data: 0.27%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주]한진칼우, 호반건설 최대주주 등극에 20.62% 올라…한진칼 지분... | 대동금속 이틀 연속 상한가...한진칼 경영권 경쟁·기업 구조개편주도 ... | 곽규택 “산은, 대한항공이 통합 LCC 부산 설립 거부시 호반지원해야”

### 7. 현대지에프홀딩스 (005440)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **26.00**
- Error-note adjustment score: **-0.71**
- Event-type performance adjustment score: **2.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **25.79**
- Risk level: **HIGH**
- Event type: `spin_off`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: 1.83%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]회사분할결정(종속회사의주요경영사항)              
- Next open return data: -0.09%
- Next close return data: 1.83%
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Negative keyword count is 3. Historical error notes subtracted 0.71 points. Event-type performance added 2.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 현대홈쇼핑 인적분할 일정 변경…기일 12월 14일 | [유통가 인사]② 현대백화점그룹, 주력 사업 강화 속 지누스 반등 과제 | 현대홈쇼핑, 중간지주 구조 해소…현대百 지주체제 재편 속도↑

### 8. 한미사이언스 (008930)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.97**
- Adjusted recommendation score: **29.27**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 39, success rate: 15.38%, avg next close: 0.45%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 1.21%
- Next close return data: 5.87%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.97 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한미사이언스, 케어미 영양식 3종으로 확대…약국 유통 강화 | 한미사이언스, 케어푸드 '케어미' 영양식으로 약국 공략 | 한미사이언스, '케어미 영양식' 신제품 2종 약국 유통 개시

### 9. 유안타증권 (003470)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **47.00**
- Error-note adjustment score: **-1.76**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.82**
- Adjusted recommendation score: **36.42**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 45, success rate: 11.11%, avg next close: -0.54%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -0.12%
- Next close return data: -0.62%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 1.76 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.82 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [여의도단신]신한투자증권·유안타증권·KB자산운용 | [금융권 이모저모]삼성자산운용, 연금 투자성향별 KODEX ETF 제안 外 | 11월 강세장 공식 통할까…코스피 반등 열쇠는 외국인·반도체

### 10. 광명전기 (017040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **91.00**
- Error-note adjustment score: **-1.06**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.12**
- Adjusted recommendation score: **77.82**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 5, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 3. Historical error notes subtracted 1.06 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.12 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 10월 30일 주식시장 주요공시 | [이넷뉴스 브랜드평판] 두산에너빌리티, 전력설비 상장기업 11월 1위··... | [개장 전 주요 공시] 한미약품·넷마블·이마트·현대차·삼성전자 등

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
