# Daily Stock Candidate Report - 2026-06-24

Generated at: 2026-06-24 17:07:41

ML dataset: `data/processed/ml_dataset_20260624.csv`

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Method

Candidates are ranked using a rule-based score that combines event score, news sentiment, news attention, prediction direction, simple risk filters, and historical confidence adjustments from advanced error notes.

## Error-Note Learning Adjustment

The recommender now reads past error notes and applies event-type level confidence adjustments. Event types that repeatedly received `increase` signals can receive a small positive adjustment. Event types that repeatedly received `decrease` or `slightly_decrease` signals can receive a conservative penalty.

| Event Type | Notes | Success | Failure | Pending | Adjustment |
|---|---:|---:|---:|---:|---:|
| convertible_bond | 18 | 0 | 0 | 18 | 0.00 |
| disclosure_violation | 5 | 0 | 0 | 5 | 0.00 |
| investment_decision | 5 | 0 | 0 | 5 | 0.00 |
| lawsuit | 8 | 0 | 0 | 8 | 0.00 |
| major_shareholder_change | 10 | 0 | 0 | 10 | 0.00 |
| merger | 8 | 0 | 0 | 8 | 0.00 |
| paid_in_capital_increase | 17 | 0 | 0 | 17 | 0.00 |
| spin_off | 1 | 0 | 0 | 1 | 0.00 |
| supply_contract | 12 | 0 | 0 | 12 | 0.00 |

## Positive Candidates

### 1. 삼호개발 (010960)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **142.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **142.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Historical error-note cases: 12 (success 0, failure 0)
- Disclosure title: [기재정정]단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 11. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: [단독] 서울시 건설공사 부실벌점, 상반기에만 17건 | 삼호개발, GTX-B노선 제4공구 공사비 소폭 증액…계약 규모 978억원 유지 | 일성건설 주가 파죽지세… 건설주 혼조세 속 투자 기회는 어디?

### 2. HEM파마 (376270)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **127.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **127.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Historical error-note cases: 12 (success 0, failure 0)
- Disclosure title: 단일판매ㆍ공급계약체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: HEM파마, 46억 3천만 원대 공급계약→매출 기반 확대 기대 | [속보] HEM파마, 46.3억원 규모 프로바이오틱스 공급계약 체결…전년 연... | [주가] 6월 24일 주요 제약·바이오·기기 5% 변동 현황 - 38개사 증가

### 3. 원티드랩 (376980)

- Candidate type: **POSITIVE_CANDIDATE**
- Expected direction: **positive**
- Base recommendation score: **110.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **110.00**
- Risk level: **LOW**
- Event type: `supply_contract`
- Historical error-note cases: 12 (success 0, failure 0)
- Disclosure title: 유동성공급계약의체결              
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is supply_contract. Initial direction is positive. Event score is 70. News attention score is 5. News sentiment score is 4. Historical error notes did not change the score.
- Related news examples: [52주] 최고가 3개, 최저가 693개 ... 지수는 반등 | ‘삼전·하이닉스 직행’ 반도체 계약학과, 서울대 자연계 넘었다 | AI 다음은 양자컴퓨터…빅테크 승부 시작

## Volatile Watchlist

### 1. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 2. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 3. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 4. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 5. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 6. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 7. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 8. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 9. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

### 10. 알에프텍 (061040)

- Candidate type: **WATCHLIST_VOLATILE**
- Expected direction: **volatile**
- Base recommendation score: **72.00**
- Error-note adjustment score: **0.00**
- Adjusted recommendation score: **72.00**
- Risk level: **MEDIUM**
- Event type: `merger`
- Historical error-note cases: 8 (success 0, failure 0)
- Disclosure title: [기재정정]증권신고서(합병)
- Next open return data: Not available
- Next close return data: Not available
- Reason: Event type is merger. Initial direction is volatile. Event score is 30. News attention score is 5. News sentiment score is 8. Negative keyword count is 1. Historical error notes did not change the score.
- Related news examples: 화면 곡면이 곧 기술력… 제이앤티씨, 글로벌 빅테크 러브콜 쏟아진다 | 글로벌 에스테틱 시장의 중심…휴젤, 톡신·필러 쌍끌이로 해외 공략 | 글로벌 외주 생산 붐 타고…인탑스, 대형 신규 바이어 확보 기대감

## General Watchlist

No candidates in this section.

## Risk / Avoid Review List

No candidates in this section.

## Data Readiness

At this stage, candidates are still generated using rule-based scoring. The system now also uses historical error-note patterns as a conservative confidence adjustment layer. Expected return values will become more meaningful after enough evaluated event-reaction samples are accumulated.

## How to Read This Report

- Positive Candidates: relatively favorable event and news conditions.
- Volatile Watchlist: potentially important events with uncertain direction.
- General Watchlist: events worth monitoring but not strong enough for positive classification.
- Risk / Avoid Review List: negative or high-risk events such as capital increases, CB/BW, lawsuits, or disclosure violations.
- Error-note adjustment score: historical learning signal from previous success/failure notes.

## Next Step

The next step is to improve the adjustment logic using event-type success rates, stock-specific historical reactions, market index movement, and trading volume.
