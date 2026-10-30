"""Small public research progress, explicitly distinct from validated performance."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path


def render_algorithm_research_card(path, now=None):
    badge, note, details = 'Preparing<br>연구 준비 중', '운영 모델과 분리된 수식 탐색을 준비합니다.', ''
    try:
        path = Path(path)
        if path.stat().st_size > 100_000:
            raise ValueError('Oversized research status.')
        data = json.loads(path.read_text())
        clock = now or datetime.now(timezone.utc)
        generated = datetime.fromisoformat(data['generated_at'])
        counts = [data[key] for key in ['trials_reserved', 'trials_completed', 'trials_failed', 'trials_incomplete']]
        passed = data['research_screen_passed']
        if (data['schema'] != 'algorithm_research_status_v1' or generated.tzinfo is None
                or generated > clock + timedelta(minutes=5)
                or any(type(count) is not int or not 0 <= count <= 120 for count in counts)
                or counts[0] != sum(counts[1:])
                or type(passed) is not int or not 0 <= passed <= counts[1]
                or data['status'] not in ['waiting_for_price_history', 'snapshot_already_researched',
                                          'interrupted_research_requires_review', 'research_budget_requires_review',
                                          'researching_not_production_validated']
                or any(data[key] is not False for key in ['llm_enabled', 'paid_api_calls', 'production_promotion',
                                                         'recommendation_enabled', 'automatic_orders'])):
            raise ValueError('Invalid research status.')
        if clock - generated > timedelta(days=7):
            badge, note = 'Update Needed<br>연구 상태 확인 필요', '최근 연구 실행 상태를 확인해야 합니다.'
        elif data['status'] == 'waiting_for_price_history':
            badge, note = 'Waiting for Data<br>연구 데이터 대기', '가격 이력이 준비되면 제한된 수식 탐색을 시작합니다.'
        else:
            badge = 'Offline Research<br>수식 탐색 실험'
            details = f'<div class="muted-helper">실험 평가 {counts[1]:,}개 · 실행 오류 {counts[2]:,}개<br>중단 {counts[3]:,}개 · 과거 비교 기준 통과 {passed:,}개</div>'
            note = '과거 실험을 기억해 다음 후보를 탐색합니다. LLM 미연결·운영 모델 미반영이며 성능 향상은 검증 전입니다.'
            if data['status'] in ['research_budget_requires_review', 'interrupted_research_requires_review']:
                badge = 'Review Needed<br>연구 검토 필요'
    except FileNotFoundError:
        pass
    except (KeyError, ValueError, TypeError, OSError, OverflowError):
        badge, note, details = 'Review Needed<br>연구 상태 점검 필요', '연구 결과를 검증 완료로 표시하지 않습니다.', ''
    return f'''<div class="card" id="algorithm-research-state">
      <div class="label">Algorithm Research</div><div class="ko-desc">알고리즘 연구</div>
      <span class="status-pill badge-orange">{badge}</span>
      {details}<div class="muted-helper">{note}</div>
    </div>'''
