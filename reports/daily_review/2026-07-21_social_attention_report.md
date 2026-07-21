# Social Attention Feature Report - 2026-07-21

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **17**
- High attention rows: **0**
- Medium attention rows: **8**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **10**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 011420 | 갤럭시아에스엠 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 066430 | 아이로보틱스 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 053580 | 웹케시 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000500 | 가온전선 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 397030 | 에이프릴바이오 | investment_decision | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 119850 | 지엔씨에너지 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 179530 | 애드바이오텍 | convertible_bond | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 008470 | 부스타 | bonus_issue | 6.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 276730 | 한울앤제주 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 066790 | 씨씨에스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 348950 | 제이알글로벌리츠 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 006220 | 제주은행 | disclosure_violation | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 106240 | 파인테크닉스 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 071950 | 코아스 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 159910 | 에코글로우 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 340810 | 시선AI | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 900120 | 씨엑스아이 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
