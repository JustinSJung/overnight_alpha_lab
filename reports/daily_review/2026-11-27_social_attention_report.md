# Social Attention Feature Report - 2026-11-27

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **91**
- High attention rows: **6**
- Medium attention rows: **48**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **45**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 295310 | 에이치브이엠 | supply_contract | 19.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 331920 | 셀레믹스 | major_shareholder_change | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 037350 | 성도이엔지 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 115180 | 큐리언트 | paid_in_capital_increase | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 462350 | 이노스페이스 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 000590 | CS홀딩스 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 092870 | 엑시콘 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 086390 | 유니테스트 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 277880 | 티에스아이 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 101360 | 에코앤드림 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 196170 | 알테오젠 | investment_decision | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 351320 | 넥사다이내믹스 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 066970 | 엘앤에프 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 066970 | 엘앤에프 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 066970 | 엘앤에프 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 066970 | 엘앤에프 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 069540 | 빛과전자 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
