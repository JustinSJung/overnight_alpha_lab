# Social Attention Feature Report - 2026-11-05

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **66**
- High attention rows: **4**
- Medium attention rows: **28**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **31**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 277880 | 티에스아이 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 241690 | 유니테크노 | convertible_bond | 12.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 041960 | 코미팜 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 017000 | 신원종합개발 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 468530 | 프로티나 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 468530 | 프로티나 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 468530 | 프로티나 | convertible_bond | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 468530 | 프로티나 | convertible_bond | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 013360 | 일성건설 | disclosure_violation | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 143210 | 핸즈코퍼레이션 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 140410 | 메지온 | investment_decision | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 007610 | 선도전기 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 072770 | 멤레이비티 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 035890 | 서희건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 017510 | 세명전기 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 277410 | 인산가 | bond_with_warrant | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 003470 | 유안타증권 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010130 | 고려아연 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 326030 | 에스케이바이오팜 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 023350 | 한국종합기술 | supply_contract | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
