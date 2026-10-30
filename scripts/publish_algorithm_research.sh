#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONDONTWRITEBYTECODE=1
PYTHON=.venv-ml/bin/python

regenerate() {
    "$PYTHON" -m src.report_generator.dashboard_generator
}

"$PYTHON" -c 'from src.research.memory import read_memory; read_memory("data/algorithm_research")'
regenerate
git add -- data/algorithm_research/event_*.json data/algorithm_research/head.json
git add reports/daily_review/algorithm_research_status.json reports/daily_review/algorithm_research_report.md
git add docs/dashboard.html docs/diagnostics.html
if git diff --cached --quiet; then exit 0; fi
git config user.name github-actions
git config user.email github-actions@github.com
git commit -m "Record offline algorithm research"

for attempt in 1 2 3; do
    git fetch origin main
    if ! GIT_EDITOR=true git rebase origin/main; then
        while [ -d "$(git rev-parse --git-path rebase-merge)" ] || [ -d "$(git rev-parse --git-path rebase-apply)" ]; do
            conflicts=$(git diff --name-only --diff-filter=U)
            if [ -z "$conflicts" ]; then exit 1; fi
            while IFS= read -r file; do
                case "$file" in
                    docs/dashboard.html|docs/diagnostics.html) ;;
                    *) echo "Research publication needs review: $file" >&2; exit 1 ;;
                esac
            done <<< "$conflicts"
            regenerate
            git add docs/dashboard.html docs/diagnostics.html
            GIT_EDITOR=true git rebase --continue || {
                if [ -z "$(git diff --name-only --diff-filter=U)" ]; then exit 1; fi
            }
        done
    fi
    regenerate
    git add docs/dashboard.html docs/diagnostics.html
    if ! git diff --cached --quiet; then git commit -m "Refresh research dashboard from latest data"; fi
    if git push origin HEAD:main; then exit 0; fi
done
echo "Research push failed; immutable experiment records are preserved in artifacts." >&2
exit 1
