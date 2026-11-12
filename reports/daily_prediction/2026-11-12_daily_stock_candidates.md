# Daily Stock Candidate Report - 2026-11-12

Generated at: 2026-11-12 03:55:05

ML dataset: `data/processed/ml_dataset_20261112.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 950260 | 인제니아테라퓨틱스 | 9 | 9 | 100.00% | 3.04% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 248170 | 샘표식품 | 22 | 22 | 95.45% | 26.45% | relatively_positive_history | 8.89 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1531 | 1198 | 57.76% | 0.52% | 3.00 |
| paid_in_capital_increase | 2846 | 2325 | 55.96% | -0.19% | 3.00 |
| merger | 824 | 728 | 43.82% | 5.12% | 1.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| investment_decision | 580 | 465 | 51.61% | 0.24% | 0.00 |
| lawsuit | 578 | 457 | 52.08% | -0.47% | 0.00 |
| disclosure_violation | 214 | 144 | 40.97% | -0.34% | -3.00 |
| bond_with_warrant | 154 | 142 | 43.66% | 0.05% | -3.00 |
| spin_off | 154 | 118 | 38.98% | 0.93% | -3.00 |
| major_shareholder_change | 2930 | 2296 | 40.20% | -0.71% | -3.00 |
| supply_contract | 1741 | 1415 | 35.83% | -0.65% | -3.00 |
| earnings_guidance | 86 | 82 | 19.51% | -1.89% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1531 | 692 | 506 | 333 | 1.27 |
| paid_in_capital_increase | 2846 | 1301 | 1024 | 521 | 1.21 |
| lawsuit | 578 | 238 | 219 | 121 | 0.92 |
| bond_with_warrant | 154 | 62 | 80 | 12 | 0.45 |
| disclosure_violation | 214 | 59 | 85 | 70 | 0.19 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 580 | 240 | 225 | 115 | -0.65 |
| supply_contract | 1741 | 507 | 908 | 326 | -0.94 |
| merger | 824 | 319 | 409 | 96 | -1.54 |
| major_shareholder_change | 2930 | 923 | 1373 | 634 | -1.71 |

## Positive Candidates

### 1. HJ중공업 (097230)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **137.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **3.78**
- Adjusted recommendation score: **136.84**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 29, success rate: 65.52%, avg next close: -1.71%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.16%
- Next close return data: 0.62%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 10. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 3.78 points. Stock pattern label is relatively_positive_history.
- Related news examples: 계룡건설, 공공공사·재개발 '쌍끌이'...수주 늘고 실적도 웃었다 | HJ중공업, 조선부문 이익 성장세…컨테이너선 수주로 실적 동력 확보 | 11월 11일 주식시장 주요공시

### 2. 브리지텍 (064480)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **122.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.12**
- Adjusted recommendation score: **118.18**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: 0.34%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.23%
- Next close return data: 1.83%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 7. Negative keyword count is 1. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 0.12 points. Stock pattern label is not_enough_data.
- Related news examples: 11월 11일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 12일] 美 증시, AI 투자 우려 걷히자 반도체... | 브리지텍, 525억원 규모 비씨카드 콜센터 상담시스템 재구축 수주

### 3. GS건설 (006360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-0.94**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.02**
- Adjusted recommendation score: **105.08**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 57.14%, avg next close: 1.38%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -1.31%
- Next close return data: 1.97%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.94 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.02 points. Stock pattern label is relatively_positive_history.
- Related news examples: [카드] "안산 성포동·중앙동 생활권을 동시에…" 아르뮤제자이 출격 | GS건설, 안산 '아르뮤제자이' 견본주택 개관…중대형 984가구 공급 | [굿모닝! 12일 건설업계 소식] 현대건설·GS건설·현대엔지니어링·DL이...

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 2. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 3. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 4. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 5. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 6. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 7. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 8. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 9. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

### 10. NC (036570)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **neutral_positive**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-2.02**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-8.69**
- Adjusted recommendation score: **56.29**
- Risk level: **HIGH**
- Event type: `earnings_guidance`
- Stock-specific evaluated cases: 12, success rate: 0.00%, avg next close: -10.21%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]연결재무제표기준영업실적등에대한전망(공정공시)              
- Next open return data: -0.24%
- Next close return data: -10.21%
- Reason: Event type is earnings_guidance. Initial direction is neutral_positive. Event score is 50. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 2.02 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 8.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김도영 앞세운 한국 야구, 호주전부터 우승 도전…김민준은 첫 국제무대... | 겨울에도 야구하는 삼성 배찬승·김백산·김현준, 호주프로야구 브리즈... | LG 오스틴 딘, 200만 달러에 2027시즌 재계약...외국인 타자 역대 최고액

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
