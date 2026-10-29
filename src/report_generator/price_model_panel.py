"""Dependency-light public UI for precomputed, absolute-return ML forecasts."""
from datetime import datetime, timedelta, timezone
from html import escape
import json
import math
from pathlib import Path


def load_public_forecast(path):
    try:
        path = Path(path)
        if path.stat().st_size > 10_000_000:
            return None
        data = json.loads(path.read_text(encoding='utf-8'))
        if (data['schema'] != 'public_price_forecast_v1' or data['model_state'] not in {'research', 'validated', 'stale'}
                or type(data['recommendation_enabled']) is not bool or not 1 <= data['horizon_sessions'] <= 20
                or not 0 <= data['cost_assumption'] < 1 or not data['stocks']):
            return None
        price_date = datetime.strptime(data['price_date'], '%Y-%m-%d').date()
        target = data.get('prediction_target', 'signal_close')
        if target not in {'signal_close', 'next_open_to_fifth_close_v1'}:
            return None
        next_open = target == 'next_open_to_fifth_close_v1'
        if next_open and (data['horizon_sessions'] != 5 or data['cost_assumption'] != .003
                          or datetime.strptime(data['learned_labels_through'], '%Y-%m-%d').date() > price_date
                          or data['forward'].get('scope') != 'learning_system'
                          or data.get('prediction_origin') not in {'frozen_original', 'research_snapshot'}):
            return None
        now = datetime.now(timezone(timedelta(hours=9)))
        generated = datetime.fromisoformat(data['generated_at'])
        if generated.tzinfo is None or generated > now + timedelta(minutes=5) or price_date > now.date():
            return None
        stale = (now.date() - price_date).days > 7 or (now - generated).days > 7
        codes = set()
        for row in data['stocks']:
            code = row['stock_code']
            if not isinstance(code, str) or len(code) != 6 or not code.isascii() or not code.isalnum() or code in codes:
                return None
            codes.add(code)
            if (not isinstance(row['stock_name'], str) or not isinstance(row['aliases'], list)
                    or not all(isinstance(alias, str) for alias in row['aliases'])
                    or not math.isfinite(row['probability']) or not 0 <= row['probability'] <= 1
                    or (row['predicted_return'] is not None if next_open else not math.isfinite(row['predicted_return']))
                    or type(row['recommended']) is not bool
                    or type(row['stale']) is not bool):
                return None
            signal = datetime.strptime(row['signal_date'], '%Y-%m-%d').date()
            if signal > price_date:
                return None
            row['stale'] = row['stale'] or (now.date() - signal).days > 7 or stale
            row['recommended'] = row['recommended'] and not row['stale'] and row['signal_date'] == data['price_date']
        for key in ['recorded', 'resolved', 'pending', 'signal_dates', 'integrity_issues']:
            if type(data['forward'][key]) is not int or data['forward'][key] < 0:
                return None
        if next_open and (type(data['forward'].get('unavailable')) is not int
                          or data['forward']['unavailable'] < 0
                          or data['forward']['recorded'] != data['forward']['resolved'] + data['forward']['pending'] + data['forward']['unavailable']):
            return None
        performance = data.get('observed_performance')
        if performance is not None:
            counts = ['evaluated_cases', 'success_count', 'failure_count', 'signal_dates', 'selected_cases',
                      'selected_evaluated_cases', 'selected_pending_or_unavailable', 'selected_success_count',
                      'selected_failure_count', 'selected_signal_dates']
            if any(type(performance[key]) is not int or performance[key] < 0 for key in counts):
                return None
            if (performance['evaluated_cases'] != data['forward']['resolved']
                    or performance['success_count'] + performance['failure_count'] != performance['evaluated_cases']
                    or performance['selected_success_count'] + performance['selected_failure_count'] != performance['selected_evaluated_cases']
                    or performance['selected_evaluated_cases'] + performance['selected_pending_or_unavailable'] != performance['selected_cases']
                    or performance['selected_cases'] > data['forward']['recorded']
                    or performance['selected_evaluated_cases'] > performance['evaluated_cases']):
                return None
            for prefix in ['', 'selected_']:
                count = performance[prefix + 'evaluated_cases']
                rate = performance[prefix + 'success_rate']
                if (rate is not None if count == 0 else
                        rate is None or not math.isclose(float(rate), performance[prefix + 'success_count'] / count, abs_tol=1e-12)):
                    return None
        enabled = (not next_open and data['recommendation_enabled'] and data['model_state'] == 'validated'
                   and data['forward']['passed'] is True and data['forward']['resolved'] >= 200
                   and data['forward']['signal_dates'] >= 60 and data['forward']['integrity_issues'] == 0 and not stale)
        if not isinstance(data['recommendations'], list) or not isinstance(data['watchlist'], list):
            return None
        data['recommendation_enabled'] = bool(enabled)
        if data['model_state'] == 'validated' and not enabled:
            data['model_state'] = 'research'
        data['recommendations'] = [row['stock_code'] for row in data['stocks'] if row['recommended'] and enabled][:20]
        data['watchlist'] = [code for code in data['watchlist'] if code in codes]
        if stale:
            data['model_state'] = 'stale'
        return data
    except (OSError, ValueError, KeyError, TypeError, OverflowError, AttributeError):
        return None


