# Frozen Foundation Price Transfer

RESEARCH ONLY. Frozen Chronos-Bolt-Tiny weights from the exact 2024 commit; no external inference service or remote custom code.
This adds learned price-pattern features, not guaranteed new market information. It is not a newly invented foundation architecture.
Same BUY next-open/fifth-close target and 0.3% assumed cost for all arms. No outcome-based inference-universe filtering.
Supervised heads share input-only sampled training rows, fixed logistic capacity, full calibration rows and monotone-score calibration.
The price-only control includes the same input-availability indicator. The shuffled control preserves each date and availability pattern.
Open/close quantile ratios are INPUT PROXIES, not a joint return probability distribution, predicted profit or confidence interval.
Unsupported/invalid price sequences keep the candidate and explicit zero-feature fallback plus availability flag.

| Period | Method | All candidates | Foundation supported | Top5 evaluated | Unknown | Conditional daily success | Conditional net proxy | Brier |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| earlier_development | price_only | 32590 | 28507 | 189 | 6 | 33.72% | -5.26% | 0.24803010956631366 |
| earlier_development | foundation_shuffled | 32590 | 28507 | 190 | 5 | 36.28% | -4.08% | 0.24809282501207927 |
| earlier_development | foundation_augmented | 32590 | 28507 | 187 | 8 | 27.82% | -6.64% | 0.24843239875870854 |
| primary_development | price_only | 52017 | 43611 | 283 | 27 | 40.46% | 0.99% | 0.24708613653305697 |
| primary_development | foundation_shuffled | 52017 | 43611 | 290 | 20 | 41.91% | 1.46% | 0.24711664068251193 |
| primary_development | foundation_augmented | 52017 | 43611 | 290 | 20 | 48.71% | 3.07% | 0.24705455496803924 |
| recent_development | price_only | 7535 | 5999 | 27 | 18 | 23.33% | -2.71% | 0.23890802640218606 |
| recent_development | foundation_shuffled | 7535 | 5999 | 28 | 17 | 13.70% | -6.08% | 0.2389231012832833 |
| recent_development | foundation_augmented | 7535 | 5999 | 27 | 18 | 35.37% | 9.54% | 0.23965071213069003 |

## Prespecified Fit

```json
{
  "train": {
    "rows": 8047,
    "dates": 252,
    "start": "2025-01-03",
    "end": "2026-01-16",
    "latest_label": "2026-01-23"
  },
  "calibration": {
    "rows": 50854,
    "dates": 60,
    "start": "2026-01-26",
    "end": "2026-04-23",
    "latest_label": "2026-04-30"
  },
  "training_input_samples": 8064,
  "unknown_sampled_training_labels": 17
}
```

## Full Development Results

