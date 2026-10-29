"""Internal-only presentation of already-computed nature-inspired research."""
from html import escape
import json
import math
from pathlib import Path

NAMES = {
    'last_mlp': 'Snapshot MLP / 하루 요약 신경망', 'gru': 'GRU / 일반 시계열 신경망',
    'cfc_dense': 'Dense CfC / 시간 적응 신경망', 'cfc_ncp': 'NCP CfC / 희소 신경회로',
    'extra_trees': 'Extra Trees / 트리 대조군', 'local_ncp': 'Local NCP / 개별 종목 신경회로',
    'peer_ncp_real': 'Peer NCP / 실제 연결 전달', 'peer_ncp_shuffled': 'Shuffled NCP / 무작위 연결 대조',
    'peer_gru_real': 'Peer GRU / 일반 신경망 전달',
}


def number(value, percent=False):
    try:
        value = float(value)
        if not math.isfinite(value):
            return 'N/A'
        return f'{value:.2%}' if percent else f'{value:.4f}'
    except (TypeError, ValueError):
        return 'N/A'


def render_nature_diagnostics(root):
    tables = []
    for suffix, heading in [('neural_circuit_research', 'Neural Circuit / 생체모방 신경회로'),
                            ('swarm_circuit_research', 'Peer Communication / 종목 간 정보 교환')]:
        paths = sorted((Path(root) / 'reports/daily_review').glob('*_' + suffix + '.json'))
        if not paths:
            continue
        try:
            path = paths[-1]
            if path.stat().st_size > 5_000_000:
                continue
            summary = json.loads(path.read_text())
            results = summary['results']['primary_development']
            rows = []
            for name, metrics in results.items():
                top = metrics['top20']
                rows.append('<tr><td>' + escape(NAMES.get(name, name)) + '</td><td>'
                            + str(int(metrics['input_candidates'])) + '</td><td>'
                            + str(int(metrics['evaluated_cases'])) + '</td><td>'
                            + number(metrics['mean_daily_auc']) + '</td><td>'
                            + number(metrics['date_brier']) + '</td><td>'
                            + number(top['conditional_date_success_rate'], True) + '</td></tr>')
            tables.append(f'<h3>{escape(heading)}</h3><div class="nature-table-wrap"><table class="nature-table">'
                          '<thead><tr><th>Model / 모델</th><th>Candidates / 후보</th><th>Evaluated / 평가</th>'
                          '<th>Daily AUC</th><th>Brier</th><th>Top20 success / 상위 20 성공률</th></tr></thead>'
                          '<tbody>' + ''.join(rows) + '</tbody></table></div>')
        except (OSError, ValueError, KeyError, TypeError):
            continue
    if not tables:
        return ''
    return '''<style>
      .nature-research { margin:0 0 28px; padding:20px 0; border-bottom:1px solid #dce3eb; }
      .nature-research h2 { margin:0 0 12px; font-size:22px; }
      .nature-research h3 { margin:22px 0 8px; font-size:17px; }
      .nature-research p { line-height:1.6; font-size:14px; }
      .nature-table-wrap { max-width:100%; overflow:auto; }
      .nature-table { min-width:780px; font-size:13px; }
      .nature-table th { text-align:left; padding:10px; border-bottom:1px solid #ccd5df; }
      .nature-table td:first-child { width:250px; color:inherit; }
      .nature-research .research-warning { color:#986000; font-weight:700; }
    </style><section class="nature-research" id="nature-research">
      <h2>Nature-Inspired Research / 자연모방 모델 연구</h2>
      <p class="research-warning">RESEARCH ONLY / 검증 전 실험입니다. 운영 추천 모델로 승격하지 않았습니다.</p>
      <p>각 실험의 주 과거 개발 기간에서 동일 후보군을 비교합니다. 이미 검토한 기간이며 독립적인 미래 검증이 아닙니다.
      Brier는 작을수록 좋습니다. 상위 20 성공률은 평가 가능한 결과의 날짜별 평균이며, 미확인 종목은 다른 종목으로 바꾸지 않았습니다.</p>
    ''' + ''.join(tables) + '''<p>이 표만으로 자연모방 구조의 우수성이나 미래 적중률을 확정할 수 없습니다.
      다른 모델과의 실제 사전 예측을 별도 기록하며, 높은 추정 확률을 검증된 신뢰도로 표시하지 않습니다.</p></section>'''
