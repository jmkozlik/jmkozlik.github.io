#!/usr/bin/env bash
# Create a new blog post file, pre-filled with front matter.
# Usage:  ./new-post.sh "My Post Title"
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: ./new-post.sh \"Your Post Title\""
  exit 1
fi

title="$*"
date_prefix="$(date +%Y-%m-%d)"
datetime="$(date '+%Y-%m-%d %H:%M:%S %z')"

# slugify: lowercase, spaces->dashes, strip non-alphanumeric-dash
slug="$(echo "$title" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"

file="_posts/${date_prefix}-${slug}.md"

if [ -e "$file" ]; then
  echo "already exists: $file"
  exit 1
fi

cat > "$file" <<EOF
---
layout: post
title: "${title}"
date: ${datetime}
tags: []
---

Write here.
EOF

echo "created $file"
echo "when you're done:  git add -A && git commit -m \"post: ${title}\" && git push"
