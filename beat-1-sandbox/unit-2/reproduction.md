# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

Record of your claim and reproduction on the issue you chose in Unit 1, and of the
evaluation runs that produced `eval-run.txt`. This file is graded at the path above; a copy
kept anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your identity upstream

**GitHub username**

kelp-Shake

---

## Posted upstream

**Claim comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/17#issuecomment-5986965058

I'm claiming this issue. I think the problem is that session state is only held in memory and isn't written to Redis until a review completes, so a restart loses progress, but I haven't confirmed that yet. I'm looking at where `agent/memory/context_manager.py` holds that state before it's written to Redis. Next I'll read how `context_manager.py` and `agent/orchestrator.py` handle it, try to reproduce the lost progress, and post a report with what I find. This is my first contribution here.

**Reproduction comment**

Not completed yet.

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

1. `--limit 3` smoke test: 3/3 (partial run).
2. Full run with `--include-calibration`: 18/20 scored. Disagreements: pkg-03 (failed `ai-disclosure`), pkg-05 (failed `steps-rerunnable`), and calib-01 (unscored, failed `claimed-work`).
3. After narrowing `ai-disclosure`, `--only pkg-03,pkg-20,pkg-07`: 3/3 (partial run).
4. Confirming full run saved with `--save-run`: 19/20 (agreement line: `agreement: 19/20 scored items  (bar: 18/20: PASS)`).

**Package analysis**

**pkg-05** (conda/conda#16543). Gold: accept. My rubric: reject, failing only `steps-rerunnable` (in both full runs).

The report says it "wrote a minimal `env.yml` containing a valid `dependencies:` list plus a `category:` section" and then shows the commands and output, but it never pastes the file. My check passes only when "every command, input file, and config a stranger would need is shown in the report or points to the issue's own text". An input file that is only described is not shown, so the grader failed it: "env.yml content is described verbally but never pasted; a stranger cannot reproduce without knowing the exact YAML structure." The gold note calls it a "minimal env.yml repro", so gold read the description as enough to recreate the file. I read it more strictly than gold did. Every other check passed (artifact, target, environment, claim, claimed-work, ai-disclosure). I left it as is rather than loosening the check: a looser wording could let a private input through, and pkg-18 (private monorepo, gold reject) is only caught by this check.

**Check rationale**

`ai-disclosure`, quoted exactly as it reads in `tools/repro-check/rubric.md`:

```
| ai-disclosure | The "contribution policy" line of the repo-facts block, read against the text of the claim comment and the repro report. Treat the package as AI-assisted work. | **Passes when:** the policy line does not require AI use to be disclosed in issue comments.<br>**Passes when:** a comment states that AI assistance was used.<br>**Fails when:** the policy explicitly tells contributors to disclose AI use in comments or issues, and neither comment discloses.<br>**Note:** a requirement that covers only pull requests does not apply here.<br>**Note:** a rule that comments be written by a human in their own words is not a disclosure requirement. | required |
```

It first said the policy fails the package when it "requires disclosure in comments or issues". On the first full run that failed pkg-03 (ripgrep), whose policy says comments "must be written by humans in their own words, and AI-generated comments may be hidden". The grader read that as a disclosure requirement, but gold accepts it because a human-voiced comment satisfies the rule. I narrowed the fail condition to a policy that "explicitly tells contributors to disclose AI use in comments or issues" and added the note that a human-written-comments rule is not a disclosure requirement, rather than deleting the check. The check stays because pkg-20 (ghostty, all AI use must be disclosed) is the only package in the disclosure category, and without it the category floor cannot be met.

**Trade-offs**

Narrowing `ai-disclosure` could have loosened it, so I re-ran `--only pkg-03,pkg-20,pkg-07` as a canary before the confirming run: pkg-03 flipped to accept, pkg-20 stayed reject, and pkg-07 (which discloses) stayed accept. The cost is that a policy which implies disclosure without saying so will now pass. A case I accept it misses: `steps-rerunnable` rejects pkg-05, which gold accepts, and I chose not to loosen it. `claimed-work` also rejects calib-01 (unscored), whose claim says it will "make the untracked-only case either warn or stash with `--include-untracked`", because the check fails a claim that promises a fix; gold accepts that claim.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/repro-check/`.
