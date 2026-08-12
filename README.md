# Common agent skills

This repository is the shared source for skills used across agent harnesses.
Each skill is a self-contained directory with a `SKILL.md` entry point.

## Available skills

- `de-ai-ify`: Edit human-facing prose to remove formulaic machine-written
  patterns while preserving facts, technical precision, and the author's voice.
- `write-like-alex`: Rewrite text in Alex Kaszynski's evidenced voice, with
  separate registers for collaboration, GitHub, documentation, papers, reports,
  and presentations.

## Install

List the skills exposed by this repository:

```bash
npx skills add akaszynski/skills --list
```

Install the skills for the agents supported by the local Skills CLI:

```bash
npx skills add akaszynski/skills --global --agent '*' --yes
```

The skill format is portable. A harness that does not use the Skills CLI can
copy or link the desired skill directory into its configured skills path.

## Validate

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
npx skills add . --list
```

Third-party material and its license are identified inside the relevant skill.
