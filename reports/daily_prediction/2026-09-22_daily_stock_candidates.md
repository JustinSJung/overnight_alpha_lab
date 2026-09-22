# Daily Stock Candidate Report - 2026-09-22

Generated at: 2026-09-22 02:11:38

ML dataset: `data/processed/ml_dataset_20260922.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 003060 | 에이프로젠바이오로직스 | 4 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.31 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |
| 003850 | 보령 | 6 | 6 | 100.00% | 2.48% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 276 | 178 | 61.24% | -0.59% | 3.00 |
| paid_in_capital_increase | 1440 | 1137 | 58.58% | 0.25% | 3.00 |
| convertible_bond | 752 | 479 | 49.69% | 1.20% | 2.00 |
| bonus_issue | 64 | 61 | 47.54% | 0.59% | 0.00 |
| disclosure_violation | 119 | 69 | 52.17% | -0.09% | 0.00 |
| investment_decision | 310 | 209 | 51.20% | 0.27% | 0.00 |
| bond_with_warrant | 71 | 61 | 8.20% | -0.04% | -6.00 |
| spin_off | 69 | 46 | 28.26% | 0.14% | -6.00 |
| merger | 187 | 109 | 22.02% | 0.84% | -6.00 |
| supply_contract | 814 | 552 | 28.44% | -0.77% | -6.00 |
| major_shareholder_change | 1463 | 980 | 33.57% | -1.08% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1440 | 666 | 471 | 303 | 1.33 |
| lawsuit | 276 | 109 | 69 | 98 | 1.22 |
| disclosure_violation | 119 | 36 | 33 | 50 | 0.68 |
| convertible_bond | 752 | 238 | 241 | 273 | 0.62 |
| investment_decision | 310 | 107 | 102 | 101 | -0.58 |
| bonus_issue | 64 | 29 | 32 | 3 | -0.86 |
| supply_contract | 814 | 157 | 395 | 262 | -1.25 |
| major_shareholder_change | 1463 | 329 | 651 | 483 | -1.99 |
| bond_with_warrant | 71 | 5 | 56 | 10 | -2.01 |

## Positive Candidates

### 1. 덱스터 (206560)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **120.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **4.00**
- Adjusted recommendation score: **116.75**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 1.09%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: 1.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history added 4.00 points. Stock pattern label is relatively_positive_history.
- Related news examples: 덱스터, 이엠텍아이엔씨와 MOU…AI인프라 시장 공략 | 9월 21일 주식시장 주요공시 | [더벨][K콘텐츠 밸류체인 점검] 덱스터, 성장 프리미엄 축소…상장 유지...

### 2. 린드먼아시아 (277070)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **110.25**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 4.24%, pattern: relatively_positive_history
- Disclosure title: 유동성공급계약의체결              
- Next open return data: 1.52%
- Next close return data: 4.24%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [N2 모닝 경제 브리핑-9월 22일] 美 증시, 유가·금리 하락에 상승 마감... | [공시] 9월 22일, 코스닥 상장사 60개 종목 자사주 매수 신청 | 모태펀드 LP성장펀드, '스코펀' 데자뷔?

### 3. 프레스티지바이오로직스 (334970)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **112.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **107.25**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 0.15%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.13%
- Next close return data: 0.15%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 1. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 21일 주식시장 주요공시 | 프레스티지바이오로직스, SC제형 '효소 CDMO'로 사업 확대 | 프레스티지바이오파마, 허셉틴 바이오시밀러 '투즈뉴' 트리니다드토바...

### 4. 판타지오 (032800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.17**
- Adjusted recommendation score: **104.92**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 100.00%, avg next close: 1.10%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 7.73%
- Next close return data: 1.64%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: ‘김부장’ 다음은 일일극…판타지오 ‘엄마가 미쳤어요’ 제작 | 판타지오, KBS 1TV '엄마가 미쳤어요'로 일일드라마 제작 확장 | 판타지오, 일일드라마 ‘엄마가 미쳤어요’ 제작 계약 체결

### 5. 판타지오 (032800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.17**
- Adjusted recommendation score: **104.92**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 100.00%, avg next close: 1.10%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 7.73%
- Next close return data: 1.64%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: ‘김부장’ 다음은 일일극…판타지오 ‘엄마가 미쳤어요’ 제작 | 판타지오, KBS 1TV '엄마가 미쳤어요'로 일일드라마 제작 확장 | 판타지오, 일일드라마 ‘엄마가 미쳤어요’ 제작 계약 체결

### 6. 판타지오 (032800)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **7.17**
- Adjusted recommendation score: **104.92**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 100.00%, avg next close: 1.10%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 7.73%
- Next close return data: 1.64%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history added 7.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: ‘김부장’ 다음은 일일극…판타지오 ‘엄마가 미쳤어요’ 제작 | 판타지오, KBS 1TV '엄마가 미쳤어요'로 일일드라마 제작 확장 | 판타지오, 일일드라마 ‘엄마가 미쳤어요’ 제작 계약 체결

### 7. 비에이치아이 (083650)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **89.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.56**
- Adjusted recommendation score: **87.31**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 0.60%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자율공시)              
- Next open return data: 0.48%
- Next close return data: 0.48%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.56 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 21일 주식시장 주요공시 | 반도체에 밀렸던 원전 ETF '활짝'…수익률은 제각각 [ETF업&다운] | [코스닥 기관] 반도체 담고 네오사피엔스·에코프로 팔았다

## Volatile Watchlist

### 1. 삼성물산 (028260)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **77.00**
- Error-note adjustment score: **-0.58**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **6.96**
- Adjusted recommendation score: **83.38**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 17, success rate: 82.35%, avg next close: 1.00%, pattern: relatively_positive_history
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 3.80%
- Next close return data: 0.41%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.58 points. Event-type performance did not change the score. Stock-specific history added 6.96 points. Stock pattern label is relatively_positive_history.
- Related news examples: 법무법인 세종, ‘AIDC 인프라센터’ 출범 | 삼성물산, 美 카이로스 파워 '맞손'…"차세대 원전 시장 선도 위한 중요... | 삼성물산, 美 차세대 SMR 시장 공략…카이로스파워와 전략적 협력

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.92**
- Adjusted recommendation score: **74.83**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -2.10%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.43%
- Next close return data: -2.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.92 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김건희 '매관매직' 항소심 오늘 선고…1심은 징역 7년 | "하지 않은 일 인정 못 해" 김건희 매관매직 항소심, 오늘 선고 | 현대판 '매관매직' 김건희 항소심 오늘 선고..1심은 징역 7년

### 2. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.92**
- Adjusted recommendation score: **74.83**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -2.10%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.43%
- Next close return data: -2.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.92 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김건희 '매관매직' 항소심 오늘 선고…1심은 징역 7년 | "하지 않은 일 인정 못 해" 김건희 매관매직 항소심, 오늘 선고 | 현대판 '매관매직' 김건희 항소심 오늘 선고..1심은 징역 7년

### 3. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.92**
- Adjusted recommendation score: **74.83**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -2.10%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.43%
- Next close return data: -2.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.92 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김건희 '매관매직' 항소심 오늘 선고…1심은 징역 7년 | "하지 않은 일 인정 못 해" 김건희 매관매직 항소심, 오늘 선고 | 현대판 '매관매직' 김건희 항소심 오늘 선고..1심은 징역 7년

### 4. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.92**
- Adjusted recommendation score: **74.83**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -2.10%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.43%
- Next close return data: -2.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.92 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김건희 '매관매직' 항소심 오늘 선고…1심은 징역 7년 | "하지 않은 일 인정 못 해" 김건희 매관매직 항소심, 오늘 선고 | 현대판 '매관매직' 김건희 항소심 오늘 선고..1심은 징역 7년

### 5. 서희건설 (035890)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-7.92**
- Adjusted recommendation score: **74.83**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -2.10%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.43%
- Next close return data: -2.39%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 7.92 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 김건희 '매관매직' 항소심 오늘 선고…1심은 징역 7년 | "하지 않은 일 인정 못 해" 김건희 매관매직 항소심, 오늘 선고 | 현대판 '매관매직' 김건희 항소심 오늘 선고..1심은 징역 7년

### 6. 대아티아이 (045390)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **92.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.90**
- Adjusted recommendation score: **77.85**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: -1.01%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.76%
- Next close return data: -3.33%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 6. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.90 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 21일 주식시장 주요공시 | 철도망 넓어지자 관련주도 움직였다…전력·차량株 '휘파람' | 철도 투자 다시 부각…통신·전력·터널 관련株 동반 함박웃음

### 7. 태양 (053620)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **79.75**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.58%, pattern: weak_historical_reaction
- Disclosure title: 유동성공급계약의체결              
- Next open return data: -0.15%
- Next close return data: -0.58%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: “나랑 별 보러 가지 않을래?” | 한시련 제작 화면해설방송 주간 편성안내(9월 21일~27일) | 한가위 밤 밝힐 보름달…25일 오후 5시 34분 ‘둥실’

### 8. 아이디스홀딩스 (054800)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **91.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **80.75**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 0.00%, pattern: weak_historical_reaction
- Disclosure title: 유동성공급계약의체결              
- Next open return data: 0.62%
- Next close return data: 0.00%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 3. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 양자암호통신 핵심 기술 품었다… 우리로, AI 데이터센터 확대의 뜻밖 ... | [주요공시] 삼성중공업, 세보엠이씨, 우리로, SK바이오팜, 대화제약, 포... | 자회사 가치 재평가 기대감에 지주사 들썩…종목별 희비

### 9. 지엘팜텍 (204840)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **99.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-3.00**
- Adjusted recommendation score: **88.75**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.44%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.11%
- Next close return data: -0.44%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 2. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 3.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 9월 21일 주식시장 주요공시 | [비즈人워치]지엘팜텍 "안구 신약, 출시 3년 내 매출 100억 목표" | '신약 개발'에도…혁신형 인증, 중소 제약사에 높은 문턱

### 10. 승일 (049830)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **100.00**
- Error-note adjustment score: **-1.25**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-2.25**
- Adjusted recommendation score: **90.50**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: -0.63%, pattern: weak_historical_reaction
- Disclosure title: 유동성공급계약의체결              
- Next open return data: 0.00%
- Next close return data: -0.63%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.25 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 2.25 points. Stock pattern label is weak_historical_reaction.
- Related news examples: KB손해보험, 금감원·금융권 추석 나눔 진행…공동 후원금 1억3000만원 | 가을 풍경이 아름다운 철원, 역사와 자연이 공존하는 가볼 만한 곳 | 서초복지돌봄재단, 주민참여복지 아카데미 운영…참여자 모집 시작

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
