# Social Attention Feature Report - 2026-10-05

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **67**
- High attention rows: **3**
- Medium attention rows: **31**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **30**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 277880 | 티에스아이 | supply_contract | 17.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 068330 | 일신바이오 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 103590 | 일진전기 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 207940 | 삼성바이오로직스 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000210 | DL | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 375500 | DL이앤씨 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010140 | 삼성중공업 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 017000 | 신원종합개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 235980 | 메드팩토 | investment_decision | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 394280 | 오픈엣지테크놀로지 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 189330 | 씨이랩 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 215790 | 이노인스트루먼트 | spin_off | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 101000 | KS인더스트리 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 101000 | KS인더스트리 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 101000 | KS인더스트리 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 101000 | KS인더스트리 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 363280 | 티와이홀딩스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009410 | 태영건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006360 | GS건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 037330 | 인지디스플레 | spin_off | 8.5 | 0 | 9 | medium_attention | no_rumor_signal | high_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
