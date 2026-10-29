# Execution Target Audit / 진입 가격 기준 점검

RESEARCH_ONLY. No recommendation, production promotion, candidate-pool reduction or legacy label rewrite.

## What Changed

The signal uses completed closing data. The new target starts at the NEXT observed session open, not the already observed signal close.
Both fixed ExtraTrees models use the same 19 inputs, training/calibration dates and resolved fit rows. Only the supervised target differs.
Both are evaluated on the new next-open target. This is NOT a before/after success-rate comparison against different answers.
Rank and threshold selections use every input-eligible candidate before outcomes are inspected. Unknown picks are never replaced.
Suspended/missing execution bars and exceptional single-session price discontinuities remain explicitly unresolved. Corporate-action causes are not inferred.
The 30.5% review threshold is a conservative research heuristic, not a claim about all exchange rules. Multi-session gains are not clipped.

## Raw Data Audit

```json
{
  "rows": 796665,
  "duplicate_dates": 0,
  "invalid_dates": 0,
  "weekend_dates": 0,
  "nonfinite_ohlcv": 0,
  "nonpositive_close": 0,
  "negative_volume": 0,
  "zero_volume": 27178,
  "invalid_active_candles": 0,
  "exceptional_one_day_moves": 26
}
```

## Outcome Audit

```json
{
  "target_version": "next_open_to_fifth_close_v1",
  "horizon_sessions": 5,
  "cost_assumption": 0.003,
  "target_definition": "close_on_fifth_session / next_session_open - 1 > cost",
  "execution_note": "Hypothetical next-open entry / fifth-close exit; not guaranteed fills. Fixed round-trip cost does not model queueing, taxes by product, impact or delisting proceeds.",
  "calendar_note": "Union of observed universe dates, not an authoritative exchange calendar.",
  "discontinuity_rule": "Absolute one-session close change above 30.5% inside holding interval, or entry intraday change above 30.5%, requires review. Not proof of error.",
  "input_candidates": 751899,
  "resolved_candidates": 744579,
  "label_status_counts": {
    "resolved": 744579,
    "awaiting_future_sessions": 4165,
    "exit_price_unavailable": 1913,
    "entry_price_unavailable": 934,
    "price_discontinuity_requires_review": 279,
    "missing_session_prices": 29
  },
  "universe_note": "Current observed universe and retrospectively adjusted prices; survivorship bias remains."
}
```

## Matched Historical Development Results

| Period | Training target | Input candidates | Resolved | Unresolved | Date Brier | Past constant Brier | Daily AUC |
|---|---|---:|---:|---:|---:|---:|---:|
| policy_diagnostic | same_close_trained_control | 32590 | 32420 | 170 | 0.27700150738652923 | 0.25473970329933343 | 0.5183632382675954 |
| policy_diagnostic | next_open_trained | 32590 | 32420 | 170 | 0.26376743082655296 | 0.25473970329933343 | 0.5166600457056335 |
| historical_development | same_close_trained_control | 52017 | 51483 | 534 | 0.2507626517419572 | 0.2514088879352742 | 0.5350801222279267 |
| historical_development | next_open_trained | 52017 | 51483 | 534 | 0.2474097654556091 | 0.2514088879352742 | 0.53686435418582 |
| recent_tail | same_close_trained_control | 5867 | 5783 | 84 | 0.2679237227861599 | 0.2562675305538926 | 0.513968587674718 |
| recent_tail | next_open_trained | 5867 | 5783 | 84 | 0.2559605604074944 | 0.2562675305538926 | 0.5158050708187234 |

Success/return numbers below are conditional on resolved outcomes. They are not complete-policy performance when unresolved > 0.

| Period | Training target | Group | Selected | Resolved | Unresolved | Conditional success | Conditional daily success | Conditional net proxy | Full-policy all-date net proxy |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| policy_diagnostic | same_close_trained_control | fixed_policy | 195 | 189 | 6 | 0.3492063492063492 | 0.34102564102564104 | -0.036171537115081524 | None |
| policy_diagnostic | same_close_trained_control | top20 | 780 | 763 | 17 | 0.37745740498034075 | 0.3760785195769715 | -0.02722234153003854 | None |
| policy_diagnostic | next_open_trained | fixed_policy | 194 | 188 | 6 | 0.35106382978723405 | 0.3431623931623931 | -0.03136240009741155 | None |
| policy_diagnostic | next_open_trained | top20 | 780 | 761 | 19 | 0.3508541392904074 | 0.34940583295846456 | -0.029692451697712972 | None |
| historical_development | same_close_trained_control | fixed_policy | 310 | 287 | 23 | 0.47038327526132406 | 0.47284946236559144 | 0.011931866403380195 | None |
| historical_development | same_close_trained_control | top20 | 1240 | 1193 | 47 | 0.4526404023470243 | 0.45184954004238936 | 0.010415756785416596 | None |
| historical_development | next_open_trained | fixed_policy | 298 | 282 | 16 | 0.49645390070921985 | 0.49166666666666675 | 0.022965699892909454 | None |
| historical_development | next_open_trained | top20 | 1240 | 1200 | 40 | 0.4608333333333333 | 0.4588396196056238 | 0.011396633142250288 | None |
| recent_tail | same_close_trained_control | fixed_policy | 35 | 34 | 1 | 0.38235294117647056 | 0.39285714285714285 | -0.019132564006312733 | None |
| recent_tail | same_close_trained_control | top20 | 140 | 135 | 5 | 0.3333333333333333 | 0.34068504594820387 | 0.003908113794180555 | None |
| recent_tail | next_open_trained | fixed_policy | 35 | 32 | 3 | 0.1875 | 0.21666666666666665 | -0.04403159393880074 | None |
| recent_tail | next_open_trained | top20 | 140 | 136 | 4 | 0.2426470588235294 | 0.2468253968253968 | -0.038002908369589805 | None |

## Paired Probability Error: New Minus Control

Negative favors next-open training; five-session-block intervals are development diagnostics only.

```json
{
  "policy_diagnostic": {
    "date_brier_delta": -0.013234076559976318,
    "lower_95": -0.018774825382598864,
    "upper_95": -0.007194496116706574
  },
  "historical_development": {
    "date_brier_delta": -0.003352886286348036,
    "lower_95": -0.007099860349761063,
    "upper_95": 0.0011921109735777886
  },
  "recent_tail": {
    "date_brier_delta": -0.011963162378665506,
    "lower_95": null,
    "upper_95": null
  }
}
```

## Timing and Limits

```json
{
  "train": {
    "rows": 614781,
    "dates": 744,
    "start": "2023-02-01",
    "end": "2026-02-20",
    "latest_label": "2026-02-27"
  },
  "calibration": {
    "rows": 31902,
    "dates": 38,
    "start": "2026-03-03",
    "end": "2026-04-23",
    "latest_label": "2026-04-30"
  }
}
```

Repeatedly inspected historical dates are development evidence, not independent final validation. No hyperparameter or policy search was performed.
Current-universe survivorship, retrospective adjustments, an observed-universe calendar, exceptional corporate actions and unmodeled fills remain limitations.
Overlapping five-session returns minus 0.3% assumed cost are research proxies, not compounded trading returns or investment advice.
All output recommendations remain ABSTAIN. Genuine new predictions require immutable recording after signal close and before next opening.
