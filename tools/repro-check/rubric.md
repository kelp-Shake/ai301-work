# Rubric: is this reproduction package ready to post?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever
checks you define here. It ships empty on purpose: the judgment is your
work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four
   columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where in the package. Name
     the part (the claim comment, the repro report's environment
     record, the artifacts read against the issue's description, the
     repo-facts block) or a location from your
     references/evidence-guide.md. "The report" is not a source; "the
     output excerpt read against the error the issue describes" is.
   - Pass condition: a decision rule about the OUTCOME that someone
     else could apply and get your answer. Judge the thing itself (does
     the artifact show the issue's behavior?), never the write-up's
     shape (how many steps it has, how long it is, whether it uses a
     template's headings). Structure-shaped checks are what make
     graders disagree with themselves.
   - Weight: `required` (a fail here holds the package) or `preferred`
     (never changes the verdict).

2. A verdict rule below the table: how the check grades combine into
   accept (ready) or reject (hold), including how `unclear` is
   treated. The verdict space is binary. If you write no rule for
   `unclear`, the skill treats it as fail.

Cover what actually gets bad packages posted. The lecture named the
proof families: the environment is recorded, the steps are complete
and followable, the behavior shown matches the issue (not an adjacent
one), the outcome is stated honestly (an evidenced cannot-reproduce is
a pass, a confident wrong-target is not), and the words respect the
repo's conventions. A rubric that ignores a family will fail eval
packages designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| artifact-present | The pasted output, log, or transcript in the repro report, read against the behavior the issue body describes. | **Passes when:** the report has at least one pasted artifact of the attempt, showing what happened when the issue's steps were run (the reported behavior, or an honest failure to see it).<br>**Fails when:** the report has no pasted artifact.<br>**Fails when:** the artifacts show only that the tool is installed or running (a version banner, a session list). | required |
| right-target | The error text, exit code, or output in the pasted artifact, and the input and version the report says it ran, read against the symptom, input, and version in the issue body. | **Passes when:** the artifact shows the same symptom the issue names, produced by the issue's input, and any difference in input or version is stated in the report.<br>**Fails when:** the artifact shows a different symptom narrated as the issue's.<br>**Fails when:** the input or version was changed without saying so.<br>**Note:** an honest cannot-reproduce passes when the attempt used the issue's input. | required |
| env-recorded | The environment record in the repro report. | **Passes when:** the report states both the operating system and the version of the software under test.<br>**Fails when:** either is missing. | required |
| steps-rerunnable | The steps and inputs in the repro report. | **Passes when:** every command, input file, and config a stranger would need is shown in the report or points to the issue's own text.<br>**Fails when:** a step depends on private material the reader cannot get. | required |
| claim-specific | The claim comment only. | **Passes when:** the claim names at least one detail particular to this issue (a function, file, error message, or behavior from the issue body).<br>**Fails when:** the claim would fit any other issue unchanged. | required |
| claimed-work | The claim comment only. | **Passes when:** the claim offers only to investigate or report back.<br>**Fails when:** the claim promises a fix or a delivery date.<br>**Fails when:** the claim asks to be assigned or to have the issue reserved.<br>**Fails when:** the claim states no work the author will do next. | required |
| ai-disclosure | The "contribution policy" line of the repo-facts block, read against the text of the claim comment and the repro report. Treat the package as AI-assisted work. | **Passes when:** the policy line does not require AI use to be disclosed in issue comments.<br>**Passes when:** a comment states that AI assistance was used.<br>**Fails when:** the policy explicitly tells contributors to disclose AI use in comments or issues, and neither comment discloses.<br>**Note:** a requirement that covers only pull requests does not apply here.<br>**Note:** a rule that comments be written by a human in their own words is not a disclosure requirement. | required |

## Verdict rule

Accept only when every check passes. A single fail rejects the package.

`unclear` on any check counts as `fail`. A package that is wrongly accepted costs more than one that is held, so a check the rubric cannot decide does not get the benefit of the doubt.
