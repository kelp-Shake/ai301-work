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

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/17#issuecomment-6117552702

Plan for #17, building on my repro above.

**What I found:** `Orchestrator.run` in `agent/orchestrator.py` writes to Redis once, after the whole tool loop. In my repro, killing the third of four tools (with `KeyboardInterrupt` and with `SIGKILL`) left `redis after kill: None`, and the next run executed `tech_detector` and `readme_scorer` again. From reading the code (not yet tested), there is a second gap: `run` loads the stored session state but never uses it to skip a finished tool, so a per-tool write alone would not be enough.

**What I'll do:** in the tool loop of `Orchestrator.run`, (1) write each tool's result to Redis as soon as it succeeds, and (2) skip a tool on restart when Redis already holds a successful result for it with the same input hash. The change is in `agent/orchestrator.py`, plus one new unit test in `tests/unit/`.

**Not doing:** wiring the API to the orchestrator (`_run_agent_orchestration` is still a placeholder), or any change to `ContextManager`, `SessionStore` or the TTL.

**How I'll prove it:** re-run my `repro17.py` from the repro comment. After the fix, `redis after kill` should hold the two finished tools' results, and a restarted run should call only `skill_extractor` and `market_analyzer`.

**Unknowns:** I haven't tested whether the real tools' results serialize to JSON (the repro used stubs), and `market_analyzer`'s input is constant, so its input hash won't catch changes upstream. I'll flag both in the PR.

AI disclosure: I'm using Claude Code to help plan and build this, and I read every diff before keeping it.

---

## Your branch

**Branch**

fix/17-persist-tool-progress

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
