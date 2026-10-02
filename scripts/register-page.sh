#!/usr/bin/env bash
# Usage: scripts/register-page.sh "Section Dir/filename.md"
# Ensures the file has GitBook width:wide frontmatter and is listed in SUMMARY.md.
set -euo pipefail

FILE="$1"
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"

if [[ ! -f "$FILE" ]]; then
  echo "register-page: file not found: $FILE" >&2
  exit 1
fi

# ── 1. Ensure width:wide frontmatter ─────────────────────────────────────────
first_line=$(head -1 "$FILE")
if [[ "$first_line" != "---" ]]; then
  printf -- '---\nlayout:\n  width: wide\n---\n\n' | cat - "$FILE" > /tmp/rp_tmp
  mv /tmp/rp_tmp "$FILE"
  echo "register-page: added frontmatter → $FILE"
fi

# ── 2. Extract H1 title ───────────────────────────────────────────────────────
TITLE=$(grep -m1 '^# ' "$FILE" | sed 's/^# //')
if [[ -z "$TITLE" ]]; then
  echo "register-page: no H1 title found in $FILE — add one before calling this script" >&2
  exit 1
fi

# ── 3. Check if already in SUMMARY.md ────────────────────────────────────────
ESCAPED=$(printf '%s' "$FILE" | sed 's/[[\.*^$(){}+?|]/\\&/g')
if grep -qF "$FILE" SUMMARY.md; then
  echo "register-page: already in SUMMARY.md — nothing to do"
  exit 0
fi

# ── 4. Find the section anchor (the README.md link for this directory) ────────
DIR=$(dirname "$FILE")
ANCHOR="<${DIR}/README.md>"

if ! grep -qF "$ANCHOR" SUMMARY.md; then
  echo "register-page: section anchor not found in SUMMARY.md: $ANCHOR" >&2
  echo "  Add a '* [Section Name]($ANCHOR)' line to SUMMARY.md first." >&2
  exit 1
fi

# ── 5. Find the last existing entry for this section and insert after it ──────
# We look for the last line that references a file inside $DIR, then append after.
LAST_LINE=$(grep -n "<${DIR}/" SUMMARY.md | tail -1 | cut -d: -f1)

NEW_ENTRY="  * [${TITLE}](<${FILE}>)"

# Use awk to insert the new entry after line $LAST_LINE
awk -v line="$LAST_LINE" -v entry="$NEW_ENTRY" '
  NR == line { print; print entry; next }
  { print }
' SUMMARY.md > /tmp/rp_summary && mv /tmp/rp_summary SUMMARY.md

echo "register-page: added to SUMMARY.md → [$TITLE](<$FILE>)"
