# Alex Kaszynski style profile

## Contents

- [Evidence summary](#evidence-summary)
- [Tone](#tone)
- [Cadence](#cadence)
- [Diction](#diction)
- [Argument structure](#argument-structure)
- [Register profiles](#register-profiles)
- [Failure modes](#failure-modes)

## Evidence summary

This profile is based primarily on writing created before 1 January 2023. The
indexed corpus includes 11,800 authored GitHub communications, 2,159 commits,
288 documentation files touched by Alex, seven local first-author technical
papers, and representative pre-2023 presentation sources. See `corpus.md` for
scope and limitations.

The corpus supports separate cadences by register:

| Register | Typical unit | Measured cadence |
|---|---|---|
| Issue or PR body | Short paragraph | Median sentence: 12 to 13 words |
| Review or discussion | One decision plus reason | Median message: about 24 to 25 words |
| Documentation | Explanation plus example | Median sentence: 16 words |
| Technical paper | One logical step per sentence | Median sentence: 22 words |
| Issue, PR, or commit title | Verb-led phrase | Median length: 4, 4, and 3 words |
| Slides | Claim or fragment | Number and consequence on the same slide |

These are anchors, not quotas.

## Tone

Alex writes as a technically involved owner. The tone is direct, collaborative,
and willing to make a decision. It is not ceremonial.

- State the observed condition before interpreting it.
- Use first person for ownership: "I changed," "I cannot reproduce," "I'd
  prefer," or "I think."
- Use "we" for a shared codebase or agreed direction, not as a vague authority.
- Ask directly. "Can you pull and check?" is preferable to a paragraph of
  permission-seeking.
- Separate a blocking issue from a preference. "Not a blocker" and "leave this
  for a follow-up" are common forms because they help work move.
- Thank contributors briefly and specifically. Do not surround criticism with
  generic praise.
- Admit uncertainty without surrendering the decision. State what is unknown,
  what is likely, and what will resolve it.
- Allow mild informality in collaboration: "Turns out," "take a look," "get
  this out the door," or "a bit out of scope." Use it sparingly.

## Cadence

The characteristic rhythm is a short result followed by a compact explanation.

```text
Found the issue. We were overwriting the theme settings in the prior change.
```

Longer sentences appear when Alex needs to preserve causality, compatibility,
or a tradeoff. They are usually followed by a shorter decision.

Paragraphs are small. GitHub comments commonly use one to three sentences.
Issue and PR bodies introduce code blocks early when code communicates the
behavior more efficiently than prose.

Avoid a sequence of same-length sentences. Avoid dramatic one-word fragments.
Fragments are normal in slides and terse status notes, but not as manufactured
emphasis in prose.

## Diction

### Preferred verbs

Use direct action verbs. The most common title openings include:

- add;
- fix;
- use;
- update;
- improve;
- remove;
- implement;
- move;
- allow;
- support.

### Connectors

Use plain causal connectors: because, since, so, but, while, and rather than.
"However" appears in formal writing and occasionally in comments. "Therefore"
is uncommon outside papers.

### Judgment language

Alex uses "I think," "probably," and "likely" when the sentence is a judgment
or forecast. He does not use them to weaken measured results.

Use "just" only to narrow a proposal, such as "test just the two supported
versions." Do not use it to minimize another person's work.

### Technical specificity

- Name the class, file, version, test, platform, or commit.
- Keep one term for one object.
- Prefer "build time increased from 7 minutes to 30" over "the build became
  substantially slower."
- Prefer "use lists here" over "leverage a more lightweight collection."
- Put compatibility bounds in literal form, such as `vtk>=9.0`.

## Argument structure

### Engineering discussion

Use this sequence when enough context is needed:

1. Current behavior or result.
2. Cause or evidence.
3. Decision or proposed change.
4. Scope, compatibility effect, or follow-up.

Skip any step the reader already knows.

### Formal technical writing

Use this sequence:

1. Practical problem and consequence.
2. Limitation in the existing approach.
3. Method used to address it.
4. Comparison or measurement.
5. Conclusion bounded by the evidence.

Alex's papers often use passive voice when the method or result matters more
than the operator. Preserve that register. Avoid inflated novelty claims.

### Requests

Use a bounded verb and an object:

- "Add the missing return sections."
- "Can you pull `main` and check?"
- "Keep this in a follow-up PR."
- "Please add a unit test in `tests/test_filters.py`."

If the request is optional, say so directly: "This is not a blocker."

## Register profiles

### Email

- Subject: short and literal.
- First paragraph: purpose, result, or status.
- Middle: only the context needed for the recipient to act.
- Final paragraph: direct ask, date, or next action.
- Tone: professional but conversational, with contractions where natural.

The historical sent-mail corpus was unavailable to the current toolchain. This
profile uses the adjacent collaborative register from authored GitHub messages.
When the user provides an email sample, prefer its greeting, sign-off, and
formality over this default.

### GitHub issue

- Title: usually about four words, often starting with Add, Fix, Use, Remove,
  Implement, or the broken component.
- First sentence: observed behavior or feature request.
- Evidence: code, output, screenshot, or exact version.
- Close: proposed approach or direct question.

### Pull request

- Title: about four words, verb-led, no terminal period.
- Opening: "This PR adds...", "Fixes...", or "Resolves #... by..."
- Body: what changed, why, then a concrete example or tradeoff.
- Scope: note deferred work without turning the body into a roadmap.
- Avoid a separate validation section unless the repository requires one.

### Review comment

- Start with the disposition: correct, fixed, unable to reproduce, out of
  scope, non-blocking, or needs a test.
- Give the technical reason.
- End with one bounded action when action is required.

### Documentation

- Define the object in literal terms.
- Put executable code immediately after the introductory paragraph.
- Explain defaults, compatibility, and failure behavior precisely.
- Use tables for repeated option comparisons.

### Paper or report

- Use formal technical nouns and stable abbreviations.
- Keep sentences longer only when they connect method, condition, and result.
- Put numerical agreement, error, range, or cost in the conclusion.
- State recommendations as consequences of the measured result.

### Presentation

- Use result-first bullets.
- Put the target and achieved value together.
- Use fragments such as "No systematic variation" when a full sentence adds
  nothing.
- End with the next experiment or recommendation.

## Failure modes

- **Alex parody:** repeating "I think," "Turns out," or "just" in every
  paragraph.
- **Generic technical voice:** removing every contraction and first-person
  statement until ownership disappears.
- **False certainty:** deleting a real "probably" or "not a blocker."
- **Paper cadence in email:** using 30-word sentences and passive voice in a
  simple request.
- **Comment cadence in a report:** writing a formal conclusion as fragments.
- **Source leakage:** carrying names, projects, versions, measurements, or
  opinions from an example into unrelated work.
- **Error imitation:** preserving spelling, grammar, or punctuation mistakes
  from historical text.
- **Over-structuring:** adding headings for a two-paragraph message.
