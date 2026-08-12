# Humanizer pattern catalog and local alignment

This reference adapts the writing-pattern catalog and editorial method from
[blader/humanizer](https://github.com/blader/humanizer), version 2.9.1 at
commit `523374d`. Humanizer is Copyright (c) 2025 Siqi Chen and licensed under
the MIT License. The complete license is in `../LICENSE.humanizer`.

The local rules below resolve places where a general-purpose Humanizer rule
could damage technical writing. They are intentional, not accidental drift.

## How to use the catalog

Patterns are diagnostic clues. A cluster of them, repeated structure, or a
clear mismatch with the author's context warrants an edit. A single phrase may
be legitimate. Preserve odd but specific details, mixed feelings, dated
references, deliberate sentence fragments, and other evidence of genuine
authorship.

Rewrite from meaning rather than performing phrase substitution. After the
first pass, audit again for remaining formulaic language and for accidental
changes to facts.

## Content patterns

1. **Inflated significance.** Claims that an ordinary detail is pivotal,
   historic, foundational, or part of a sweeping trend without evidence.
   Replace the claim with the concrete consequence or remove it.

2. **Notability by name-dropping.** Lists of publications, companies, or public
   figures used as a substitute for evidence. Keep only directly relevant,
   sourced references.

3. **Superficial participial clauses.** Trailing clauses beginning with words
   such as "highlighting," "underscoring," or "showcasing" that restate rather
   than explain. State the causal connection or delete the clause.

4. **Promotional language.** Terms such as groundbreaking, vibrant, stunning,
   renowned, and must-see that sell rather than inform. Use measurable or
   observable descriptions.

5. **Vague attribution.** "Experts say," "observers note," and similar claims
   without a named, relevant source. Name the source or remove the attribution.

6. **Generic challenges and future outlook.** Stock paragraphs saying that
   challenges remain but the future is promising. Replace them with specific
   constraints, next decisions, or no paragraph at all.

7. **Stock machine vocabulary.** Clusters of terms such as delve, landscape,
   tapestry, testament, pivotal, multifaceted, foster, robust, seamless, and
   nuanced. The problem is not any single word; it is density and generic use.

8. **Copula avoidance.** Needlessly replacing "is," "has," or "uses" with
   "serves as," "boasts," "features," or "represents." Prefer the direct verb.

9. **Negative parallelism.** Repeated "not only ... but also," "it is not X;
   it is Y," or tailing negations that manufacture contrast. Keep the contrast
   only when it is substantively important.

10. **Rule of three.** Forcing ideas into triplets for rhetorical polish. Use
    the number of items the subject requires.

11. **Synonym cycling.** Renaming the same object in adjacent sentences to
    avoid repetition. Technical writing usually benefits from one stable term.

12. **False ranges.** "From X to Y" constructions whose endpoints do not form
    a meaningful scale. Name the items or relationship directly.

13. **Subjectless or passive fragments.** Sentences that omit the actor to sound
    formal. Restore the actor when responsibility or causality matters. Keep
    legitimate technical passive voice when the actor is unknown or irrelevant.

## Style and formatting patterns

14. **Unicode dash punctuation.** Replace em dashes and en dashes used as
    punctuation with commas, parentheses, colons, or separate sentences. This
    repository's maintained prose uses ASCII punctuation even if a voice sample
    uses Unicode dashes. Do not alter quotations, code, or mathematical symbols.

15. **Bold overuse.** Remove decorative bold and sentence fragments bolded only
    for rhythm. Keep emphasis that has a real navigational or semantic purpose.

16. **Inline-header lists.** Lists in which every item starts with a bold label
    and colon can feel templated. Use plain bullets, a table, or prose when the
    labels do not improve scanning.

17. **Title case everywhere.** Use sentence case for headings unless a product,
    publication, or repository style guide requires title case.

18. **Decorative emojis.** Remove emojis used as section markers or applause.
    Keep them only when they carry intended meaning in an informal source.

19. **Curly quotation marks.** Do not treat curly quotes alone as a defect.
    Normalize them only when the target style requires ASCII punctuation.

20. **Chatbot artifacts.** Remove offers for more help, references to the prompt
    or conversation, training-cutoff disclaimers, and other text that does not
    belong in the document.

21. **Unsupported gap filling.** Do not speculate about missing facts or add
    caveats based on model limitations. Identify the missing source or leave the
    claim out.

## Communication patterns

22. **Sycophancy.** Remove automatic agreement, praise, congratulations, and
    claims that the reader's framing is correct before evidence is considered.

23. **Filler.** Delete openings such as "It's important to note" and "In order
    to" when they add no meaning. Do not replace them with another stock phrase.

24. **Excessive hedging.** Reduce stacked qualifiers such as "might possibly
    perhaps." Preserve uncertainty that is required by the evidence.

25. **Generic conclusions.** Remove summaries that merely repeat the preceding
    paragraphs. End on the result, decision, limitation, or next action.

26. **Hyphen-pair overuse.** Avoid invented paired modifiers and incorrect
    predicate hyphenation. Preserve established technical compounds and terms
    of art.

27. **Authority tropes.** Remove "this is the kind of" and similar framing that
    tries to persuade by asserting what experts, teams, or leaders value.

28. **Signposting announcements.** Delete "here's the key point," "let's break
    this down," and similar announcements when the following sentence can make
    the point directly.

29. **Fragmented headers.** Avoid stacking short fragments as headings solely
    to create drama. Use a heading only when it helps navigation.

30. **Diff-anchored writing.** Do not describe a revision only as "previously X,
    now Y" when the current behavior can be stated directly. Retain the before
    and after comparison when compatibility or migration is the subject.

31. **Manufactured punch lines.** Remove staccato fragments such as "The result?
    Faster." when ordinary sentences are clearer. Deliberate fragments may
    remain in a demonstrated personal voice.

32. **Aphorism formulas.** Avoid slogan-like "X is not Y. It is Z." structures
    unless the contrast carries necessary information.

33. **Conversational rhetorical openers.** Remove "And X?" or "But Y?" openers
    that simulate dialogue without helping the reader. Use a direct sentence.

## Voice and false-positive guards

- Specificity is evidence. Preserve exact observations, peculiar details,
  measured values, and named constraints.
- Preserve the author's mixed or unresolved reaction. Do not manufacture a
  cleaner emotional arc.
- Keep sentence-length variation and genuine asides when they fit the medium.
- Historical text can contain phrases now associated with machine writing.
  Context and date matter.
- Personal writing can support humor, opinion, and mild messiness. Technical
  writing should remain precise and restrained.
- Never fabricate a person, source, quote, number, or citation to make prose
  feel more human.
