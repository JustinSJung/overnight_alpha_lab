# Within-Day Pairwise Price Learning

RESEARCH ONLY. Same next-open BUY labels and assumed 0.3% cost. No broad candidate-pool reduction or trading.
Two matched pointwise controls distinguish feature normalization from the pairwise objective.
Features are ranked inside each day BEFORE outcomes are filtered. Cross-sectional ranks are never probabilities.
Date-specific training pairs have equal total weight across informative days; pairs are compute samples, not an inference-universe cap.
All engines use the same fixed tree/iteration/seed budget. No early stopping, threshold search or result-selected winner.
Shared calibration context is fitted only on separate past calibration rows, with a nonnegative own-score coefficient.

| Period | Method | Input candidates | Top5 selected | Evaluated | Unknown | Conditional daily success | Conditional net proxy | Brier |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| earlier_development | pointwise_raw | 32590 | 195 | 189 | 6 | 32.56% | -3.89% | 0.25032602838275925 |
| earlier_development | pointwise_cross_section | 32590 | 195 | 194 | 1 | 33.46% | -2.24% | 0.25997142149783464 |
| earlier_development | pairwise_cross_section | 32590 | 195 | 194 | 1 | 42.44% | -0.10% | 0.25066649009548675 |
| primary_development | pointwise_raw | 52017 | 310 | 293 | 17 | 48.25% | 2.08% | 0.24552064174727914 |
| primary_development | pointwise_cross_section | 52017 | 310 | 309 | 1 | 45.16% | 0.09% | 0.24629338779544807 |
| primary_development | pairwise_cross_section | 52017 | 310 | 309 | 1 | 42.58% | 0.38% | 0.24762008705612765 |
| recent_development | pointwise_raw | 7535 | 45 | 44 | 1 | 32.22% | 0.73% | 0.24059161034700832 |
| recent_development | pointwise_cross_section | 7535 | 45 | 45 | 0 | 20.00% | -6.43% | 0.24011566755150998 |
| recent_development | pairwise_cross_section | 7535 | 45 | 44 | 1 | 17.78% | -5.35% | 0.24211599596888345 |

Unknown selections are never replaced. Conditional results do not establish complete-policy returns.
This repeatedly inspected historical development history cannot certify the agreed 60% reliability goal.

## Fit and Calibration

```json
{
  "train": {
    "rows": 423264,
    "dates": 504,
    "start": "2023-12-19",
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
  "informative_pair_dates": 504,
  "training_pairs": 1032192,
  "pair_weight_sum": 423264.0000000008
}
```

Own-score calibration slopes: {
  "pointwise_raw": 0.16158629768182348,
  "pointwise_cross_section": 0.1751522294934592,
  "pairwise_cross_section": 0.13074126268225014
}

## Complete Diagnostics

