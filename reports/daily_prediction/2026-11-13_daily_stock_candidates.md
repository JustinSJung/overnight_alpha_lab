# Daily Stock Candidate Report - 2026-11-13

Generated at: 2026-11-13 04:20:50

ML dataset: `data/processed/ml_dataset_20261113.csv`

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
| 006280 | 녹십자 | 13 | 13 | 100.00% | 4.07% | relatively_positive_history | 9.00 |
| 138080 | 오이솔루션 | 5 | 5 | 100.00% | 3.56% | relatively_positive_history | 9.00 |
| 475460 | 미트박스 | 13 | 13 | 100.00% | 5.44% | relatively_positive_history | 9.00 |
| 424870 | 이뮨온시아 | 9 | 9 | 100.00% | 18.42% | relatively_positive_history | 9.00 |
| 012030 | DB | 3 | 3 | 100.00% | 7.97% | relatively_positive_history | 9.00 |
| 200130 | 콜마비앤에이치 | 15 | 15 | 100.00% | 3.14% | relatively_positive_history | 9.00 |
| 122830 | 원포유 | 9 | 9 | 100.00% | 6.26% | relatively_positive_history | 9.00 |
| 007540 | 샘표 | 113 | 113 | 99.12% | 28.00% | relatively_positive_history | 8.98 |
| 126340 | 비나텍 | 19 | 19 | 94.74% | 13.58% | relatively_positive_history | 8.91 |
| 248170 | 샘표식품 | 22 | 22 | 95.45% | 26.45% | relatively_positive_history | 8.89 |

## Event-Type Success Rate Adjustment

The recommender also applies event-type performance adjustments based on historical success rates and average next-day returns.

| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Total Adj |
|---|---:|---:|---:|---:|---:|
| merger | 858 | 762 | 46.19% | 5.04% | 4.00 |
| convertible_bond | 1543 | 1210 | 57.19% | 0.55% | 3.00 |
| investment_decision | 592 | 477 | 51.15% | 0.25% | 0.00 |
| bonus_issue | 119 | 116 | 48.28% | 0.38% | 0.00 |
| paid_in_capital_increase | 2891 | 2370 | 54.94% | -0.13% | 0.00 |
| lawsuit | 609 | 488 | 48.77% | -0.26% | 0.00 |
| disclosure_violation | 214 | 144 | 40.97% | -0.34% | -3.00 |
| bond_with_warrant | 154 | 142 | 43.66% | 0.05% | -3.00 |
| spin_off | 155 | 119 | 39.50% | 0.89% | -3.00 |
| major_shareholder_change | 3111 | 2477 | 37.75% | -0.66% | -3.00 |
| supply_contract | 1768 | 1442 | 36.75% | -0.55% | -3.00 |
| earnings_guidance | 90 | 86 | 23.26% | -1.74% | -8.00 |

## Error-Note Learning Adjustment

The recommender also reads past error notes and applies event-type level confidence adjustments from `confidence_adjustment` values.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 1543 | 692 | 518 | 333 | 1.24 |
| paid_in_capital_increase | 2891 | 1302 | 1068 | 521 | 1.14 |
| lawsuit | 609 | 238 | 250 | 121 | 0.72 |
| bond_with_warrant | 154 | 62 | 80 | 12 | 0.45 |
| disclosure_violation | 214 | 59 | 85 | 70 | 0.19 |
| bonus_issue | 119 | 56 | 60 | 3 | -0.44 |
| investment_decision | 592 | 244 | 233 | 115 | -0.69 |
| supply_contract | 1768 | 530 | 912 | 326 | -0.87 |
| merger | 858 | 352 | 410 | 96 | -1.29 |
| earnings_guidance | 90 | 20 | 66 | 4 | -1.71 |

## Positive Candidates

