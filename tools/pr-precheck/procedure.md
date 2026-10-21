# Procedure: how this tool grades a PR package

## Read order

1. In eval mode, use only the bundle text and fetch nothing. In live mode, read `plan.md` (with its `## Deviations`), the output of `git diff main...HEAD` and the branch's commit list, `pr_draft.md`, and `test_evidence.md`, plus the issue thread, `.github/PULL_REQUEST_TEMPLATE.md` and `docs/CONTRIBUTING.md`. Treat nothing else in the working directory as part of the package.
2. Read **Repo facts** first (live: the template and CONTRIBUTING). Write down each ask the repo states: the template's sections and checklist, the issue link, any changelog or release-note entry, the test commands it asks for, and whether the contribution policy requires AI-use disclosure in a pull request (a rule that only asks for comments in the author's own words does not count). Read it first so the PR is judged against what the repo asked, not against what the PR chose to show.
3. Read the **Plan context** (live: `plan.md`) before opening the diff. Write down the in-scope deliverables, the not-in-scope line, the files named, every deferral, any deviation, and the test plan with each scenario it names. The plan is the yardstick for every comparison that follows, so read it before the diff and before the description.
4. Read the **Diff** and the **Commits** (live: `git diff main...HEAD` and its `--stat`). Write down every changed file, and for each hunk whether it adds or changes behavior, an option, a file or a function, or only reformats, reorders, comments out or prints. Write down any debug output, commented-out code, or dead code.
5. Read the **Test evidence** (live: `test_evidence.md`). Write down each command that was run, its output, and which plan scenario each one exercises, before and after.
6. Read the **Title** and **Description** last (live: `pr_draft.md`), after everything it has to be checked against. Write down every claim about what the change does or leaves out, every template section and whether it has real content, and any statement about AI use.

## Evidence gathering

1. For `diff-within-plan`, list every hunk from the read-order notes that adds or changes behavior, an option, a file or a function, and for each one copy the plan line or the deviation that covers it, or record "uncovered". Then list each deliverable the plan names and record where it appears in the diff, or "absent", and whether the plan or description states it as deferred.
2. For `description-matches-diff`, copy each claim the description makes about the change ("exactly as planned", "docs updated", "no other changes") and record whether the diff bears it out, or contradicts it by naming the hunk or the missing deliverable. Record any plan item the diff lacks and whether the description says it was deferred.
3. For `repro-before-after`, list the plan's repro steps and each scenario the test plan names. For each one copy the evidence's before output and after output, or record "no output shown". Note whether the output comes from the path the fix changes or from a control or a different scenario.
4. For `repo-checks-shown`, list the test commands the repo asks for (from the read-order notes). For each one copy the command and its outcome from the evidence, or the stated reason it could not run, or record "not shown". A line that only says "tests pass" with no command named is "not shown".
5. For `diff-clean`, go back to the debris notes from the read order and list each one with its file and line: debug output, commented-out code, dead code, formatting or re-print hunks. Record "none" if there are none.
6. For `template-asks-met`, take each ask from the read-order notes (step 2) and copy where the description or diff meets it, or record "unmet". For each template section copy a line of its content, or record "empty or left as the template's comment". If the repo states no template and no asks, record "none stated".
7. For `ai-disclosure`, take the policy result from read-order step 2 and copy the description's statement about AI use (what tool was used and how), or record that it has none.

## Check execution

1. Run the checks in the order the rubric lists them, grading each one from the notes gathered for it.
2. Grade `pass` only when the check's pass condition is met as written, and a check that meets its condition passes even if the PR feels weak overall (a terse PR can be ready).
3. Grade `fail` when the notes show the pass condition is not met, including when the PR has no text at all for what the check reads (no test evidence, no description, no plan line to compare against).
4. Grade `pass` for `template-asks-met` when the repo states no template and no asks, and for `ai-disclosure` when the policy does not require AI-use disclosure in a pull request.
5. Treat a deviation or deferral stated in the plan or the description as covered: it keeps `diff-within-plan`, `description-matches-diff` and `repro-before-after` from failing on the thing it names. A difference that appears only in the diff, or only in the evidence, is not disclosed.
6. Grade `unclear` when the package does not hold what the check needs to be decided (for example, no plan at all, or a diff that is cut off) or when two honest readings of the notes give different grades.
7. Do not re-read the whole package to grade a check unless that check's notes are empty or contradict each other.
8. Write one line of evidence per check that quotes the package (a hunk, a command and its output, a sentence from the description), not a summary or a feeling.

## Verdict assembly

1. List the grade of every check.
2. If any `required` check graded `fail` or `unclear`, the verdict is `reject`. If every `required` check graded `pass`, the verdict is `accept`, and `preferred` checks never change it.
3. In the output, put the evidence for the first failed required check in the rubric's table order first, quoted from the package.
4. Put the JSON block last, with one entry per check and the verdict, and add any step this procedure did not cover to the readable summary above it.