def model_status(data):
    if not data:
        return 'NOT CONNECTED', '모델 연결 대기', 'badge-gray'
    if data['model_state'] == 'stale':
        return 'UPDATE NEEDED', '가격 갱신 필요', 'badge-orange'
    if data['recommendation_enabled']:
        return 'VALIDATED', '검증 기준 통과', 'badge-green'
    return 'BETA / UNDER VALIDATION', '검증 중 베타', 'badge-orange'


PANEL_CSS = """
    .ml-section, .ml-section * { letter-spacing: 0; }
    .ml-status-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; }
    .ml-status-grid > .card { min-width:0; }
    .ml-status-grid .label { overflow-wrap:anywhere; letter-spacing:0; }
    .ml-observed { margin-top:20px; padding:18px 0; border-block:1px solid var(--line); }
    .ml-observed-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:18px; }
    .ml-observed-grid > div { min-width:0; }
    .ml-observed strong { display:block; font-size:24px; margin:8px 0; overflow-wrap:anywhere; }
    .ml-section h3 { margin:0 0 12px; font-size:18px; }
    .ml-section .ko-desc { word-break:keep-all; }
    .ml-query { margin-top:24px; padding-top:22px; border-top:1px solid var(--line); }
    .ml-form { display:flex; flex-wrap:wrap; gap:10px; margin:12px 0; }
    .ml-form input { flex:1 1 240px; min-width:0; padding:12px; border:1px solid #b8c7d4; border-radius:6px; font:inherit; background:white; }
    .ml-form button { padding:12px 20px; border:0; border-radius:6px; background:#176b55; color:white; font:inherit; font-weight:700; cursor:pointer; }
    .ml-form :focus-visible, .ml-stock-button:focus-visible { outline:3px solid #319381; outline-offset:3px; }
    .ml-result { padding:18px 0; border-block:1px solid var(--line); }
    .ml-result-values { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:18px; margin:14px 0; }
    .ml-result-values dt { font-size:12px; color:var(--muted); margin-bottom:8px; }
    .ml-result-values dd { margin:0; font-size:24px; font-weight:750; overflow-wrap:anywhere; }
    .ml-result-values dd.ml-result-decision { font-size:18px; }
    .ml-caption { font-size:13px; color:var(--muted); line-height:1.6; overflow-wrap:anywhere; }
    .ml-error { color:#a12a3a; font-size:14px; }
    .ml-lists { margin-top:24px; }
    .ml-watchlist { margin-top:22px; }
    .ml-watchlist summary { cursor:pointer; font-weight:700; padding:14px 0; }
    .ml-table-wrap { overflow:auto; }
    .ml-table { width:100%; border-collapse:collapse; font-size:14px; }
    .ml-table th { text-align:left; font-size:12px; color:var(--muted); font-weight:600; }
    .ml-table td, .ml-table th { padding:12px 8px; border-bottom:1px solid var(--line); }
    .ml-table td:first-child { width:auto; color:var(--ink); }
    .ml-stock-button { padding:0; border:0; background:none; color:#176b55; font:inherit; text-decoration:underline; cursor:pointer; text-align:left; overflow-wrap:anywhere; }
    .ml-table .ml-numeric { white-space:nowrap; text-align:right; font-variant-numeric:tabular-nums; }
    @media(max-width:920px) { .ml-status-grid { grid-template-columns:repeat(2,minmax(0,1fr)); } }
    @media(max-width:620px) { .ml-result-values, .ml-observed-grid { grid-template-columns:1fr; } .ml-status-grid { grid-template-columns:1fr 1fr; } .ml-table { font-size:12px; } }
    @media(max-width:360px) { .ml-status-grid { grid-template-columns:1fr; } }
"""