### 1. 삼일기업공사 (002290)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **147.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.17**
- Adjusted recommendation score: **148.30**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: 0.37%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.11%
- Next close return data: 1.27%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 12. Negative keyword count is 1. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.17 points. Stock pattern label is relatively_positive_history.
- Related news examples: 건설株 실적 턴어라운드 기대…해외 플랜트·주택 수주 회복에 러브콜 ... | 11월 12일 주식시장 주요공시 | 정부 주택 공급 정책 기대 확산…중소형 건설주 주가 날개

### 2. 미래컴퍼니 (049950)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **145.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **0.08**
- Adjusted recommendation score: **141.21**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 50.00%, avg next close: -0.26%, pattern: not_enough_data
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: -0.69%
- Next close return data: 4.64%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 0.08 points. Stock pattern label is not_enough_data.
- Related news examples: 삼성·글로벌 패널사 증설 기대…OLED 수혜주 어디까지 가나 | 11월 12일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 12일] 美 증시, 젠슨 황 사임 충격에 3대 지수...

### 3. 테스 (095610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **136.63**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 4.03%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.36%
- Next close return data: 4.03%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: SK하이닉스·삼성전자 동반 강세… AI 반도체 슈퍼사이클 다시 오나 | [미리보는 소부장 테크페어]〈6·끝〉아이큐랩, 8인치 SiC 양산 본격화…... | [대한민국 건설 리더십 해부] (8) SK에코플랜트 김영식 '원톱' 체제 시험...

### 4. 테스 (095610)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **5.50**
- Adjusted recommendation score: **136.63**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 4.03%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.36%
- Next close return data: 4.03%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 5.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: SK하이닉스·삼성전자 동반 강세… AI 반도체 슈퍼사이클 다시 오나 | [미리보는 소부장 테크페어]〈6·끝〉아이큐랩, 8인치 SiC 양산 본격화…... | [대한민국 건설 리더십 해부] (8) SK에코플랜트 김영식 '원톱' 체제 시험...

### 5. AP위성 (211270)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **135.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **4.83**
- Adjusted recommendation score: **135.96**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 1, success rate: 100.00%, avg next close: 3.48%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 1.45%
- Next close return data: 3.48%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 4.83 points. Stock pattern label is relatively_positive_history.
- Related news examples: "유닛 넘어 시스템"… AP위성, SAR 위성과 달 탐사 로버 개발중 | 통신장비株 신바람…위성통신·광통신·6G 투자 확대 기대감 | 경기연구원, “19만 5천대 CCTV로 ‘인공지능 재난 대응’ 가능”

### 6. 한울소재과학 (091440)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **132.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.42**
- Adjusted recommendation score: **130.55**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 66.67%, avg next close: -5.94%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.00%
- Next close return data: -5.63%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 9. Negative keyword count is 1. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.42 points. Stock pattern label is relatively_positive_history.
- Related news examples: 통신장비株 신바람…위성통신·광통신·6G 투자 확대 기대감 | 11월 12일 주식시장 주요공시 | [N2 모닝 경제 브리핑-11월 12일] 美 증시, 젠슨 황 사임 충격에 3대 지수...

### 7. HD한국조선해양 (009540)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **130.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-0.01**
- Adjusted recommendation score: **126.12**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 16, success rate: 50.00%, avg next close: 0.54%, pattern: not_enough_data
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결(자회사의 주요경영사항)              
- Next open return data: 1.05%
- Next close return data: 2.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 0.01 points. Stock pattern label is not_enough_data.
- Related news examples: "완전자율운항선박 상용화 '기술력 확보' 관건" | 서울고법 “가스公, ‘LNG 화물창’ 손해 본 SK해운에 2200억 배상하라”... | 배 만들수록 돈 번다… 조선 3사부터 기자재株까지 '뱃노래'

### 8. 강원에너지 (114190)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **114.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **8.41**
- Adjusted recommendation score: **118.54**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 85.71%, avg next close: 3.64%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 1.30%
- Next close return data: 2.72%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 2. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 8.41 points. Stock pattern label is relatively_positive_history.
- Related news examples: 강원에너지, 수세설비 계약 2억8200만원 증액 | AI 데이터센터 투자 확대에 전자장비株 들썩…기판·MLCC주 동반 급등 | 11월 12일 주식시장 주요공시

