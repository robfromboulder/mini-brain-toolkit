#!/usr/bin/env bash
# Print a comparable snapshot of each directory named: its HEAD and `git status --porcelain` when it is a git repository,
# then a checksum over every file outside .git. Run it before and after an agent scenario, and diff the two outputs.
# usage: bash tests/MBT_SNAPSHOT.sh <dir>...
for d in "$@"; do
  echo "## $d"
  if git -C "$d" rev-parse --git-dir >/dev/null 2>&1; then
    echo "HEAD $(git -C "$d" rev-parse HEAD 2>/dev/null || echo none)"
    git -C "$d" status --porcelain
  fi
  echo "files $(cd "$d" && find . -path ./.git -prune -o -type f -print0 | LC_ALL=C sort -z | xargs -0 shasum | shasum | cut -d' ' -f1)"
done