def render_observed_performance(data):
    m = data.get('observed_performance')
    if not m:
        return ''
    all_rate = '미확정' if m['success_rate'] is None else f'{m["success_rate"]:.1%}'
    selected_rate = '미확정' if m['selected_success_rate'] is None else f'{m["selected_success_rate"]:.1%}'
    return f'''<section class="ml-observed" id="ml-observed-performance">
      <h3>Recorded Forecast Results <span class="heading-ko">사전 예측 실제 결과</span></h3>
      <div class="ml-observed-grid">
        <div><span class="ml-caption">All Forecasts / 전체 사전 예측 성공률</span><strong>{all_rate}</strong>
          <span class="ml-caption">평가 {m['evaluated_cases']:,}건 · 성공 {m['success_count']:,}건 · 실패 {m['failure_count']:,}건</span></div>
        <div><span class="ml-caption">Selected Candidates / 고정 기준 선택 후보 성공률</span><strong>{selected_rate}</strong>
          <span class="ml-caption">평가 {m['selected_evaluated_cases']:,}건 · 미확인 {m['selected_pending_or_unavailable']:,}건</span></div>
        <div><span class="ml-caption">Evaluated Signal Days / 평가된 신호일</span><strong>{m['signal_dates']:,}일</strong>
          <span class="ml-caption">선택 후보 평가 {m['selected_signal_dates']:,}일</span></div>
      </div><p class="ml-caption">결과가 확인된 사전 예측의 관측치이며, 표본이 작으면 크게 바뀔 수 있습니다. 선택 후보도 검증 전 관찰 대상입니다. 이 결과는 목표 등록 전 예측을 포함하며 위 목표 검증과 범위가 다릅니다. 미확인 결과를 성공·실패로 바꾸지 않습니다.</p>
    </section>'''


