# Learning from actual forecast errors

The product goal is a stock-name/code forecast and, only when independently
validated, a useful short list of recommendations. Raising a displayed
probability is not a performance target. The target is the existing next open
to fifth close return after the 0.3% cost assumption.

ML Beta now runs an isolated comparison after grading the original forecasts.
This experiment does not change stock lookup, the candidate pool, production
probabilities, the 60% cutoff, the registered certification budget, or orders.
The [latest feedback report](../reports/daily_review/forecast_feedback_status.json)
is separate from legacy event or price scores.

* Calibration: compare forecast probabilities with realized frequencies in fixed
  probability bands. Ranking: compare the top and bottom fifths **within each
  signal day**. Ties have the same rank; ranks include unresolved stocks.
* Learn signed outcome-minus-probability errors over the last 60 eligible issue
  dates. Only original signals with outcomes available by the forecast close are
  used; require at least 100 issues and 95% resolved on each of at least five
  dates. A day of correlated stocks is not hundreds of independent days.
* Market correction = sum of daily mean errors / (days + 20). Rank correction
  uses daily quintile errors after removing the daily mean, with the same
  shrinkage. Stock correction uses repeated errors beyond the day/quintile
  mean, divided by (observations + 40), requiring at least five observations.
  Add corrections to the original probability and clip to [0, 1]. No parameter
  is chosen by looking for a higher retrospective hit rate.
* Save every eligible stock's shadow probability once, alongside its original
  cohort fingerprint, **before** the next opening. Never reconstruct missed
  batches after outcomes arrive. If the algorithm fingerprint changes, start a
  separately reviewed version rather than pooling incompatible experiments.
* Grade only those frozen pairs. Compare equal-day Brier loss (lower is better)
  with the raw model and the original base-rate forecast. Compare top five and
  threshold-selected hit counts with unresolved cases retained. These are
  descriptive results, not a certification test.

Even a lower Brier loss is not sufficient to recommend stocks. The production
goal still requires at least 60 selected signal dates and 300 resolved selected
cases, a 60% conservative lower hit-rate bound, net and benchmark performance,
and adequate coverage. The shadow has no automatic promotion path.
