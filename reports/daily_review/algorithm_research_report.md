# Algorithm Research / 알고리즘 연구

RESEARCH_ONLY. Offline program search, not autonomous LLM reasoning or verified investment performance.

운영 모델과 분리된 연구입니다. 유료 API 호출과 LLM 연결은 없으며 추천·자동 주문은 하지 않습니다.
과거 개발 데이터는 반복 탐색에 사용됩니다. 점수가 좋아도 독립 검증이나 신뢰도 상승으로 해석할 수 없습니다.

```json
{
  "schema": "algorithm_research_status_v1",
  "generated_at": "2026-10-30T00:19:27.337080+00:00",
  "status": "snapshot_already_researched",
  "llm_enabled": false,
  "paid_api_calls": false,
  "future_validation_required": true,
  "automatic_orders": false,
  "trials_reserved": 2,
  "trials_completed": 2,
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
  "no_error_reduction_against_matched_control": 2,
  "does_not_beat_past_constant": 2,
  "unstable_across_development_periods": 2,
  "development_outcomes_incomplete": 2,
  "too_few_selected_development_cases": 2
}
```

## Current Development Candidates / 다음 연구 후보

| Program | Date Brier improvement vs matched control |
|---|---:|
| ef0c657c6f84 | -0.00030402 |
| 1ec6e36fbf39 | -0.00031045 |

All attempts, including failures, consume the fixed 120-trial budget. The best development result is not a production approval. No candidate is inserted into the existing registered eight-family competition.

New algorithms need separate prospective registration, multiplicity accounting, immutable forecasts and future evaluation before deployment. Existing production thresholds, confidence scores, candidate pools and forecast originals are unchanged.
