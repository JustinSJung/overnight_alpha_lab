# Social Attention Feature Report - 2026-11-02

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **174**
- High attention rows: **6**
- Medium attention rows: **104**
- Rumor-noise detected rows: **11**
- Risk-noise detected rows: **65**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 391710 | 코닉오토메이션 | merger | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 323350 | 다원넥스뷰 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 398120 | 에스지헬스케어 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 340360 | 다보링크 | supply_contract | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 348350 | 위드텍 | supply_contract | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 420770 | 기가비스 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 054220 | 비츠로시스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 054220 | 비츠로시스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 096240 | 크레버스 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 056730 | CNT85 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 056730 | CNT85 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 056730 | CNT85 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 056730 | CNT85 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 054930 | 유신 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 412350 | 레이저쎌 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 475150 | SK이터닉스 | supply_contract | 9.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 026910 | 광진실업 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 026910 | 광진실업 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 026910 | 광진실업 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