```json
{
  "earlier_development": {
    "input_candidates": 32590,
    "evaluated_cases": 32420,
    "unresolved_cases": 170,
    "foundation_supported": 28507,
    "date_brier": {
      "price_only": 0.24803010956631366,
      "foundation_shuffled": 0.24809282501207927,
      "foundation_augmented": 0.24843239875870854
    },
    "top5": {
      "price_only": {
        "selected_cases": 195,
        "selected_dates": 39,
        "evaluated_cases": 189,
        "unresolved_cases": 6,
        "outcome_coverage": 0.9692307692307692,
        "conditional_success_rate": 0.3386243386243386,
        "conditional_date_success_rate": 0.3371794871794872,
        "conditional_mean_net_return_proxy": -0.0526385474508083,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 4,
          "exit_price_unavailable": 2
        }
      },
      "foundation_shuffled": {
        "selected_cases": 195,
        "selected_dates": 39,
        "evaluated_cases": 190,
        "unresolved_cases": 5,
        "outcome_coverage": 0.9743589743589743,
        "conditional_success_rate": 0.3631578947368421,
        "conditional_date_success_rate": 0.36282051282051286,
        "conditional_mean_net_return_proxy": -0.040813156715446816,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 4,
          "exit_price_unavailable": 1
        }
      },
      "foundation_augmented": {
        "selected_cases": 195,
        "selected_dates": 39,
        "evaluated_cases": 187,
        "unresolved_cases": 8,
        "outcome_coverage": 0.958974358974359,
        "conditional_success_rate": 0.28342245989304815,
        "conditional_date_success_rate": 0.2782051282051282,
        "conditional_mean_net_return_proxy": -0.06640640372275257,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 7,
          "exit_price_unavailable": 1
        }
      }
    },
    "fixed_policy": {
      "price_only": {
        "selected_cases": 51,
        "selected_dates": 13,
        "evaluated_cases": 47,
        "unresolved_cases": 4,
        "outcome_coverage": 0.9215686274509803,
        "conditional_success_rate": 0.48936170212765956,
        "conditional_date_success_rate": 0.5083333333333333,
        "conditional_mean_net_return_proxy": -0.024371528778399983,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 3,
          "exit_price_unavailable": 1
        }
      },
      "foundation_shuffled": {
        "selected_cases": 50,
        "selected_dates": 13,
        "evaluated_cases": 46,
        "unresolved_cases": 4,
        "outcome_coverage": 0.92,
        "conditional_success_rate": 0.5434782608695652,
        "conditional_date_success_rate": 0.5583333333333332,
        "conditional_mean_net_return_proxy": 0.010579336789213512,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 3,
          "exit_price_unavailable": 1
        }
      },
      "foundation_augmented": {
        "selected_cases": 61,
        "selected_dates": 15,
        "evaluated_cases": 58,
        "unresolved_cases": 3,
        "outcome_coverage": 0.9508196721311475,
        "conditional_success_rate": 0.3793103448275862,
        "conditional_date_success_rate": 0.36,
        "conditional_mean_net_return_proxy": -0.006114218688785855,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 2,
          "exit_price_unavailable": 1
        }
      }
    },
    "primary_top5_comparisons": {
      "price_only": {
        "conditional_date_success_difference": -0.04,
        "paired_complete_dates": 30,
        "total_dates": 39,
        "unresolved_selected_across_arms": 14,
        "family_adjusted_lower": -0.13333333333333333,
        "family_adjusted_upper": 0.04117647058823531,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      },
      "foundation_shuffled": {
        "conditional_date_success_difference": -0.07096774193548387,
        "paired_complete_dates": 31,
        "total_dates": 39,
        "unresolved_selected_across_arms": 13,
        "family_adjusted_lower": -0.14375000000000002,
        "family_adjusted_upper": 0.0,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      }
    }
  },
  "primary_development": {
    "input_candidates": 52017,
    "evaluated_cases": 51483,
    "unresolved_cases": 534,
    "foundation_supported": 43611,
    "date_brier": {
      "price_only": 0.24708613653305697,
      "foundation_shuffled": 0.24711664068251193,
      "foundation_augmented": 0.24705455496803924
    },
    "top5": {
      "price_only": {
        "selected_cases": 310,
        "selected_dates": 62,
        "evaluated_cases": 283,
        "unresolved_cases": 27,
        "outcome_coverage": 0.9129032258064517,
        "conditional_success_rate": 0.40636042402826855,
        "conditional_date_success_rate": 0.4045698924731183,
        "conditional_mean_net_return_proxy": 0.009936014654984839,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "exit_price_unavailable": 12,
          "entry_price_unavailable": 6,
          "missing_session_prices": 5,
          "price_discontinuity_requires_review": 4
        }
      },
      "foundation_shuffled": {
        "selected_cases": 310,
        "selected_dates": 62,
        "evaluated_cases": 290,
        "unresolved_cases": 20,
        "outcome_coverage": 0.9354838709677419,
        "conditional_success_rate": 0.4206896551724138,
        "conditional_date_success_rate": 0.4190860215053763,
        "conditional_mean_net_return_proxy": 0.014612972119879756,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "exit_price_unavailable": 7,
          "entry_price_unavailable": 5,
          "missing_session_prices": 5,
          "price_discontinuity_requires_review": 3
        }
      },
      "foundation_augmented": {
        "selected_cases": 310,
        "selected_dates": 62,
        "evaluated_cases": 290,
        "unresolved_cases": 20,
        "outcome_coverage": 0.9354838709677419,
        "conditional_success_rate": 0.4862068965517241,
        "conditional_date_success_rate": 0.48709677419354835,
        "conditional_mean_net_return_proxy": 0.03067500417147166,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "exit_price_unavailable": 8,
          "entry_price_unavailable": 6,
          "missing_session_prices": 4,
          "price_discontinuity_requires_review": 2
        }
      }
    },
    "fixed_policy": {
      "price_only": {
        "selected_cases": 6,
        "selected_dates": 2,
        "evaluated_cases": 6,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.8333333333333334,
        "conditional_date_success_rate": 0.9,
        "conditional_mean_net_return_proxy": 0.30102274784097277,
        "all_date_net_return_proxy": 0.01184290916573079,
        "all_date_net_lower_95": 0.0,
        "unknown_states": {}
      },
      "foundation_shuffled": {
        "selected_cases": 7,
        "selected_dates": 3,
        "evaluated_cases": 7,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.7142857142857143,
        "conditional_date_success_rate": 0.3333333333333333,
        "conditional_mean_net_return_proxy": 0.22074232459520068,
        "all_date_net_return_proxy": 0.004722557351082346,
        "all_date_net_lower_95": -0.0008682561362632039,
        "unknown_states": {}
      },
      "foundation_augmented": {
        "selected_cases": 15,
        "selected_dates": 7,
        "evaluated_cases": 15,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.8666666666666667,
        "conditional_date_success_rate": 0.7142857142857143,
        "conditional_mean_net_return_proxy": 0.3383202455689298,
        "all_date_net_return_proxy": 0.024382187324575318,
        "all_date_net_lower_95": 0.0008915950196916817,
        "unknown_states": {}
      }
    },
    "primary_top5_comparisons": {
      "price_only": {
        "conditional_date_success_difference": 0.016666666666666656,
        "paired_complete_dates": 36,
        "total_dates": 62,
        "unresolved_selected_across_arms": 47,
        "family_adjusted_lower": -0.07295454545454545,
        "family_adjusted_upper": 0.1071923076923075,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      },
      "foundation_shuffled": {
        "conditional_date_success_difference": 0.020000000000000004,
        "paired_complete_dates": 40,
        "total_dates": 62,
        "unresolved_selected_across_arms": 40,
        "family_adjusted_lower": -0.056840062111801225,
        "family_adjusted_upper": 0.1,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      }
    }
  },
  "recent_development": {
    "input_candidates": 7535,
    "evaluated_cases": 7440,
    "unresolved_cases": 95,
    "foundation_supported": 5999,
    "date_brier": {
      "price_only": 0.23890802640218606,
      "foundation_shuffled": 0.2389231012832833,
      "foundation_augmented": 0.23965071213069003
    },
    "top5": {
      "price_only": {
        "selected_cases": 45,
        "selected_dates": 9,
        "evaluated_cases": 27,
        "unresolved_cases": 18,
        "outcome_coverage": 0.6,
        "conditional_success_rate": 0.2962962962962963,
        "conditional_date_success_rate": 0.23333333333333328,
        "conditional_mean_net_return_proxy": -0.02712429232423734,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "missing_session_prices": 14,
          "price_discontinuity_requires_review": 3,
          "entry_price_unavailable": 1
        }
      },
      "foundation_shuffled": {
        "selected_cases": 45,
        "selected_dates": 9,
        "evaluated_cases": 28,
        "unresolved_cases": 17,
        "outcome_coverage": 0.6222222222222222,
        "conditional_success_rate": 0.17857142857142858,
        "conditional_date_success_rate": 0.13703703703703704,
        "conditional_mean_net_return_proxy": -0.060840928793058295,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "missing_session_prices": 14,
          "price_discontinuity_requires_review": 3
        }
      },
      "foundation_augmented": {
        "selected_cases": 45,
        "selected_dates": 9,
        "evaluated_cases": 27,
        "unresolved_cases": 18,
        "outcome_coverage": 0.6,
        "conditional_success_rate": 0.4074074074074074,
        "conditional_date_success_rate": 0.3537037037037037,
        "conditional_mean_net_return_proxy": 0.09537940357679629,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "missing_session_prices": 14,
          "price_discontinuity_requires_review": 3,
          "entry_price_unavailable": 1
        }
      }
    },
    "fixed_policy": {
      "price_only": {
        "selected_cases": 4,
        "selected_dates": 3,
        "evaluated_cases": 1,
        "unresolved_cases": 3,
        "outcome_coverage": 0.25,
        "conditional_success_rate": 0.0,
        "conditional_date_success_rate": 0.0,
        "conditional_mean_net_return_proxy": -0.22120615796519416,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "missing_session_prices": 3
        }
      },
      "foundation_shuffled": {
        "selected_cases": 3,
        "selected_dates": 2,
        "evaluated_cases": 1,
        "unresolved_cases": 2,
        "outcome_coverage": 0.3333333333333333,
        "conditional_success_rate": 0.0,
        "conditional_date_success_rate": 0.0,
        "conditional_mean_net_return_proxy": -0.22120615796519416,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "missing_session_prices": 2
        }
      },
      "foundation_augmented": {
        "selected_cases": 2,
        "selected_dates": 2,
        "evaluated_cases": 1,
        "unresolved_cases": 1,
        "outcome_coverage": 0.5,
        "conditional_success_rate": 0.0,
        "conditional_date_success_rate": 0.0,
        "conditional_mean_net_return_proxy": -0.22120615796519416,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "missing_session_prices": 1
        }
      }
    },
    "primary_top5_comparisons": {
      "price_only": {
        "conditional_date_success_difference": 0.0,
        "paired_complete_dates": 1,
        "total_dates": 9,
        "unresolved_selected_across_arms": 36,
        "family_adjusted_lower": null,
        "family_adjusted_upper": null,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      },
      "foundation_shuffled": {
        "conditional_date_success_difference": 0.19999999999999996,
        "paired_complete_dates": 1,
        "total_dates": 9,
        "unresolved_selected_across_arms": 35,
        "family_adjusted_lower": null,
        "family_adjusted_upper": null,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      }
    }
  }
}
```

Repeatedly inspected development history cannot certify the 60% prospective goal. All recommendations remain ABSTAIN.
Current-universe survivorship, retrospective adjustment, observed-universe calendar and unmodeled fills remain limitations.
Official model: https://huggingface.co/amazon/chronos-bolt-tiny
