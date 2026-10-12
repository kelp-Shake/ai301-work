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

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/17#issuecomment-6116829252

Reproduced the mechanism behind #17 in isolation: when the process running `Orchestrator.run` dies partway through, nothing from the tools that already finished is in Redis, and the next run starts over. I could not reproduce it through the API, because at this commit the API does not call the orchestrator (details at the end). I ran it in my own environment against `agent/orchestrator.py` and `agent/memory/session_store.py`. AI disclosure: I used Claude Code to help write the repro script and read the code, and I ran everything below myself.

**What I think causes it** (code read, not yet tested beyond this repro): `Orchestrator.run` collects tool results in a local `results` dict and calls `session_store.set` once, after the whole tool loop (`agent/orchestrator.py` lines 65-68). `ContextManager` is only a dict (`self.results = {}`) and has no Redis code, so it cannot persist anything either. This corrects my claim comment, which said `context_manager.py` writes to Redis. The single Redis write is in the orchestrator.

**Environment**
- Repo: `kelp-Shake/pathreview-ai301-fa26-s1`, commit `f89c06f` (`f89c06fc3ff292df2a04a39ac51319d32a76b779`), unmodified apart from `frontend/package-lock.json` changed by `npm install`.
- macOS 26.6.2 (Apple Silicon), Python 3.14.5, redis-py 8.1.0.
- Redis `redis:7-alpine` (server 7.4.10) and Postgres `postgres:16-alpine`, started with `docker compose up -d` in the repo (Colima).
- Setup from `docs/SETUP.md`: `cp .env.example .env`, `docker compose up -d`, `make setup`. I used the default `REDIS_URL=redis://localhost:6379/0`; the script uses scratch database 15 on that Redis and flushes it.

**Steps**
1. Save the script below as `repro17.py`.
2. From the repo root run:
   `.venv/bin/python repro17.py 2>&1 | grep -E "^(run|calls|redis|B )"`

The script uses stub tools that return `{"tool": name, "ok": True}`, a real `Orchestrator` and a real `SessionStore` on Redis. The plan is `tech_detector`, `readme_scorer`, `skill_extractor`, `market_analyzer`. In run 1 the third tool, `skill_extractor`, dies. Part A raises `KeyboardInterrupt` in the same process. Part B kills a child process with `SIGKILL`. A fresh `Orchestrator` then runs the same profile.

```python
import os
import signal
import subprocess
import sys

import redis
from agent.orchestrator import Orchestrator
from agent.memory.session_store import SessionStore

r = redis.Redis.from_url("redis://localhost:6379/15")  # scratch db index
store = SessionStore(r)
calls = {}

class Tool:
    def __init__(self, name, die=False):
        self.name, self.die = name, die
    def execute(self, inp):
        calls[self.name] = calls.get(self.name, 0) + 1
        if self.die:
            raise KeyboardInterrupt("simulated process kill")
        return {"tool": self.name, "ok": True}

profile = {"files": ["a.py"], "readme_content": "# x", "resume_text": "python"}
def tools(die_on=None):
    return {n: Tool(n, n == die_on) for n in
            ["tech_detector", "readme_scorer", "skill_extractor", "market_analyzer"]}

# Child mode (used by part B): run the plan in a separate process whose 3rd tool
# kills the whole process with SIGKILL, so nothing gets a chance to clean up.
if len(sys.argv) > 1 and sys.argv[1] == "child":
    class KillTool(Tool):
        def execute(self, inp):
            print("child: running", self.name, flush=True)
            if self.die:
                os.kill(os.getpid(), signal.SIGKILL)
            return {"tool": self.name, "ok": True}

    ts = {n: KillTool(n, n == "skill_extractor") for n in
          ["tech_detector", "readme_scorer", "skill_extractor", "market_analyzer"]}
    Orchestrator(ts, store).run("p2", profile)
    sys.exit(0)

# ---- Part A: simulated kill (exception in the same process) ----
r.flushdb()

# run 1: dies while running skill_extractor (3rd of 4 tools)
try:
    Orchestrator(tools("skill_extractor"), store).run("p1", profile)
except KeyboardInterrupt:
    print("run 1 interrupted")
print("calls after run 1:", calls)
print("redis after run 1:", store.get("p1"), "keys:", r.keys("*"))

# run 2: new Orchestrator = restart
calls.clear()
Orchestrator(tools(), store).run("p1", profile)
print("calls after run 2 (restart):", calls)
r.flushdb()

# ---- Part B: real kill (SIGKILL to a child process, then a fresh process runs again) ----
proc = subprocess.run([sys.executable, os.path.abspath(__file__), "child"],
                      capture_output=True, text=True)
ran = [l.split()[-1] for l in proc.stdout.splitlines() if l.startswith("child: running")]
print("B child exit code:", proc.returncode, "(-9 = killed by SIGKILL)")
print("B tools started in child:", ran)
print("B redis after kill:", store.get("p2"), "keys:", r.keys("*"))

calls.clear()
Orchestrator(tools(), store).run("p2", profile)
print("B calls in fresh process after kill:", calls)
r.flushdb()
```

**Observed output** (identical on three runs, including after `make setup`)
```
run 1 interrupted
calls after run 1: {'tech_detector': 1, 'readme_scorer': 1, 'skill_extractor': 1}
redis after run 1: None keys: []
calls after run 2 (restart): {'tech_detector': 1, 'readme_scorer': 1, 'skill_extractor': 1, 'market_analyzer': 1}
B child exit code: -9 (-9 = killed by SIGKILL)
B tools started in child: ['tech_detector', 'readme_scorer', 'skill_extractor']
B redis after kill: None keys: []
B calls in fresh process after kill: {'tech_detector': 1, 'readme_scorer': 1, 'skill_extractor': 1, 'market_analyzer': 1}
```
`tech_detector` and `readme_scorer` finished before the kill, yet Redis holds no session key afterward, and the fresh process runs both again.

**What this shows and what it doesn't**
- Shows: the in-progress state from finished tools is lost when the process dies, which matches the issue's "not written to Redis until completion".
- Differences from the issue: it calls `Orchestrator.run` directly, not through the API server, and uses stub tools, not the real GitHub or LLM tools. The issue also describes reviews with 5+ repositories, but `_build_plan` only plans the first repo (`break  # Only process first repo for now`), so I used a four-tool plan.
- Not reproducible through the API at this commit (from reading the code, not from running it): `POST /reviews` in `api/routes/reviews.py` starts `process_review` in `core/services/review_service.py` as a `BackgroundTasks` job, and that calls `_run_agent_orchestration`, which is a placeholder (`# Placeholder: actual agent orchestration logic`) returning a hardcoded dict. Nothing under `api/`, `core/`, `rag/`, `ingestion/` or `scripts/` references `Orchestrator` or `SessionStore`, so an API restart does not lose orchestrator state today. The issue's scenario only applies once that placeholder is wired to the orchestrator.
- Not tested: whether a completed run is resumed correctly, and what an API restart does to an in-flight `BackgroundTasks` review (I expect its review row to stay at `processing`, but I haven't run it).

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
