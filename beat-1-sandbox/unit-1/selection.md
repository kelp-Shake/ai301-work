# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in
the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the
wrong label is not graded.

---

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/17

**Verdict output**

Live-mode run of 2026-09-26, grading three candidates from the Path Review repo.
`gh` was not installed on this machine, so the skill gathered its evidence by
fetching the issue, commit and CONTRIBUTING pages directly.

```
All three candidates are inside the scoped repo (codepath/pathreview-ai301-fa26-s1). Applying the Path Review house rule (classmate claim comments do not block) is moot - none of them have claim comments anyway.

Repo facts (captured 2026-09-26): not archived, 3 stars, no releases (passes), last commits Sep 16 / Aug 24 2026 by Aburke225 (the maintainer). docs/CONTRIBUTING.md is silent on AI use.

Ranked read-out

1. #17 - Agent state persistence across restarts (accept - tier-3, 7-10h, deepest of the three; matches Rachel's "challenged rather than finish quickly")
2. #34 - X-RateLimit-Remaining middleware (accept - tier-2, 3-5h; middleware integration across api/, safety/)
3. #19 - contribution_streak field (accept - tier-2, 4-6h; single computation in one file, shallowest)

Per-check summary (identical grades for all three):
- unclaimed: pass - no assignees, no linked PRs, no claim comments
- commit-alive: pass - Sep 16 2026 default-branch commit
- repo-used: pass - not archived; no releases cut (allowed)
- ai-policy: pass - CONTRIBUTING.md silent on AI-assisted work
- bounded-work: pass - each asks for one finite change in named files with hour estimate
- direction-settled: pass - opener Aburke225 is the sole committer on the repo (maintainer), and each issue carries maintainer-applied enhancement/tier labels
```

```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/17",
    "checks": [
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: none; no linked PRs; no comments on the thread"},
      {"name": "commit-alive", "grade": "pass", "evidence": "default-branch commit Sep 16 2026 by Aburke225 (within 90d of 2026-09-26)"},
      {"name": "repo-used", "grade": "pass", "evidence": "no archive banner; no releases cut (allowed by rubric)"},
      {"name": "ai-policy", "grade": "pass", "evidence": "docs/CONTRIBUTING.md covers style/CI/tests but says nothing about AI-assisted work"},
      {"name": "bounded-work", "grade": "pass", "evidence": "one finite change: persist session state to Redis in agent/memory/context_manager.py and agent/orchestrator.py, 7-10h"},
      {"name": "direction-settled", "grade": "pass", "evidence": "bug report (in-progress reviews are lost on restart); opener Aburke225 is the sole committer on the repo, labels tier-3/agent applied"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/34",
    "checks": [
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: none; no linked PRs; no comments on the thread"},
      {"name": "commit-alive", "grade": "pass", "evidence": "default-branch commit Sep 16 2026 by Aburke225 (within 90d of 2026-09-26)"},
      {"name": "repo-used", "grade": "pass", "evidence": "no archive banner; no releases cut (allowed by rubric)"},
      {"name": "ai-policy", "grade": "pass", "evidence": "docs/CONTRIBUTING.md silent on AI-assisted contributions"},
      {"name": "bounded-work", "grade": "pass", "evidence": "one finite change: wire check_rate_limit into middleware and add X-RateLimit-{Limit,Remaining} headers; files api/middleware/, safety/rate_limiter.py, api/main.py; 3-5h"},
      {"name": "direction-settled", "grade": "pass", "evidence": "enhancement opened by Aburke225 (sole committer on the repo) with enhancement + tier-2 labels applied by the same maintainer"}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/19",
    "checks": [
      {"name": "unclaimed", "grade": "pass", "evidence": "assignees: none; no linked PRs; no comments on the thread"},
      {"name": "commit-alive", "grade": "pass", "evidence": "default-branch commit Sep 16 2026 by Aburke225 (within 90d of 2026-09-26)"},
      {"name": "repo-used", "grade": "pass", "evidence": "no archive banner; no releases cut (allowed by rubric)"},
      {"name": "ai-policy", "grade": "pass", "evidence": "docs/CONTRIBUTING.md silent on AI-assisted contributions"},
      {"name": "bounded-work", "grade": "pass", "evidence": "one finite change: add contribution_streak computation in agent/tools/github_tool.py, 4-6h"},
      {"name": "direction-settled", "grade": "pass", "evidence": "enhancement opened by Aburke225 (sole committer on the repo) with enhancement + tier-2 labels applied by the same maintainer"}
    ],
    "verdict": "accept"
  }
]
```

