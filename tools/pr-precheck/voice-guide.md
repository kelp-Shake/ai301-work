# Voice guide: how I talk upstream

<!--
THIS IS THE PART YOU WRITE (new this week). Live mode reads this file
before any comment of yours goes out the door; eval mode ignores it
entirely, because your voice is yours and carries no gold labels.

This is not etiquette. "Be polite and concise" is advice for everyone
and therefore rules for no one. Write rules YOU need, in your own
words, each one concrete enough that the skill can hold a draft
against it and say which rule it breaks.

Three sections. Fill all three.
-->

## Who I am in threads

I'm a new contributor, and #17 is the first issue I'm working on in this repo.
Before I commit to an issue, I do a quick check that the issue and the versions
are clear and that it looks reproducible, to decide whether I want to take it on.

## Rules I write by

### Rule: Say what I think and mark it unconfirmed

When I'm unsure of the cause, I say what I think and that I haven't confirmed it. I don't apologize for not knowing.

- Wrong: "I think maybe the issue is something to do with state? Not sure, sorry."
- Right: "I think the issue is that agent state isn't persisted across restarts, but I haven't confirmed it yet."

### Rule: State my next step

I claim the issue and say what I'll do next. I don't ask permission or whether I'm the right person.

- Wrong: "I'd like to try this if that's okay, I'm new so I might not be able to do it."
- Right: "I'm claiming this issue. I'll work on the next step with what I know now and come back with what I find."

### Rule: Name a detail from the issue

Every comment names something particular to this issue, so it couldn't fit any other one.

- Wrong: "Is anyone working on this? Can I try it?"
- Right: "I'm looking at where agent/memory/context_manager.py holds session state in memory before it's written to Redis."

## Things I never post

- Apologizing or hedging with "sorry" or "not sure" instead of saying what I think and marking it unconfirmed.
- Asking whether I'm allowed to take an issue, or whether I'm the right person for it.
- A claim with no detail from the issue.
