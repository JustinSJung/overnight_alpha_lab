# Social Attention Feature Report - 2026-07-09

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **30**
- High attention rows: **5**
- Medium attention rows: **10**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **21**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 276730 | 한울앤제주 | paid_in_capital_increase | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 276730 | 한울앤제주 | paid_in_capital_increase | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 276730 | 한울앤제주 | paid_in_capital_increase | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 276730 | 한울앤제주 | paid_in_capital_increase | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 025950 | 동신건설 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 058730 | 다스코 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 040910 | 아이씨디 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 465770 | STX그린로지스 | lawsuit | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 468530 | 프로티나 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 043260 | 성호전자 | major_shareholder_change | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | lawsuit | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 241840 | 에이스토리 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002020 | 코오롱 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 229000 | 젠큐릭스 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 296160 | 프로젠 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 109070 | 주성코퍼레이션 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 109070 | 주성코퍼레이션 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 109070 | 주성코퍼레이션 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 109070 | 주성코퍼레이션 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
