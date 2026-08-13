# Common agent skills moved

The canonical skill source is now
[`akaszynski/agents`](https://github.com/akaszynski/agents/tree/main/skills).
This repository is retained for history and is no longer updated.

## Available skills

- `de-ai-ify`: Edit human-facing prose to remove formulaic machine-written
  patterns while preserving facts, technical precision, and the author's voice.
- `write-like-alex`: Rewrite text in Alex Kaszynski's evidenced voice, with
  separate registers for collaboration, GitHub, documentation, papers, reports,
  and presentations.

## Install

List the skills exposed by the agents repository:

```bash
npx skills add akaszynski/agents --list
```

Install the skills for the agents supported by the local Skills CLI:

```bash
npx skills add akaszynski/agents --global --agent '*' --yes
```

The skill format is portable. A harness that does not use the Skills CLI can
copy or link the desired skill directory into its configured skills path.

The historical skill files and third-party license notices remain available in
this repository. New changes belong under `skills/` in `akaszynski/agents`.