def render_model_panel(data):
    if not data:
        return '<section class="section ml-section"><h2>ML Forecasts <span class="heading-ko">학습 모델 예측</span></h2><p class="ml-caption">모델 예측 데이터가 아직 연결되지 않았습니다. 기존 가격 신호 평가 점수는 ML 예측 정확도가 아닙니다.</p></section>', ''
    en, ko, css = model_status(data)
    forward = data['forward']
    unavailable_note = f" · 확인 불가 {forward['unavailable']}건" if forward.get('unavailable', 0) else ''
    next_open = data.get('prediction_target') == 'next_open_to_fifth_close_v1'
    target_note = ('다음 거래일 시가 → 5번째 거래일 종가' if next_open else f"{data['horizon_sessions']}거래일 가격 예측")
    return_note = ('다음 날 진입 가격 기준의 연구용 확률이며, 수익률 점추정은 제공하지 않습니다.' if next_open
                   else '수익률은 종가 기준의 연구용 예측입니다.')
    learning_note = (f" · 학습 정답 기준일 {escape(data['learned_labels_through'])}" if next_open else '')
    recording_note = (('표시된 확률은 장 시작 전에 기록한 원본입니다. 재학습 후에도 과거 예측을 바꾸지 않습니다.'
                       if data.get('prediction_origin') == 'frozen_original' else
                       '현재 값은 사전 기록되지 않은 연구용 추정치이며 실제 미래 평가에 포함하지 않습니다.') if next_open else '')
    safe = {key: data[key] for key in ['price_date', 'generated_at', 'horizon_sessions', 'cost_assumption',
                                       'recommendation_enabled', 'recommendations', 'watchlist']}
    fields = ['stock_code', 'stock_name', 'aliases', 'signal_date', 'probability', 'predicted_return', 'stale', 'recommended']
    safe['stocks'] = [{key: row[key] for key in fields} for row in data['stocks']]
    safe['prediction_target'] = data.get('prediction_target', 'signal_close')
    encoded = json.dumps(safe, ensure_ascii=False, allow_nan=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    html = f'''
    <section class="section ml-section" id="ml-forecasts">
      <div class="section-heading"><h2>ML Forecasts <span class="heading-ko">학습 모델 예측</span></h2>
      <p class="section-subtitle">{target_note} · 예측 가능 {len(data['stocks'])}종목 · 저장된 완료 일봉 기준{learning_note}</p></div>
      <p class="ml-caption">{recording_note}</p>
      <div class="ml-status-grid">
        <div class="card"><div class="label">Model Status</div><div class="ko-desc">모델 검증 상태</div><span class="status-pill {css}" id="ml-panel-state">{escape(en)}<br>{escape(ko)}</span></div>
        <div class="card"><div class="label">Price Data As Of</div><div class="ko-desc">가격 기준일</div><strong>{escape(data['price_date'])}</strong><p class="ml-caption">실시간 현재가 아님</p></div>
        <div class="card"><div class="label">Future Evaluations</div><div class="ko-desc">{'학습 시스템의 실제 미래 평가' if next_open else '이 모델의 실제 미래 평가'}</div><div class="value">{forward['resolved']}</div><p class="ml-caption">완료 {forward['signal_dates']}개 신호일 · 대기 {forward['pending']}건{unavailable_note}</p></div>
        <div class="card"><div class="label">Recommendations</div><div class="ko-desc">추천 기준 통과 종목</div><div class="value" id="ml-recommendation-count">{len(data['recommendations'])}</div><p class="ml-caption">{'모델 검증 기준 통과' if data['recommendation_enabled'] else '성능 검증 전에는 추천 보류'}</p></div>
      </div>
      {render_observed_performance(data)}
      <div class="ml-query" id="ml-search">
        <h3>Stock Forecast <span class="heading-ko">종목별 예측</span></h3>
        <p class="ml-error" id="ml-runtime-warning" hidden>가격 갱신이 필요합니다. 아래 값은 오래된 가격으로 계산된 과거 예측입니다.</p>
        <form class="ml-form" id="ml-search-form"><input id="ml-stock-input" aria-label="종목명 또는 6자리 종목코드" placeholder="종목명 또는 6자리 종목코드" list="ml-stock-names" autocomplete="off" required><datalist id="ml-stock-names"></datalist><button type="submit">예측 조회</button></form>
        <p class="ml-error" id="ml-search-error" role="alert"></p>
        <div class="ml-result" id="ml-stock-result" hidden aria-live="polite"><h3 id="ml-result-name"></h3><p class="ml-caption" id="ml-result-date"></p>
          <dl class="ml-result-values"><div><dt>Probability / 비용 초과 상승 확률 추정</dt><dd id="ml-result-probability"></dd></div><div><dt>Return Estimate / 예상 종가 수익률</dt><dd id="ml-result-return"></dd></div><div><dt>Decision / 추천 판단</dt><dd class="ml-result-decision" id="ml-result-decision"></dd></div></dl>
          <p class="ml-caption" id="ml-result-note"></p>
        </div>
        <p class="ml-caption">확률은 학습 모델의 추정치이며 실제 적중률이나 보장된 신뢰도가 아닙니다. {return_note}</p>
      </div>
      <div class="ml-lists"><h3>Recommendations <span class="heading-ko">추천 종목</span></h3><p class="ml-caption" id="ml-recommendation-note"></p><div class="ml-table-wrap" id="ml-recommendations"></div></div>
      <details class="ml-watchlist"><summary>Research Watchlist / 검증 전 관찰 목록 · 추천 아님</summary><p class="ml-caption">모델 추정 확률 순으로 정렬한 참고 목록입니다. 매수 추천이나 검증된 우수 종목 목록이 아닙니다.</p><div class="ml-table-wrap" id="ml-watchlist"></div></details>
    </section>
    <script id="ml-public-data" type="application/json">{encoded}</script>'''
    return html, PANEL_SCRIPT


PANEL_SCRIPT = r'''
  <script>
  (() => {
    const data = JSON.parse(document.getElementById('ml-public-data').textContent);
    const byCode = new Map(data.stocks.map(row => [row.stock_code, row]));
    const input = document.getElementById('ml-stock-input');
    const percent = value => Number.isFinite(value) ? new Intl.NumberFormat('ko-KR', {style:'percent', maximumFractionDigits:1}).format(value) : '미제공';
    const today = new Intl.DateTimeFormat('en-CA', {timeZone:'Asia/Seoul', year:'numeric', month:'2-digit', day:'2-digit'}).format(new Date());
    const publicationStale = (Date.parse(today) - Date.parse(data.price_date)) / 86400000 > 7 || (Date.now() - Date.parse(data.generated_at)) / 86400000 > 7;
    const stale = row => row.stale || publicationStale || (Date.parse(today) - Date.parse(row.signal_date)) / 86400000 > 7;
    if (publicationStale) {
      data.recommendation_enabled = false;
      document.getElementById('ml-runtime-warning').hidden = false;
      document.getElementById('ml-recommendation-count').textContent = '0';
      ['ml-hero-state', 'ml-panel-state', 'ml-hero-badge'].forEach(id => { const node = document.getElementById(id); if (node) { node.textContent = '가격 갱신 필요'; node.classList.remove('badge-green'); if (id !== 'ml-hero-state') node.classList.add('badge-orange'); } });
    }
    const safeRecommendation = row => data.recommendation_enabled && row.recommended && !stale(row) && row.signal_date === data.price_date;
    const datalist = document.getElementById('ml-stock-names');
    data.stocks.forEach(row => { const option = document.createElement('option'); option.value = row.stock_name; option.label = row.stock_code; datalist.append(option); });
    function show(row) {
      document.getElementById('ml-search-error').textContent = '';
      document.getElementById('ml-result-name').textContent = row.stock_name + ' (' + row.stock_code + ')';
      document.getElementById('ml-result-date').textContent = '가격 기준일 ' + row.signal_date + ' · ' + (data.prediction_target === 'next_open_to_fifth_close_v1' ? '다음 거래일 시가 → 5번째 거래일 종가' : '향후 ' + data.horizon_sessions + '거래일');
      document.getElementById('ml-result-probability').textContent = percent(row.probability);
      document.getElementById('ml-result-return').textContent = percent(row.predicted_return);
      document.getElementById('ml-result-decision').textContent = stale(row) ? '가격 갱신 필요' : safeRecommendation(row) ? '관찰 추천' : '추천 보류';
      document.getElementById('ml-result-note').textContent = stale(row) ? '오래된 가격으로 계산된 과거 예측입니다. 현재 추천에 사용할 수 없습니다.' : '가정 비용 ' + percent(data.cost_assumption) + '를 초과해 상승할 확률입니다. ' + (safeRecommendation(row) ? '검증 기준과 개별 종목 조건을 통과했지만 수익은 보장되지 않습니다.' : '모델 검증 또는 개별 종목 기준을 충족하지 못했습니다.');
      document.getElementById('ml-stock-result').hidden = false;
    }
    document.getElementById('ml-search-form').addEventListener('submit', event => {
      event.preventDefault();
      const query = input.value.trim().normalize('NFC').toLocaleLowerCase();
      const matches = query ? data.stocks.filter(row => row.stock_code.toLowerCase() === query || row.stock_name.normalize('NFC').toLocaleLowerCase() === query || row.aliases.some(name => name.normalize('NFC').toLocaleLowerCase() === query)) : [];
      if (matches.length !== 1) {
        document.getElementById('ml-stock-result').hidden = true;
        document.getElementById('ml-search-error').textContent = matches.length > 1 ? '같은 이름의 종목이 여러 개입니다. 6자리 종목코드로 조회해 주세요.' : '저장된 ML 예측에 해당 종목이 없습니다.';
        return;
      }
      show(matches[0]);
    });
    function table(target, codes, recommended) {
      const rows = codes.map(code => byCode.get(code)).filter(row => row && !stale(row) && (!recommended || safeRecommendation(row)));
      if (!rows.length) return 0;
      const table = document.createElement('table'); table.className = 'ml-table';
      const header = table.createTHead().insertRow();
      ['종목', '가격 기준일', '상승 확률 추정', '예상 수익률'].forEach((label, index) => { const th = document.createElement('th'); th.textContent = label; th.scope = 'col'; if (index > 1) th.className = 'ml-numeric'; header.append(th); });
      const body = table.createTBody();
      rows.forEach(row => { const tr = body.insertRow(); const cell = tr.insertCell(); const button = document.createElement('button'); button.className = 'ml-stock-button'; button.textContent = row.stock_name + ' (' + row.stock_code + ')'; button.addEventListener('click', () => { input.value = row.stock_code; show(row); document.getElementById('ml-search').scrollIntoView({block:'start',behavior:'smooth'}); }); cell.append(button);
        [row.signal_date, percent(row.probability), percent(row.predicted_return)].forEach((value, index) => { const td = tr.insertCell(); td.textContent = value; if (index > 0) td.className = 'ml-numeric'; }); });
      document.getElementById(target).append(table); return rows.length;
    }
    const recommended = table('ml-recommendations', data.recommendations, true);
    document.getElementById('ml-recommendation-note').textContent = recommended ? '검증 기준과 개별 종목 조건을 통과한 관찰 추천입니다. 수익 보장이나 자동 매매는 아닙니다.' : '현재 추천 기준을 충족한 종목이 없습니다. 검증되지 않은 관찰 목록을 추천으로 대체하지 않습니다.';
    if (!table('ml-watchlist', data.watchlist, false)) document.getElementById('ml-watchlist').textContent = '새로운 완료 일봉 예측이 필요합니다.';
  })();
  </script>'''
