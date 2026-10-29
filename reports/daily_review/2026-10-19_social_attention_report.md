# Social Attention Feature Report - 2026-10-19

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **86**
- High attention rows: **0**
- Medium attention rows: **22**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **51**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 0203K0 | 송우인포텍 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 469480 | IBKS제24호스팩 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 498390 | 한화플러스제5호스팩 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 189330 | 씨이랩 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 047040 | 대우건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 246720 | 아스타 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013870 | 지엠비코리아 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 210980 | SK디앤디 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 290650 | 엘앤씨바이오 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 025560 | 미래산업 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028100 | 동아지질 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 004800 | 효성 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 089790 | 제이티 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 215090 | 솔디펜스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 475230 | 엔알비 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000640 | 동아제약 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 348350 | 위드텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 222420 | 쎄노텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 019660 | 글로본 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 007680 | 대원 | merger | 6.8 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
