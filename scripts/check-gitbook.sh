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

done < <(rg --files -g '*.md' | sort)

# SUMMARY.md is the curated GitBook navigation. Historical or superseded
# reports may remain in the repository without appearing in the sidebar.
while IFS= read -r line; do
  if [[ "$line" =~ \]\(\<([^\>]*)\>\) ]]; then
    target=${BASH_REMATCH[1]}
  elif [[ "$line" =~ \]\(([^\<][^\)]*)\) ]]; then
    target=${BASH_REMATCH[1]}
  else
    continue
  fi

  if [[ ! -f "$target" ]]; then
    printf 'Missing SUMMARY.md target: %s\n' "$target" >&2
    failed=1
  fi
done < SUMMARY.md

if (( failed )); then
  exit 1
fi

printf 'GitBook check passed. All pages have wide frontmatter and SUMMARY.md links resolve.\n'
