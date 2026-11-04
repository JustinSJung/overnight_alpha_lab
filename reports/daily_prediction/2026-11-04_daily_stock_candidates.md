# Daily Stock Candidate Report - 2026-11-04

Generated at: 2026-11-04 02:54:15

ML dataset: `data/processed/ml_dataset_20261104.csv`

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
| 248170 | 샘표식품 | 21 | 21 | 100.00% | 27.77% | relatively_positive_history | 9.00 |
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 036830 | 솔브레인홀딩스 | 5 | 5 | 100.00% | 4.60% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 112 | 112 | 100.00% | 28.26% | relatively_positive_history | 9.00 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 161000 | 애경케미칼 | 25 | 25 | 92.00% | 3.49% | relatively_positive_history | 8.86 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 759 | 663 | 46.91% | 5.67% | 4.00 |
| convertible_bond | 1369 | 1036 | 57.92% | 0.36% | 3.00 |
| lawsuit | 507 | 386 | 56.48% | -0.52% | 3.00 |
| paid_in_capital_increase | 2577 | 2056 | 57.59% | -0.20% | 3.00 |
| spin_off | 118 | 86 | 51.16% | 1.62% | 2.00 |
| investment_decision | 515 | 400 | 49.00% | -0.11% | 0.00 |
| bond_with_warrant | 145 | 133 | 39.85% | 0.23% | -3.00 |
| bonus_issue | 105 | 102 | 41.18% | -0.58% | -3.00 |
| disclosure_violation | 203 | 133 | 40.60% | -0.28% | -3.00 |
| major_shareholder_change | 2639 | 2006 | 39.13% | -0.77% | -3.00 |
| earnings_guidance | 63 | 59 | 27.12% | 0.28% | -6.00 |
| supply_contract | 1597 | 1271 | 34.23% | -0.66% | -6.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| paid_in_capital_increase | 2577 | 1184 | 872 | 521 | 1.28 |
| convertible_bond | 1369 | 600 | 436 | 333 | 1.24 |
| lawsuit | 507 | 218 | 168 | 121 | 1.16 |
| bond_with_warrant | 145 | 53 | 80 | 12 | 0.17 |
| disclosure_violation | 203 | 54 | 79 | 70 | 0.16 |
| spin_off | 118 | 44 | 42 | 32 | -0.63 |
| investment_decision | 515 | 196 | 204 | 115 | -0.87 |
| supply_contract | 1597 | 435 | 836 | 326 | -1.04 |
| bonus_issue | 105 | 42 | 60 | 3 | -1.16 |
| earnings_guidance | 63 | 16 | 43 | 4 | -1.16 |

## Positive Candidates

### 1. 삼성바이오로직스 (207940)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **-1.04**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **122.46**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 46, success rate: 56.52%, avg next close: -0.88%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.21%
- Next close return data: -0.84%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes subtracted 1.04 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [굿모닝! 4일 제약바이오 소식] 셀트리온·삼성바이오·시지바이오·GC케... | 'AI, 재생에너지 시장의 게임체인저'...한경ESG 11월호 발간 | '몸값 높이고 부담 낮추고'…K제약바이오, 글로벌 계약서 다시 쓴다

### 2. DL (000210)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.04**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.10**
- Adjusted recommendation score: **115.06**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 2.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.86%
- Next close return data: 9.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.04 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.10 points. Stock pattern label is relatively_positive_history.
- Related news examples: 대형 건설사, 수주 목표 달성률 64% … 연말 주택사업이 희비 가른다 | 여의도 첫 ‘아크로’ 준공…최고 40억 오피스텔 492실 들어섰다 | 대기업 사업장 있는 화성·천안아산 아파트 거래 증가…지방 분양 이어...

### 3. DL (000210)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **115.00**
- Error-note adjustment score: **-1.04**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.10**
- Adjusted recommendation score: **115.06**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 2.17%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.86%
- Next close return data: 9.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Historical error notes subtracted 1.04 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.10 points. Stock pattern label is relatively_positive_history.
- Related news examples: 대형 건설사, 수주 목표 달성률 64% … 연말 주택사업이 희비 가른다 | 여의도 첫 ‘아크로’ 준공…최고 40억 오피스텔 492실 들어섰다 | 대기업 사업장 있는 화성·천안아산 아파트 거래 증가…지방 분양 이어...

## Volatile Watchlist

### 1. 영화금속 (012280)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.43**
- Adjusted recommendation score: **32.68**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 57.14%, avg next close: -0.24%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.77%
- Next close return data: -1.39%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.43 points. Stock pattern label is relatively_positive_history.
- Related news examples: 자동차부품주, 해외 수주·로봇 사업 기대…오리엔트정공 질주 | 삼신정밀 측 영화금속 지분 31.19%로 확대 | [창원소식]경남소상공인연합회, 도의회 경제환경위 차담회 등

