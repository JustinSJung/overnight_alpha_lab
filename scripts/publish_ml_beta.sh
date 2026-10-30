#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONDONTWRITEBYTECODE=1
PYTHON=.venv-ml/bin/python

regenerate() {
    "$PYTHON" -m src.report_generator.dashboard_generator
}

stage_outputs() {
    git add docs/dashboard.html docs/diagnostics.html docs/price_model.json docs/reliability_goal.json
    if [ -f docs/stock_lookup.json ]; then
        git add docs/stock_lookup.json
    fi
    git add -- 'data/predictions/ml_next_open_forward_[0-9]*.csv' 'data/predictions/ml_next_open_forward_[0-9]*.manifest.json'
    git add -- 'reports/daily_review/*_ml_beta_release*.json'
    if [ -f reports/daily_review/news_learning_status.json ]; then
        git add reports/daily_review/news_learning_status.json
    fi
    if [ -f reports/daily_review/model_improvement_status.json ]; then
        git add reports/daily_review/model_improvement_status.json
    fi
    if compgen -G 'data/model_improvement/originals/*.csv' > /dev/null; then
        "$PYTHON" -c 'from src.pipeline.model_improvement import load_protocol, read_trials; read_trials("data/model_improvement/originals", load_protocol()[0])'
        git add -- data/model_improvement/originals/*.csv data/model_improvement/originals/*.manifest.json
    fi
}

regenerate
stage_outputs
if git diff --cached --quiet; then
    echo "No beta publication changes."
    exit 0
fi
git config user.name github-actions
git config user.email github-actions@github.com
git commit -m "Update learning-model beta forecasts"

for attempt in 1 2 3; do
    git fetch origin main
    if ! GIT_EDITOR=true git rebase origin/main; then
        while [ -d "$(git rev-parse --git-path rebase-merge)" ] || [ -d "$(git rev-parse --git-path rebase-apply)" ]; do
            conflicts=$(git diff --name-only --diff-filter=U)
            if [ -z "$conflicts" ]; then
                echo "Rebase needs manual review; no source or original forecast was discarded." >&2
                exit 1
            fi
            while IFS= read -r file; do
                case "$file" in
                    docs/dashboard.html|docs/diagnostics.html) ;;
                    *) echo "Manual resolution required: $file" >&2; exit 1 ;;
                esac
            done <<< "$conflicts"
            regenerate
            git add docs/dashboard.html docs/diagnostics.html
            GIT_EDITOR=true git rebase --continue || {
                if [ -z "$(git diff --name-only --diff-filter=U)" ]; then exit 1; fi
            }
        done
    fi
    # Remote supplementary data may have advanced while the model was training.
    regenerate
    git add docs/dashboard.html docs/diagnostics.html
    if ! git diff --cached --quiet; then git commit -m "Refresh beta dashboard with latest supplementary data"; fi
    if git push origin HEAD:main; then exit 0; fi
done
echo "Push could not be completed. Original forecasts are retained in the run artifacts." >&2
exit 1
