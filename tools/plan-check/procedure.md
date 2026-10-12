# Procedure: how this skill grades a plan package

<!--
THIS IS THE PART YOU WRITE, and it is a new kind of part. Weeks 1 and
2, SKILL.md carried a numbered workflow and you only wrote judgment
files. This week the workflow is gone from the frame: SKILL.md says
"execute procedure.md", and these are the operating steps you author.
The machinery is in your hands now.

Your operator swap is the design brief. When your executor stalled
because your rubric said WHAT to decide but not HOW to find the
evidence, that was a procedure gap. This file is where those gaps get
closed: a complete procedure lets someone who has never seen a plan
package before (a groupmate, or the skill itself) grade one exactly the
way you would.

Under each stage heading below, write the concrete steps for that
stage. The one-line note under each heading says what a complete
procedure must decide there. Write steps, not intentions: "read the
repro evidence before the plan, and note what behavior it pins down"
is a step; "understand the context" is a wish.
-->

## Read order

1. In eval mode, use only the bundle text and fetch nothing. In live mode, read the drafts (`plan.md`, `comment.md`), the issue thread, and the author's posted repro comment, and treat nothing else in the working directory as part of the package.
2. Read the **Repro evidence** first. Write down the steps that were run, every output, every control or variant run (and what each one rules in or out), and the expected-versus-actual line. Read it first so the plan is judged against what was observed, not against the plan's own framing.
3. Read the **Issue** next. Write down the one behavior it reports, from its title and body.
4. Read the **Thread highlights**. Write down each maintainer or collaborator line that gives direction (a constraint, a preferred approach, a limit on what to try), and mark theories from other commenters as theories, not facts.
5. Read the **Repo facts**. Write down the contribution-policy line, and whether it requires AI-use disclosure in comments or issues (a pull-request-only rule, or a rule that comments be in the author's own words, does not count as a disclosure requirement).
6. Read the **Candidate plan**. Write down its stated cause, its in-scope and not-in-scope lines, the files or functions it names, its approach, its test plan, and its risks.
7. Read the **Candidate plan comment** last, after everything it has to be checked against.

## Evidence gathering

1. For `diagnosis-consistent`, copy the plan's cause sentence word for word, then list each result in the repro evidence and mark any result the stated cause cannot explain.
2. For `diagnosis-evidenced`, find the plan sentence that ties the cause to a result in the repro evidence and copy it, or record that the cause rests only on a guess ("probably", "somewhere in") or on a thread theory ("as identified in this thread").
3. For `scope-bounded`, list every change the plan says it will make, and for each one note whether the issue's reported behavior needs it.
4. For `scope-fenced`, copy the plan's not-in-scope line or its statement of what it defers, or record "none stated".
5. For `buildable-by-a-stranger`, copy the file or function names and the description of the change, or record that none are given.
6. For `test-decisive`, copy the test plan, then record whether it re-runs the repro steps and what output it says to expect after the fix.
7. For `unknowns-honest`, copy the plan's risks or unknowns, then list anything the plan relies on that the repro evidence did not test, and note whether each is labeled unconfirmed.
8. For `comment-faithful`, list every promise and every claim in the plan comment, and for each one find the plan line that backs it.
9. For `thread-direction`, take the maintainer directions from step 4 of the read order and, for each one, copy the comment or plan line that engages it, or record that none does. If the thread has no maintainer direction, record "none in thread".
10. For `ai-disclosure`, take the policy result from step 5 of the read order and copy the comment's statement about AI use, or record that it has none.

## Check execution

1. Run the checks in the order the rubric lists them, grading each one from the notes gathered for it.
2. Grade `pass` only when the check's pass condition is met as written, and a check that meets its condition passes even if the plan feels weak overall.
3. Grade `fail` when the notes show the pass condition is not met, including when the plan has no text at all for what the check reads (no test plan, no scope line, no files named).
4. Grade `pass` for `thread-direction` when the thread has no maintainer direction, and for `ai-disclosure` when the policy does not require disclosure in comments or issues.
5. Grade `unclear` when the package does not hold the evidence the check needs to be decided (for example, no repro evidence block at all) or two honest readings of the notes give different grades.
6. Do not re-read the whole package to grade a check unless that check's notes are empty or contradict each other.
7. Write one line of evidence per check that quotes the package, not a summary or a feeling.

## Verdict assembly

1. List the grade of every check.
2. If any `required` check graded `fail` or `unclear`, the verdict is `reject`.
3. If every `required` check graded `pass`, the verdict is `accept`, and `preferred` checks never change it.
4. In the output, write the deciding check's evidence first (the failed `diagnosis-consistent` evidence if it failed, otherwise the first failed required check in rubric order), quoted from the package.
5. Put the JSON block last, with one entry per check and the verdict, and add any step this procedure did not cover to the readable summary above it.
