# Quiet Technical Notebook Copy Refinement

Date: 2026-07-26

## Objective

Keep the existing simplified visual implementation and make the writing sound
like Jonathan describing work he is curious about. Remove audit-report
language, repeated qualification, and résumé-like phrasing without weakening
material attribution boundaries.

Do not commit or push.

## Homepage

Keep the plain header, stacked projects, conditional Notes section, contact
links, and conditional Resume/OpenReview links.

Use this copy:

> I build AI applications and tools for working with agents.
>
> I’m studying computer science and applied mathematics at NJIT. I co-founded
> TrainSafe and currently work on enterprise AI applications at Southern
> Company.
>
> Lately, I’ve been interested in a narrower question: how do you tell whether
> adding agents and execution constraints actually makes a system more
> reliable?
>
> kozlikj18@gmail.com · GitHub · LinkedIn
>
> Selected work
>
> Constitutional Agent Stack
>
> A set of execution hooks, isolated workspaces, and review mechanisms for
> coding agents. I built it to explore what can be enforced by the environment
> instead of left entirely to prompts.
>
> Code →
>
> Macrograd
>
> A matrix automatic-differentiation engine I wrote from scratch to better
> understand reverse-mode differentiation and gradient flow.
>
> Code →
>
> MyCelium
>
> A federated-learning prototype built during HackMIT. I worked on the Modal
> compute workers and model aggregation path.
>
> Code →
>
> Now — July 2026
>
> I’m working toward a controlled comparison of prompt-only agent rules and
> mechanically enforced execution constraints.

Do not call this an established research program or completed experiment.

## Work

Use natural project prose rather than identical fact schemas. Each entry can
explain what the project is, Jonathan’s contribution, a natural next step, and
links.

Remove the headings “My work,” “What exists publicly,” and “What remains
unresolved.” Do not foreground test counts, stale fixtures, reproducibility
discrepancies, closed pull requests, or disclaimers.

Constitutional Agent Stack:

> Constitutional Agent Stack is an experiment in constraining coding agents
> through their execution environment rather than prompts alone. It includes
> isolated Git worktrees, contract checks, controlled agent spawning,
> adversarial review, and append-only records.
>
> I designed and built the public implementation. My next step is to compare
> it against simpler baselines and measure whether the added machinery
> actually improves reliability.

Macrograd should describe its pure-Python matrix operations, broadcasting,
computation graph, and reverse-mode differentiation as a way to understand
what frameworks do underneath `backward()`. Do not use test counts as
marketing.

MyCelium should identify it as a HackMIT 2024 team prototype, attribute the
Modal-hosted TensorFlow workers and model aggregation path to Jonathan, and
use one short prototype-stage note.

NANDA-related copy:

> I explored client tracking and pseudonymous identifiers for a NANDA-related
> TypeScript SDK through two upstream pull requests. The work remained
> experimental and was not merged.

MakeProteins should remain a small codon language-model experiment and state
Jonathan’s parsing, tokenization, probability-model, and sampling work in
plain language.

## About

Use four short paragraphs:

> I’m Jonathan, a computer science and applied mathematics student at NJIT. I
> co-founded TrainSafe and currently work on enterprise AI applications at
> Southern Company.
>
> Most of my interest in agents came from trying to build them. Once a system
> can call tools, change files, and delegate work, it becomes difficult to tell
> whether more orchestration is actually helping or just creating new ways to
> fail.
>
> I’m interested in evaluation, reliable tool use, execution constraints, and
> the practical problem of debugging long-running agent workflows. I’m
> currently building small systems and experiments that help me understand
> those problems more concretely.
>
> You can reach me at kozlikj18@gmail.com.

Do not list every project or repeat the complete homepage.

## Visual Adjustments

Preserve the current system font, off-white background, width, navigation,
stacked rows, blue links, dark mode, accessibility, and metadata.

Make only these adjustments:

- reduce homepage top spacing slightly
- use the main text color for the important introductory paragraphs
- remove redundant rules where headings already separate sections
- reduce the footer to a quiet email and copyright line

Do not add cards, badges, gradients, dots, animations, branding, or a new
design system.

## Optional Artifact

Support an optional real artifact beneath Constitutional Agent Stack using
conditional front matter. Render a semantic figure only when a real source
and alt text are present. Do not publish a placeholder.

The future artifact may be a real CLI screenshot, architecture diagram,
ledger excerpt, or code excerpt. Record the reminder only in the ignored
local audit note.

## Validation

- GitHub Pages build
- source and generated-output verification
- no public placeholder artifact
- Notes hidden while no posts exist
- Resume and OpenReview hidden while unset
- desktop and 320px mobile inspection
- no horizontal overflow
- no new linter errors
