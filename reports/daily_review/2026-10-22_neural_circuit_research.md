# Neural Circuit Memory Research / 생체모방 신경회로 연구

RESEARCH_ONLY. Known NCP/CfC architecture applied to a new project experiment; not a newly discovered universal algorithm or a finance performance guarantee.

## Fixed Comparison

Same 19 causal OHLCV inputs, next-open to fifth-close target after 0.3% assumed cost, date-equal fitting, partitions, fixed two-seed mean and sigmoid calibration.
last_mlp uses only the final snapshot; GRU is the ordinary temporal control; dense CfC and sparse AutoNCP CfC test alternative dynamics/architectures.
All recurrent models reset state per stock/window. Missing history uses a counted last_mlp fallback, never another stock or invented bars.
Input-only per-date sampling limits training cost, not the prediction candidate pool. All arms use identical mature complete-sequence fitting endpoints.
Architectures have different parameter counts; a difference cannot be attributed to wiring alone. No best seed, epoch, architecture or threshold is chosen using external outcomes.

## Fit Audit

```json
{
  "train": {
    "rows": 46071,
    "dates": 725,
    "start": "2023-02-28",
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

## Historical Development

| Period | Arm | Candidates | Evaluated | Unknown | Date Brier | Past constant Brier | Daily AUC | Sequence fallback |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| earlier_development | last_mlp | 32590 | 32420 | 170 | 0.2608477483553124 | 0.25473970329933343 | 0.512440731042288 | 0 |
| earlier_development | gru | 32590 | 32420 | 170 | 0.2579691740427532 | 0.25473970329933343 | 0.5262805332710372 | 170 |
| earlier_development | cfc_dense | 32590 | 32420 | 170 | 0.26249926526367623 | 0.25473970329933343 | 0.5213081960982855 | 170 |
| earlier_development | cfc_ncp | 32590 | 32420 | 170 | 0.25583757325386064 | 0.25473970329933343 | 0.5351671824982883 | 170 |
| earlier_development | extra_trees | 32590 | 32420 | 170 | 0.26599589115645433 | 0.25473970329933343 | 0.5271081324570509 | 0 |
| primary_development | last_mlp | 52017 | 51483 | 534 | 0.24773699327022428 | 0.2514088879352742 | 0.5306540855821721 | 0 |
| primary_development | gru | 52017 | 51483 | 534 | 0.24811031918290047 | 0.2514088879352742 | 0.5301765994880492 | 231 |
| primary_development | cfc_dense | 52017 | 51483 | 534 | 0.24821673534255176 | 0.2514088879352742 | 0.5273211507711685 | 231 |
| primary_development | cfc_ncp | 52017 | 51483 | 534 | 0.2474954039068679 | 0.2514088879352742 | 0.5333759298730282 | 231 |
| primary_development | extra_trees | 52017 | 51483 | 534 | 0.24924222707718333 | 0.2514088879352742 | 0.5292906985169945 | 0 |
| recent_tail | last_mlp | 6703 | 6612 | 91 | 0.2557896361138973 | 0.2556372241771462 | 0.5087398876482194 | 0 |
| recent_tail | gru | 6703 | 6612 | 91 | 0.25174922402133654 | 0.2556372241771462 | 0.530325649288433 | 63 |
| recent_tail | cfc_dense | 6703 | 6612 | 91 | 0.2570257158456448 | 0.2556372241771462 | 0.5138118185547169 | 63 |
| recent_tail | cfc_ncp | 6703 | 6612 | 91 | 0.2548150923228831 | 0.2556372241771462 | 0.5177076496231461 | 63 |
| recent_tail | extra_trees | 6703 | 6612 | 91 | 0.25958136787965397 | 0.2556372241771462 | 0.5138222649731157 | 0 |

## Equal-Coverage Monitoring and Fixed Policy

Selections are ranked BEFORE outcomes; unknown selections are not replaced. Conditional results are not complete-policy performance.

| Period | Arm | Group | Selected | Resolved | Unknown | Conditional daily success | Conditional mean net proxy |
|---|---|---|---:|---:|---:|---:|---:|
| earlier_development | last_mlp | top20 | 780 | 761 | 19 | 0.34576662873876496 | -0.032706845573893195 |
| earlier_development | last_mlp | fixed_policy | 195 | 192 | 3 | 0.39615384615384613 | -0.025233270934896884 |
| earlier_development | gru | top20 | 780 | 762 | 18 | 0.36772379667116506 | -0.025257490326142464 |
| earlier_development | gru | fixed_policy | 184 | 182 | 2 | 0.3572649572649572 | -0.027761540543930117 |
| earlier_development | cfc_dense | top20 | 780 | 775 | 5 | 0.3553456290298396 | -0.034798138625234024 |
| earlier_development | cfc_dense | fixed_policy | 195 | 194 | 1 | 0.3525641025641026 | -0.03720061379614294 |
| earlier_development | cfc_ncp | top20 | 780 | 777 | 3 | 0.35285650022492127 | -0.03181606974409695 |
| earlier_development | cfc_ncp | fixed_policy | 193 | 193 | 0 | 0.33333333333333337 | -0.0414414656726838 |
| earlier_development | extra_trees | top20 | 780 | 762 | 18 | 0.3588072115935893 | -0.03075032773753582 |
| earlier_development | extra_trees | fixed_policy | 195 | 191 | 4 | 0.37820512820512825 | -0.0323176745836999 |
| primary_development | last_mlp | top20 | 1240 | 1179 | 61 | 0.44755678728763715 | 0.0051611665565947885 |
| primary_development | last_mlp | fixed_policy | 295 | 259 | 36 | 0.45819672131147543 | 0.009961575000151136 |
| primary_development | gru | top20 | 1240 | 1194 | 46 | 0.4422070752466238 | -0.0029184466242141464 |
| primary_development | gru | fixed_policy | 232 | 213 | 19 | 0.4322033898305085 | 0.009647346542442103 |
| primary_development | cfc_dense | top20 | 1240 | 1200 | 40 | 0.43836845434268784 | -0.0020002147874319844 |
| primary_development | cfc_dense | fixed_policy | 309 | 285 | 24 | 0.44650537634408605 | -0.0021575885997943338 |
| primary_development | cfc_ncp | top20 | 1240 | 1205 | 35 | 0.4366534616110168 | -0.0023892659900334088 |
| primary_development | cfc_ncp | fixed_policy | 309 | 283 | 26 | 0.3892473118279569 | -0.007375429048147399 |
| primary_development | extra_trees | top20 | 1240 | 1207 | 33 | 0.45771080928126767 | 0.005417764373724896 |
| primary_development | extra_trees | fixed_policy | 310 | 292 | 18 | 0.4916666666666667 | 0.00832947279278723 |
| recent_tail | last_mlp | top20 | 160 | 137 | 23 | 0.33560855263157896 | -0.01365293441592276 |
| recent_tail | last_mlp | fixed_policy | 40 | 26 | 14 | 0.3645833333333333 | -0.009940806315480675 |
| recent_tail | gru | top20 | 160 | 144 | 16 | 0.2654395639834881 | -0.03729316038064215 |
| recent_tail | gru | fixed_policy | 39 | 25 | 14 | 0.29166666666666663 | -0.041199844210320385 |
| recent_tail | cfc_dense | top20 | 160 | 143 | 17 | 0.24734477124183007 | -0.04396554865197082 |
| recent_tail | cfc_dense | fixed_policy | 40 | 26 | 14 | 0.1875 | -0.06836426601466447 |
| recent_tail | cfc_ncp | top20 | 160 | 141 | 19 | 0.24527272531819744 | -0.056099783629338915 |
| recent_tail | cfc_ncp | fixed_policy | 40 | 26 | 14 | 0.3333333333333333 | -0.06907307291312022 |
| recent_tail | extra_trees | top20 | 160 | 155 | 5 | 0.2716008771929824 | -0.03680861937899872 |
| recent_tail | extra_trees | fixed_policy | 40 | 37 | 3 | 0.21875 | -0.045919420737308675 |

## Primary NCP Minus Each Control: Date Brier

Four prespecified comparisons, Bonferroni family alpha 0.05; five-session circular-block bootstrap, 5,000 samples. Approximate development intervals, not untouched validation.

```json
{
  "last_mlp": {
    "mean": -0.00024158936335636478,
    "lower": -0.00449346148932103,
    "upper": 0.0027711145214766803
  },
  "gru": {
    "mean": -0.0006149152760325422,
    "lower": -0.00223044310530831,
    "upper": 0.0007265719114688663
  },
  "cfc_dense": {
    "mean": -0.000721331435683838,
    "lower": -0.003006324185015168,
    "upper": 0.002302586096854853
  },
  "extra_trees": {
    "mean": -0.0017468231703154254,
    "lower": -0.00505459990382319,
    "upper": 0.001367653186225747
  }
}
```

## Parameters and Calibration

```json
{
  "last_mlp": {
    "parameters": 3393,
    "training": [
      {
        "seed": 17,
        "training_loss_by_epoch": [
          0.6790645098968775,
          0.6768468843247782,
          0.6761783576832416,
          0.6756007108404039,
          0.6752984863241899,
          0.6747968393222284,
          0.6743876851225238,
          0.6738704504767704
        ]
      },
      {
        "seed": 42,
        "training_loss_by_epoch": [
          0.681037452832553,
          0.677463211462829,
          0.6768258217386529,
          0.6762061648937467,
          0.6757716672638008,
          0.6755709540866992,
          0.6753721403921924,
          0.6748473733137647
        ]
      }
    ],
    "calibration_slope": 0.8637230075128222,
    "calibration_intercept": 0.3635018694654859
  },
  "gru": {
    "parameters": 5121,
    "training": [
      {
        "seed": 17,
        "training_loss_by_epoch": [
          0.6787706867091001,
          0.6766011678865378,
          0.6755535308084779,
          0.6746515794921886,
          0.6739072694332044,
          0.6730335465498779,
          0.6723725424644803,
          0.6719199405333666
        ]
      },
      {
        "seed": 42,
        "training_loss_by_epoch": [
          0.6796760884966296,
          0.6762361520098102,
          0.6753663924207123,
          0.6745801367317964,
          0.6738146306137346,
          0.6733255012599292,
          0.6729817632943569,
          0.6723452341833154
        ]
      }
    ],
    "calibration_slope": 0.5825549400369514,
    "calibration_intercept": 0.244088168380897
  },
  "cfc_dense": {
    "parameters": 5921,
    "training": [
      {
        "seed": 17,
        "training_loss_by_epoch": [
          0.6805197881422179,
          0.6754486458588913,
          0.6740404496369711,
          0.6731155207566428,
          0.6723582890340032,
          0.6711577370063226,
          0.6699805860214497,
          0.669032550462795
        ]
      },
      {
        "seed": 42,
        "training_loss_by_epoch": [
          0.6813249787574599,
          0.6756157237368573,
          0.6744904864983495,
          0.6733520670711939,
          0.6721831022035782,
          0.6716043275882313,
          0.6707951830494373,
          0.6697710511033451
        ]
      }
    ],
    "calibration_slope": 0.7407331701567459,
    "calibration_intercept": 0.328586338588456
  },
  "cfc_ncp": {
    "parameters": 4447,
    "training": [
      {
        "seed": 17,
        "training_loss_by_epoch": [
          0.688254758578168,
          0.6776134396714065,
          0.6754256632052152,
          0.6745808990272177,
          0.6739230266703298,
          0.6732605672721501,
          0.6725599112572989,
          0.6719398232293055
        ]
      },
      {
        "seed": 42,
        "training_loss_by_epoch": [
          0.682633319621115,
          0.6766100959251429,
          0.6752299881220014,
          0.6738736526140834,
          0.6729594015117237,
          0.6722928879795131,
          0.6717648953804217,
          0.6710077763452464
        ]
      }
    ],
    "calibration_slope": 0.7324638758667766,
    "calibration_intercept": 0.33013820255742327
  },
  "extra_trees": {
    "calibration_slope": 1.5988882095735282,
    "calibration_intercept": 0.5749728546088092
  }
}
```

## Limits

These historical periods have already been inspected in earlier experiments. They remain development evidence, not a new independent test.
Current-universe survivorship, retrospective adjustments, observed-universe calendars, outcome unavailability and unmodeled execution remain limitations.
The primary research output is NCP CfC even if another model looks better; all outputs remain ABSTAIN. No production model, public dashboard metric or prior forecast is replaced.
The comparison does not test bee/ant communication or homeostatic risk control. Those mechanisms must be separate ablations, not names attached to this model.

References: https://github.com/mlech26l/ncps and https://arxiv.org/abs/2106.13898
