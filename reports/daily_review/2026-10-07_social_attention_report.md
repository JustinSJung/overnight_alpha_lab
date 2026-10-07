# Social Attention Feature Report - 2026-10-07

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **98**
- High attention rows: **6**
- Medium attention rows: **43**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **59**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 002720 | 국제약품 | major_shareholder_change | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 002720 | 국제약품 | major_shareholder_change | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 002720 | 국제약품 | major_shareholder_change | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 002720 | 국제약품 | major_shareholder_change | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 069640 | 한세엠케이 | major_shareholder_change | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 372800 | 아이티아이즈 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 070300 | 퀀텀레일 | convertible_bond | 11.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 073570 | 리튬포어스 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 412350 | 레이저쎌 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 950250 | 테라뷰 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 005940 | NH투자증권 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013520 | 화승코퍼레이션 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 015590 | DKME | lawsuit | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 300080 | 플리토 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 373170 | 엠아이큐브솔루션 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003670 | 포스코퓨처엠 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 192410 | 오늘이엔엠 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 062040 | 산일전기 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 347700 | 스피어 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 027040 | 서울전자통신 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
