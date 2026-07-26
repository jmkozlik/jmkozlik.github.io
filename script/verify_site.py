#!/usr/bin/env python3
"""Verify public site source and generated output without extra dependencies."""

from __future__ import annotations

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
LOCAL_AUDIT = ROOT / "CONTENT_AUDIT.local.md"

PUBLIC_SUFFIXES = {".css", ".html", ".md", ".py", ".xml", ".yml", ".yaml"}
SKIP_PARTS = {".git", "_site", ".jekyll-cache", "vendor"}

REQUIRED_CONFIG = {
    "title": "Jonathan Kozlik",
    "description": "Jonathan Kozlik builds AI applications and tools for working with agents.",
    "author": "Jonathan Kozlik",
    "url": "https://jmkozlik.github.io",
    "email": "kozlikj18@gmail.com",
    "github_url": "https://github.com/jmkozlik",
    "linkedin_url": "https://www.linkedin.com/in/jkozlik/",
}

REQUIRED_HOMEPAGE_TEXT = (
    "Jonathan Kozlik",
    "I build AI applications and tools for working with agents.",
    "I’m studying computer science and applied mathematics at NJIT.",
    "I co-founded TrainSafe and currently work on enterprise AI applications",
    "at Southern Company.",
    "Lately, I’ve been interested in a narrower question: how do you tell",
    "whether adding agents and execution constraints actually makes a system",
    "more reliable?",
    "{{ site.email }}",
    "Selected work",
    "Constitutional Agent Stack",
    "A set of execution hooks, isolated workspaces, and review mechanisms",
    "for coding agents. I built it to explore what can be enforced by the",
    "environment instead of left entirely to prompts.",
    "Macrograd",
    "A matrix automatic-differentiation engine I wrote from scratch to",
    "better understand reverse-mode differentiation and gradient flow.",
    "MyCelium",
    "A federated-learning prototype built during HackMIT. I worked on the",
    "Modal compute workers and model aggregation path.",
    ">Code <span",
    "Now — July 2026",
    "I’m working toward a controlled comparison of prompt-only agent rules",
    "and mechanically enforced execution constraints.",
)

OBSOLETE_NOTEBOOK_CLASSES = (
    "hero",
    "eyebrow",
    "hero-brief",
    "rail-label",
    "status-line",
    "status-dot",
    "selected-work",
    "selected-item",
    "research-section",
    "question-list",
    "contact-section",
    "project-entry",
    "status-label",
    "project-facts",
    "contribution-fact",
    "next-evaluation",
)


def public_source_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == LOCAL_AUDIT:
            continue
        if any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() in PUBLIC_SUFFIXES:
            files.append(path)
    return files


def local_denylist() -> list[str]:
    if not LOCAL_AUDIT.exists():
        return []
    prefix = "- deny: "
    return [
        line.removeprefix(prefix).strip()
        for line in LOCAL_AUDIT.read_text(encoding="utf-8").splitlines()
        if line.startswith(prefix) and line.removeprefix(prefix).strip()
    ]


def find_forbidden(paths: list[Path]) -> list[str]:
    failures: list[str] = []
    denylist = local_denylist()
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        for index, phrase in enumerate(denylist, start=1):
            if phrase.casefold() in text.casefold():
                failures.append(
                    f"{path.relative_to(ROOT)} matches local denylist item {index}"
                )
    return failures


def config_value(text: str, key: str) -> str | None:
    match = re.search(
        rf"(?m)^{re.escape(key)}:\s*(?:\"([^\"]*)\"|'([^']*)'|([^\n#]*))\s*$",
        text,
    )
    if not match:
        return None
    return next((value for value in match.groups() if value is not None), "").strip()


def check_config() -> list[str]:
    failures: list[str] = []
    text = (ROOT / "_config.yml").read_text(encoding="utf-8")
    for key, expected in REQUIRED_CONFIG.items():
        actual = config_value(text, key)
        if actual != expected:
            failures.append(f"_config.yml {key!r}: expected {expected!r}, found {actual!r}")
    for key in ("resume_url", "openreview_url"):
        actual = config_value(text, key)
        if actual != "":
            failures.append(f"_config.yml {key!r} must remain empty, found {actual!r}")
    return failures


