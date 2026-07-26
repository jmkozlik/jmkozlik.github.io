# Quiet Notebook Copy Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development or superpowers:executing-plans.
> Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the existing quiet notebook sound conversational and personal
without changing its core visual system.

**Architecture:** Keep Jekyll, current templates, and CSS structure. Replace
page prose directly, add one front-matter-driven optional figure, and make
small spacing, rule, text-color, and footer adjustments.

**Tech Stack:** Jekyll/GitHub Pages, Liquid, HTML, CSS, Markdown, Python
standard-library verification.

## Global Constraints

- Keep the existing simplified visual implementation.
- Use the approved homepage copy verbatim.
- Keep Notes conditional on at least one real post.
- Keep Resume and OpenReview conditional.
- Do not publish an artifact placeholder.
- Preserve accessibility, metadata, Atom, responsive behavior, and dark mode.
- Do not commit or push.

### Task 1: Update copy verification

**Files:**
- Modify: `script/verify_site.py`
- Modify: `_config.yml`

- [ ] Replace the required homepage phrases with the approved headline,
  introduction, three project descriptions, “Code,” and July 2026 note.
- [ ] Reject the removed Work-page audit headings.
- [ ] Require conditional artifact rendering and no public placeholder.
- [ ] Run the verifier and confirm it fails against the old copy.

### Task 2: Revise homepage and footer

**Files:**
- Modify: `index.html`
- Modify: `_layouts/default.html`

- [ ] Insert the approved homepage copy and “Code” link labels.
- [ ] Keep conditional Notes and profile links.
- [ ] Replace repeated footer profile links with copyright and email.
- [ ] Run source verification.

### Task 3: Rewrite Work and About

**Files:**
- Modify: `work.md`
- Modify: `about.md`
- Modify: `CONTENT_AUDIT.local.md`

- [ ] Replace audit-like Work prose with the approved natural descriptions.
- [ ] Add a conditional `<figure>` beneath Constitutional Agent Stack that
  requires both `page.stack_artifact_src` and `page.stack_artifact_alt`.
- [ ] Add only the future real-artifact reminder to the ignored local audit.
- [ ] Replace About with the approved four-paragraph version.
- [ ] Run source verification.

### Task 4: Make restrained visual adjustments

**Files:**
- Modify: `assets/style.css`

- [ ] Reduce homepage introduction top padding.
- [ ] Use the primary text color for homepage introductory paragraphs.
- [ ] Remove the redundant rule above the project list and page section
  headings while retaining project-row rules.
- [ ] Style the optional figure without a card treatment.
- [ ] Style the one-line footer.

### Task 5: Verify

- [ ] Build with the GitHub Pages gem in Docker.
- [ ] Run `script/verify_site.py`, `bash -n new-post.sh`, and
  `git diff --check`.
- [ ] Check lints.
- [ ] Inspect desktop and 320px mobile layouts.
- [ ] Confirm no horizontal overflow.
- [ ] Confirm Notes, Resume, OpenReview, and empty artifact markup do not
  render.
- [ ] Do not commit or push.
