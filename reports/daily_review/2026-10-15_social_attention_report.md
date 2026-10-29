# Social Attention Feature Report - 2026-10-15

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **79**
- High attention rows: **1**
- Medium attention rows: **25**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **53**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 199730 | 바이오인프라 | merger | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 000720 | 현대건설 | supply_contract | 11.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 299660 | 셀리드 | paid_in_capital_increase | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 065650 | 하이퍼코퍼레이션 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 017000 | 신원종합개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 452430 | 사피엔반도체 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 019210 | 와이지-원 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 078860 | 아이오케이이엔엠 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 005690 | 파미셀 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010400 | 우진아이엔에스 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 006740 | 블루산업개발 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 068270 | 셀트리온 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 293780 | 압타바이오 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 064350 | 현대로템 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 351320 | 넥사다이내믹스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 351320 | 넥사다이내믹스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
