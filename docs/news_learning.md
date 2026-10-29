# News Learning / 뉴스 기반 학습

The deployed beta still uses the price-only model. News is an unapproved
challenger, not a proven accuracy improvement. Recommendations remain disabled.

## What Is Collected

- Public headline metadata, publication timestamps, publisher links and first
  observation timestamps. Full article bodies and private posts are not stored.
- A deterministic rotating set of 20 company names from the broad catalog,
  independent of candidate scores, plus four English-language global topics:
  rates, semiconductors, energy and international trade.
- Existing supplementary news and locally collected DART disclosure lists are
  also archived. A DART date without a publication time is conservatively treated
  as available no earlier than the end of that Korean calendar day.
- No actual social-media feed is connected. Existing social-attention keyword
  proxies must not be described as SNS collection.

Collection runs at 08:20, 11:20, 14:20, 16:20 and 20:20 KST. GitHub scheduling can
be delayed; actual observation timestamps, not scheduled times, determine use.
The rotating budget does not provide daily coverage of every stock and never
reduces the price candidate universe. Names absent from the catalog cannot be
queried automatically; six-character alphanumeric identifiers are supported.

## Availability and Quality Rules

뉴스를 처음 확인한 실제 시각부터 기록합니다. 과거 파일명이나 기사 발표일만으로
과거에도 알고 있었던 것처럼 학습시키지 않습니다. 수집 실패와 기사 없음도 구분합니다.

`data/news_learning/*.jsonl` and matching checksum manifests are immutable
observation batches. Reruns add new batches rather than rewrite old ones.
These locally timestamped records are auditable, not externally attested timestamps.

The research feature cutoff is fixed at 16:30 KST on each signal date. An article
must have been observed AND published by that cutoff, and published within the
preceding 24 hours. Later observations, revisions and collection statuses do not
change earlier feature rows. Invalid or timezone-free timestamps are excluded.
GDELT index timestamps are not accepted as verified publication times.

Entity links require a literal catalog name/code in the headline, or a verified
DART stock code. A company search query alone is not proof of relevance.
This conservative matching misses aliases, translated names and some inflections.
Global topics are market-wide context, not claimed causal company links.

Identical normalized headlines on the same UTC publication day are counted once
per stock. This is not semantic or multilingual duplicate detection. Counts,
publisher diversity and bilingual event-keyword indicators are initial features;
they are not LLM sentiment predictions or manually assigned scoring boosts.

## Matched Learning Comparison

가격 데이터만 쓰는 모델과 뉴스 입력을 추가한 모델을 같은 종목·날짜·정답으로
비교합니다. 실제 뉴스 이력이 부족한 동안은 학습 대기 상태로 남습니다.

```bash
bash scripts/price_model.sh collect-learning-news
bash scripts/price_model.sh news-shadow-model --data-root data/ml_history/kis_updated_20261028 --as-of 2026-10-28
```

The comparison uses the existing fixed ExtraTrees parameters, 19 OHLCV inputs,
the same next-open/fifth-close target and 0.3% cost assumption. Ten additional
news inputs are used only by the challenger. No parameter/policy search occurs.
Both arms use identical rows with actual collection coverage; dates before the
first observation are not fabricated as zero-news training history.

At least 20 purged training signal dates, five purged calibration dates and ten
resolved evaluation dates are required. Last ten resolved signal dates form
the development evaluation, preceded by ten calendar signal dates reserved for
calibration; five-session label purging can require more than 40 observed dates.
Selections are made before unresolved outcomes are filtered. Conditional returns
are not complete-policy returns when selected outcomes are missing.

`reports/daily_review/news_learning_status.json` reports accumulation or a matched
development comparison during the ML beta release. Repeatedly viewed rolling
comparisons are NOT independent validation. Promotion still requires the separate
fixed reliability protocol and genuinely future evidence. No model is promoted,
and no dashboard confidence number is increased merely because collection works.

Metadata batches are bounded to 2 MB each and contain no API keys or full bodies.
Git is the initial durable observation store; longer-term higher-volume archives
will need an explicitly chosen object store and retention policy.
