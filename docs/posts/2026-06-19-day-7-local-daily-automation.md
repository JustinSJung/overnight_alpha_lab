# Day 7: Local Daily Automation Scripts

## What I Built Today

Today, I added local automation scripts to Overnight Alpha Lab.

Until now, each part of the system had to be executed manually with Python commands.

Now, the main daily pipeline and the pending event re-evaluation process can be executed with simple shell scripts.

## Why This Matters

A daily learning system should be repeatable.

If the process requires too many manual commands, it becomes difficult to run consistently.

The purpose of this step was to make the workflow easier to execute and easier to review.

## New Scripts

I added two local automation scripts.

```text
scripts/run_daily_pipeline.sh
scripts/run_pending_re_evaluator.sh
```

The first script runs the full daily pipeline.

```text
./scripts/run_daily_pipeline.sh
```

The second script runs the pending event re-evaluation process.

```text
./scripts/run_pending_re_evaluator.sh
```

## Daily Pipeline Script

The daily pipeline script performs the following steps:

```text
Move to project root
↓
Activate the virtual environment
↓
Create a log directory
↓
Run the daily pipeline
↓
Save execution logs
```

This makes the pipeline easier to run from a single command.

## Pending Re-Evaluation Script

The pending re-evaluation script performs the following steps:

```text
Move to project root
↓
Activate the virtual environment
↓
Create a log directory
↓
Run pending event re-evaluation
↓
Save execution logs
```

This is useful because some events cannot be evaluated immediately.

When next trading day price data becomes available, old pending events can be checked again.

## Log System

The automation scripts also save logs.

Example log files:

```text
logs/daily_pipeline_YYYY-MM-DD.log
logs/pending_re_evaluator_YYYY-MM-DD.log
```

The logs make it easier to check whether the process completed successfully.

The `logs/` folder is excluded from GitHub because log files change every time the scripts run.

## Current Workflow

The workflow is now simpler.

```text
Run daily pipeline script
↓
Check daily log
↓
Run pending re-evaluation script
↓
Check pending re-evaluation log
↓
Commit useful reports and code changes
```

## Current System Status

The project now includes:

```text
DART disclosure collection
Disclosure event parsing
Key event selection
Rule-based event scoring
Naver news metadata collection
News feature generation
Stock price data collection
Event-price reaction evaluation
Prediction review and error-note generation
Machine learning dataset building
Baseline machine learning model
Pending event re-evaluation
Local automation scripts
Log file generation
```

## Why This Is Progress

This step moves the project closer to a real daily operating system.

The project is no longer just a set of Python files.

It now has an execution structure that can be run repeatedly.

This also prepares the project for future automation using cron, launchd, or GitHub Actions.

## Next Step

The next step is to register these scripts with a scheduler.

Possible future directions include:

* macOS launchd automation
* cron-based scheduling
* GitHub Actions automation
* automatic report generation
* automatic Git commit and push
* automatic daily blog post generation
* model performance tracking over time

The current local automation scripts are the foundation for that next step.

