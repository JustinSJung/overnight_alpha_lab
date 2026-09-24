# Daily Stock Candidate Report - 2026-09-24

Generated at: 2026-09-24 00:59:04

ML dataset: `data/processed/ml_dataset_20260924.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, historical confidence adjustments, event-type performance adjustments, and stock-specific historical pattern adjustments.

## Stock-Specific Pattern Adjustment

The recommender now applies a stock-specific historical adjustment. Stocks with relatively positive historical reactions can receive a small positive adjustment, while stocks with weak historical reactions can receive a conservative penalty.

| Stock | Company | Total | Evaluated | Success Rate | Avg Next Close | Pattern Label | Stock Adj |
|---|---|---:|---:|---:|---:|---|---:|
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 373170 | 엠아이큐브솔루션 | 8 | 8 | 100.00% | 29.86% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 8 | 8 | 100.00% | 7.75% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 8 | 8 | 100.00% | 21.21% | relatively_positive_history | 9.00 |
| 096350 | 대창솔루션 | 3 | 3 | 100.00% | 3.60% | relatively_positive_history | 9.00 |
| 267250 | HD현대 | 22 | 21 | 100.00% | 3.09% | relatively_positive_history | 8.95 |
| 044380 | 주연테크 | 17 | 12 | 100.00% | 6.76% | relatively_positive_history | 8.71 |
| 006980 | 우성 | 13 | 7 | 100.00% | 13.04% | relatively_positive_history | 8.54 |
| 336260 | 두산퓨얼셀 | 9 | 6 | 66.67% | 8.34% | relatively_positive_history | 8.28 |
| 003060 | 에이프로젠바이오로직스 | 16 | 3 | 66.67% | 8.64% | relatively_positive_history | 8.08 |
| 052400 | 코나아이 | 16 | 16 | 100.00% | 1.74% | relatively_positive_history | 7.50 |
| 003850 | 보령 | 7 | 7 | 100.00% | 2.22% | relatively_positive_history | 7.50 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 100.00% | 2.14% | 4.00 |
| lawsuit | 295 | 182 | 60.99% | -0.58% | 3.00 |
| paid_in_capital_increase | 1536 | 1165 | 58.03% | 0.28% | 3.00 |
| convertible_bond | 801 | 513 | 48.93% | 1.08% | 2.00 |
| bonus_issue | 65 | 62 | 46.77% | 0.56% | 0.00 |
| disclosure_violation | 125 | 70 | 52.86% | -0.13% | 0.00 |
| investment_decision | 322 | 216 | 50.46% | 0.29% | 0.00 |
| bond_with_warrant | 72 | 61 | 8.20% | -0.04% | -6.00 |
| spin_off | 72 | 48 | 31.25% | 0.28% | -6.00 |
| merger | 197 | 117 | 21.37% | 0.83% | -6.00 |
| supply_contract | 858 | 580 | 28.79% | -0.74% | -6.00 |
| major_shareholder_change | 1554 | 1015 | 33.30% | -1.06% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| earnings_guidance | 6 | 2 | 0 | 4 | 1.67 |
| paid_in_capital_increase | 1536 | 676 | 489 | 371 | 1.25 |
| lawsuit | 295 | 111 | 71 | 113 | 1.16 |
| disclosure_violation | 125 | 37 | 33 | 55 | 0.69 |
| convertible_bond | 801 | 251 | 262 | 288 | 0.59 |
| investment_decision | 322 | 109 | 107 | 106 | -0.63 |
| bonus_issue | 65 | 29 | 33 | 3 | -0.89 |
| supply_contract | 858 | 167 | 413 | 278 | -1.24 |
| major_shareholder_change | 1554 | 338 | 677 | 539 | -1.96 |
| bond_with_warrant | 72 | 5 | 56 | 11 | -1.99 |

## Positive Candidates

### 1. 에코앤드림 (101360)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **155.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **147.76**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 13. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [공시]에코앤드림, 유미코아 대상 177억 전구체 수주 | 에코앤드림, 유미코아에 177억원 규모 전구체 공급 | 에코앤드림, 177억 규모 전구체 수주…"북미 공급 안정화"

### 2. 남화토건 (091590)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **127.76**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [데이터 뉴스룸] 건설업체 50곳 영업益 1년 새 30% 넘게 증가…영업곳간... | 글로벌 탄소중립 타고 돛 달았다… LS마린솔루션, 해저케이블 성장 가속 | 건설회사 2026년 9월 브랜드평판...현대건설, 롯데건설, 대우건설 順

### 3. 에스케이바이오팜 (326030)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **104.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.15**
- Adjusted recommendation score: **101.91**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 9, success rate: 66.67%, avg next close: -0.30%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 2. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.15 points. Stock pattern label is relatively_positive_history.
- Related news examples: 9월 17일 주식시장 주요공시 | SK바이오팜, 파킨슨병 치료제 신약 도입 | [오늘의 IR] 폴라리스오피스ㆍ 메가터치ㆍ엘디티 등

### 4. 삼화네트웍스 (046390)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **90.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **3.50**
- Adjusted recommendation score: **86.26**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 1.92%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history added 3.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: [공시] 9월 23일, 코스닥 상장사 58개 종목 자사주 매매 신청 | [공시] 9월 22일, 코스닥 상장사 60개 종목 자사주 매수 신청 | [공시] 9월 18일, 코스닥 상장사 64개 종목 자사주 매수 신청

### 5. 비에이치아이 (083650)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **87.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **5.45**
- Adjusted recommendation score: **85.21**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 0.60%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history added 5.45 points. Stock pattern label is relatively_positive_history.
- Related news examples: [주간 코스닥 기관] ISC·브이엠·파두 사고 실리콘투·SFA반도체 팔았다 | [주간 코스닥 외국인] 반도체株 쓸어담았다…심텍·SFA반도체·하나마이... | 코스피, 美 반도체 훈풍에 0.9% 상승…7080선 마감[마감시황]

## Volatile Watchlist

### 1. 삼성제약 (001360)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **45.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.08**
- Adjusted recommendation score: **44.45**
- Risk level: **MEDIUM**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.53%, pattern: not_enough_data
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 0.63 points. Event-type performance did not change the score. Stock-specific history added 0.08 points. Stock pattern label is not_enough_data.
- Related news examples: (주)에픽스에이치앤엘, 삼성제약 공동개발 제품 2종 '대한민국 존경받는... | 삼성제약, 'GV1001' 국내 3상 자진 취하…"임상 설계 보완 후 재신청 예... | 삼성제약, 진행성핵상마비 치료제 임상 3상 자진 취하…“임상시험계획...

### 2. 두올 (016740)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **50.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **40.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 7. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [단독] "코인거래와 똑같다"…'시세조종' 실형 신모씨, 세종메디칼 인수... | [데이터 뉴스룸] 車업체 50곳 영업益 1년 새 30% 후진해 울상…성우하이... | 제넨셀 주가조작 세력 의심정황... 세종메디칼 투자 조합에 '기업 사냥...

### 3. 씨싸이트 (109670)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **45.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **35.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주변경을수반하는주식양수도계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [주식마감] 'AI 확산에 양자암호 기대' 우리넷 상한가... 티엔엔터, 씨싸... | 씨싸이트, 구미현 외 5인과 최대주주 변경 주식양수도 계약 | 씨싸이트 주가, 급등세... 무슨 회사길래?

### 4. 에코마케팅 (230360)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-2.17**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **33.83**
- Risk level: **MEDIUM**
- Event type: `spin_off`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 주요사항보고서(회사분할결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is spin_off. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 2.17 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 베인캐피탈, 에코마케팅서 안다르 분리…독립매각 가능성 | 베인, 에코마케팅서 '알짜' 안다르 분리한다…독립매각 가능성 | [공시]에코마케팅, 안다르홀딩스 인적분할

### 5. 삼영무역 (002810)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **42.00**
- Error-note adjustment score: **-2.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **33.37**
- Risk level: **MEDIUM**
- Event type: `merger`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 합병등종료보고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 2.63 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [데이터 뉴스룸] 유통상사 50곳 상반기 영업곳간 50% 넘게 불어…삼성물... | [오늘의 주요공시] 삼영무역·인바이오·롯데리츠 등 | 효율 극대화로 승부 띄웠다… 아모그린텍, 첨단 소재 영토 확장 속도

### 6. 일양약품 (007570)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **0.93**
- Adjusted recommendation score: **15.97**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 9, success rate: 55.56%, avg next close: -1.25%, pattern: relatively_positive_history
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history added 0.93 points. Stock pattern label is relatively_positive_history.
- Related news examples: 일양약품 정도언에서 정유석으로 승계 한 발 더⋯대표보고자도 변경 | 일양약품 정유석 지분 14.65%…최대주주 오른 뒤 35만주 더 받았다 | [HIT알공] 셀트리온, 짐펜트라 미국 류마티스 관절염 3상 승인

### 7. 넷마블 (251270)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **15.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 넷마블 'SOL: enchant', 출시 100일·추석 맞이 대규모 보상 이벤트 연다 | 추석 연휴 시간 순삭 '게임 영화·애니메이션' 추천 上 | 넷마블 ‘나 혼자만 레벨업: 카르마’, 27년의 군주 전쟁, 로그라이트로...

### 8. 국제약품 (002720)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **19.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **9.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Negative keyword count is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [HIT알공] 셀트리온, 짐펜트라 미국 류마티스 관절염 3상 승인 | 천연물 원료 영토 넓히는 현대바이오랜드… 실적 모멘텀 부각 | 한컴라이프케어·케이피엠테크 주가 꿈틀…마스크주에 무슨 호재 있나

### 9. 녹십자홀딩스 (005250)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **14.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **4.04**
- Risk level: **MEDIUM**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [HIT알공] 셀트리온, 짐펜트라 미국 류마티스 관절염 3상 승인 | GC 자회사 메이드 사이언티픽, 美 세포치료제 공장 인수…GMP 생산시설 ... | 원격진료 시장 커진다…플랫폼·의료데이터·진단주 '훨훨'

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. 아모레퍼시픽 (090430)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **20.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-4.54**
- Adjusted recommendation score: **5.50**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 42, success rate: 4.76%, avg next close: 1.15%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 4.54 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 외교무대서도 존재감 드러내는 K-뷰티…美 넘어 멕시코 공략 | [K뷰티 밸류체인 지도]⑪ 해외매출 92% 에이피알, 의료기기도 통할까 | 한우 대신 샤넬?…확 달라진 명절 선물 풍경

### 2. 가비아 (079940)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **14.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **1.46**
- Adjusted recommendation score: **5.50**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 1, success rate: 0.00%, avg next close: 4.63%, pattern: weak_historical_reaction
- Disclosure title: 최대주주변경을수반하는주식양수도계약해제ㆍ취소등              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 1. Negative keyword count is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history added 1.46 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 추석 전날 '올빼미 공시' 91건…매각 무산·상폐 우려도 | [AI 비용 최적화③] GPU부터 AI 게이트웨이까지 ··· 비용 통제도 '자동... | "혹시 내 주식도?"...연휴 전 올빼미 공시에 개미들 '휴~'

### 3. 크래프톤 (259960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **25.00**
- Error-note adjustment score: **-1.96**
- Event-type performance adjustment score: **-8.00**
- Stock-specific pattern adjustment score: **-7.40**
- Adjusted recommendation score: **7.64**
- Risk level: **HIGH**
- Event type: `major_shareholder_change`
- Stock-specific evaluated cases: 3, success rate: 0.00%, avg next close: -1.41%, pattern: weak_historical_reaction
- Disclosure title: 최대주주등소유주식변동신고서              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is major_shareholder_change. Initial direction is volatile. Event score is 10. News attention score is 5. News sentiment score is 2. Historical error notes subtracted 1.96 points. Event-type performance subtracted 8.00 points. Stock-specific history subtracted 7.40 points. Stock pattern label is weak_historical_reaction.
- Related news examples: "공정성 지키지 못한 책임 통감"...크래프톤, 'PUBG 아시아 스타즈' 운영... | 멀리 떠나긴 짧은 연휴…'올 추석엔 게임이나 해 볼까' | 한복 입고 송편 빚고 보상까지...엔씨·넷마블·크래프톤 '한가위 총공세...

### 4. 젠큐릭스 (229000)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **29.00**
- Error-note adjustment score: **-2.63**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-4.18**
- Adjusted recommendation score: **16.19**
- Risk level: **HIGH**
- Event type: `merger`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: 1.75%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]주요사항보고서(회사합병결정)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Negative keyword count is 2. Historical error notes subtracted 2.63 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 4.18 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 클래시스 1위 지켰다…엘앤씨바이오·인바디·셀바스AI 順 | 유방암 진단검사 한시 재개···젠큐릭스, 정상화까지 장기전 | [더벨]젠큐릭스, 진스웰BCT 판매 재개…거래정지 해소 첫 관문

### 5. SIMPAC (009160)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **21.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **20.37**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is -1. Negative keyword count is 3. Historical error notes subtracted 0.63 points. Event-type performance did not change the score. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: [속보] SIMPAC, 합병무효 소송서 승소…법원 원고 청구 기각 | [주요공시] 셀리드, 멀티캠퍼스, 포스코퓨처엠, 보령, 아이파크현대산업... | 비철금속 업종 약세인데… 첨단 소재주는 홀로 웃었다

### 6. 마음AI (377480)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **35.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-2.00**
- Adjusted recommendation score: **32.37**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 2, success rate: 0.00%, avg next close: -0.49%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (국책과제 선정 (완전자율운항선박 전선(Ship-wide) 자율안전관리 통합 대응플랫폼 개발,  산업통상부))
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 0. Historical error notes subtracted 0.63 points. Event-type performance did not change the score. Stock-specific history subtracted 2.00 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [속보] 이명박 예방한 나경원…“원전·4대강, AI 생존사업 증명” | 추석 연휴 4일, 책 어떠세요? | '추석연휴 딱 한 권'…증권가 책벌레 리더들이 꼽은 책①

### 7. 셀트리온 (068270)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **65.00**
- Error-note adjustment score: **-0.63**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-5.79**
- Adjusted recommendation score: **58.58**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 9, success rate: 0.00%, avg next close: -0.60%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              (CTP13 SC(짐펜트라) 미국 임상 3상 시험계획 승인)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 6. Historical error notes subtracted 0.63 points. Event-type performance did not change the score. Stock-specific history subtracted 5.79 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 기존 치료에도 버틴 두드러기…KIT 표적약이 뚫었다 | 셀트리온 짐펜트라, 장질환 이어 류마티스관절염 공략 | [리스트] 돈 잘 벌고 공장·설비도 늘렸다...국내 외형성장 20선

### 8. 씨메스로보틱스 (475400)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **86.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **78.76**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Negative keyword count is 3. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: "캐터필라 장비 몸값 뛰었다"… 혜인, 해외 인프라 재건 수혜 탄력 | 데이터 폭증 잡는 무기... 엑셈, AI 연계 분석 앞세워 성장 엔진 달았다 | 휴머노이드 관절 움직인다… 엔비알모션, 차세대 감속기 상용화 박차

### 9. 현대건설 (000720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **95.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **-6.69**
- Adjusted recommendation score: **81.07**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 28.57%, avg next close: -1.89%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 1. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history subtracted 6.69 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 한가위 지나면 '분양 성수기'…신반포22차 등 주요단지 등판 대기 | 풍경으로 넓힌 집, 비선목장 L하우스 | 용산 유엔사 부지 '더파크사이드 서울' 복합개발 추진 중… 주거·호텔...

### 10. 동일금속 (109860)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **91.00**
- Error-note adjustment score: **-1.24**
- Event-type performance adjustment score: **-6.00**
- Stock-specific pattern adjustment score: **0.00**
- Adjusted recommendation score: **83.76**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 0, success rate: 0.00%, avg next close: 0.00%, pattern: mostly_pending
- Disclosure title: 유동성공급계약의체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 3. Historical error notes subtracted 1.24 points. Event-type performance subtracted 6.00 points. Stock-specific history did not change the score. Stock pattern label is mostly_pending.
- Related news examples: 기업공시 [9월 23일] | 페로타임즈 손바닥뉴스 9월23일(수) | [주요공시] 셀리드, 멀티캠퍼스, 포스코퓨처엠, 보령, 아이파크현대산업...

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
