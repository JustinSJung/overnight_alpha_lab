# Social Attention Feature Report - 2026-07-09

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **15**
- High attention rows: **0**
- Medium attention rows: **9**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **9**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 141080 | 리가켐바이오 | convertible_bond | 10.5 | 0 | 9 | medium_attention | no_rumor_signal | high_risk_noise |
| 302430 | 이노메트리 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009540 | HD한국조선해양 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 329180 | HD현대중공업 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002020 | 코오롱 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 900120 | 씨엑스아이 | paid_in_capital_increase | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 199290 | 바이오프로테크 | convertible_bond | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 012160 | 영흥 | major_shareholder_change | 6.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 210120 | 캔버스엔 | lawsuit | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 004710 | 한솔테크닉스 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 000760 | 이화산업 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 000760 | 이화산업 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 000760 | 이화산업 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 000760 | 이화산업 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
