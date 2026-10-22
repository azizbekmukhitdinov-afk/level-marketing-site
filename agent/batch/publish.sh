#!/bin/bash
# Emit batch articles, build, push, wait until GitHub Pages serves the given URL, then notify search engines.
set -e
cd "$(dirname "$0")/../.."
python3 agent/batch/emit.py
python3 build.py | tail -1
git add -A
git commit -qm "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q
for i in $(seq 1 40); do
  [ "$(curl -s -o /dev/null -w '%{http_code}' "$2")" = 200 ] && { echo "live: $2"; break; }
  sleep 10
done
python3 agent/indexnow.py
