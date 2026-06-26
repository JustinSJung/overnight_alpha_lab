# Phase 2: Dashboard, Social Attention, and Auto Rule Updater

## What I Added

After completing the first 30-day MVP, I extended Overnight Alpha Lab with three important Phase 2 features.

These additions move the project from a local report-generation MVP toward an automated monitoring and learning system.

The new additions are:

- GitHub Actions automation
- GitHub Pages dashboard
- Social attention feature layer
- Auto rule updater

## Why This Matters

The first MVP could collect disclosure events, generate reports, evaluate price reactions, and build machine learning datasets.

However, it still needed a better way to monitor the system and a clearer learning mechanism.

Phase 2 improves the project in two directions.

First, the system can now be monitored through a web dashboard.

Second, the system can now generate learned event-rule adjustments from accumulated success and failure history.

This is an important step because simply recording success and failure is not enough.

A learning system should use those results to adjust future scoring logic.

## GitHub Actions Automation

I added a GitHub Actions workflow that can run the catch-up pipeline automatically.

Main file:

- .github/workflows/daily-catchup.yml

The workflow supports:

- scheduled execution
- manual execution from the GitHub Actions tab

This means the project can continue collecting data and generating reports without always running the pipeline manually from a local machine.

## GitHub Pages Dashboard

I added a dashboard page for monitoring the system.

Main files:

- docs/dashboard.html
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
- learned rule status
- quick stock lookup

The dashboard uses English labels with short Korean sublabels.

This makes the page easier to understand for both international readers and Korean readers.

## Social Attention Feature Layer

I also added a social attention feature layer.

Main file:

- src/features/social_attention_features.py

The goal is to capture investor attention, rumor-like noise, and risk-related text signals from existing disclosure and news data.

This layer does not treat rumors as facts.

Instead, it treats rumor-like language as a noise signal that may help explain short-term stock reactions.

Generated features include:

- social attention score
- rumor noise score
- risk noise score
- attention label
- rumor label
- risk label

This helps the project separate different possible causes of stock movement.

For example, a stock may move because of:

- the disclosure itself
- related news coverage
- retail investor attention
- rumor-like noise
- risk-related keywords
- trading volume reaction
- broader market movement

Adding this layer gives the model more context before changing any scoring rules.

## Auto Rule Updater

The most important Phase 2 addition is the auto rule updater.

Main file:

- src/models/auto_rule_updater.py

Generated outputs:

- data/processed/learned_event_rules_YYYYMMDD.csv
- reports/daily_review/YYYY-MM-DD_auto_rule_update_report.md

The auto rule updater reads accumulated prediction results and calculates event-type performance.

It then creates learned score adjustments.

For example:

- if an event type has a high success rate, its score can be increased
- if an event type has a low success rate, its score can be decreased
- if there is not enough evaluated data, the rule is held
- if performance is neutral, no adjustment is applied

The original event scoring rules are not overwritten.

Instead, learned adjustments are saved separately.

This makes the learning layer safer and easier to review.

## From Evaluation to Learning

Before this update, the project followed this structure:

```text
prediction
→ actual price reaction check
→ success / failure / pending
→ error note
→ ML dataset
