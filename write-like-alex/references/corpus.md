# Corpus and methodology

## Contents

- [Cutoff and identity](#cutoff-and-identity)
- [Corpus inventory](#corpus-inventory)
- [Method](#method)
- [Coverage limits](#coverage-limits)
- [Publication and privacy rules](#publication-and-privacy-rules)

## Cutoff and identity

The primary cutoff is 1 January 2023. GitHub records use the author account
`akaszynski`. Git commits use the historical author name Alex Kaszynski and the
author's known email identity. Later writing is not used to establish the core
style because it may include text drafted by automated tools or other authors.

## Corpus inventory

### GitHub communication

Work MCP contained 11,800 pre-2023 records authored by `akaszynski`, totaling
about 3.19 million body characters:

| Kind | Records | Body characters |
|---|---:|---:|
| Issues | 375 | 208,443 |
| Issue comments | 2,899 | 1,000,110 |
| Pull requests | 1,064 | 569,243 |
| Pull request comments | 2,393 | 749,160 |
| Pull request review comments | 5,069 | 663,838 |

The largest public sources were PyVista, PyMAPDL, PyAEDT, PyDPF-Core,
PyVista-Support, the PyAnsys developer guide, and MAPDL Reader.

### Commits

The indexed local corpus contained 2,159 non-merge commits before the cutoff
under Alex's historical author identity. Most were terse subjects from FEMORPH
and related engineering repositories. The median subject was three words.

### Documentation

The documentation analysis inspected the pre-2023 snapshots of 288 Markdown,
reStructuredText, and LaTeX files that Alex had edited across 11 repositories.
The resulting corpus contained 92,652 words. The median prose sentence was 16
words. Files included public PyVista and PyAnsys documentation and private
engineering repositories. No private documentation text is bundled here.

### Papers

Seven locally archived first-author technical papers were converted to text and
reviewed, totaling about 54,000 extracted words:

- *Uncertainties of an Automated Optical 3D Geometry Measurement, Modeling, and
  Analysis Process for Mistuned Integrally Bladed Rotor Reverse Engineering*;
- *Automated Finite Element Model Mesh Updating Scheme Applicable to Mistuning
  Analysis*;
- *Experimental Validation of a Mesh Quality Optimized Morphed Geometric
  Mistuning Model*;
- *Accurate Blade Tip Timing Limits Through Geometry Mistuning Modeling*;
- *Harmonic Convergence Estimation Through Strain Energy Superconvergence*;
- *Experimental Validation of an Optically Measured Digital Replica of a
  Geometrically Mistuned Rotor Using a System ID Approach*;
- *Automated Meshing Algorithm for Generating As-Manufactured Finite Element
  Models Directly From As-Measured Fan Blades and Integrally Bladed Disks*.

The median extracted sentence was 22 words. Bibliographic searches also found
the broader publication record, including conference and journal variants, but
only full local texts were used for close cadence analysis.

### Presentations

Representative pre-2023 LaTeX sources covered technical measurement reviews,
software architecture, PyAnsys demonstrations, project management, and PyVista
training. Slide evidence supports terse bullets, numbers adjacent to claims,
explicit limitations, and recommendation-oriented conclusions.

### Email

The Work MCP mailbox was configured for AgentMail and did not expose the
historical Gmail sent folder. No historical sent-mail corpus or private email
text is bundled. The email register therefore uses the adjacent collaborative
style found in public GitHub discussions. It must yield to a user-provided email
sample when one is available.

## Method

- Process every indexed pre-2023 GitHub body for aggregate cadence, marker, and
  punctuation measurements.
- Remove fenced code and URLs before prose measurements.
- Separate issues, PRs, comments, review comments, commits, docs, and papers.
- Use medians rather than averages for target cadence because the corpus
  contains large issue templates and one-word review dispositions.
- Inspect representative source text across years, repositories, and content
  lengths after the aggregate pass.
- Prefer first-author papers for close academic analysis. Treat coauthored docs
  as supporting evidence rather than pure voice samples.
- Correct obvious spelling and grammar in bundled examples. Replace details
  that could identify a customer or disclose private work.

## Coverage limits

"Pre-2023 corpus" means the records and files accessible through Work MCP,
public repository history, and the local archive at the time of analysis. It is
not a claim that every document Alex has ever written was available.

GitHub review records include quoted text, templates, and brief dispositions.
Paper text extraction contains headers, references, tables, and line-wrap
artifacts. Quantitative values are anchors and were checked against direct
reading rather than used as automatic rules.

## Publication and privacy rules

- Publish only public-source examples or genericized local examples.
- Never publish email addresses, customer identifiers, contract terms, part
  numbers, controlled markings, or unpublished measurements.
- Keep source URLs only for public GitHub or DOI records.
- Store style rules and provenance, not the raw private corpus.
- Refresh the profile through the same pre-2023 cutoff unless the user
  explicitly asks to incorporate later writing.
