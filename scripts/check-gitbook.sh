#!/usr/bin/env bash
set -euo pipefail

repo_root=$(git rev-parse --show-toplevel)
cd "$repo_root"

failed=0

while IFS= read -r file; do
  [[ "$file" == "SUMMARY.md" ]] && continue

  if ! awk '
    NR == 1 && $0 != "---" { exit 1 }
    NR > 1 && $0 == "---" { exit found_wide ? 0 : 1 }
    NR > 1 && $0 ~ /^[[:space:]]*width:[[:space:]]*wide[[:space:]]*$/ { found_wide = 1 }
    END { if (NR == 0) exit 1 }
  ' "$file"; then
    printf 'Missing GitBook wide frontmatter: %s\n' "$file" >&2
    failed=1
  fi

  if ! rg -F "<$file>" SUMMARY.md >/dev/null && ! rg -F "($file)" SUMMARY.md >/dev/null; then
    printf 'Missing from SUMMARY.md: %s\n' "$file" >&2
    failed=1
  fi
done < <(rg --files -g '*.md' | sort)

if (( failed )); then
  exit 1
fi

printf 'GitBook check passed. All pages are wide and listed in SUMMARY.md.\n'
