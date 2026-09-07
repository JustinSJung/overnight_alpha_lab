# Social Attention Feature Report - 2026-09-07

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **89**
- High attention rows: **6**
- Medium attention rows: **35**
- Rumor-noise detected rows: **3**
- Risk-noise detected rows: **48**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 096770 | SK이노베이션 | merger | 17.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 294630 | 서남 | supply_contract | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 223310 | 사토시홀딩스 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 223310 | 사토시홀딩스 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 223310 | 사토시홀딩스 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 223310 | 사토시홀딩스 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 336260 | 두산퓨얼셀 | supply_contract | 11.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 226330 | 신테카바이오 | paid_in_capital_increase | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 036190 | 금화피에스시 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 376270 | HEM파마 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 302430 | 이노메트리 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 098070 | 한텍 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010130 | 고려아연 | lawsuit | 8.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 011090 | 에넥스 | investment_decision | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 011090 | 에넥스 | investment_decision | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 009410 | 태영건설 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 175250 | 아이큐어 | major_shareholder_change | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002020 | 코오롱 | supply_contract | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 131400 | 이브이첨단소재 | spin_off | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 0004V0 | 엔비알모션 | convertible_bond | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
