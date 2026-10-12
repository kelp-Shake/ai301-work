# Evidence guide: where evidence lives in a plan package

<!--
THIS IS THE PART YOU WRITE (second week running: the judgment files
stay in your hands). The skill uses this guide as its map: for every
kind of evidence a rubric check names, this file says WHERE to find it
in a plan package and WHAT GOOD LOOKS LIKE when you do.

Under each family heading below, write:

- Where it lives: the exact places to look. In an eval bundle (which
  section of the package: the issue context, the repro-evidence block,
  the candidate plan's scope statement or test plan, the plan comment,
  the repo-facts block). In live mode (where on GitHub or in the
  draft: the issue thread, the student's posted repro comment, the
  repo's docs, the draft plan and comment).
- What good looks like: one or two sentences someone else could apply.
  Prefer observable conditions ("the stated cause cites behavior the
  repro evidence actually shows") over adjectives ("diagnosis is
  solid").

A rubric check whose evidence this guide cannot locate is a check
nobody else can execute, and this week that cuts twice: your
procedure.md tells the skill WHEN to gather each family, and this
guide tells it WHERE. Write the map you wish your executor had.
-->

## Diagnosis and grounding

**Where it lives.**
- Eval bundle: the plan states its cause in the **Candidate plan** (usually a line starting "Cause" or under "Diagnosis"), and the behavior that cause must explain is in the **Repro evidence** block (its steps, outputs, controls, and the "Actual" line).
- Live: the cause is in `plan.md`, and the repro evidence is the author's posted repro comment on the issue, or the house repro pack quoted in the drafts.

**What good looks like.** The stated cause explains every result in the repro evidence, including the controls, and the plan points to a specific result that supports it (for example "the no-pager run still fails, so the cause is upstream of the pager"). A cause that is only "probably", or that is borrowed from a thread comment with no repro result behind it, is not grounded.

## Scope

**Where it lives.**
- Eval bundle: the in-scope and not-in-scope lines in the **Candidate plan** (a "Scope" or "In / Out" section), read against the **Issue** title and body.
- Live: the scope section of `plan.md`, read against the issue.

**What good looks like.** One change that fixes the reported behavior, plus a stated not-in line naming what the plan leaves alone (including any part of the issue it defers). A plan that adds a rename, a migration, a redesign, or a docs pass has gone past the issue, and a plan with no not-in line has no boundary.

## Executability

**Where it lives.**
- Eval bundle: the files and approach in the **Candidate plan** ("Change", "Changes", or "Approach").
- Live: the files and approach sections of `plan.md`.

**What good looks like.** The plan names the files or functions it will change and what the change is, so a stranger could make the first edit without asking the author anything. "Poke around the editor code" or "make undo work" gives them nowhere to start.

## Test plan

**Where it lives.**
- Eval bundle: the "Test" or "Test plan" section of the **Candidate plan**, read against the numbered steps in the **Repro evidence**.
- Live: the test plan in `plan.md`, read against the steps in the author's posted repro comment.

**What good looks like.** The test plan re-runs the repro steps (or a named check on the same behavior) and states the output expected after the fix, such as "step 3 shows the pushed color without leaving the view". "Run the test suite", "make sure nothing regresses", and "check that it works" name no observable result.

## Honesty

**Where it lives.**
- Eval bundle: the risks or unknowns lines in the **Candidate plan**, read against what the **Repro evidence** actually tested.
- Live: the risks section of `plan.md`, and the `## Deviations` section after a build.

**What good looks like.** Anything the plan relies on but the repro did not test is labeled as unconfirmed ("not tested: whether a completed run resumes correctly"). A deviation from the posted plan is recorded in `plan.md`, not only in the diff.

## Comms

**Where it lives.**
- Eval bundle: the **Candidate plan comment** read against the **Candidate plan**, the **Thread highlights** (for maintainer direction), and the **Repo facts** contribution-policy line (for AI-use disclosure).
- Live: the draft in `comment.md` read against `plan.md`, the live issue thread, and the repo's CONTRIBUTING file and issue templates.

**What good looks like.**
- The comment states the cause, the change, and the test, and promises nothing the plan does not hold (no PR dates, no "please assign me").
- It engages every explicit maintainer direction in the thread, such as a constraint or a preferred approach.
- It states that AI assistance was used if, and only if, the policy requires disclosure in comments or issues (a pull-request-only rule does not apply here).
- A comment that is only enthusiasm, or that ignores a maintainer's stated limit, is boilerplate.
