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
