# Algorithm Research / 알고리즘 연구

RESEARCH_ONLY. Offline program search, not autonomous LLM reasoning or verified investment performance.

운영 모델과 분리된 연구입니다. 유료 API 호출과 LLM 연결은 없으며 추천·자동 주문은 하지 않습니다.
과거 개발 데이터는 반복 탐색에 사용됩니다. 점수가 좋아도 독립 검증이나 신뢰도 상승으로 해석할 수 없습니다.

```json
{
  "schema": "algorithm_research_status_v1",
  "generated_at": "2026-10-30T14:51:25.487709+00:00",
  "status": "researching_not_production_validated",
  "llm_enabled": false,
  "paid_api_calls": false,
  "future_validation_required": true,
  "automatic_orders": false,
  "trials_reserved": 6,
  "trials_completed": 6,
  "trials_failed": 0,
  "trials_incomplete": 0,
  "research_screen_passed": 0,
  "production_promotion": false,
  "recommendation_enabled": false
}
```

## Remembered Failures / 누적 실험의 한계

```json
{
  "does_not_beat_past_constant": 6,
  "development_outcomes_incomplete": 6,
  "too_few_selected_development_cases": 6,
  "unstable_across_development_periods": 4,
  "no_error_reduction_against_matched_control": 3
}
```

## Current Development Candidates / 다음 연구 후보

| Program | Date Brier improvement vs matched control |
|---|---:|
| be7c8685e10b | 0.00213978 |
| ed0c5513caed | 0.00005328 |
| 2061c308fac5 | 0.00002809 |
| 9da1278de84a | -0.00002727 |
| ef0c657c6f84 | -0.00030402 |

All attempts, including failures, consume the fixed 120-trial budget. The best development result is not a production approval. No candidate is inserted into the existing registered eight-family competition.

New algorithms need separate prospective registration, multiplicity accounting, immutable forecasts and future evaluation before deployment. Existing production thresholds, confidence scores, candidate pools and forecast originals are unchanged.
