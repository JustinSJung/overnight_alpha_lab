# Social Attention Feature Report - 2026-08-29

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **122**
- High attention rows: **6**
- Medium attention rows: **53**
- Rumor-noise detected rows: **3**
- Risk-noise detected rows: **65**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 088390 | 이녹스 | supply_contract | 16.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 389680 | 유디엠텍 | supply_contract | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 253590 | 네오셈 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 253590 | 네오셈 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 253590 | 네오셈 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 253590 | 네오셈 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 114190 | 강원에너지 | supply_contract | 11.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 227610 | 아우딘퓨쳐스 | major_shareholder_change | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 123010 | MSDI | convertible_bond | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 317400 | 자이에스앤디 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 317400 | 자이에스앤디 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 317400 | 자이에스앤디 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 317400 | 자이에스앤디 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033540 | 파라텍 | supply_contract | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226340 | 본느 | convertible_bond | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226340 | 본느 | convertible_bond | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226340 | 본느 | convertible_bond | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226340 | 본느 | convertible_bond | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 004440 | 삼일씨엔에스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003030 | 세아제강지주 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
