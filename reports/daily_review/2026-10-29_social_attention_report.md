# Social Attention Feature Report - 2026-10-29

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **119**
- High attention rows: **4**
- Medium attention rows: **45**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **52**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 061040 | 알에프텍 | merger | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 017000 | 신원종합개발 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 069920 | 엑시온그룹 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 036530 | SNT홀딩스 | major_shareholder_change | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 025000 | KPX케미칼 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 0088M0 | 메쥬 | merger | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 101000 | KS인더스트리 | paid_in_capital_increase | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 079940 | 가비아 | major_shareholder_change | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 079940 | 가비아 | major_shareholder_change | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 097230 | HJ중공업 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 089030 | 테크윙 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 069540 | 빛과전자 | convertible_bond | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 299480 | 지앤이헬스케어 | disclosure_violation | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 102460 | 이연제약 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 060980 | HL홀딩스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 389470 | 인벤티지랩 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 308170 | 씨티알모빌리티 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012330 | 현대모비스 | spin_off | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 340360 | 다보링크 | convertible_bond | 8.5 | 0 | 9 | medium_attention | no_rumor_signal | high_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