### 2. 영화금속 (012280)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.43**
- Adjusted recommendation score: **32.68**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 57.14%, avg next close: -0.24%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.77%
- Next close return data: -1.39%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.43 points. Stock pattern label is relatively_positive_history.
- Related news examples: 자동차부품주, 해외 수주·로봇 사업 기대…오리엔트정공 질주 | 삼신정밀 측 영화금속 지분 31.19%로 확대 | [창원소식]경남소상공인연합회, 도의회 경제환경위 차담회 등

### 3. 영화금속 (012280)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.43**
- Adjusted recommendation score: **32.68**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 57.14%, avg next close: -0.24%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: -1.77%
- Next close return data: -1.39%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.43 points. Stock pattern label is relatively_positive_history.
- Related news examples: 자동차부품주, 해외 수주·로봇 사업 기대…오리엔트정공 질주 | 삼신정밀 측 영화금속 지분 31.19%로 확대 | [창원소식]경남소상공인연합회, 도의회 경제환경위 차담회 등

### 4. 미래에셋증권 (006800)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.50**
- Adjusted recommendation score: **31.75**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 100.00%, avg next close: -2.69%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.61%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 한국항공우주 주가 장중 11%대 올라, 1조4천억 규모 완제기 신규 수주 성... | 3% 급등하더니 하락 반전…美 중간선거에 코스피 '롤러코스터' | 크래프톤, 오전 주가↑…자사주 3천억 전량 매입 소각 발표

### 5. 미래에셋증권 (006800)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.50**
- Adjusted recommendation score: **31.75**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 100.00%, avg next close: -2.69%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.61%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 한국항공우주 주가 장중 11%대 올라, 1조4천억 규모 완제기 신규 수주 성... | 3% 급등하더니 하락 반전…美 중간선거에 코스피 '롤러코스터' | 크래프톤, 오전 주가↑…자사주 3천억 전량 매입 소각 발표

### 6. 미래에셋증권 (006800)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.50**
- Adjusted recommendation score: **31.75**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 100.00%, avg next close: -2.69%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.61%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 한국항공우주 주가 장중 11%대 올라, 1조4천억 규모 완제기 신규 수주 성... | 3% 급등하더니 하락 반전…美 중간선거에 코스피 '롤러코스터' | 크래프톤, 오전 주가↑…자사주 3천억 전량 매입 소각 발표

### 7. 미래에셋증권 (006800)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.50**
- Adjusted recommendation score: **31.75**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 100.00%, avg next close: -2.69%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.61%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 한국항공우주 주가 장중 11%대 올라, 1조4천억 규모 완제기 신규 수주 성... | 3% 급등하더니 하락 반전…美 중간선거에 코스피 '롤러코스터' | 크래프톤, 오전 주가↑…자사주 3천억 전량 매입 소각 발표

### 8. 미래에셋증권 (006800)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.50**
- Adjusted recommendation score: **31.75**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 100.00%, avg next close: -2.69%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.61%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 한국항공우주 주가 장중 11%대 올라, 1조4천억 규모 완제기 신규 수주 성... | 3% 급등하더니 하락 반전…美 중간선거에 코스피 '롤러코스터' | 크래프톤, 오전 주가↑…자사주 3천억 전량 매입 소각 발표

### 9. 미래에셋증권 (006800)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **32.00**
- Error-note adjustment score: **-1.75**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.50**
- Adjusted recommendation score: **31.75**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 14, success rate: 100.00%, avg next close: -2.69%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: 0.61%
- Next close return data: -2.25%
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 1.75 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 한국항공우주 주가 장중 11%대 올라, 1조4천억 규모 완제기 신규 수주 성... | 3% 급등하더니 하락 반전…美 중간선거에 코스피 '롤러코스터' | 크래프톤, 오전 주가↑…자사주 3천억 전량 매입 소각 발표

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. KG모빌리티플랫폼 (381970)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **36.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **28.63**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 24, success rate: 0.00%, avg next close: -0.67%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]투자판단관련주요경영사항              
- Next open return data: -0.19%
- Next close return data: 1.12%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 3. Historical error notes subtracted 0.87 points. Event-type performance did not change the score. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [52주] 최고가 2개, 최저가 55개...코스피 3%대 상승 출발 | KG모빌리티플랫폼, 주요주주 지분 인수단가 정정 | 11월 3일 주식시장 주요공시

### 2. SBS (034120)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **40.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **2.00**
- Stock-specific pattern adjustment score: **-1.50**
- Adjusted recommendation score: **39.87**
- Risk level: **HIGH**
- Event type: `spin_off`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 1.97%, pattern: weak_historical_reaction
- Disclosure title: 회사분할결정(종속회사의주요경영사항)              
- Next open return data: 1.43%
- Next close return data: 1.97%
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 0.63 points. Event-type performance added 2.00 points. Stock-specific history subtracted 1.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: '불법촬영 논란' 32기 영수 "나쁜 의도 아니었다 하더라도...생각 짧았다... | 스타트렌드 영화·드라마 여자 투표 1위 김혜윤, 67만 표 팬심에 '굿파트... | Ateez hits new chart milestone with prerelease single 'Drip'

