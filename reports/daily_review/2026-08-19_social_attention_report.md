# Social Attention Feature Report - 2026-08-19

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **23**
- High attention rows: **1**
- Medium attention rows: **13**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **14**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 389680 | 유디엠텍 | disclosure_violation | 18.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 043090 | 더테크놀로지 | spin_off | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 294870 | IPARK현대산업개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 277880 | 티에스아이 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012630 | HDC | supply_contract | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002020 | 코오롱 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028260 | 삼성물산 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 148250 | 알엔투테크놀로지 | disclosure_violation | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | convertible_bond | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 307870 | 비투엔 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 003070 | 코오롱글로벌 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033530 | SJG세종 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 352940 | 인바이오 | disclosure_violation | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226330 | 신테카바이오 | convertible_bond | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 020560 | 아시아나항공 | lawsuit | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 074610 | 이엔플러스 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 322780 | 코퍼스코리아 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 290270 | 휴네시온 | disclosure_violation | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 210120 | 캔버스엔 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
