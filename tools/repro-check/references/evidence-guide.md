# Evidence guide: where proof lives in a reproduction package

<!--
THIS IS THE PART YOU WRITE (new this week: Unit 1 handed you this file
finished; the scaffolding fades). The skill uses this guide as its map:
for every kind of proof a rubric check names, this file says WHERE to
find it in a package and WHAT GOOD LOOKS LIKE when you do.

Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the issue context, the repo-facts block, the
  claim comment, the repro report and its parts). In live mode (where
  on GitHub or in the draft: the issue thread, the repo's docs, the
  student's draft comment).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("the versions named match what the
  issue targets, or the difference is called out") over adjectives
  ("environment is thorough").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute; the rubric swap showed you what that feels
like. Write the map you wish your grader had.
-->

## Environment

**Where it lives.** Eval: the repro report's environment line (usually the first line, "Environment: ..."), read against the `## Issue` section and the `repo-facts` block's latest release. Live: the environment line of the draft report, read against the issue's version and OS.

**What good looks like.** The report names the operating system and the version of the software under test. If the issue targets a different version or platform, the report says so.

## Steps

**Where it lives.** Eval: the `Steps` part of the repro report, including pasted commands, inputs, and config. Live: the same part of the draft, plus any files it links to.

**What good looks like.** A stranger with the stated environment could run each step in order from a clean start. Every command, input file, and config is shown in the report, or the report points to the issue's own text for it. A step that depends on a private repo, config, or machine is not followable.

## Behavior shown

**Where it lives.** Eval: the pasted output, log, or transcript in the repro report, read against the behavior described in the issue body under `## Issue`. Live: the same, against the issue page.

**What good looks like.** The artifact shows the symptom the issue names: the same error text, exit code, or output, from the issue's input and version. An artifact of a different symptom (a graceful error where the issue reports a crash, an input the author changed) shows an adjacent behavior, not this one. A version banner or a session list shows the tool runs, not the behavior.

## Honesty

**Where it lives.** Eval: the report's `Result` or `Expected` and `Actual` lines, read against what its pasted artifacts show. Live: the same, in the draft.

**What good looks like.** What the report says happened is what the artifact shows. A report that says it could not reproduce, names what it tried, and says how its setup differed from the issue's is honest. A report that claims confirmation, a root cause, or repeated runs that the artifact does not show is not.

## Comms

**Where it lives.** Eval: the `## Candidate claim comment` section against the `## Issue` section, and both comments against the "contribution policy" line of the `repo-facts` block. Live: the draft claim against the issue thread, and the repo's CONTRIBUTING.md or AI policy file.

**What good looks like.** The claim names something only this issue has (a function, file, error message, or behavior), offers to investigate or report back, and states the next work the author will do. Boilerplate that fits any issue, a promised fix or date, or a request to be assigned is not that. If the policy line explicitly tells contributors to disclose AI use in comments, a comment states it. A requirement that covers only pull requests does not apply to comments, and a rule that comments be human-written is not a disclosure requirement.
