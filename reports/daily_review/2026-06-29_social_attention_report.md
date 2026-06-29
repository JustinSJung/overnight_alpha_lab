# Social Attention Feature Report - 2026-06-29

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **12**
- High attention rows: **0**
- Medium attention rows: **0**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **4**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 300080 | 플리토 | supply_contract | 4.0 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 480370 | 씨케이솔루션 | supply_contract | 4.0 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 068790 | DMS | supply_contract | 4.0 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 445090 | 에이직랜드 | supply_contract | 4.0 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 300080 | 플리토 | supply_contract | 4.0 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 066790 | 씨씨에스 | major_shareholder_change | 2.0 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 000210 | DL | investment_decision | 2.0 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 375500 | DL이앤씨 | investment_decision | 2.0 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 322780 | 코퍼스코리아 | convertible_bond | 0.0 | 0 | 3 | no_attention_signal | no_rumor_signal | risk_noise_detected |
| 322780 | 코퍼스코리아 | paid_in_capital_increase | 0.0 | 0 | 3 | no_attention_signal | no_rumor_signal | risk_noise_detected |
| 001470 | 삼부토건 | paid_in_capital_increase | 0.0 | 0 | 3 | no_attention_signal | no_rumor_signal | risk_noise_detected |
| 011930 | 신성이엔지 | major_shareholder_change | 0.0 | 0 | 0 | no_attention_signal | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
