# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

Record of the pull request you opened against the Path Review repo, and of the evaluation
runs that produced `eval-run.txt`. This file is graded at the path above; a copy kept
anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s1/pull/233

**Branch**

fix/17-persist-tool-progress

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

I did one full run, and it scored 20/20 (the bar is 18/20, and every category matched, with standards-wall 2/2). That is the run saved in `eval-run.txt`, so its agreement line is the last score here: 20/20. I changed no rubric, procedure, evidence guide or SKILL.md after it. Afterward I re-graded `pkg-17` on its own with `--only` to read its per-check output. That was a partial run (1/1), so it is not a second scored run and it did not touch `eval-run.txt`.

**Package analysis**

`pkg-17` (silent-drift). The gold label is `reject` and my rubric said `reject`, so they agree. The plan promised two deliverables: a dev-mode warning in `reactive.ts` and an update to the reactivity-core docs page. The diff has only the warning and its test, and the description says the docs "now document the limitation". Three checks failed. `diff-within-plan` failed with: "Plan names the reactivity-core documentation page as a deliverable; no docs file appears in the diff; description does not state a deferral". `description-matches-diff` failed because the description's docs claim is contradicted by the diff. My rubric read it this way because a deliverable that is missing from the diff only passes when it is stated as deferred, and here the description claimed it was done instead. The third failure, `repro-before-after`, I did not plan for: the evidence shows the dev warning firing but no before output of the silent skip, and no stated reason. The gold note only names the docs claim, so I think that third failure is a stricter reading by my check than the instructor's, but I have not confirmed that.

**Check rationale**

`diff-within-plan`, exactly as it reads in `tools/pr-precheck/rubric.md`:

| diff-within-plan | The diff's changed files and hunks, read against the plan's in-scope list, its not-in-scope line, and any recorded deviation (the plan's `## Deviations` section, or a deferral the plan or description states). | **Passes when** every code hunk that adds or changes behavior, an option, a file, or a function is covered by the plan or a recorded deviation, and every deliverable the plan names is either in the diff or stated as deferred. | required |

I wrote it this way because the failure is the diff and the plan disagreeing without anyone saying so, and the cases that go the other way look the same on the page. `pkg-13` and `pkg-16` are accepts where the plan and the description both state a deferral, so a check that only asks "does the diff equal the plan" would reject them. That is why a "recorded deviation" or a stated deferral counts as covered, and why a missing deliverable passes only if it is stated as deferred. I limited it to hunks that add or change behavior, an option, a file, or a function, so that reformatting churn is left to `diff-clean` and is not counted twice. I did not revise it after the run, because it agreed on the drift packages the first time. I have not run a canary on it.

**Trade-offs**

The cost of `diff-within-plan` is that anything recorded as a deviation passes, whatever its size. It checks that the diff and the plan agree, not whether the deviation was a good idea, so a package that stated a large extra change honestly would pass this check and would have to be caught by some other check or a human. It also only reads hunks that add or change behavior, so a rewrite that only reformats code is left to `diff-clean`. I did not change any other file after the full run, and the run was 20/20, so I have no package whose result this check changed. I also have not run any canary with `--only`, so a package that a later loosening of this check would flip is not something I have tested.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/pr-precheck/`.
