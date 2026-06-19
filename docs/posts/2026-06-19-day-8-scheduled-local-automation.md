# Day 8: Scheduled Local Automation

## What I Built Today

Today, I added scheduled local automation to Overnight Alpha Lab.

The project already had shell scripts for running the daily pipeline and the pending event re-evaluation process.

Today, I registered those scripts with cron so they can run automatically at scheduled times on my local Mac.

## Why This Matters

A daily learning system needs consistency.

If the system depends only on manual execution, it is easy to forget to run the pipeline.

Scheduled automation helps the project move closer to a real operating system.

## Scheduled Jobs

The current schedule is:

```text
16:10 every day - Run daily pipeline
16:40 every day - Run pending event re-evaluation
```

The cron jobs execute:

```text
scripts/run_daily_pipeline.sh
scripts/run_pending_re_evaluator.sh
```

## Daily Pipeline Schedule

The daily pipeline runs after the Korean stock market closes.

It performs:

```text
DART disclosure collection
↓
Disclosure event parsing
↓
Key event selection
↓
Event scoring
↓
News metadata collection
↓
News feature generation
↓
Price data collection
↓
Event reaction evaluation
↓
Error-note generation
↓
ML dataset building
↓
Baseline model execution
```

## Pending Re-Evaluation Schedule

The pending re-evaluation job runs later.

It checks old pending events and attempts to convert them into success or failure cases when price data becomes available.

```text
Find pending rows
↓
Update price data
↓
Re-evaluate event reaction
↓
Regenerate error notes
↓
Rebuild ML dataset
↓
Re-run baseline model
```

## Log Files

Each scheduled job writes logs to the local `logs/` directory.

Example log files:

```text
logs/daily_pipeline_YYYY-MM-DD.log
logs/pending_re_evaluator_YYYY-MM-DD.log
```

The logs are useful for checking whether the automation ran successfully.

The `logs/` directory is excluded from GitHub because log files change every time the system runs.

## Important Limitation

This local automation depends on the Mac being turned on and connected to the internet.

If the Mac is turned off or asleep at the scheduled time, the cron job may not run.

This is acceptable for the current stage because the goal is to build and test the automation structure first.

## Why This Is Progress

The project now has a repeatable daily operating structure.

It can collect data, generate features, evaluate results, update pending cases, rebuild the ML dataset, and run the baseline model with much less manual work.

This is an important step toward a fully automated market event-reaction learning system.

## Next Step

The next step is to improve the automation layer.

Possible improvements include:

* checking whether scheduled jobs ran successfully
* creating a daily automation status report
* adding automatic Git commit and push
* adding automatic blog post generation
* moving from cron to macOS launchd
* eventually moving the workflow to GitHub Actions with GitHub Secrets

The current cron setup is the first scheduled automation layer for the project.

