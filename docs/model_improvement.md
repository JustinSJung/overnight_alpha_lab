# Model Improvement / 모델 자동개선

This is bounded, preregistered champion/challenger AutoML. It retrains and compares
approved model families automatically; it does not invent arbitrary algorithms,
edit its own production code, guarantee rising confidence or place orders.

## What Starts Now

- The existing 504-session ExtraTrees model is the control and safe default.
- Three fixed challengers use 504-session regularized logistic regression,
  504-session shallow histogram gradient boosting, and 252-session ExtraTrees.
- All use the existing 19 OHLCV inputs, 60 mature calibration signal dates,
  date-balanced training, purged labels and the same 0.3% cost / next-open to
  fifth-session-close target. No hyperparameter or feature search is run.
- News remains a separate challenger until enough authentic news history exists.
  It is not silently inserted into this registered experiment.

새 정답이 도착하면 후보 모델들도 다시 학습합니다. 같은 날짜·같은 종목의 예측을
장 시작 전에 함께 저장하고, 실제 결과가 나온 뒤에만 비교합니다. 과거 백테스트
최고 점수만으로 서비스 모델을 바꾸지 않습니다.

`model_improvement_20261029.json` fixes the search space, implementation hashes,
target and family budget before any new prospective trial outcomes. The three
challengers consume the three remaining slots in the existing eight-family
statistical budget. The original five-family goal file is not rewritten.
An unregistered implementation change blocks self-improvement; it does not reset
bad evidence or silently start a new unbudgeted trial.

## Automatic Replacement Gate

Each candidate must pass the unchanged user-agreed goal on prospective originals:

- At least 300 resolved selected cases and 60 selected signal dates.
- Observed success and the conservative one-sided date-block lower bound >=60%.
- Complete selected outcomes, adequate issuance frequency and recent health.
- Positive lower bounds for cost-adjusted net return and exact-window excess
  over the two-ETF benchmark. These are overlapping research return proxies,
  not executable or compounded trading returns.

It must ALSO have positive paired date-Brier improvement over the control and,
when replacing an existing challenger, over that incumbent. All candidates share
one complete input-eligible pool; missing outcomes are never replaced by winners.
Paired comparisons require >=99% common outcome coverage and >=60 observed dates.
Twelve directed comparisons and the existing fixed case-count looks receive
explicit alpha spending. Five-session block bootstrap assumptions remain limits,
not distribution-free guarantees under arbitrary market dependence.

The gate is deliberately stricter than merely observing a 60% hit rate. Even
60 perfect days may fail the finite-block small-sample guard. There is no promised
promotion date, and the system may correctly retain the control indefinitely.

A passing challenger becomes the forecast model on a subsequent eligible release.
If its current audit fails, the next release falls back to the control. Already
issued forecasts remain immutable, including when a model switches that day.
This fallback is not a claim that the control is profitable or high-confidence.
It is model rollback, not proof of recovered accuracy.

Recommendation activation remains separately disabled in this beta. Automatic
model replacement does not authorize buy recommendations or automatic orders.

## Persistence and Operation

```bash
bash scripts/price_model.sh improve-model \
  --data-root data/ml_history/kis_updated_20261028 \
  --benchmark-root data/ml_history/kis_benchmark_20261028
```

ML Beta audits old originals before choosing the serving family, runs ordinary
learning, then fits/records the next challenger batch. Checksum manifests contain
only portable model provenance, not private paths, keys or estimators. A single
wide CSV records all model probabilities and frozen selections for every common
eligible stock. Originals are Git-persisted under `data/model_improvement/originals`;
each file is bounded to 2 MB. Estimators stay in the disposable ML state cache,
compacted to two bundles per family while provenance is retained.

`reports/daily_review/model_improvement_status.json` records decisions and reasons.
The public dashboard shows only the phase and sample progress, not internal
family IDs or code-like rule strings. Both missing data and audit failures fail
closed to the control without raising the displayed confidence score.

These are locally timestamped, hash-verified records, not externally attested
market timestamps. Current-universe survivorship, retrospectively adjusted
prices, the observed-universe session calendar and unmodeled execution remain
limitations. A source/checksum defect requires review, not statistical optimism.
