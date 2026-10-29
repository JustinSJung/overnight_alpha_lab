"""Public goal progress, explicitly distinct from model accuracy or confidence."""
from datetime import datetime, timedelta, timezone
from html import escape
import json
import math
from pathlib import Path


def render_goal_progress(path, now=None):
    try:
        path = Path(path)
        if path.stat().st_size > 100_000:
            return ''
        data = json.loads(path.read_text())
        if data['schema'] != 'public_reliability_goal_v1' or data['recommendation_enabled'] is not False:
            return ''
        now = now or datetime.now(timezone(timedelta(hours=9)))
        generated = datetime.fromisoformat(data['generated_at'])
        day = datetime.strptime(data['price_date'], '%Y-%m-%d').date()
        if generated.tzinfo is None or generated > now + timedelta(minutes=5) or day > now.date():
            return ''
        for key in ['minimum_cases', 'minimum_dates', 'evaluated_cases', 'selected_signal_dates']:
            if type(data[key]) is not int or data[key] < 0:
                return ''
        if data['minimum_cases'] == 0 or data['minimum_dates'] == 0:
            return ''
        target, lower = float(data['target_success_rate']), float(data['target_lower'])
        if not (0 < target <= 1 and 0 < lower <= 1):
            return ''
        actual = data['actual_success_rate']
        if actual is not None and (not math.isfinite(float(actual)) or not 0 <= float(actual) <= 1):
            return ''
        measured = '미확정' if actual is None else f'{float(actual):.1%}'
        cases, days = data['evaluated_cases'], data['selected_signal_dates']
        case_goal, day_goal = data['minimum_cases'], data['minimum_dates']
        case_width, day_width = min(100, cases / case_goal * 100), min(100, days / day_goal * 100)
    except (OSError, ValueError, KeyError, TypeError, OverflowError):
        return ''
    return f'''<style>
      .ml-goal-progress {{ padding:18px 0; margin:18px 0; border-block:1px solid var(--line); }}
      .ml-goal-progress h3 {{ margin:0 0 10px; font-size:18px; overflow-wrap:anywhere; }}
      .ml-goal-values {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:20px; }}
      .ml-goal-values > div {{ min-width:0; }}
      .ml-goal-caption {{ font-size:12px; line-height:1.6; color:var(--muted); overflow-wrap:anywhere; }}
      .ml-goal-values strong {{ display:block; margin:6px 0; font-size:20px; }}
      .ml-goal-bar {{ height:5px; background:#e3eaf1; }}
      .ml-goal-bar span {{ display:block; height:100%; background:#697b8b; }}
      @media(max-width:620px) {{ .ml-goal-values {{ grid-template-columns:1fr; gap:14px; }} }}
    </style><section class="ml-goal-progress" id="ml-goal-progress">
      <h3>Reliability Goal / 학습 목표: 적중률 {target:.0%} 이상</h3>
      <div class="ml-goal-values">
        <div><span class="ml-goal-caption">Future Policy Evaluations / 새 목표의 실제 선택 후보 평가</span>
          <strong>{cases:,} / 최소 {case_goal:,}건</strong><div class="ml-goal-bar" role="progressbar" aria-label="평가 건수 진행률" aria-valuemin="0" aria-valuemax="{case_goal}" aria-valuenow="{min(cases, case_goal)}"><span style="width:{case_width:.1f}%"></span></div></div>
        <div><span class="ml-goal-caption">Evaluated Signal Days / 선택 신호일</span>
          <strong>{days:,} / 최소 {day_goal:,}일</strong><div class="ml-goal-bar" role="progressbar" aria-label="평가 신호일 진행률" aria-valuemin="0" aria-valuemax="{day_goal}" aria-valuenow="{min(days, day_goal)}"><span style="width:{day_width:.1f}%"></span></div></div>
        <div><span class="ml-goal-caption">Observed Success Rate / 실제 미래 성공률</span><strong>{escape(measured)}</strong>
          <span class="ml-goal-caption">통계 하한·손익·시장 대비 성과도 검증합니다.</span></div>
      </div><p class="ml-goal-caption">목표 등록 이후의 사전 예측만 집계합니다. 과거 성공률이나 모델 추정 확률과 별개이며, 표본 기준만 채웠다고 추천을 승인하지 않습니다. 기준일 {escape(data['price_date'])}.</p>
    </section>'''
