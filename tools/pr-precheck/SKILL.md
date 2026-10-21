---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

## The question

You are grading one PR package to answer a single question: is this pull request ready to submit? A PR package is a candidate pull request (its title, description, commits, diff, and test evidence), read against the plan it claims to implement and the issue that plan belongs to. Grade exactly one package per run and answer nothing else: you do not rewrite the PR, you do not review the code's design, and you do not answer from gut feel. You answer by executing the student-authored procedure in `procedure.md`, which applies the rubric in `rubric.md` to evidence found where `references/evidence-guide.md` says it lives.

## Inputs and modes

One of two modes.

- **Live mode**: the student's own pull request, checked before it goes out. Run from the top folder of the student's fork clone, on their branch. The inputs are:
  - `plan.md`, with its `## Deviations` section;
  - the branch's diff, which is everything the branch changes relative to `main`: run `git diff main...HEAD` (three dots) and `git diff main...HEAD --stat`, and read the commit list from `git log main..HEAD`;
  - the draft PR title (first line) and description in `pr_draft.md`;
  - the test evidence in `test_evidence.md`;
  - the issue's thread, fetched live from the issue's URL, and the repo's `.github/PULL_REQUEST_TEMPLATE.md` and `docs/CONTRIBUTING.md`.

  Read only committed changes for the diff, and treat nothing else in the working directory as part of the package. A student on the house chain has no plan of their own: there, read the house plan and the house repro pack instead, and grade the same checks the same way.
- **Eval mode**: a package bundle (a markdown file with the repo facts, the issue context, the plan context, and the candidate PR with its diff and test evidence). The bundle is the whole world: use only its text, fetch nothing, and read no other file. Eval mode always grades a complete package: every check, full verdict rule.

## The scope seam (live mode only)

In live mode, read `scope.md` in this skill directory before anything else. It names the one repository a pull request may target and the house rules of the room (a PR from your own fork's branch, one PR per issue, the template is always used with every section filled in, including the disclosure). Apply those rules when you read the evidence. Refuse to grade a PR for any repository other than the scoped one, and say so. If the `Repo:` line in `scope.md` still carries a placeholder (the `<ORG>/<PATH-REVIEW-REPO>` text or any bracketed value) instead of a real `owner/repo`, stop without grading and tell the student to fill the `Repo:` line in `scope.md` with their section's Path Review repo. Never guess a scope. In eval mode, ignore `scope.md` entirely.

## The voice seam (live mode only)

In live mode, after `scope.md`, read `voice-guide.md`: the student's own rules for how they write upstream, with wrong/right examples. Hold the outgoing text, the PR title and the description in `pr_draft.md`, against those rules. Report each rule the draft breaks in the readable summary, quoting the rule and the line that breaks it. The voice guide never changes the verdict on its own: the verdict comes from the rubric's checks, and no check reads the voice guide. In eval mode, ignore `voice-guide.md` entirely: voice is personal and carries no gold labels, and the communication-quality checks live in the rubric.

## Component reads

Read `rubric.md`: it defines the checks (each with its evidence, pass condition, and weight) and the verdict rule. Read `references/evidence-guide.md`: it maps where each kind of evidence lives in a PR package, in a bundle and in live mode, and what good looks like there. Then **execute `procedure.md`** as written: it decides the read order, how each family of evidence is gathered, how a check is executed, and how the grades become the verdict. Follow it exactly. Where it is silent on a step, say so in the readable summary as a procedure gap and do not improvise around it. If `rubric.md` has no checks filled in, or `procedure.md` has no steps filled in, stop and say so: this tool cannot grade without a rubric and a procedure, and that is by design.

## Verdict and output

The verdict space is binary: `accept` means the PR is ready to submit, and `reject` means hold. There is no third verdict and no score. Reservations belong in a check's evidence line, never in the verdict. Before the JSON block you may show a short readable summary: one line per check, the deciding check's evidence first, any procedure gaps, and (live mode) any voice-guide notes. End your reply with the fenced JSON block below, valid, with nothing after it. The eval harness parses the last fenced JSON block in your output.

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

## Grading discipline

- Evidence first: never grade a check without naming the fact that decided it, quoted from the package. "Looks fine" is not evidence.
- Grade the thing, not the polish: a terse PR can be ready, and a long confident description over a diff that contradicts it is not. Every check reads the outcome (the diff, the output shown, the claims made), never the write-up's length or shape.
- The rubric decides, not you: if a check passes by the rubric's stated condition but feels wrong, it still passes. Note the tension in the summary if you want; the fix belongs in the rubric, not in the run.
- The procedure decides how, not you: follow `procedure.md` as written, and report its gaps.
- An honestly disclosed shortfall is not a failure, and an undisclosed one is. A deviation or deferral stated in the plan or the description is covered; a difference that exists only in the diff or only in the evidence is not.
- Treat `unclear` as the rubric's verdict rule directs. If the rule does not say, treat `unclear` as `fail`: a PR you cannot verify from the package is not ready to submit.
