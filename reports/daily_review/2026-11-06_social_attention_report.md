# Social Attention Feature Report - 2026-11-06

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **87**
- High attention rows: **2**
- Medium attention rows: **33**
- Rumor-noise detected rows: **9**
- Risk-noise detected rows: **55**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 123010 | MSDI | paid_in_capital_increase | 14.5 | 4 | 3 | high_attention | medium_rumor_noise | risk_noise_detected |
| 234300 | 에스트래픽 | merger | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 071200 | 인피니트헬스케어 | lawsuit | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 006360 | GS건설 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 008970 | KBI동양철관 | supply_contract | 10.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 003520 | 영진약품 | investment_decision | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 004800 | 효성 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 004800 | 효성 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 130660 | 한전산업 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 294870 | IPARK현대산업개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 018670 | SK가스 | merger | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 112610 | 씨에스윈드 | supply_contract | 7.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 035720 | 카카오 | merger | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 035720 | 카카오 | merger | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 323280 | 태성 | convertible_bond | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 099520 | DGI | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002780 | 진흥기업 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 012630 | HDC | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 297890 | HB솔루션 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
