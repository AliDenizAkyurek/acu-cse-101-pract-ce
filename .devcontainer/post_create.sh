#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "============================================="
echo "  Setting up ACU CSE 101 Environment..."
echo "============================================="

# Install with the same interpreter used by the editor. Fail visibly on errors.
bash "$ROOT/scripts/check_environment.sh" --packages

# Configure safe git defaults for students
git config --global pull.rebase false
git config --global core.autocrlf input

# Set execution permissions on scripts
chmod +x scripts/*.py 2>/dev/null || true

# Ensure student starts on the 'workspace' branch, keeping 'main' pristine
if git show-ref --verify --quiet refs/heads/workspace; then
    git checkout workspace
else
    git checkout -b workspace
fi

echo "✅ Course packages ready. Editor extensions will be checked when VS Code connects."
