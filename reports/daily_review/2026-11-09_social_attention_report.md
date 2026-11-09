# Social Attention Feature Report - 2026-11-09

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **94**
- High attention rows: **0**
- Medium attention rows: **37**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **46**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 002780 | 진흥기업 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 069540 | 빛과전자 | convertible_bond | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 091590 | 남화토건 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 317400 | 자이에스앤디 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 123010 | MSDI | paid_in_capital_increase | 9.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 033310 | 엠투엔 | major_shareholder_change | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 439580 | 블루엠텍 | convertible_bond | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 265560 | 영화테크 | supply_contract | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 418620 | E8 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 455180 | 케이지에이 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 383930 | 디티앤씨알오 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 255440 | 야스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 418420 | 라온텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 418420 | 라온텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 039980 | 폴라리스AI | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 039980 | 폴라리스AI | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 418420 | 라온텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 418420 | 라온텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028050 | 삼성E&A | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 064480 | 브리지텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
