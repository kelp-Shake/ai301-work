# Rubric: is this plan ready to post and build from?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever
checks you define here (via your procedure.md). It ships empty on
purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the plan's scope statement, the test plan read against
     the repro evidence's steps, the plan comment read against the
     thread highlights, the repo-facts block) or a location from your
     references/evidence-guide.md. "The plan" is not a source; "the
     plan's stated cause read against what the repro evidence shows"
     is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself (is
     this one bounded change? could a stranger start executing it?),
     never the write-up's shape (how many sections it has, how long it
     is, whether it uses headings). Structure-shaped checks are what
     make graders disagree with themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (ready) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. If you write no rule for
   `unclear`, the skill treats it as fail.

Cover what actually gets bad plans posted. The lecture named the
failure families: the diagnosis ignores or contradicts the reproduced
evidence, the change is unbounded (scope creep), the plan targets the
symptom while the evidence points at the cause, a stranger could not
start executing it, the test plan proves nothing observable, the
unknowns are dressed up as certainty, and the comment ignores what the
thread or the repo's stated conventions ask. A rubric that ignores a
family will fail eval packages designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| diagnosis-consistent | The plan's stated cause, read against the repro evidence's steps, controls, and outputs. | **Passes when** no result in the repro evidence (such as a control run or a variant that still fails) contradicts the stated cause. | required |
| diagnosis-evidenced | The plan's stated cause, read against what the repro evidence shows. | **Passes when** the plan ties its cause to something the repro evidence shows, not to a guess or to a theory from the issue thread. | required |
| scope-bounded | The plan's scope statement, read against the issue's title and body. | **Passes when** the plan describes one change that fixes the reported behavior and adds no unrelated work. | required |
| scope-fenced | The plan's scope statement. | **Passes when** the plan says what it leaves alone, including any part of the issue it defers. | required |
| buildable-by-a-stranger | The plan's files and approach, read as if by someone who has not seen the repo. | **Passes when** the plan names the area of code to change (a file, module, or function) and what the change is, so a stranger would know where to start. | required |
| test-decisive | The plan's test plan, read against the repro evidence's steps. | **Passes when** the test plan re-runs the repro steps and states the output expected after the fix. | required |
| unknowns-honest | The plan's risks and unknowns, read against what the repro evidence actually tested. | **Passes when** anything the plan relies on but the repro did not test is labeled as unconfirmed. | preferred |
| comment-faithful | The plan comment, read against the plan. | **Passes when** the comment states the cause, the change, and the test, and promises nothing the plan does not contain. | required |
| thread-direction | The thread highlights, read against the plan comment and the plan. | **Passes when** every explicit maintainer direction in the thread (a constraint, a preferred approach, a limit) is engaged or respected. | required |
| ai-disclosure | The contribution-policy line of the repo-facts block, read against the plan comment. | **Passes when** the policy does not require AI disclosure in comments or issues, or the comment states that AI assistance was used. | required |

## Verdict rule

Accept only when every `required` check passes, and a single `fail` on a required check rejects the plan. `preferred` checks never change the verdict. `unclear` on a required check counts as `fail`, and `unclear` on a preferred check is ignored. When more than one required check fails, quote the evidence for `diagnosis-consistent` first if it failed.
