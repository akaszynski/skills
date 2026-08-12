---
name: write-like-alex
description: Rewrite emails, GitHub issues and comments, pull requests, commit messages, documentation, technical reports, papers, and presentations in Alex Kaszynski's established writing style. Use when the user asks for Alex's style, Alex's voice, wording that sounds like Alex, or a revision matching his tone, cadence, diction, and register while preserving every fact.
---

# Write Like Alex

Reproduce Alex's evidenced writing habits without copying errors, private
details, or source-specific wording. Keep the facts fixed. Change the voice.

## Required references

Read the references before editing:

- Read [`references/style-profile.md`](references/style-profile.md) for every
  task.
- Read [`references/examples.md`](references/examples.md) for the target
  register or when the draft does not sound right after one pass.
- Read [`references/corpus.md`](references/corpus.md) when updating this skill,
  explaining its evidence, or deciding whether a claimed habit is supported.

## Workflow

1. Identify the register: email, issue, PR, review comment, commit, docs, paper,
   report, or slides. Do not blend their cadences.
2. Lock facts, numbers, qualifiers, citations, links, code, and explicit asks.
3. Remove generic machine-written phrasing with `de-ai-ify` when available.
   Preserve the genuine Alex features listed below even if a general style
   audit marks them.
4. Rewrite from the result, current state, or decision. Add only the context
   needed to explain why.
5. Apply the target register from the style profile.
6. Compare the result with two or three examples from the matching section.
   Match the habits, not the subject matter or exact phrases.
7. Run the voice audit when a file is available:

   ```bash
   python3 scripts/audit_voice.py --mode pr path/to/body.md
   ```

8. Read the result once for cadence. Remove staged transitions, unnecessary
   summaries, and repeated conclusions.
9. Run the deterministic Unicode-dash check last when it is available.

## Core voice

- Lead with the result, problem, decision, or request.
- Prefer concrete verbs: add, fix, use, remove, update, implement, keep, move,
  compare, measure, and verify.
- Keep technical nouns stable. Do not cycle through synonyms.
- Put numbers next to the claim they support.
- Use short declarative sentences for decisions. Use a longer sentence only
  when it carries a real causal chain or technical qualification.
- Use contractions in conversational work. Papers and formal reports remain
  formal.
- Use first person when it clarifies ownership or judgment: "I think," "I'd
  prefer," "I'm unable to reproduce this," or "I will." Do not add false
  personal experience.
- Use "probably," "likely," and "I think" for genuine engineering judgment.
  Do not turn supported results into hedged opinions.
- State scope explicitly: "outside the scope of this PR," "not a blocker," or
  "leave this for a follow-up."
- Make requests direct and bounded. Name the file, test, behavior, or decision.
- Acknowledge useful work briefly, then address the substance.
- Favor simple implementations and public interfaces, but state the technical
  reason rather than calling an approach simple or clean without evidence.

## Register routing

### Email

Open with the purpose or current state. Use short paragraphs. State the request
and any deadline directly. Close after the action is clear. Use a greeting and
sign-off only when the existing thread or audience expects them.

### GitHub issue

Use a short verb-led or problem-led title. Start with the observed behavior or
desired feature. Include a reproducer or concrete example early. End with the
proposed direction, unresolved question, or acceptance condition.

### Pull request

Use a short verb-led title without a terminal period. Open with what changed
and which issue it resolves. Explain the cause or tradeoff in one or two short
paragraphs. Add code, screenshots, or measurements when they carry the review.
Do not add a generic validation section.

### Review or issue comment

Give the verdict first: fixed, reproducible, out of scope, non-blocking, or
still failing. Follow with the reason and a bounded request. A normal comment is
usually one to three short paragraphs.

### Commit

Use a concise imperative or plain action subject. Omit the terminal period.
Add a body only when the reason, compatibility effect, or non-obvious tradeoff
will matter later.

### Documentation

State what the object does, then show the shortest useful example. Explain the
constraint after the example. Use tables for option matrices. Keep terminology
literal and stable.

### Paper or formal report

Use the sequence context, constraint, method, result, and bounded conclusion.
Prefer measured statements over novelty claims. Keep uncertainty, assumptions,
and comparison conditions visible. Formal sentences may be longer than Alex's
GitHub prose, but each sentence should carry one logical step.

### Presentation

Put the result and number on the slide. Use terse factual bullets and sentence
fragments when they scan better. End status or decision slides with the next
action, limitation, or direct recommendation. Do not repeat the same result in
the title, first bullet, and conclusion.

## Preserve these authentic habits

Do not automatically remove the following when they are doing real work:

- "This PR" at the start of a PR body;
- "I think" for a recommendation rather than a measured fact;
- "Turns out" for a short diagnostic update;
- "For example" before an actual example;
- "just" when it narrows scope rather than minimizing effort;
- a real contrast between two live options;
- a brief "Thanks for ..." before a specific review comment.

These are frequent in the pre-2023 corpus. Repeating them mechanically is not.

## Guardrails

- Never invent facts, opinions, memories, relationships, measurements, or
  confidence.
- Never preserve source typos merely because they are authentic.
- Never expose private email text, customer identifiers, contact details,
  controlled information, or unpublished technical details.
- Do not copy a source example when the new artifact has different evidence.
- Do not turn every title into a slogan or every paragraph into a verdict.
- Do not force catchphrases. The voice comes from structure, diction, and
  cadence.
- Use ASCII punctuation in maintained text. Historical samples occasionally
  contain Unicode punctuation, but current house style controls the output.
- Follow repository-specific format and attribution rules.

## Output

Return the revised text. If the user asks for a review, also identify:

- the selected register;
- the main voice changes;
- any protected fact or qualification that constrained the rewrite;
- any sentence that remains ambiguous and needs the author's decision.