def check_local_audit() -> list[str]:
    failures: list[str] = []
    if not LOCAL_AUDIT.exists():
        failures.append("CONTENT_AUDIT.local.md is missing")
        return failures

    ignored = subprocess.run(
        ["git", "check-ignore", "--quiet", LOCAL_AUDIT.name],
        cwd=ROOT,
        check=False,
    )
    if ignored.returncode != 0:
        failures.append("CONTENT_AUDIT.local.md is not ignored by Git")

    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", LOCAL_AUDIT.name],
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if tracked.returncode == 0:
        failures.append("CONTENT_AUDIT.local.md is tracked by Git")

    history = subprocess.run(
        ["git", "log", "--all", "--format=%H", "--", LOCAL_AUDIT.name],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if history.stdout.strip():
        failures.append("CONTENT_AUDIT.local.md appears in Git history")
    return failures


def check_source_structure() -> list[str]:
    failures: list[str] = []
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    for phrase in REQUIRED_HOMEPAGE_TEXT:
        if phrase not in index:
            failures.append(f"index.html is missing required text: {phrase!r}")

    required_pages = {
        ROOT / "work.md": "permalink: /work/",
        ROOT / "writing.md": "permalink: /writing/",
        ROOT / "about.md": "permalink: /about/",
    }
    for path, marker in required_pages.items():
        if not path.exists():
            failures.append(f"{path.name} is missing")
        elif marker not in path.read_text(encoding="utf-8"):
            failures.append(f"{path.name} is missing {marker!r}")

    work_path = ROOT / "work.md"
    if work_path.exists():
        work_text = work_path.read_text(encoding="utf-8")
        work_markers = (
            "Experience",
            "Projects",
            "TrainSafe",
            "Southern Company",
            "Constitutional Agent Stack",
            "Macrograd",
            "MyCelium",
            "NANDA",
            "MakeProteins",
            "I designed and built the public implementation.",
            "My next step is to compare it",
            "against simpler baselines",
            "page.stack_artifact_src and page.stack_artifact_alt",
            '<figure class="project-artifact">',
        )
        for marker in work_markers:
            if marker not in work_text:
                failures.append(f"work.md is missing required content: {marker!r}")
        for heading in (
            "#### My work",
            "#### What exists publicly",
            "#### What remains unresolved",
        ):
            if heading in work_text:
                failures.append(f"work.md retains audit-like heading: {heading!r}")

    if (ROOT / "_posts" / "2026-07-14-welcome.md").exists():
        failures.append("placeholder welcome post still exists")

    layout = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
    layout_markers = (
        'rel="canonical"',
        'property="og:title"',
        'property="og:description"',
        'property="og:url"',
        'application/ld+json',
        "site.resume_url",
        "site.openreview_url",
        "'/work/' | relative_url",
        "'/writing/' | relative_url",
        "{% if site.posts.size > 0 %}",
        ">Notes</a>",
        "&copy; {{ site.time | date: '%Y' }} {{ site.author }}",
    )
    for marker in layout_markers:
        if marker not in layout:
            failures.append(f"default layout is missing {marker!r}")

    visual_sources = {
        ROOT / "index.html": index,
        ROOT / "work.md": work_path.read_text(encoding="utf-8") if work_path.exists() else "",
        ROOT / "assets" / "style.css": (ROOT / "assets" / "style.css").read_text(
            encoding="utf-8"
        ),
    }
    for path, text in visual_sources.items():
        for class_name in OBSOLETE_NOTEBOOK_CLASSES:
            if re.search(rf"(?<![a-z-]){re.escape(class_name)}(?![a-z-])", text):
                failures.append(
                    f"{path.relative_to(ROOT)} retains obsolete visual class "
                    f"{class_name!r}"
                )

    feed = (ROOT / "feed.xml").read_text(encoding="utf-8")
    feed_markers = ("<published>", "<summary type=\"html\">", "site.posts.first")
    for marker in feed_markers:
        if marker not in feed:
            failures.append(f"feed.xml is missing {marker!r}")

    post_script = (ROOT / "new-post.sh").read_text(encoding="utf-8")
    for marker in ("summary:", "repository:", "experiment:"):
        if marker not in post_script:
            failures.append(f"new-post.sh is missing front matter field {marker!r}")

    optional_field_checks = {
        ROOT / "_layouts" / "post.html": (
            "{% if page.summary and page.summary != empty %}",
            "{% if page.repository and page.repository != empty %}",
        ),
        ROOT / "writing.md": ("{% if post.summary and post.summary != empty %}",),
        ROOT / "feed.xml": ("{% if post.summary and post.summary != empty %}",),
    }
    for path, markers in optional_field_checks.items():
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"{path.relative_to(ROOT)} is missing {marker!r}")
    return failures


def generated_files() -> list[Path]:
    if not SITE.exists():
        return []
    return [
        path
        for path in SITE.rglob("*")
        if path.is_file() and path.suffix.lower() in {".css", ".html", ".xml"}
    ]


def resolve_internal_link(source: Path, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "tel:", "#")):
        return None
    clean = unquote(parsed.path)
    if not clean:
        return None
    if clean.startswith("/"):
        target = SITE / clean.lstrip("/")
    else:
        target = source.parent / clean
    if clean.endswith("/"):
        target = target / "index.html"
    elif not target.suffix:
        html_target = target.with_suffix(".html")
        directory_target = target / "index.html"
        if html_target.exists():
            target = html_target
        elif directory_target.exists():
            target = directory_target
    return target


def check_generated_output() -> list[str]:
    if not SITE.exists():
        return []

    failures = find_forbidden(generated_files())
    feed_path = SITE / "feed.xml"
    if feed_path.exists():
        try:
            ET.parse(feed_path)
        except ET.ParseError as error:
            failures.append(f"_site/feed.xml is not valid XML: {error}")
    for page in SITE.rglob("*.html"):
        text = page.read_text(encoding="utf-8", errors="replace")
        if 'rel="canonical"' not in text:
            failures.append(f"{page.relative_to(ROOT)} has no canonical URL")
        if 'property="og:title"' not in text:
            failures.append(f"{page.relative_to(ROOT)} has no Open Graph title")
        if 'application/ld+json' not in text:
            failures.append(f"{page.relative_to(ROOT)} has no Person JSON-LD")
        for href in re.findall(r'''href=["']([^"']+)["']''', text):
            target = resolve_internal_link(page, href)
            if target is not None and not target.exists():
                failures.append(
                    f"{page.relative_to(ROOT)} has broken internal link {href!r}"
                )
    return failures


def main() -> int:
    failures: list[str] = []
    failures.extend(find_forbidden(public_source_files()))
    failures.extend(check_config())
    failures.extend(check_local_audit())
    failures.extend(check_source_structure())
    failures.extend(check_generated_output())

    if failures:
        print(f"Site verification failed with {len(failures)} issue(s):")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Site verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
