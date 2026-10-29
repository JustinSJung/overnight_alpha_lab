#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."

# This job can only publish small immutable metadata batches, never models or credentials.
git add -- data/news_learning/*.jsonl data/news_learning/*.manifest.json
if git diff --cached --quiet; then exit 0; fi
git config user.name github-actions
git config user.email github-actions@github.com
git commit -m "Preserve point-in-time learning news metadata"
for attempt in 1 2 3; do
    git fetch origin main
    GIT_EDITOR=true git rebase origin/main
    if git push origin HEAD:main; then exit 0; fi
done
echo "News publication needs review; original batches remain in the workflow artifact." >&2
exit 1
