# Social Attention Feature Report - 2026-09-22

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **113**
- High attention rows: **6**
- Medium attention rows: **42**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **60**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 123890 | 한국자산신탁 | lawsuit | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 123890 | 한국자산신탁 | lawsuit | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 123890 | 한국자산신탁 | lawsuit | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 123890 | 한국자산신탁 | lawsuit | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 068270 | 셀트리온 | investment_decision | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 054800 | 아이디스홀딩스 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 121600 | 나노신소재 | bond_with_warrant | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 121600 | 나노신소재 | bond_with_warrant | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 032820 | 우리기술 | supply_contract | 10.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 059090 | 미코 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 351320 | 넥사다이내믹스 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 121600 | 나노신소재 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 121600 | 나노신소재 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 204840 | 지엘팜텍 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 334970 | 프레스티지바이오로직스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010580 | 에스엠벡셀 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 105840 | 우진 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
