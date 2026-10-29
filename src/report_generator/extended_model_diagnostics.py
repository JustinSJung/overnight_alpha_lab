"""Internal tables for prespecified ranking and frozen-feature experiments."""
from html import escape
import json
from pathlib import Path


def render_extended_diagnostics(root):
    parts = []
    specifications = [
        ('pairwise_price_research', 'Pairwise Ranking / 같은 날 종목 순위 학습', 'selections',
         [('pointwise_raw', 'Price classifier / 가격 분류 대조군'),
          ('pointwise_cross_section', 'Normalized classifier / 순위 입력 분류 대조군'),
          ('pairwise_cross_section', 'Pairwise ranker / 종목 쌍 순위 학습')]),
        ('foundation_price_transfer', 'Frozen Pattern Transfer / 사전학습 패턴 전이', 'top5',
         [('price_only', 'Price features / 가격 특징 대조군'),
          ('foundation_shuffled', 'Shuffled patterns / 섞은 패턴 대조군'),
          ('foundation_augmented', 'Frozen patterns / 사전학습 패턴 추가')]),
    ]
    for suffix, title, selection_key, names in specifications:
        paths = sorted((Path(root) / 'reports/daily_review').glob('*_' + suffix + '.json'))
        if not paths:
            continue
        try:
            if paths[-1].stat().st_size > 5_000_000:
                continue
            summary = json.loads(paths[-1].read_text())
            m = summary['results']['primary_development']
            rows = []
            for name, label in names:
                stats = m[selection_key][('top5_' + name) if selection_key == 'selections' else name]
                rate = stats['conditional_date_success_rate']
                value = 'N/A' if rate is None else f'{float(rate):.2%}'
                rows.append(f'<tr><td>{escape(label)}</td><td>{int(stats["selected_cases"])}</td><td>{int(stats["evaluated_cases"])}</td><td>{int(stats["unresolved_cases"])}</td><td>{value}</td></tr>')
            parts.append(f'<h3>{escape(title)}</h3><div class="extended-table-wrap"><table><thead><tr>'
                         '<th>Method / 방식</th><th>Selected / 선택</th><th>Evaluated / 평가</th><th>Unknown / 미확인</th>'
                         '<th>Daily success / 일별 성공률</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>')
        except (OSError, ValueError, KeyError, TypeError):
            continue
    if not parts:
        return ''
    return '''<style>
      .extended-research { padding:20px 0; border-bottom:1px solid #dce3eb; margin-bottom:24px; }
      .extended-research h2 { font-size:22px; margin:0 0 12px; overflow-wrap:anywhere; }
      .extended-research h3 { font-size:17px; margin:22px 0 8px; }
      .extended-research p { font-size:14px; line-height:1.6; }
      .extended-research .research-warning { color:#986000; font-weight:700; }
      .extended-table-wrap { max-width:100%; overflow:auto; }
      .extended-research table { min-width:740px; font-size:13px; }
      .extended-research th { text-align:left; padding:10px; border-bottom:1px solid #ccd5df; }
      .extended-research td:first-child { width:310px; color:inherit; }
    </style><section class="extended-research" id="extended-research"><h2>Additional Model Research / 추가 모델 연구</h2>
    <p class="research-warning">RESEARCH ONLY / 독립 미래 검증 전입니다. 운영 추천으로 승격하지 않았습니다.</p>
    <p>주 과거 개발 구간에서 모든 후보를 분석하고 일별 같은 5개를 고른 비교입니다. 성공률은 확인 가능한 선택 결과의 날짜별 평균이며,
    미확인 선택을 다른 종목으로 대체하지 않았습니다. 전체 기간의 수익이나 고신뢰도를 뜻하지 않습니다.</p>''' + ''.join(parts) + '''
    <p>기존에 여러 번 확인한 과거 자료입니다. 유리한 기간이나 소수 선택의 높은 성공률만 골라 목표 달성으로 처리하지 않습니다.</p></section>'''
