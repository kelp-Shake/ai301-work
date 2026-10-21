# Rubric: is this pull request ready to submit?

<!--
THIS IS THE PART YOU WRITE (fourth week running; this is the rubric's
final form in the sandbox). Your frame in SKILL.md executes whatever
checks you define here, via your procedure.md. It ships empty on
purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the diff read against the plan's scope, the test
     evidence read against the plan's test plan, the description read
     against the diff, the repo-facts block's template asks) or a
     location from your references/evidence-guide.md. "The PR" is not
     a source; "the diff's changed files read against the plan's
     stated boundary" is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself
     (does the diff fall inside the plan plus its deviation notes? is
     the claimed evidence observable?), never the write-up's shape
     (how long the description is, how many commits there are).
     Structure-shaped checks are what make graders disagree with
     themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (submit) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. State the `unclear`
   treatment explicitly: the frame here is YOUR SKILL.md, so a rubric
   that stays silent is only covered if your frame's grading
   discipline says what happens (the contract's own default is that
   an unverifiable claim fails).

Cover what actually gets bad PRs submitted. The failure families the
lecture named ARE the harness's scoring categories, same names as the
eval README: silent drift (the diff silently does more or less than
the posted plan, or the description claims fidelity the diff
contradicts), not tested (the evidence proves nothing observable, or
the repo's own checks were never run), unreviewable (debris or
unrelated hunks bury the change), and standards wall (the repo's
stated template and disclosure asks are ignored). Your evidence
guide's four headings map onto these one to one (plan fidelity =
silent drift, test evidence = not tested, diff quality =
unreviewable, standards and comms = standards wall), and the category
floor is scored on exactly these names plus clear accept. A rubric
that ignores a category will fail the eval packages built around
that category. And remember the honest-outcome
rule, fourth week running: a PR that honestly discloses a shortfall
can be ready; a rubric that equates "less than everything" with
"hold" fails the set.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| diff-within-plan | The diff's changed files and hunks, read against the plan's in-scope list, its not-in-scope line, and any recorded deviation (the plan's `## Deviations` section, or a deferral the plan or description states). | **Passes when** every code hunk that adds or changes behavior, an option, a file, or a function is covered by the plan or a recorded deviation, and every deliverable the plan names is either in the diff or stated as deferred. | required |
| description-matches-diff | The description's claims about what the change does and leaves out (such as "exactly as planned", "docs updated", "no other changes"), read against the diff. | **Passes when** every such claim is true of the diff, and anything the plan promised that the diff lacks is stated as deferred. | required |
| repro-before-after | The test evidence, read against the plan's test plan (and the repro steps it re-runs). | **Passes when** the evidence shows the output of the plan's repro steps before and after the fix, on the path the fix changes, for every scenario the test plan names or with the omission stated. | required |
| repo-checks-shown | The test evidence, read against the repo facts' stated test commands or PR template checks (live: the template's Testing checklist). | **Passes when** the evidence names each test command the repo asks for with its outcome, or says why one could not be run. | required |
| diff-clean | The diff's added and removed lines, read hunk by hunk (live: `git diff main...HEAD`). | **Passes when** the diff holds no debris: no debug output left in, no commented-out code, no dead code, and no hunk that only reformats, reorders, or re-prints lines the change does not need. | required |
| template-asks-met | The repo facts' pull-request line (the template's required sections, checklist items, issue link, and any changelog or release-note entry), read against the description and the diff (live: the repo's `.github/PULL_REQUEST_TEMPLATE.md` and `docs/CONTRIBUTING.md`, with every section of the template filled in). | **Passes when** every ask the repo states is met in the description or the diff, and each section the template carries has real content, or the repo states no template or asks. | required |
| ai-disclosure | The contribution-policy line of the repo facts (live: also the AI-use disclosure the scope's template rule asks for), read against the description. | **Passes when** the policy does not require AI-use disclosure in a PR, or the description states that AI was used and how. | required |

## Verdict rule

<!-- State how the grades above combine into accept or reject, and how
unclear is treated. Example shape (write your own): "accept if every
required check passes; preferred checks never change the verdict;
unclear counts as fail." -->

Accept only when every `required` check passes, and a single `fail` on a required check rejects the PR. `preferred` checks never change the verdict. `unclear` on a required check counts as `fail`, and `unclear` on a preferred check is ignored. A shortfall the PR discloses is not a failure: the pass conditions above already count a deferral stated in the plan or the description as covered. When more than one required check fails, quote the evidence for the first failed check in the table's order.
