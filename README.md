# Overnight Alpha Lab

Overnight Alpha Lab is a Python-based research and portfolio project that analyzes Korean stock disclosure events, news signals, price reactions, market-adjusted returns, trading volume reactions, and model performance history.

The goal of this project is to build a local daily event-driven stock analysis pipeline that can collect public data, evaluate event reactions, generate structured reports, and track model readiness over time.

This project is for research, education, and portfolio demonstration purposes only. It is not financial advice and does not provide buy or sell recommendations.

---

## 1. Project Goal

Overnight Alpha Lab explores the following question:

Can public disclosure events, news signals, market-adjusted returns, and trading volume reactions be combined into a structured daily stock analysis pipeline?

The system is designed to:

- collect public disclosure events
- classify disclosure event types
- apply rule-based event scoring
- collect related news metadata
- evaluate next-trading-day price reactions
- compare stock movement against market movement
- measure trading volume reactions
- generate daily candidate reports
- generate single-stock analysis reports
- create prediction review notes
- build machine learning datasets
- monitor performance history over time
- document the project as a portfolio

---

## 2. Current MVP Status

Current stage: Day 30 Final MVP Cleanup

The MVP now includes:

- DART disclosure collection
- disclosure event parsing
- rule-based event scoring
- Naver news feature generation
- stock price reaction evaluation
- market index collection
- market-adjusted return calculation
- market-adjusted evaluation
- market-adjusted score integration
- trading volume feature generation
- trading volume score integration
- daily stock candidate reports
- volume and market-adjusted candidate report
- single-stock predictor
- advanced error-note generation
- machine learning dataset builder
- baseline model report
- return prediction report
- event-type performance report
- stock-specific pattern report
- model performance history report
- local automation scripts
- catch-up execution mode
- GitHub Pages development blog

---

## 3. Important Disclaimer

This project is not a trading system.

It is built for:

- research practice
- data pipeline design
- model evaluation practice
- portfolio demonstration
- event-driven financial data analysis experimentation

The outputs should not be interpreted as investment advice.

---

## 4. System Architecture

The current pipeline follows this structure:

Disclosure Data  
→ Event Parsing  
→ Event Scoring  
→ News Features  
→ Stock Price Reaction  
→ Market-Adjusted Features  
→ Market-Adjusted Evaluation  
→ Market-Adjusted Score  
→ Trading Volume Features  
→ Trading Volume Score  
→ Candidate Reports  
→ Performance History Report

The full catch-up pipeline currently runs 19 steps:

1. Daily Pipeline
2. Pending Re-Evaluator
3. Market Index Collection
4. Market-Adjusted Features
5. Market-Adjusted Evaluation
6. Market-Adjusted Score Integration
7. Market-Adjusted Daily Candidate Report
8. Trading Volume Features
9. Trading Volume Score Integration
10. Volume + Market-Adjusted Daily Candidate Report
11. Model Performance History Report
12. Automation Status Report
13. Automation History
14. Confidence Report
15. Return Prediction Report
16. Daily Stock Candidate Report
17. Event-Type Performance Report
18. Stock-Specific Pattern Report
19. Completed

---

## 5. Main Components

### 5.1 DART Disclosure Collection

Collects Korean disclosure data using OpenDART.

Main file:

- src/crawler/dart_collector.py

Output:

- data/raw/dart_disclosures_YYYYMMDD.csv

### 5.2 Disclosure Event Parsing

Classifies disclosure titles into event types.

Main file:

- src/parser/dart_parser.py

Example event types:

- supply_contract
- paid_in_capital_increase
- bonus_issue
- convertible_bond
- bond_with_warrant
- major_shareholder_change
- earnings_guidance
- lawsuit
- disclosure_violation
- investment_decision
- merger
- spin_off
- other

### 5.3 Event Scoring

Applies rule-based scoring to key disclosure events.

Main file:

- src/features/event_scoring.py

The scoring system assigns:

- prediction_direction
- event_score
- confidence_level

### 5.4 News Feature Generation

Collects Naver news metadata and creates simple news features.

Main files:

- src/crawler/news_collector.py
- src/features/news_features.py

Generated features include:

- news_count
- positive_keyword_count
- negative_keyword_count
- news_sentiment_score
- news_attention_score
- top_news_titles

### 5.5 Price Reaction Evaluation

Collects stock price data and evaluates next-trading-day reactions.

Main files:

- src/crawler/price_collector.py
- src/evaluator/event_price_reaction.py

Output:

- data/predictions/event_price_reaction_STOCK.csv

### 5.6 Error Note Generator

Generates structured review notes for prediction results.

Main file:

- src/evaluator/error_note_generator.py

