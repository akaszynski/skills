---
name: de-ai-ify
description: Edit human-facing prose, reports, presentations, documentation, emails, pull requests, release notes, and other published text to remove formulaic machine-written patterns while preserving facts, technical precision, intent, and the author's voice. Use as the final editorial pass before rendering, committing, posting, or sending text.
---

# De-AI-ify

Make the text sound like a competent person wrote it for a specific reader and
purpose. Preserve the substance. Improve the writing.

This skill incorporates the pattern catalog and editing method from
`blader/humanizer` and aligns them with the local technical-writing rules. Read
[`references/humanizer-patterns.md`](references/humanizer-patterns.md) when the
text needs a full editorial pass or when the likely problem is not obvious.

## Non-negotiable rules

- Preserve facts, names, numbers, dates, units, equations, quotations,
  citations, links, and technical claims.
- Never invent evidence or strengthen a claim beyond its support.
- Do not discard specific detail merely to make prose shorter.
- Do not flatten a recognizable authorial voice into generic corporate prose.
- Do not treat one isolated phrase as proof of machine-written text. Look for
  clusters, repetition, and mismatch with context.
- Use ASCII punctuation in maintained prose. Preserve punctuation inside
  verbatim quotations, licensed third-party text, code, and mathematical
  notation.
- Keep established technical compounds. Fix hyphenation only when it is wrong
  or makes the sentence hard to parse.
- Keep passive voice when the actor is unknown, irrelevant, or properly
  de-emphasized. Rewrite it when omitted agency obscures responsibility.

## Editing method

1. Identify the document's audience, purpose, and voice from the text and its
   surrounding context.
2. Mark facts and protected material that must not change.
3. Run the deterministic audit when a file is available:

   ```bash
   python3 scripts/audit_text.py path/to/file
   ```

4. Review the text for the full Humanizer pattern catalog. Treat scanner hits
   as leads, not automatic defects.
5. Rewrite paragraphs as units. Preserve information rather than copying the
   original sentence shape.
6. Read the result aloud or simulate a spoken reading. Break formulaic rhythm,
   repeated transitions, and manufactured punch lines.
7. Perform a second audit with two questions:
   - What still sounds generic, staged, promotional, or overly agreeable?
   - Did any fact, number, qualifier, or citation change?
8. Run the available deterministic no-Unicode-dash check as the final pass.

## Core checks

### Substance and claims

- Lead with the result, decision, or request.
- Replace significance claims with concrete evidence.
- Remove vague authorities such as "experts say" unless the source is named.
- Keep uncertainty visible and proportional to the evidence.
- Delete generic challenge, future-work, and conclusion sections that add no
  information.
- Prefer measurements, coverage, parity, and reproducible observations over
  adjectives.

### Voice and rhythm

- Prefer flat, declarative sentences for technical work.
- Vary sentence length naturally. Do not force every sentence into the same
  cadence.
- Remove canned transitions, summaries, and signposting that announce what the
  next sentence already says.
- Avoid the rule of three, false ranges, synonym cycling, and repeated sentence
  templates.
- Remove rhetorical questions, aphorisms, and staccato fragments unless they
  are clearly part of the author's established voice.
- Keep real caveats and useful asides short and direct.

### Tone

- Remove sycophancy, congratulatory filler, and fabricated emotional framing.
- Remove promotional language and claims of importance that the evidence does
  not establish.
- Avoid chatbot language, including offers to do more work or references to the
  conversation that do not belong in the artifact.
- Use contractions only when they fit the author and medium.
- Do not add personality to formal technical material. For personal writing,
  preserve opinions, reactions, humor, and uncertainty that are already
  supported by the source.

### Formatting

- Use headings only when they make navigation easier.
- Prefer sentence case unless the target style guide requires otherwise.
- Remove decorative bold, inline header lists, emojis, and excessive sectioning.
- Do not use Unicode em dashes, en dashes, minus signs as punctuation, or
  horizontal bars in maintained prose.
- Preserve code, equations, citations, literal strings, test fixtures, and
  verbatim quotations.

## Technical reports and presentations

- Use claim-oriented titles when the evidence supports a claim.
- State what a plot or table shows; do not merely name it.
- Tie executive framing to operational consequences, decisions, or measured
  outcomes.
- Preserve benchmark conditions, baselines, caveats, and units.
- Do not convert careful scientific uncertainty into marketing certainty.
- Avoid repeating the same conclusion in a title, first sentence, and summary.

## Pull requests and release notes

- State the behavior change and why it matters.
- Describe implementation details only when they help the reviewer assess risk.
- Include benchmark evidence when performance changes, with the baseline and
  measurement conditions.
- Do not narrate the drafting process or add generic validation claims.
- Follow repository-specific publication and attribution rules.

## Output

Return the revised text. If the user asks for a review, also report:

- which pattern families were present;
- which facts or protected details were deliberately preserved;
- any sentence that remains awkward because its meaning is ambiguous;
- any mechanical audit result that still needs human judgment.
