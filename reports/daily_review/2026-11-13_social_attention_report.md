# Social Attention Feature Report - 2026-11-13

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **108**
- High attention rows: **8**
- Medium attention rows: **32**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **46**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 211270 | AP위성 | supply_contract | 18.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 320000 | 한울반도체 | major_shareholder_change | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 114190 | 강원에너지 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 352910 | 오비고 | major_shareholder_change | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 091440 | 한울소재과학 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 109740 | 디에스케이 | major_shareholder_change | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 432720 | 퀄리타스반도체 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 275630 | 에스에스알 | merger | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 046940 | 우원개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 083640 | 인콘 | convertible_bond | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002990 | 금호건설 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 095610 | 테스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 301300 | 바이브컴퍼니 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 177830 | 파버나인 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002290 | 삼일기업공사 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 036190 | 금화피에스시 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 215090 | 솔디펜스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 123860 | 아나패스 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 091590 | 남화토건 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
