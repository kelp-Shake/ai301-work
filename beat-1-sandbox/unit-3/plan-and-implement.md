# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

Record of your plan, the branch you built it on, and the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in the
repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Posted upstream

**GitHub username**

kelp-Shake

**Plan comment**

[Link to the comment where you posted your plan on the issue. Use the comment's own
permalink. **Then paste the text of that comment underneath the link** — the pasted text is
what this field is graded on, so copy across what you actually posted.]

---

## Your branch

**Branch**

[The name of the branch you built the change on, exactly as it appears in your fork. The
naming shape is a type prefix, then the issue number, then a short description. **The issue
number in the branch name must be the number of the issue you claimed** — a name carrying
any other number does not satisfy this field.]

**Evidence**

[Your Unit 2 reproduction steps re-run against the built change: the before, then the
after. Paste both, including the commands you ran and their output.]

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. Run 1: 19/20. `pkg-14` was the only disagreement (gold accept, my rubric reject).
2. Run 2: 20/20, after rewording `buildable-by-a-stranger`. This matches the agreement line in `eval-run.txt` ("agreement: 20/20 scored items (bar: 18/20: PASS)").

**Package analysis**

`pkg-14` (zellij-org/zellij#5174, the OSC color sequences leaking on reattach). The gold label is accept. In run 1 my rubric said reject, so it disagreed. In run 2 it said accept, so it agrees.

In run 1 every check passed except `buildable-by-a-stranger`, and the grader's evidence was: "exact functions to be pinned in the PR after tracing the query issuance with debug logs" — only module-level locations named; a stranger cannot make the first edit without asking which file or function to open." My rubric read it that way because the old pass condition said the plan had to name "the files or functions to change" so that "a stranger could start the first edit without asking a question". The plan named the area (the reattach path in `zellij-server`'s session connection handling and `zellij-client`'s terminal query issuance) and the change (drain pending OSC color responses before pane input is wired), but not exact functions, so the grader failed it.

The gold label says accept because the plan is honest about what is not pinned yet and still tells a reader where to start and what to do, which is different from a plan that names nothing. I changed the check, and in run 2 the grader's evidence was: "Modules named: 'zellij-server (session connection handling)' and 'zellij-client's terminal query issuance'; change is 'drain OSC responses before pane input is wired' — sufficient for a stranger to locate and start." The verdict became accept.

**Check rationale**

The check as it reads in `tools/plan-check/rubric.md`:

| buildable-by-a-stranger | The plan's files and approach, read as if by someone who has not seen the repo. | **Passes when** the plan names the area of code to change (a file, module, or function) and what the change is, so a stranger would know where to start. | required |

It reads that way because of `pkg-14`. My first version said "**Passes when** the plan names the files or functions to change and what the change is, so a stranger could start the first edit without asking a question." That was too strict: it failed a plan that named the modules and the exact change but left the function names for tracing in the PR. I rejected keeping the strict wording, because it made the check grade whether the plan had already finished the investigation, which is not what "buildable" should mean. I also rejected dropping the check, since the unbuildable packages need it to be rejected. I changed it to "area of code (a file, module, or function)" and "would know where to start", so a plan with a located area and a stated change passes, and a plan with no location at all still fails.

**Trade-offs**

Loosening `buildable-by-a-stranger` gives up some precision: a plan that names only a module and a general change now passes, where the old wording would have held it for not naming a function. A vague plan that happens to name a module could slip through, and I accept that, because the check only needs to separate "no idea where to start" from "knows where to start".

I did not re-run canaries with `--only`. I went straight to a second full run, so the evidence that nothing else flipped is the run itself. All 20 packages agreed, and the three `unbuildable` packages still rejected on this same check: `pkg-10` ("No file, module, or function named; 'investigate the git modules' performance' gives a stranger nowhere to start."), `pkg-17` ("Plan writes '(gocui? tcell? not sure which layer is responsible)' — no files, modules, or functions named"), and `pkg-18` ("add a recover() safety net somewhere around linter execution" — no file, module, or function named anywhere in the plan"). That shows the looser wording still separates them from `pkg-14`.

---

Related paths: `plan.md` and `eval-run.txt` in this directory; your skill's files in
`tools/plan-check/`.
