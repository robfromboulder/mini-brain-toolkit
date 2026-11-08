# Minimum Acceptance Testing: Burndown

Everything between working code and a merged PR.

## Routine

* commit and push the finished change on the work branch
* create draft PR
* review code changes
* full rebuild and automated retest on PR code
* review PR description against final code one last time
* request feedback from reviewers
* respond to review feedback
* automated checks — see `MBT_MAT_CLAUDE.md`
* manual checks — capture steps in `MBT_MAT_TESTING.md`
* closeout notes — <deviations from the standard flow, and any canonical claim this work item reverses — see the `working/` rule in `CLAUDE.md`>

## Custom

* docs — <screenshots, user-facing docs, if any>
* porting/backporting — <if this work ships to more than one target>
* <follow-on items discovered during implementation>
