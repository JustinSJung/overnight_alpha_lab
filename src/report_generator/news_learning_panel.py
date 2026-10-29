"""Small public status card; research details remain outside the main dashboard."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path


def render_news_learning_card(path, now=None):
    en, ko, color = 'Waiting for Data', '데이터 연결 대기', 'badge-gray'
    note = '뉴스 학습 상태가 아직 연결되지 않았습니다.'
    details = ''
    try:
        path = Path(path)
        if path.stat().st_size > 100_000:
            raise ValueError('Oversized news status.')
        data = json.loads(path.read_text(encoding='utf-8'))
        if data['recommendation_enabled'] is not False or data['production_model_changed'] is not False:
            raise ValueError('Unapproved news promotion cannot be displayed as validation.')
        generated = datetime.fromisoformat(data['generated_at'])
        now = now or datetime.now(timezone.utc)
        if generated.tzinfo is None or generated > now + timedelta(minutes=5):
            raise ValueError('Invalid news status timestamp.')
        if now - generated > timedelta(days=7):
            en, ko, color = 'Update Needed', '상태 갱신 필요', 'badge-orange'
            note = '최근 뉴스 학습 상태를 다시 확인해야 합니다. 현재 예측에는 미적용입니다.'
        elif data['status'] == 'news_comparison_unavailable':
            en, ko, color = 'Needs Review', '점검 필요', 'badge-orange'
            note = '뉴스 학습 경로를 점검 중입니다. 기존 가격 예측은 별도로 유지합니다.'
        else:
            days, rows = data['mature_news_dates'], data['mature_news_rows']
            if type(days) is not int or type(rows) is not int or not 0 <= days <= rows <= 100_000_000:
                raise ValueError('Invalid news sample counts.')
            if data['status'] == 'accumulating_point_in_time_news':
                en, ko, color = 'Building History', '학습용 이력 축적 중', 'badge-orange'
                note = '뉴스 이력을 모으는 중이며, 현재 가격 예측에는 아직 적용하지 않습니다.'
            elif data['status'] == 'matched_development_comparison':
                en, ko, color = 'Comparing Models', '예측 성능 비교 중', 'badge-orange'
                note = '같은 기간의 가격 모델과 비교 중이며, 현재 예측에는 아직 적용하지 않습니다.'
            else:
                raise ValueError('Unknown news learning state.')
            details = f'<div class="muted-helper">Outcome-ready days / 평가 가능한 날짜: {days:,}일</div>'
    except FileNotFoundError:
        pass
    except (OSError, ValueError, KeyError, TypeError, OverflowError):
        en, ko, color = 'Needs Review', '점검 필요', 'badge-orange'
        note = '뉴스 학습 상태를 확인 중입니다. 현재 가격 예측에는 미적용입니다.'
    return f'''<div class="card" id="news-learning-state">
      <div class="label">News Learning</div><div class="ko-desc">뉴스 기반 학습</div>
      <span class="status-pill {color}">{en}<br>{ko}</span>
      {details}<div class="muted-helper">{note}</div>
    </div>'''
