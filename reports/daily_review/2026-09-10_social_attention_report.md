# Social Attention Feature Report - 2026-09-10

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **98**
- High attention rows: **10**
- Medium attention rows: **49**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **49**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 224060 | 더코디 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 042660 | 한화오션 | investment_decision | 12.5 | 4 | 0 | high_attention | medium_rumor_noise | no_risk_noise |
| 368600 | 아이씨에이치 | spin_off | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 109740 | 디에스케이 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 200710 | 에이디테크놀로지 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000720 | 현대건설 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012630 | HDC | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 294870 | IPARK현대산업개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 282720 | 금양그린파워 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 137400 | 피엔티 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013700 | 까뮤이앤씨 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 047040 | 대우건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
