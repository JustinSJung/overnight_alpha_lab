# Social Attention Feature Report - 2026-11-20

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **79**
- High attention rows: **0**
- Medium attention rows: **44**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **40**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 016790 | 현대사료 | lawsuit | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 900290 | GRT | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 003680 | 한성기업 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 042660 | 한화오션 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 304840 | 타임X AI | paid_in_capital_increase | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 047040 | 대우건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 025890 | 한국주강 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 445090 | 에이직랜드 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 103590 | 일진전기 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 069730 | DSR제강 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 286750 | 나노실리칸첨단소재 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 115610 | 이미지스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 424870 | 이뮨온시아 | disclosure_violation | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 145720 | 덴티움 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 412540 | 제일엠앤에스 | convertible_bond | 7.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 066970 | 엘앤에프 | convertible_bond | 7.5 | 0 | 9 | medium_attention | no_rumor_signal | high_risk_noise |
| 067630 | HLB생명과학 | merger | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 067630 | HLB생명과학 | merger | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 028300 | HLB | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028260 | 삼성물산 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
