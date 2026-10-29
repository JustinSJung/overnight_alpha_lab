"""Internal display of completed, unapproved recommendation-gate experiments."""
from html import escape
import json
import math
from pathlib import Path


def render_selective_diagnostics(root):
    paths = sorted((Path(root) / 'reports/daily_review').glob('*_selective_recommendation.json'))
    if not paths:
        return ''
    try:
        path = paths[-1]
        if path.stat().st_size > 5_000_000:
            return ''
        summary = json.loads(path.read_text())
        metrics = summary['results']['primary_development']
        names = {'monthly_base': 'Monthly base / 기존 예측',
                 'probability_only': 'Probability calibration / 확률 보정 대조군',
                 'learned_gate': 'Learned gate / 추천 판단 학습'}
        rows = []
        for key, name in names.items():
            m = metrics['selections']['top5_' + key]
            value = m['conditional_date_success_rate']
            rate = f'{float(value):.2%}' if value is not None and math.isfinite(float(value)) else 'N/A'
            rows.append(f'<tr><td>{escape(name)}</td><td>{int(m["selected_cases"])}</td>'
                        f'<td>{int(m["evaluated_cases"])}</td><td>{int(m["unresolved_cases"])}</td><td>{rate}</td></tr>')
        count = int(metrics['input_candidates'])
    except (OSError, ValueError, KeyError, TypeError):
        return ''
    return '''<style>
      .selective-research { padding:20px 0; margin-bottom:24px; border-bottom:1px solid #dce3eb; }
      .selective-research h2 { font-size:22px; margin:0 0 12px; overflow-wrap:anywhere; }
      .selective-research p { font-size:14px; line-height:1.6; }
      .selective-research .research-warning { color:#986000; font-weight:700; }
      .selective-table-wrap { overflow:auto; max-width:100%; }
      .selective-research table { min-width:700px; font-size:13px; }
      .selective-research th { text-align:left; padding:10px; border-bottom:1px solid #ccd5df; }
      .selective-research td:first-child { width:280px; color:inherit; }
    </style><section class="selective-research" id="selective-research">
      <h2>Recommendation Gate Research / 추천 판단 모델 연구</h2>
      <p class="research-warning">RESEARCH ONLY / 검증 전 실험입니다. 추천 기능을 활성화하지 않았습니다.</p>
      <p>같은 종목 전체를 분석하고 일별 5개씩 선택한 과거 개발 비교입니다. 추정 확률 자체를 실제 신뢰도로 표시하지 않습니다.
      아래 성공률은 결과가 확인된 선택 종목의 날짜별 평균이며, 미확인 결과가 있으면 완전한 전략 성과가 아닙니다.</p>
      <p>Primary development candidates / 주 개발 구간 전체 후보: ''' + str(count) + '''</p>
      <div class="selective-table-wrap"><table><thead><tr><th>Method / 방식</th><th>Selected / 선택</th>
      <th>Evaluated / 평가</th><th>Unknown / 미확인</th><th>Daily success / 일별 성공률</th></tr></thead><tbody>
    ''' + ''.join(rows) + '''</tbody></table></div>
      <p>단순 확률 보정으로도 얻는 효과와 추가 상황 학습의 효과를 나눠 비교합니다. 과거 개발 결과만으로 운영 승격하지 않으며,
      장 시작 뒤 어제 예측을 소급 생성하지 않습니다. 원본 기록 후 새 가격으로 별도 검증해야 합니다.</p></section>'''