---

## Eval iterations

Quote source text directly in each field below. Paraphrase does not satisfy them.

**Run history**

Five runs, in order:

1. **2/3** on `--limit 3`. First run of my filled rubric. issue-01 failed
   `respond-issues` and `direction-settled`.
2. **2/3** on `--limit 3` again, after I deleted my two `preferred` checks
   (`maintainer-blessed` and `fast-review-likely`). The score didn't move, which is
   what preferred checks are supposed to do. issue-01 still failed
   `respond-issues`.
3. **14/20** on the first full run. The category floor was already met. Of the six
   misses, `respond-issues` caused four (issue-01, 09, 14, 16). issue-19 was a
   false reject on `bounded-work` and issue-15 was a false accept.
4. **5/6** on `--only issue-01,issue-09,issue-14,issue-15,issue-16,issue-19`. This
   re-graded just the six I had missed, after I deleted `respond-issues`. Only
   issue-19 still disagreed.
5. **20/20** on the confirming full run. This is the one saved as `eval-run.txt`.
   `categories: claimed 4/4  clear-accept 8/8  dead-repo 3/3  policy 1/1  scope 4/4`

Between runs 3 and 4 I made one change to my rubric: I deleted `respond-issues`.
That explains issue-09, issue-14 and issue-16. It doesn't explain issue-01,
issue-15 and issue-19. All three of those changed verdict without any rubric
change touching them, so the grader isn't fully deterministic.

**Issue analysis**

**issue-01** (`conda/conda#16475`), category `clear-accept`. The gold label is
**accept**. My rubric said **reject** on the first full run, failing two required
checks. The instructor note reads "docs task with a stated home and scope; active
repo, unclaimed". I agreed with the third part and got the first two wrong.

**Why `respond-issues` failed it.** The check needed "at least one of the five
sampled issues drew a first maintainer comment within 30 days". conda's sample had
one response at `32.9 days`, and then four entries saying "no maintainer comment
in thread". So the one real response missed my cutoff by 2.9 days. This is a repo
with five default-branch commits from the day before capture, which had shipped
release 26.7.0 five days before that.

I picked 30 days because I wanted a window instead of an adjective, and I thought
I was being generous. Small volunteer projects answer unevenly and still merge, so
one response out of five seemed like enough to show somebody reads the tracker.

What I missed is that any single cutoff on this signal is an arbitrary cliff. 32.9
fails and 29.9 passes, and nothing about how healthy conda actually is changes
between those two numbers. Changing 30 to 45 wouldn't have fixed it. It would just
have moved the cliff somewhere else on the same noisy data. That's why I deleted
the check instead of retuning it.

I don't think the lesson is that thresholds are bad. `commit-alive` uses the same
kind of hard cutoff at 90 days and never got anything wrong. Commit dates are
dense and reliable, and a five-issue latency sample isn't. The real problem was a
cutoff sitting on evidence too thin to hold it up.

**Why `direction-settled` failed it.** The check said "a bug report or
documentation correction passes by default". issue-01 is labeled
`type::documentation`, but it asks for new pages rather than a correction to
existing ones. It was opened by a `CONTRIBUTOR` and had zero comments. So the
grader fell through to my new-feature branch, went looking for a maintainer
blessing, found none, and failed it. I wrote "correction" while thinking about
typo fixes. I never thought about the fact that most real documentation work is
adding things.

I want to be straight about what I actually fixed. Deleting `respond-issues` was
deliberate. I never edited `direction-settled`, and issue-01 passed it on the
later runs anyway.

**Check rationale**

`commit-alive`, quoted as it currently stands in `tools/issue-select/rubric.md`:

> **Evidence:** The "last 5 default-branch commits" list in the repo-facts block,
> with dates and authors (live: the commit list linked from the repo front page).
> The "last push to any branch" line is deliberately NOT used: a side-branch push
> shows someone touched something, not that work landed.
>
> **Pass condition:** At least one of the five most recent default-branch commits
> is dated within 90 days of the capture date. A commit authored by an account
> ending in `[bot]` counts only when it merges a human pull request.