Generated fields include:

- prediction_result
- error_category
- detailed_error_reason
- learning_point
- next_rule_adjustment
- confidence_adjustment

### 5.7 Machine Learning Dataset Builder

Combines event, news, price reaction, and error-note data.

Main file:

- src/features/ml_dataset_builder.py

Output:

- data/processed/ml_dataset_YYYYMMDD.csv

---

## 6. Market-Adjusted Layer

### 6.1 Market Index Collection

Collects KOSPI and KOSDAQ market reference data.

Main file:

- src/crawler/market_index_collector.py

If direct index collection fails, ETF proxy data is used.

Outputs:

- data/raw/market_index_YYYYMMDD.csv
- data/raw/stock_market_lookup_YYYYMMDD.csv

### 6.2 Market-Adjusted Features

Calculates stock returns relative to market returns.

Main file:

- src/features/market_adjusted_features.py

Core idea:

market-adjusted return = stock return - market return

Output:

- data/processed/market_adjusted_features_YYYYMMDD.csv

### 6.3 Market-Adjusted Evaluation

Evaluates whether a stock truly outperformed the market.

Main file:

- src/evaluator/market_adjusted_evaluator.py

Output:

- reports/daily_review/YYYY-MM-DD_market_adjusted_evaluation_report.md

Example result categories:

- market_adjusted_success
- market_driven_weak_success
- relative_success_but_absolute_loss
- market_adjusted_failure
- relative_failure_despite_absolute_gain
- market_adjusted_volatility_success
- market_driven_volatility
- volatility_overestimated
- pending

### 6.4 Market-Adjusted Score Integration

Converts market-adjusted evaluation into score adjustments.

Main file:

- src/models/market_adjusted_score_integrator.py

Output:

- reports/daily_review/YYYY-MM-DD_market_adjusted_score_report.md

---

## 7. Trading Volume Layer

### 7.1 Trading Volume Features

Measures event-day and next-day volume relative to historical volume.

Main file:

- src/features/trading_volume_features.py

Output:

- reports/daily_review/YYYY-MM-DD_trading_volume_feature_report.md

Generated labels:

- extreme_volume_spike
- strong_volume_spike
- moderate_volume_increase
- normal_or_weak_volume
- insufficient_volume_baseline
- price_file_missing

### 7.2 Trading Volume Score Integration

Converts volume reaction labels into score adjustments.

Main file:

- src/models/trading_volume_score_integrator.py

Output:

- reports/daily_review/YYYY-MM-DD_trading_volume_score_report.md

---

## 8. Candidate Reports

### 8.1 Daily Stock Candidate Report

Main daily candidate report.

Main file:

- src/models/daily_stock_recommender.py

Output:

- reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md

### 8.2 Market-Adjusted Daily Candidate Report

Candidate report using market-adjusted score adjustment.

Main file:

- src/models/market_adjusted_daily_recommender.py

Output:

- reports/daily_prediction/YYYY-MM-DD_market_adjusted_daily_candidates.md

### 8.3 Volume + Market-Adjusted Daily Candidate Report

Candidate report using both market-adjusted score and trading-volume score.

Main file:

- src/models/volume_market_adjusted_daily_recommender.py

Output:

- reports/daily_prediction/YYYY-MM-DD_volume_market_adjusted_daily_candidates.md

Current v3 score formula:

base recommendation score + market-adjusted score adjustment + trading-volume score adjustment = final score

---

## 9. Review and Monitoring Reports

The project generates multiple review reports:

- reports/daily_review/YYYY-MM-DD_automation_status_report.md
- reports/daily_review/YYYY-MM-DD_confidence_report.md
- reports/daily_review/YYYY-MM-DD_return_prediction_report.md
- reports/daily_review/YYYY-MM-DD_event_type_performance_report.md
- reports/daily_review/YYYY-MM-DD_stock_pattern_report.md
- reports/daily_review/YYYY-MM-DD_model_performance_history_report.md

The model performance history report summarizes:

- ML dataset rows
- error-note rows
- prediction success, failure, and pending counts
- market-adjusted result counts
- trading-volume adjustment counts
- event-type performance
- automation history

Main file:

- src/report_generator/model_performance_history_report.py

---

## 10. Single Stock Predictor

A focused report can be generated for one stock code.

Example:

python src/models/single_stock_predictor.py 005930

Output:

- reports/single_stock/YYYY-MM-DD_005930_single_stock_report.md

---

## 11. How to Run

Activate the environment:

cd ~/Desktop/overnight_alpha_lab  
source .venv/bin/activate

Run the full catch-up pipeline:

./scripts/run_catchup.sh

Check logs:

tail -n 800 logs/catchup_$(date +"%Y-%m-%d").log

