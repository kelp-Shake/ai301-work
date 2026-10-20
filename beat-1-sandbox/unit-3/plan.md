# Plan: persist agent progress per tool so a restart can resume (issue #17)

Issue: https://github.com/codepath/pathreview-ai301-fa26-s1/issues/17
Repro comment: https://github.com/codepath/pathreview-ai301-fa26-s1/issues/17#issuecomment-6116829252
Base commit: `f89c06f`

## Diagnosis

`Orchestrator.run` in `agent/orchestrator.py` collects tool results in a local `results` dict and calls `session_store.set` once, after the whole tool loop (the "Persist state" block). If the process dies partway through, nothing from the tools that already finished has been written to Redis.

My repro shows this. I killed the third of four tools (`skill_extractor`) with a `KeyboardInterrupt` (part A) and with `SIGKILL` on a child process (part B). Quoting the output:

```
calls after run 1: {'tech_detector': 1, 'readme_scorer': 1, 'skill_extractor': 1}
redis after run 1: None keys: []
calls after run 2 (restart): {'tech_detector': 1, 'readme_scorer': 1, 'skill_extractor': 1, 'market_analyzer': 1}
B child exit code: -9 (-9 = killed by SIGKILL)
B redis after kill: None keys: []
B calls in fresh process after kill: {'tech_detector': 1, 'readme_scorer': 1, 'skill_extractor': 1, 'market_analyzer': 1}
```

`tech_detector` and `readme_scorer` finished before the kill, yet Redis holds no session key and the fresh run executes both again.

There is a second gap, from reading the code and not yet tested: `run` loads `session_state` from the store at the start, but nothing uses it to skip a tool. So writing results earlier is not enough on its own. A restarted run would still re-run every tool. The fix needs both a per-tool write and a skip on restart.

`ContextManager` is only an in-memory dict and has no Redis code, so it is not where the fix goes (this corrects my claim comment).

## Scope

**In:** the tool loop in `Orchestrator.run` (`agent/orchestrator.py`):
1. After each tool finishes successfully, write its result into the session state in Redis right away, instead of once at the end.
2. Before running a tool, skip it and reuse its stored result when the stored session state has a successful result for that tool with the same input.

**Not in:**
- Wiring the API to the orchestrator. At this commit `_run_agent_orchestration` in `core/services/review_service.py` is a placeholder, so an API restart does not lose orchestrator state today.
- Any change to `ContextManager` or `SessionStore` (including the 1-hour TTL).
- `_build_plan`, including the "first repo only" limit.
- Retry or timeout behavior, and the tools themselves.
- Making failed tools resumable beyond re-running them.

## Files

- `agent/orchestrator.py` (the tool loop in `run`)
- `tests/unit/test_orchestrator_resume.py` (new: one unit test with an in-memory stand-in for the store)

## Approach

1. Keep the stored shape as it is today: tool name mapped to the tool's result. Add one extra key, `_inputs`, mapping tool name to the hash of the input it ran with (using the existing `ContextManager.hash_input`).
2. In the loop, before calling `_execute_tool`, check the loaded `session_state`. If it has a result for this tool, the result is not an error entry (`{"error": ..., "success": False}`), and `_inputs[tool_name]` equals the hash of the current input, use the stored result and do not run the tool.
3. After a tool succeeds, put its result and input hash into `session_state` and call `session_store.set(profile_id, session_state)` immediately.
4. Failed tools are not written, so they run again on restart. The final return value stays the same shape as today.
5. Keep the final write after the loop only if it is still needed, so a completed run still leaves a complete state.

The input hash is there so that a later run for the same profile with changed data does not silently get old results. This is the one design choice I want a reviewer's opinion on.

## Test plan

Re-run my unit 2 repro unchanged, `.venv/bin/python repro17.py 2>&1 | grep -E "^(run|calls|redis|B )"`, from the repo root against Redis (scratch db 15), and compare with the "before" output above.

Expected after the fix:
- `redis after run 1:` shows a stored session (not `None`) containing results for `tech_detector` and `readme_scorer`, and the key list has `session:p1`.
- `calls after run 2 (restart):` is `{'skill_extractor': 1, 'market_analyzer': 1}` (the two finished tools are not run again).
- `B redis after kill:` shows the same two stored results, not `None`.
- `B calls in fresh process after kill:` is `{'skill_extractor': 1, 'market_analyzer': 1}`.

Also run `make test-unit` to check that the existing unit tests and the new one pass.

## Risks and unknowns

- Not tested: whether the real tools' results survive `json.dumps`. `SessionStore.set` swallows serialization errors (it logs `session_set_error`), so a result that cannot be serialized would silently not be saved and that tool would just re-run. My repro used stubs that return plain dicts.
- Not tested: what an API restart does to an in-flight `BackgroundTasks` review. It is out of scope here and depends on the placeholder being wired up.
- `market_analyzer` takes a constant input (`{"detected_skills": {}}`), so its input hash will match even if the tools before it produced different results. It could be reused when it should not be. I will note this in the PR rather than change how that input is built.
- A tool that was mid-run when the process died runs again, so execution is at-least-once for that tool.
- The issue describes reviews of 5+ repositories, but `_build_plan` only plans the first repo, so I am testing with a four-tool plan.

## Deviations

The approach held. Two small differences from what I wrote:

- I removed the single write after the tool loop instead of keeping it. Step 5 said to keep it only if it was still needed. Every successful tool now saves itself right after it runs, so a finished run already leaves a complete state and the last write did nothing.
- The Files section said one unit test. I wrote two in `tests/unit/test_orchestrator_resume.py`: resume after a kill, and a tool re-running when its input changed. The second one checks the input hash, which is the design choice I asked a reviewer about.

Nothing else changed. I did not touch `ContextManager`, `SessionStore`, `_build_plan`, or the API wiring, and the repro gave the four expected results.
