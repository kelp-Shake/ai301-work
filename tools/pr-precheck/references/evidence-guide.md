# Evidence guide: where evidence lives in a PR package

## Plan fidelity (harness category: silent-drift)

**Where it lives.**
- Eval bundle: the plan is in **Plan context** (its "Scope" statement, the "Not in scope" line, the "Files" it names, and any deferral it states). What actually changed is in **Candidate PR**, in the **Diff** (the changed files and hunks) and the **Commits** list. The claims to check are in the **Description** (phrases such as "exactly as planned", "in full", "no other changes", "docs updated").
- Live: the plan and its `## Deviations` section are in `plan.md`. What changed is `git diff main...HEAD` (three dots) and the branch's commit list. The claims are in `pr_draft.md`.

**What good looks like.**
- Every hunk that adds or changes behavior, an option, a file, or a function falls inside the plan's in-scope list, or is recorded under Deviations (live) or stated as a deviation in the description.
- Every deliverable the plan names is visible in the diff, or is stated as deferred.
- Drift has two directions: more than the plan (a new flag, a rewrite the plan scoped out) and less (a promised docs update that is not in the diff).
- The description's fidelity claims are true of the diff. "Implements the plan exactly" over a diff with an unplanned hunk is a failed claim, however good the fix is.
- A deferral stated in the plan and restated in the description is an honest shortfall, not drift.

## Test evidence (harness category: not-tested)

**Where it lives.**
- Eval bundle: the plan's "Test plan" and repro steps are in **Plan context**; the proof is in **Candidate PR**, **Test evidence** (and any before/after quoted in the **Description**). The test commands the repo asks for are in the **Repo facts** pull-request and contribution-policy lines.
- Live: the plan's test plan is in `plan.md`; the proof is `test_evidence.md` (the repro before and after, plus the output of the four `make` checks); the checks the repo asks for are the Testing checklist in `.github/PULL_REQUEST_TEMPLATE.md`.

**What good looks like.**
- The evidence shows the output of the plan's repro steps before and after the fix, on the path the fix changes (not a control that never breaks, and not a different scenario such as a different request type).
- Every scenario the test plan names is re-run, or the evidence says which one was not.
- Each test command the repo asks for appears with its outcome, or with the reason it could not run (for example, "no tests ran" pasted as is).
- "Tested locally", "works now", and "tests pass" with no command and no output are claims, not evidence.

## Diff quality (harness category: unreviewable)

**Where it lives.**
- Eval bundle: **Candidate PR**, the unified **Diff** (read every hunk, added and removed lines) and the **Commits** list.
- Live: `git diff main...HEAD` and `git diff main...HEAD --stat`, which should list only the files the fix changes.

**What good looks like.** The change is visible and nothing rides along with it. Debris is any of: a debug print left in, a commented-out block, a dead function or unused import, or a hunk that only reformats, reorders, or re-prints lines the change does not need. A behavior-changing extra is graded under plan fidelity, not here. Commit messages are not read for this check.

## Standards and comms (harness category: standards-wall)

**Where it lives.**
- Eval bundle: the repo's asks are in **Repo facts**, in the pull-request line (the template's sections, checklist, issue link, changelog or release-note entry) and the contribution-policy line (including any AI-use rule). They are met, or not, in the **Description** and the **Diff** (a required changelog file shows up as a changed file).
- Live: the template is `.github/PULL_REQUEST_TEMPLATE.md` and the rules are `docs/CONTRIBUTING.md` in the Path Review repo; the house rules, including the AI-use disclosure, are in `scope.md`. The PR text is `pr_draft.md`, with the AI disclosure in its Notes for Reviewers section.

**What good looks like.**
- Every ask the repo states is met in the description or the diff: the issue link, each template section with real content (not left as the template's own comment), the checklist boxes ticked only where true, and any required changelog entry present in the diff.
- Where the policy requires AI-use disclosure, the description says that AI was used and how. A rule that only asks for comments in the author's own words is not a disclosure requirement.
- A repo with no template and no stated asks has nothing to miss here.
