---
layout: default
title: Work
permalink: /work/
description: "Projects and professional work by Jonathan Kozlik."
---

<article class="page" markdown="1">

# Work

These are some of the projects I’ve spent the most time on. Most started
because I wanted to understand how something worked by building it.

## Experience

### TrainSafe

I co-founded [TrainSafe](https://trainsafe.ai/), where we’re building a
workspace for SaaS teams handling pricing, deal modeling, approvals, and
renewals.

### Southern Company

I currently work on enterprise AI applications at Southern Company.

## Projects

### [Constitutional Agent Stack](https://github.com/jmkozlik/constitutional-agent-stack)

Constitutional Agent Stack is an experiment in constraining coding agents
through their execution environment rather than prompts alone. It includes
isolated Git worktrees, contract checks, controlled agent spawning,
adversarial review, and append-only records.

I designed and built the public implementation. My next step is to compare it
against simpler baselines and measure whether the added machinery actually
improves reliability.

{% if page.stack_artifact_src and page.stack_artifact_alt %}
<figure class="project-artifact">
  <img src="{{ page.stack_artifact_src | relative_url }}" alt="{{ page.stack_artifact_alt }}">
  {% if page.stack_artifact_caption %}<figcaption>{{ page.stack_artifact_caption }}</figcaption>{% endif %}
</figure>
{% endif %}

[Code →](https://github.com/jmkozlik/constitutional-agent-stack)

### [Macrograd](https://github.com/jmkozlik/macrograd)

Macrograd is a matrix automatic-differentiation engine written in pure
Python. I built the matrix operations, broadcasting behavior, computation
graph, and reverse-mode differentiation because I wanted to understand what
machine-learning frameworks are doing underneath `backward()`.

I’d like to keep extending it as a small place to explore gradient flow and
training behavior.

[Code →](https://github.com/jmkozlik/macrograd)

### [MyCelium](https://github.com/jmkozlik/mycelium_1.0)

MyCelium was a federated-learning prototype my team built during HackMIT 2024.
I worked on the Modal-hosted TensorFlow workers and the path that aggregates
model weights across workers.

It was a hackathon project and stopped at the prototype stage.

[Code →](https://github.com/jmkozlik/mycelium_1.0) ·
[Team repository →](https://github.com/s11ngh/mycelium)

### NANDA-related client tracking

I explored client tracking and pseudonymous identifiers for a NANDA-related
TypeScript SDK through two upstream pull requests. The work remained
experimental and was not merged.

[Pull request →](https://github.com/aidecentralized/typescript-sdk/pull/2) ·
[Experimental fork →](https://github.com/jmkozlik/typescript-sdk)

### [MakeProteins](https://github.com/jmkozlik/makeproteins)

MakeProteins is a small codon language-model experiment over E. coli coding
sequences. I implemented the data parsing, codon tokenization, probability
model, and sequence sampling.

I’d like to add a basic evaluation before taking the experiment further.

[Code →](https://github.com/jmkozlik/makeproteins)

</article>
