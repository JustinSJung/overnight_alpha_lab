# Social Attention Feature Report - 2026-08-04

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **27**
- High attention rows: **0**
- Medium attention rows: **12**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **23**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 229640 | LS에코에너지 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 069640 | 한세엠케이 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 351320 | 넥사다이내믹스 | supply_contract | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 078590 | 휴림에이텍 | paid_in_capital_increase | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002990 | 금호건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 166090 | 하나머티리얼즈 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 109740 | 디에스케이 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 208640 | 썸에이지 | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 208640 | 썸에이지 | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 208640 | 썸에이지 | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 208640 | 썸에이지 | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 031860 | 디에이치엑스컴퍼니 | disclosure_violation | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 092040 | 아미코젠 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 348340 | 뉴로메카 | bonus_issue | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 011000 | 진원생명과학 | lawsuit | 3.5 | 0 | 9 | low_attention | no_rumor_signal | high_risk_noise |
| 011000 | 진원생명과학 | lawsuit | 3.5 | 0 | 9 | low_attention | no_rumor_signal | high_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
