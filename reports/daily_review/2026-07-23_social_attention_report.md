# Social Attention Feature Report - 2026-07-23

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **13**
- High attention rows: **0**
- Medium attention rows: **7**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **6**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 348340 | 뉴로메카 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 348340 | 뉴로메카 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 348340 | 뉴로메카 | bonus_issue | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 348340 | 뉴로메카 | bonus_issue | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 191410 | 육일씨엔에쓰 | merger | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 176750 | 듀켐바이오 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 397030 | 에이프릴바이오 | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 340570 | 티앤엘 | bonus_issue | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 340570 | 티앤엘 | bonus_issue | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 183490 | 엔지켐생명과학 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 006490 | 프리티 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 340570 | 티앤엘 | bonus_issue | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 340570 | 티앤엘 | bonus_issue | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
