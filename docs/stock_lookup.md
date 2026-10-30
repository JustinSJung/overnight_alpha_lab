# Stock Lookup / 종목별 예측 조회

Search covers the union of the named stock catalog, fixed beta universe and
published regular forecasts. This is a supported lookup list, not a claim that
every exchange-listed stock is covered or that Pages runs live model inference.

`000660` (SK하이닉스) was in the name catalog but absent from the registered
901-stock training/evaluation universe. Searching only the 829 published
regular forecasts incorrectly made the known stock look nonexistent.

The search now distinguishes unknown symbols from known stocks without current
predictions, accepts spacing/full-width variants and formatted name/code choices,
and offers explicit choices for partial/ambiguous names. Seven-digit numeric
input is rejected with the six-digit code format rather than silently truncated.

ML Beta separately refreshes missing catalog stocks outside the fixed universe
using 180 calendar days of completed KIS prices and the cached serving model.
All 19 features, next-open target and fixed cost assumptions remain unchanged.
Additional results are current research estimates, not immutable pre-open forecasts,
recommendations, training examples or registered prospective evaluation evidence.
Existing pool membership, forecasts, recommendation lists and metrics are untouched.

`docs/stock_lookup.json` is a small public sidecar. It is bound to the exact
regular publication hash and price date. A stale/malformed/mismatched sidecar
cannot overwrite regular predictions or enable recommendations. Missing credentials
skip collection; a failed stock does not stop other stocks. Suspensions, missing
current prices and insufficient history show an unavailable reason, never an
invented probability. Quote history and model weights remain in the disposable
cache, not Git. Browser clients receive no KIS credentials.
