# Social Attention Feature Report - 2026-11-23

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **81**
- High attention rows: **5**
- Medium attention rows: **45**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **33**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 307870 | 비투엔 | convertible_bond | 12.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 307870 | 비투엔 | convertible_bond | 12.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 307870 | 비투엔 | convertible_bond | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 307870 | 비투엔 | convertible_bond | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 282720 | 금양그린파워 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 033310 | 엠투엔 | major_shareholder_change | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 294870 | IPARK현대산업개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 054930 | 유신 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 440110 | 파두 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 025950 | 동신건설 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 212710 | 아이에스티이 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 000950 | 전방 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012280 | 영화금속 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012630 | HDC | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013700 | 까뮤이앤씨 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012170 | 아센디오 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 064290 | 인텍플러스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 053610 | 프로텍 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 032350 | 롯데관광개발 | major_shareholder_change | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 046120 | 오르비텍 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