The evidence column matters more here than the pass condition does, and reading
issue-02 (`rupa/z`) is what put it there. That repo-facts block gives you two
lines that both look like signs of life:

    - last push to any branch: 2024-06-19
    - last 5 default-branch commits: 2023-12-09, 2023-12-09, 2023-12-09, 2021-05-31, 2021-05-26

Measured against the 2026-08-05 capture date, those are 777 and 970 days old. The
any-branch line makes the repo look 193 days fresher than its main line really is.
This is a repo with 17,036 stars whose tracker hasn't had a maintainer reply since
2020. Somebody pushed something to a branch, but nothing landed. The evidence
guide calls that "a lively wire, not proof of health". Naming the exact line to
read is the only way to stop a check from quietly grading the wrong one.

The `[bot]` clause comes from the same idea, applied to who wrote the commit. A
release bot committing on a schedule isn't a human maintaining a project. A bot
merging somebody's pull request is different, because it means a human reviewed
the work and accepted it, and that's the signal I want.

**Trade-offs**

Nothing changed, and here's how I know. Refusing the any-branch line didn't move a
single verdict in this eval set. All three `dead-repo` issues are more than 90
days stale on both lines, measured against the 2026-08-05 capture date:

| issue | repo | any-branch push | default-branch commit |
|---|---|---|---|
| issue-02 | `rupa/z` | 777 days | 970 days |
| issue-07 | `wting/autojump` | 524 days | 541 days |
| issue-17 | `jarun/googler` | 1726 days | 1746 days |

Either line rejects all three, and `dead-repo` scored 3/3 in my committed run. So
the restriction is really insurance against a case this eval set doesn't have: a
repo whose default branch went quiet in the last 90 days while its side branches
stayed busy. rupa/z is that shape, just far enough gone that it stops mattering.

What I give up is the opposite case, and I'm fine with that. A project doing real
work on feature branches without merging to main, like one mid-rewrite or holding
a release branch, reads as dead to this check, and I'd reject a repo that is
actually alive. I'll take that trade because the failure goes in the safe
direction. I lose a good issue instead of spending a week on a pull request nobody
will merge. Reading only the last five commits has the same bias, and the `[bot]`
clause is what stops a burst of automated commits from pushing the human ones out
of that window.

---

## Selection rationale

Graded on whether all three are answered, in your own words. Not on how good the
reasoning is, and not on length — a short honest answer to each earns the full marks.
This is also the basis for the claim comment you write in Unit 2.

**Selection rationale**

**1. Fit to my interests and to the time available.** The issue suits my
interests. It's a Python bug fix on the agent itself (in-progress reviews get lost
when the process restarts) rather than a documentation task, and preferring that
is exactly what I put in my fit profile.

On time, I'm not treating the 7-10 hour estimate as a budget I have to measure
against right now. It was the deepest of the three candidates and that's why I
picked it. How long it takes is set by when I finish it. I'd rather work until
it's done than take the 3-5 hour issue to play it safe.

**2. What the verdict identified correctly, and what I weighed that it could
not.** The verdict was mostly right. All six required checks passed on real
evidence: no assignees or claim comments, a default-branch commit from Sep 16
2026, no archive banner, a `CONTRIBUTING.md` that says nothing about AI use, one
finite change across two named files, and a bug report opened by a maintainer. I
agree with all of those readings.

What it couldn't weigh was my actual experience, and that's my fault, not the
rubric's. My fit profile is two sentences naming Java, Python and TypeScript. It
says nothing about what I've actually built in them. So the ranking had nothing
concrete to go on and fell back on depth alone. It ordered the three candidates by
how hard they looked instead of by how well they matched me, so I made that call
myself.

**3. Anticipated difficulty in claiming it.** I don't expect claiming it to be
difficult. The Path Review house rule says classmates' claim comments don't block
an issue, and course credit attaches to the pull request I open rather than to
whether it merges. So there's nothing to compete over even if someone else is
looking at the same issue.

The issue itself is unassigned, with no linked pull requests and no comments on
the thread. It was opened by the only person committing to the repo, with the tier
and area labels already on it, so what's being asked for isn't in dispute.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