### 3. 삼성에피스홀딩스 (0126Z0)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **55.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-6.29**
- Adjusted recommendation score: **47.84**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 6, success rate: 0.00%, avg next close: 0.18%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항(자회사의 주요경영사항)              (크론병, 궤양성 대장염, 류마티스 관절염 치료제 SB2(Remicade 바이오시밀러) 및 류마티스 관절염, 건선성 관절염, 건선 치료제 SB4(Enbrel 바이오시밀러) 파트너십 계약 체결)
- Next open return data: 0.00%
- Next close return data: 0.48%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 4. Historical error notes subtracted 0.87 points. Event-type performance did not change the score. Stock-specific history subtracted 6.29 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 삼성바이오에피스, 테바와 최대 5632억원 계약…미국 판매망 재편 | 11월 3일 주식시장 주요공시 | [개장 전 주요 공시] 네이버·삼성에피스홀딩스·크래프톤·이앤플러스...

### 4. KG스틸 (016380)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **56.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **52.30**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 26, success rate: 0.00%, avg next close: -0.17%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]합병등종료보고서(자산양수도)
- Next open return data: -0.40%
- Next close return data: 0.79%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 3. Historical error notes subtracted 1.20 points. Event-type performance added 4.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 3일 주식시장 주요공시 | 회생의 아이콘, 곽재선式 경영 방침 주목...KG그룹 회장의 41년 도전이 ... | 페로타임즈 손바닥뉴스 11월4일(수)

### 5. KG스틸 (016380)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **56.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **52.30**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 26, success rate: 0.00%, avg next close: -0.17%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]합병등종료보고서(자산양수도)
- Next open return data: -0.40%
- Next close return data: 0.79%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 3. Historical error notes subtracted 1.20 points. Event-type performance added 4.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 3일 주식시장 주요공시 | 회생의 아이콘, 곽재선式 경영 방침 주목...KG그룹 회장의 41년 도전이 ... | 페로타임즈 손바닥뉴스 11월4일(수)

### 6. KG스틸 (016380)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **56.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **52.30**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 26, success rate: 0.00%, avg next close: -0.17%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]합병등종료보고서(자산양수도)
- Next open return data: -0.40%
- Next close return data: 0.79%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 3. Historical error notes subtracted 1.20 points. Event-type performance added 4.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 3일 주식시장 주요공시 | 회생의 아이콘, 곽재선式 경영 방침 주목...KG그룹 회장의 41년 도전이 ... | 페로타임즈 손바닥뉴스 11월4일(수)

### 7. KG스틸 (016380)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **56.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **52.30**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 26, success rate: 0.00%, avg next close: -0.17%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]합병등종료보고서(자산양수도)
- Next open return data: -0.40%
- Next close return data: 0.79%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Negative keyword count is 3. Historical error notes subtracted 1.20 points. Event-type performance added 4.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 3일 주식시장 주요공시 | 회생의 아이콘, 곽재선式 경영 방침 주목...KG그룹 회장의 41년 도전이 ... | 페로타임즈 손바닥뉴스 11월4일(수)

### 8. 스트라드비젼 (475040)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **70.00**
- Error-note adjustment score: **-1.04**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.22**
- Adjusted recommendation score: **59.74**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -2.99%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -3.40%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is -1. Negative keyword count is 5. Historical error notes subtracted 1.04 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.22 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 11월 3일 주식시장 주요공시 | IPO 주관 실적 삼성증권 선두…미래에셋 2위 도약 | 스트라드비젼 앱티브 계약 종료일 2027년 2월로 변경

### 9. 파두 (440110)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **78.00**
- Error-note adjustment score: **-1.04**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.68**
- Adjusted recommendation score: **64.28**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: -2.73%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.46%
- Next close return data: -4.12%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 4. Historical error notes subtracted 1.04 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.68 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [데이터 뉴스룸] 코스닥 상위 50개 종목 하반기에만 시총 80조 증발…50곳... | 11월 3일 주식시장 주요공시 | [Invest]미리 사면 추적오차, 늦게 사면 고점…88조 ETF '리밸런싱 딜레...

### 10. 키움제10호스팩 (487720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **69.00**
- Error-note adjustment score: **-1.20**
- Event-type performance adjustment score: **4.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **65.30**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: -100.00%
- Next close return data: 0.00%
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 2. Historical error notes subtracted 1.20 points. Event-type performance added 4.00 points. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 합병 기대감에 스팩주 꿈틀…종목별 온도차는 뚜렷 | 11월 3일 주식시장 주요공시 | 엄주성 키움증권 대표, 스팩 시장 한파 뚫은 비결은?

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
