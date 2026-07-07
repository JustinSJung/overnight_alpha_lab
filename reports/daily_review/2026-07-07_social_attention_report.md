# Social Attention Feature Report - 2026-07-07

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **22**
- High attention rows: **2**
- Medium attention rows: **15**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **11**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 091590 | 남화토건 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 064400 | LG씨엔에스 | supply_contract | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 010960 | 삼호개발 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 263800 | 데이타솔루션 | supply_contract | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 263800 | 데이타솔루션 | supply_contract | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 263800 | 데이타솔루션 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 263800 | 데이타솔루션 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 011930 | 신성이엔지 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 216080 | 제테마 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 189330 | 씨이랩 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 189330 | 씨이랩 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 380540 | 옵티코어 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 189330 | 씨이랩 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 189330 | 씨이랩 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 023440 | 제이스코홀딩스 | major_shareholder_change | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 347700 | 스피어 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 008930 | 한미사이언스 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 288980 | 모아데이타 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 142760 | 모아라이프플러스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 066430 | 아이로보틱스 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
