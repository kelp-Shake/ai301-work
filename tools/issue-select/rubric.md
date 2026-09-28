# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

All recency thresholds are measured against the bundle's `captured:` date in eval
mode, and against today's date in live mode.

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| unclaimed | The `assignees:` and `linked PRs:` fields on the `this issue:` line of the repo-facts block, plus every comment in the Comments section (live: the Assignees box, the Development box, and the thread; where the sidebar and the thread disagree, believe the thread). | All three hold: `assignees: none`; no pull request linked in the sidebar or named in the thread is in the open state; and no comment claiming the work ("I'll take this", "working on this", "can I work on this") was posted within 90 days of the capture date without the claimer later withdrawing. A closed, unmerged pull request is an abandoned attempt, not a live claim. | required |
| commit-alive | The "last 5 default-branch commits" list in the repo-facts block, with dates and authors (live: the commit list linked from the repo front page). The "last push to any branch" line is deliberately NOT used: a side-branch push shows someone touched something, not that work landed. | At least one of the five most recent default-branch commits is dated within 90 days of the capture date. A commit authored by an account ending in `[bot]` counts only when it merges a human pull request. | required |
| repo-used | The `archived:` flag and star count on the repo line, and the "latest release" line of the repo-facts block (live: the archive banner, the star count, and the Releases box in the right sidebar). | Both hold: `archived: no`, and either the latest release is dated within 365 days of the capture date or the repo has cut no release at all. Archived is fatal on its own, whatever the release date says: a read-only repo cannot take a pull request. Repos that never release are not penalised, since docs sites and tool collections often ship nothing. | required |
| ai-policy | The "contribution policy" line of the repo-facts block, including any `CONTRIBUTING.md`, `AI_POLICY.md`, `AI_USAGE_POLICY.md`, or `AGENTS.md` it quotes or summarises (live: `CONTRIBUTING.md` in the repo root or `.github/`, plus the contributor docs it links out to). | Fails only on an outright ban on AI-assisted contribution ("we do not accept AI-generated code or documentation"). Everything short of a ban passes: a prohibition on FULLY AI-generated work while assistive use stays allowed, and conditions such as disclosure, personal understanding, testing, or human review, are terms to follow rather than walls. Silence passes; most repos state nothing, and that is not a restriction. | required |
| bounded-work | The issue title and body (live: the same, on the issue page). | The body asks for one finite change that could be finished in a single pull request. Fails when the body is mostly a list of other issue numbers, or calls itself a tracking, umbrella, or mega issue; or when it asks for a CATEGORY of change rather than one change ("more type annotations", "parts of the codebase where it makes sense"), so no state exists in which someone could call it done. A terse body, a missing reproduction, or an unpolished writeup is NOT a failure here: grade the size of the work asked for, not the polish of the writing. | required |
| direction-settled | The Comments section in full, the issue's open date against the capture date, and the `author_association` of the opener (live: the thread, the opened date, and the badge next to the opener's name). | Somebody has already agreed this change should happen. A bug report or documentation correction passes by default: the intended behavior is not in dispute. A NEW FEATURE passes only when a maintainer has blessed it, by opening the issue themselves with an Owner, Member, or Collaborator association, by applying a `good first issue` or `help wanted` label, or by supporting it in the thread. Fails either way when the thread shows the design still being argued with no maintainer having settled it: many comments over months or years, with maintainers asking clarifying questions rather than giving direction. | required |

## Verdict rule

Accept only when every `required` check grades `pass`. A single required `fail`
rejects the issue, however good the rest of it looks: these are independent ways a
first contribution dies, so they do not trade off against each other.

`unclear` on a required check counts as `fail`. A first issue whose safety cannot be
verified from the evidence in front of me is not one worth taking.

Every check in the table is `required`, so there are no preferred checks to rank
accepted candidates with. In live mode the accepted issues come back unordered and
the choice between them is mine to make by hand.