### 9. 아시아나IDT (267850)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **105.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **7.06**
- Adjusted recommendation score: **108.19**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 4, success rate: 75.00%, avg next close: 1.24%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 3.30%
- Next close return data: 5.73%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 7.06 points. Stock pattern label is relatively_positive_history.
- Related news examples: 아시아나IDT-한진정보통신, 수질 정화 봉사활동 실시 | 아시아나IDT-한진정보통신, 하천 수질정화·생태회복 공동 봉사활동 실... | 클라우드·생성형 AI가 키운 시장… IT서비스 업종 '신바람'

### 10. 프레스티지바이오로직스 (334970)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **97.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **2.50**
- Adjusted recommendation score: **95.63**
- Risk level: **LOW**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 2, success rate: 100.00%, avg next close: 0.33%, pattern: relatively_positive_history
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.09%
- Next close return data: 0.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 2. Negative keyword count is 1. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 2.50 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 12일 주식시장 주요공시 | [코스피·코스닥, 대한조선 네이버 LG 프레스티지바이오로직스 스피어 ... | 상장 제약기업 브랜드평판 11월 분석…삼바·셀트리온·유한양행 순

## Volatile Watchlist

No candidates in this section.

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

### 1. GS글로벌 (001250)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-0.69**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **67.81**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 7, success rate: 0.00%, avg next close: 0.18%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.92%
- Next close return data: 0.18%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 0.69 points. Event-type performance did not change the score. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 포스코, GS그룹과 AIDC용 맞춤형 철강 솔루션 협력 추진 | 11월 12일 주식시장 주요공시 | 포스코, GS와 AI 데이터센터 사업 협력 업무협약 체결...제38회 테크포럼...

### 2. GS글로벌 (001250)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **volatile**
- Base recommendation score: **75.00**
- Error-note adjustment score: **-0.69**
- Event-type performance adjustment score: **0.00**
- Stock-specific pattern adjustment score: **-6.50**
- Adjusted recommendation score: **67.81**
- Risk level: **HIGH**
- Event type: `investment_decision`
- Stock-specific evaluated cases: 7, success rate: 0.00%, avg next close: 0.18%, pattern: weak_historical_reaction
- Disclosure title: 투자판단관련주요경영사항              
- Next open return data: 0.92%
- Next close return data: 0.18%
- Reason: Event type is investment_decision. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Historical error notes subtracted 0.69 points. Event-type performance did not change the score. Stock-specific history subtracted 6.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 포스코, GS그룹과 AIDC용 맞춤형 철강 솔루션 협력 추진 | 11월 12일 주식시장 주요공시 | 포스코, GS와 AI 데이터센터 사업 협력 업무협약 체결...제38회 테크포럼...

### 3. 스피어 (347700)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **87.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.54**
- Adjusted recommendation score: **80.59**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 18, success rate: 44.44%, avg next close: 0.44%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 4.01%
- Next close return data: 2.32%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 0. Negative keyword count is 1. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.54 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 현대엔지니어링, 조경 디자인 경쟁력 입증 | 업무용 메신저 '카카오워크' 해킹···이메일·첨부파일까지 유출 | [개봉영화] 팝스타로 변신한 앤 해서웨이, ‘마더 메리’…삶이 곧 투쟁...

### 4. 금양그린파워 (282720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.83**
- Adjusted recommendation score: **89.30**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 42.86%, avg next close: 0.62%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 2.96%
- Next close return data: -0.53%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.83 points. Stock pattern label is weak_historical_reaction.
- Related news examples: AI 전력난에 에너지株 들썩…태양광·풍력·원전 수혜 기대 | 금양그린파워 새울 3·4호기 계약 12억3245만원 증액 | 11월 12일 주식시장 주요공시

### 5. 퀄리타스반도체 (432720)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **108.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-6.86**
- Adjusted recommendation score: **97.27**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 28.57%, avg next close: -1.96%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 10.51%
- Next close return data: 9.51%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 4. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 6.86 points. Stock pattern label is weak_historical_reaction.
- Related news examples: [특징주] 텔레칩스, 4분기 연속 영업익 흑자 행진…해외 수출 호조 부각... | SK하이닉스·삼성전자 동반 강세… AI 반도체 슈퍼사이클 다시 오나 | [종목 브리핑] 퀄리타스반도체, SK하이닉스 IP 계약 39억원대

### 6. 솔디펜스 (215090)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **96.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **6.77**
- Adjusted recommendation score: **98.90**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 6, success rate: 100.00%, avg next close: 2.45%, pattern: relatively_positive_history
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: -0.26%
- Next close return data: 4.49%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 3. Negative keyword count is 3. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history added 6.77 points. Stock pattern label is relatively_positive_history.
- Related news examples: 11월 12일 주식시장 주요공시 | 솔디펜스 전술다련장 부품 계약 종료일 연장 | 글로벌 무기 수요 늘지만 방산주 주춤…실적·수주가 주가 가른다

### 7. 나우로보틱스 (459510)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **109.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-5.42**
- Adjusted recommendation score: **99.71**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 3, success rate: 33.33%, avg next close: 0.54%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 3.36%
- Next close return data: 6.52%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 5. Negative keyword count is 2. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 5.42 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 나우로보틱스 미국 설비 계약 종료일 2027년 10월로 조정 | 휴머노이드 로봇부터 원전까지…기계株에 돈 몰리는 이유 보니 | 11월 12일 주식시장 주요공시

### 8. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.68**
- Adjusted recommendation score: **100.45**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 29, success rate: 41.38%, avg next close: 0.10%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.55%
- Next close return data: 22.51%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.68 points. Stock pattern label is weak_historical_reaction.
- Related news examples: “엔비디아 쇼크에도…” 코스피 장중 5500 돌파, 코스닥 4% 급등 | [분양] 현대건설,'디에이치 반포124' 외 | [굿모닝! 13일 건설업계 소식] GS건설·롯데건설·금호건설·반도건설·...

### 9. 금호건설 (002990)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **107.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.68**
- Adjusted recommendation score: **100.45**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 29, success rate: 41.38%, avg next close: 0.10%, pattern: weak_historical_reaction
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: 0.55%
- Next close return data: 22.51%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Negative keyword count is 1. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.68 points. Stock pattern label is weak_historical_reaction.
- Related news examples: “엔비디아 쇼크에도…” 코스피 장중 5500 돌파, 코스닥 4% 급등 | [분양] 현대건설,'디에이치 반포124' 외 | [굿모닝! 13일 건설업계 소식] GS건설·롯데건설·금호건설·반도건설·...

### 10. 한신공영 (004960)

- Candidate type: **AVOID_OR_RISK_REVIEW**
- Expected direction: **positive**
- Base recommendation score: **111.00**
- Error-note adjustment score: **-0.87**
- Event-type performance adjustment score: **-3.00**
- Stock-specific pattern adjustment score: **-2.50**
- Adjusted recommendation score: **104.63**
- Risk level: **HIGH**
- Event type: `supply_contract`
- Stock-specific evaluated cases: 7, success rate: 42.86%, avg next close: -0.88%, pattern: weak_historical_reaction
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: 0.20%
- Next close return data: 3.14%
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 6. Negative keyword count is 3. Historical error notes subtracted 0.87 points. Event-type performance subtracted 3.00 points. Stock-specific history subtracted 2.50 points. Stock pattern label is weak_historical_reaction.
- Related news examples: 건설株 실적 턴어라운드 기대…해외 플랜트·주택 수주 회복에 러브콜 ... | 11월 12일 주식시장 주요공시 | 한신공영, 00비행장 통합이전 공사 18억원 증액

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