```json
{
  "earlier_development": {
    "input_candidates": 32590,
    "evaluated_cases": 32420,
    "unresolved_cases": 170,
    "signal_dates": 39,
    "date_brier": {
      "pointwise_raw": 0.25032602838275925,
      "pointwise_cross_section": 0.25997142149783464,
      "pairwise_cross_section": 0.25066649009548675
    },
    "selections": {
      "top5_pointwise_raw": {
        "selected_cases": 195,
        "selected_dates": 39,
        "evaluated_cases": 189,
        "unresolved_cases": 6,
        "outcome_coverage": 0.9692307692307692,
        "conditional_success_rate": 0.3333333333333333,
        "conditional_date_success_rate": 0.32564102564102565,
        "conditional_mean_net_return_proxy": -0.03893971534741756,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "exit_price_unavailable": 6
        }
      },
      "top5_pointwise_cross_section": {
        "selected_cases": 195,
        "selected_dates": 39,
        "evaluated_cases": 194,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9948717948717949,
        "conditional_success_rate": 0.33505154639175255,
        "conditional_date_success_rate": 0.33461538461538465,
        "conditional_mean_net_return_proxy": -0.022366399966607164,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "price_discontinuity_requires_review": 1
        }
      },
      "top5_pairwise_cross_section": {
        "selected_cases": 195,
        "selected_dates": 39,
        "evaluated_cases": 194,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9948717948717949,
        "conditional_success_rate": 0.422680412371134,
        "conditional_date_success_rate": 0.4243589743589743,
        "conditional_mean_net_return_proxy": -0.0010497870168447892,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "price_discontinuity_requires_review": 1
        }
      },
      "matched_policy_pointwise_raw": {
        "selected_cases": 116,
        "selected_dates": 25,
        "evaluated_cases": 116,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.4482758620689655,
        "conditional_date_success_rate": 0.42133333333333334,
        "conditional_mean_net_return_proxy": -0.0034649020681390037,
        "all_date_net_return_proxy": -0.00755821954097603,
        "all_date_net_lower_95": -0.03336971050678185,
        "unknown_states": {}
      },
      "matched_policy_pointwise_cross_section": {
        "selected_cases": 116,
        "selected_dates": 25,
        "evaluated_cases": 115,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9913793103448276,
        "conditional_success_rate": 0.4608695652173913,
        "conditional_date_success_rate": 0.44866666666666666,
        "conditional_mean_net_return_proxy": 0.002336693138480272,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "price_discontinuity_requires_review": 1
        }
      },
      "matched_policy_pairwise_cross_section": {
        "selected_cases": 116,
        "selected_dates": 25,
        "evaluated_cases": 115,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9913793103448276,
        "conditional_success_rate": 0.5565217391304348,
        "conditional_date_success_rate": 0.5286666666666666,
        "conditional_mean_net_return_proxy": 0.02718357888758236,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "price_discontinuity_requires_review": 1
        }
      }
    },
    "primary_top5_comparisons": {
      "pointwise_raw": {
        "conditional_date_success_difference": 0.09999999999999999,
        "paired_complete_dates": 34,
        "total_dates": 39,
        "unresolved_selected_across_arms": 7,
        "family_adjusted_lower": -0.006451612903225808,
        "family_adjusted_upper": 0.22499999999999998,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      },
      "pointwise_cross_section": {
        "conditional_date_success_difference": 0.07894736842105263,
        "paired_complete_dates": 38,
        "total_dates": 39,
        "unresolved_selected_across_arms": 2,
        "family_adjusted_lower": 0.015789473684210516,
        "family_adjusted_upper": 0.14871794871794874,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      }
    }
  },
  "primary_development": {
    "input_candidates": 52017,
    "evaluated_cases": 51483,
    "unresolved_cases": 534,
    "signal_dates": 62,
    "date_brier": {
      "pointwise_raw": 0.24552064174727914,
      "pointwise_cross_section": 0.24629338779544807,
      "pairwise_cross_section": 0.24762008705612765
    },
    "selections": {
      "top5_pointwise_raw": {
        "selected_cases": 310,
        "selected_dates": 62,
        "evaluated_cases": 293,
        "unresolved_cases": 17,
        "outcome_coverage": 0.9451612903225807,
        "conditional_success_rate": 0.4778156996587031,
        "conditional_date_success_rate": 0.48252688172043007,
        "conditional_mean_net_return_proxy": 0.020798947231245292,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 9,
          "exit_price_unavailable": 4,
          "price_discontinuity_requires_review": 2,
          "missing_session_prices": 2
        }
      },
      "top5_pointwise_cross_section": {
        "selected_cases": 310,
        "selected_dates": 62,
        "evaluated_cases": 309,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9967741935483871,
        "conditional_success_rate": 0.44983818770226536,
        "conditional_date_success_rate": 0.4516129032258064,
        "conditional_mean_net_return_proxy": 0.0009171725415521723,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "exit_price_unavailable": 1
        }
      },
      "top5_pairwise_cross_section": {
        "selected_cases": 310,
        "selected_dates": 62,
        "evaluated_cases": 309,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9967741935483871,
        "conditional_success_rate": 0.42394822006472493,
        "conditional_date_success_rate": 0.42580645161290315,
        "conditional_mean_net_return_proxy": 0.003807017639216812,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 1
        }
      },
      "matched_policy_pointwise_raw": {
        "selected_cases": 75,
        "selected_dates": 19,
        "evaluated_cases": 70,
        "unresolved_cases": 5,
        "outcome_coverage": 0.9333333333333333,
        "conditional_success_rate": 0.5428571428571428,
        "conditional_date_success_rate": 0.5777777777777777,
        "conditional_mean_net_return_proxy": 0.072633453624889,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 3,
          "exit_price_unavailable": 2
        }
      },
      "matched_policy_pointwise_cross_section": {
        "selected_cases": 75,
        "selected_dates": 19,
        "evaluated_cases": 75,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.56,
        "conditional_date_success_rate": 0.5342105263157895,
        "conditional_mean_net_return_proxy": 0.03011787567380079,
        "all_date_net_return_proxy": 0.008516972330024878,
        "all_date_net_lower_95": -0.00954623142011638,
        "unknown_states": {}
      },
      "matched_policy_pairwise_cross_section": {
        "selected_cases": 75,
        "selected_dates": 19,
        "evaluated_cases": 74,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9866666666666667,
        "conditional_success_rate": 0.527027027027027,
        "conditional_date_success_rate": 0.5052631578947369,
        "conditional_mean_net_return_proxy": 0.06393759891505797,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 1
        }
      }
    },
    "primary_top5_comparisons": {
      "pointwise_raw": {
        "conditional_date_success_difference": -0.031111111111111114,
        "paired_complete_dates": 45,
        "total_dates": 62,
        "unresolved_selected_across_arms": 18,
        "family_adjusted_lower": -0.11519711538461538,
        "family_adjusted_upper": 0.0744186046511628,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      },
      "pointwise_cross_section": {
        "conditional_date_success_difference": -0.023333333333333327,
        "paired_complete_dates": 60,
        "total_dates": 62,
        "unresolved_selected_across_arms": 2,
        "family_adjusted_lower": -0.0918032786885246,
        "family_adjusted_upper": 0.034482758620689655,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      }
    }
  },
  "recent_development": {
    "input_candidates": 7535,
    "evaluated_cases": 7440,
    "unresolved_cases": 95,
    "signal_dates": 9,
    "date_brier": {
      "pointwise_raw": 0.24059161034700832,
      "pointwise_cross_section": 0.24011566755150998,
      "pairwise_cross_section": 0.24211599596888345
    },
    "selections": {
      "top5_pointwise_raw": {
        "selected_cases": 45,
        "selected_dates": 9,
        "evaluated_cases": 44,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9777777777777777,
        "conditional_success_rate": 0.3181818181818182,
        "conditional_date_success_rate": 0.3222222222222222,
        "conditional_mean_net_return_proxy": 0.007332138117406764,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "entry_price_unavailable": 1
        }
      },
      "top5_pointwise_cross_section": {
        "selected_cases": 45,
        "selected_dates": 9,
        "evaluated_cases": 45,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.2,
        "conditional_date_success_rate": 0.2,
        "conditional_mean_net_return_proxy": -0.06430330170262101,
        "all_date_net_return_proxy": -0.06430330170262101,
        "all_date_net_lower_95": null,
        "unknown_states": {}
      },
      "top5_pairwise_cross_section": {
        "selected_cases": 45,
        "selected_dates": 9,
        "evaluated_cases": 44,
        "unresolved_cases": 1,
        "outcome_coverage": 0.9777777777777777,
        "conditional_success_rate": 0.18181818181818182,
        "conditional_date_success_rate": 0.17777777777777776,
        "conditional_mean_net_return_proxy": -0.053529429441700443,
        "all_date_net_return_proxy": null,
        "all_date_net_lower_95": null,
        "unknown_states": {
          "missing_session_prices": 1
        }
      },
      "matched_policy_pointwise_raw": {
        "selected_cases": 16,
        "selected_dates": 4,
        "evaluated_cases": 16,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.3125,
        "conditional_date_success_rate": 0.25,
        "conditional_mean_net_return_proxy": -0.015895161384931397,
        "all_date_net_return_proxy": -0.008257460890080868,
        "all_date_net_lower_95": null,
        "unknown_states": {}
      },
      "matched_policy_pointwise_cross_section": {
        "selected_cases": 16,
        "selected_dates": 4,
        "evaluated_cases": 16,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.3125,
        "conditional_date_success_rate": 0.25,
        "conditional_mean_net_return_proxy": -0.014110546967473,
        "all_date_net_return_proxy": -0.006377767126896387,
        "all_date_net_lower_95": null,
        "unknown_states": {}
      },
      "matched_policy_pairwise_cross_section": {
        "selected_cases": 16,
        "selected_dates": 4,
        "evaluated_cases": 16,
        "unresolved_cases": 0,
        "outcome_coverage": 1.0,
        "conditional_success_rate": 0.0625,
        "conditional_date_success_rate": 0.05,
        "conditional_mean_net_return_proxy": -0.05314899491852166,
        "all_date_net_return_proxy": -0.028492694469000848,
        "all_date_net_lower_95": null,
        "unknown_states": {}
      }
    },
    "primary_top5_comparisons": {
      "pointwise_raw": {
        "conditional_date_success_difference": -0.17142857142857143,
        "paired_complete_dates": 7,
        "total_dates": 9,
        "unresolved_selected_across_arms": 2,
        "family_adjusted_lower": null,
        "family_adjusted_upper": null,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      },
      "pointwise_cross_section": {
        "conditional_date_success_difference": -0.025000000000000022,
        "paired_complete_dates": 8,
        "total_dates": 9,
        "unresolved_selected_across_arms": 1,
        "family_adjusted_lower": null,
        "family_adjusted_upper": null,
        "complete_period_lower": null,
        "interpretation": "Conditional on complete paired selected outcomes; not full policy evidence if any are unknown"
      }
    }
  }
}
```

Two primary comparisons use family-adjusted five-session blocks. Any missing paired date prevents a full-period lower-bound claim.
Current-universe survivorship, retrospective corporate-action adjustment and an observed-universe calendar remain limitations.
Overlapping return proxies are not compounded portfolio results or guaranteed executable profits.
Official implementation: https://catboost.ai/docs/en/concepts/loss-functions-ranking