---

## 12. Project Structure

Main folders:

- data/raw
- data/processed
- data/predictions
- docs/posts
- logs
- reports/daily_prediction
- reports/daily_review
- reports/single_stock
- scripts
- src/crawler
- src/evaluator
- src/features
- src/models
- src/parser
- src/pipeline
- src/report_generator

---

## 13. Development Log

The project was built incrementally from Day 1 to Day 30.

Recent milestones:

- Day 22: Market-Adjusted Return Features
- Day 23: Market-Adjusted Evaluation Logic
- Day 24: Market-Adjusted Score Integration
- Day 25: Market-Adjusted Daily Candidate Report
- Day 26: Trading Volume Feature Report
- Day 27: Trading Volume Score Integration
- Day 28: Volume + Market-Adjusted Daily Candidate Report
- Day 29: Model Performance History Report
- Day 30: Final MVP Cleanup

Detailed posts are available in the GitHub Pages blog under docs/posts.

---

## 14. Current Limitations

The current MVP still has limitations:

- limited historical sample size
- many pending rows due to next-trading-day data availability
- simple rule-based event scoring
- basic keyword-based news sentiment
- limited sector-level comparison
- limited trading volume coverage for some stocks
- no production web dashboard yet
- no live trading integration

These limitations are intentional at the MVP stage.

The project focuses on pipeline design, evaluation structure, and portfolio demonstration.

---

## 15. Future Work

Planned improvements include:

- sector-level return comparison
- more robust market classification
- expanded news sources
- SNS and investor attention indicators
- probability-based prediction output
- feature importance analysis
- dashboard prototype
- automated Git commit and blog generation
- more advanced machine learning models
- larger historical backtesting dataset

---

---

## 16. Phase 2 Updates: Dashboard and Auto-Learning Layer

After completing the first 30-day MVP, the project was extended with a lightweight web dashboard and an auto-learning rule layer.

### GitHub Actions Automation

The project now includes a GitHub Actions workflow that can run the full catch-up pipeline automatically.

The workflow can be triggered in two ways:

- scheduled weekday execution
- manual execution from the GitHub Actions tab

This allows the project to keep collecting data and updating reports even without running the pipeline manually on a local machine.

Main file:

- .github/workflows/daily-catchup.yml

### GitHub Pages Dashboard

A simple GitHub Pages dashboard was added to monitor the current system status.

Dashboard file:

- docs/dashboard.html

Dashboard generator:

- src/report_generator/dashboard_generator.py

The dashboard shows:

- system confidence status
- cumulative success rate
- evaluated cases
- pending cases
- latest ML dataset rows
- successful predictions
- failed predictions
- social attention signals
- rumor-noise signals
- risk-noise signals
- learned rule status
- quick stock lookup

The dashboard uses English metric names with short Korean sublabels so that both international and Korean readers can understand the system.

### Social Attention Feature Layer

A social attention feature layer was added to capture short-term investor attention and rumor-like noise signals from existing disclosure and news text.

Main file:

- src/features/social_attention_features.py

Generated outputs:

- data/processed/social_attention_features_YYYYMMDD.csv
- reports/daily_review/YYYY-MM-DD_social_attention_report.md

This layer does not treat rumors as facts. It only uses rumor-like language as a research feature for attention and noise detection.

Generated signals include:

- social attention score
- rumor noise score
- risk noise score
- high attention label
- rumor noise label
- risk noise label

### Auto Rule Updater

An auto rule updater was added to move the project from simple evaluation toward a learning rule system.

Main file:

- src/models/auto_rule_updater.py

Generated outputs:

- data/processed/learned_event_rules_YYYYMMDD.csv
- reports/daily_review/YYYY-MM-DD_auto_rule_update_report.md

The auto rule updater reads accumulated success and failure results and creates event-type score adjustment rules.

The original rule-based scoring file is not overwritten. Instead, learned rules are saved separately and can be safely added as an additional score layer.

The learning logic is conservative:

- if evaluated data is insufficient, the rule is held
- if historical success rate is high, the event type receives a positive adjustment
- if historical success rate is low, the event type receives a negative adjustment
- if historical performance is neutral, no adjustment is applied

This changes the project from:

```text
prediction → evaluation → error note

---

## 17. Conclusion

Overnight Alpha Lab is now a complete local MVP for event-driven stock analysis research.

It includes data collection, event parsing, rule-based scoring, news features, market-adjusted analysis, trading-volume analysis, candidate reports, performance monitoring, and portfolio documentation.

The project is not designed to provide investment advice.

It is designed to demonstrate how an event-driven financial data pipeline can be built, evaluated, and documented step by step.
