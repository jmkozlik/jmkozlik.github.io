# jmkozlik.github.io

Jonathan Kozlik's personal site, built with Jekyll and deployed through GitHub
Pages at **https://jmkozlik.github.io/**.

## Routes

- `/` — introduction, selected work, current investigation, and recent notes
- `/work/` — experience and longer project descriptions
- `/writing/` — Jekyll notes archive
- `/about/` — biography and contact
- `/feed.xml` — Atom feed

Resume and OpenReview links render only when their URLs are configured. Both
are intentionally unset.

## Notes

Create `_posts/YYYY-MM-DD-a-short-slug.md` manually or run:

```bash
./new-post.sh "Post title"
```

Posts support these front matter fields:

```yaml
---
layout: post
title: "Post title"
date: 2026-07-26 12:00:00 -0400
summary: "A short description for listings and metadata."
tags: [agents, evaluation]
repository: "https://github.com/example/project"
experiment: "optional experiment identifier"
---
```

Markdown, fenced code, figures, tables, footnotes, and normal links are
handled by kramdown.

## Public content safety

`CONTENT_AUDIT.local.md` is an ignored local evidence ledger. Never force-add,
commit, publish, or copy it into a public page. The site should contain only
public-safe claims and links.

Do not add a resume until a revised, fact-checked PDF is ready. When it is:

1. Store it under `assets/files/`.
2. Set `resume_url` in `_config.yml`.
3. Add a `/resume/` route only if a separate route is still useful.

Set `openreview_url` only after confirming the exact profile URL.

## Local development

Use Ruby 3 or newer; the macOS system Ruby is too old for current GitHub Pages
dependencies.

```bash
bundle install
bundle exec jekyll serve
# http://localhost:4000
```

Build and run the repository/output checks with:

```bash
bundle exec jekyll build
python3 script/verify_site.py
```

## Structure

```
_config.yml                 identity, profile links, build settings
index.html                  homepage
work.md                     complete work and evidence page
writing.md                  post archive
about.md                    biography
_layouts/                   global and post templates
_posts/                     Markdown writing
assets/style.css            complete visual system
feed.xml                    Atom feed template
new-post.sh                 post scaffolding helper
script/verify_site.py       source and generated-output checks
```
