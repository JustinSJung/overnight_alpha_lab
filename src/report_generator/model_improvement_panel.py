"""Plain-language public progress, not internal family names or backtest claims."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path


def render_model_improvement_card(path, now=None):
    en, ko, color = 'Preparing', '자동 비교 준비 중', 'badge-gray'
    note = '후보 모델을 비교 학습하는 경로를 준비 중입니다.'
    details = ''
    try:
        path = Path(path)
        if path.stat().st_size > 100_000:
            raise ValueError('Oversized improvement status.')
        data = json.loads(path.read_text())
        generated = datetime.fromisoformat(data['generated_at'])
        now = now or datetime.now(timezone.utc)
        if (data['schema'] != 'model_improvement_status_v1' or generated.tzinfo is None
                or generated > now + timedelta(minutes=5) or data['recommendation_enabled'] is not False
                or data['automatic_orders'] is not False):
            raise ValueError('Invalid improvement status.')
        if now - generated > timedelta(days=7):
            en, ko, color = 'Update Needed', '상태 갱신 필요', 'badge-orange'
            note = '자동 비교 학습의 최근 실행 상태를 확인해야 합니다.'
        elif data['status'] == 'audit_unavailable':
            en, ko, color = 'Needs Review', '점검 필요', 'badge-orange'
            note = '자동 모델 교체를 보류하고 검증 데이터를 점검합니다.'
        else:
            goals = data['candidate_goals']
            count = data['challenger_count']
            dates = [item['selected_signal_dates'] for item in goals.values()]
            recorded = data.get('original_batches', 0)
            if type(recorded) is not int or recorded < 0:
                raise ValueError('Invalid recorded forecast count.')
            recorded += int(data.get('recording') == 'new_prospective_batch_recorded')
            if count != 3 or len(goals) != count or any(type(day) is not int or day < 0 for day in dates):
                raise ValueError('Invalid comparison counts.')
            details = f'<div class="muted-helper">후보 모델 {count}개 · 사전 예측 {recorded:,}일<br>선택 후보 평가 {max(dates, default=0):,}일</div>'
            if data['status'] == 'collecting_forward_evidence':
                en, ko, color = 'Learning & Comparing', '학습·비교 검증 중', 'badge-orange'
                note = '후보 모델을 학습하고 사전 예측 결과를 축적합니다. 기준 통과 전에는 기존 모델을 유지합니다.'
            elif data['status'] == 'validated_challenger_active':
                active = data['active_family']
                proof = goals[active]
                if (proof['goal_passed'] is not True or proof['evaluated_cases'] < 300
                        or proof['selected_signal_dates'] < 60 or proof['success_lower'] < .6
                        or data['comparisons'][active + '_vs_baseline']['passed'] is not True):
                    raise ValueError('An active challenger needs actual passing evidence.')
                en, ko, color = 'Improved Model Active', '검증 통과 모델 적용', 'badge-green'
                note = '검증 기준을 통과한 모델로 예측합니다. 추천 개방은 별도이며 자동 주문은 하지 않습니다.'
                if data.get('activation') == 'existing_original_preserved':
                    en, ko = 'Validated, Pending Next Forecast', '검증 통과·다음 예측 적용'
                    note = '이미 공개한 예측은 바꾸지 않고, 다음 새 예측부터 검증 통과 모델을 적용합니다.'
            else:
                raise ValueError('Unknown improvement phase.')
    except FileNotFoundError:
        pass
    except (OSError, ValueError, KeyError, TypeError, OverflowError):
        en, ko, color = 'Needs Review', '점검 필요', 'badge-orange'
        note = '자동 비교 학습 상태를 확인 중입니다. 검증 완료로 표시하지 않습니다.'
        details = ''
    return f'''<div class="card" id="model-improvement-state">
      <div class="label">Model Improvement</div><div class="ko-desc">모델 자동개선</div>
      <span class="status-pill {color}">{en}<br>{ko}</span>
      {details}<div class="muted-helper">{note}</div>
    </div>'''
