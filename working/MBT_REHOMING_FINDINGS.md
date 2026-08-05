# Work-Item Re-homing: Decision Record

## Problem

In a component brain, a work item's owning unit is settled at intake as the nearest common ancestor of the units the work *will* concern — a prediction. Mid-flight scope growth can invalidate it: a child-owned item turns out to need a sibling's changes, so the owner should have been their parent. When that happens there is no move procedure — re-homing means `git mv` plus a token rename across every doc plus the runbook's branch declaration, and nothing says so. Worse, re-running work setup with the corrected owner silently scaffolds a duplicate, because the setup audit lists only the new owner's directories.

## Preferred approach: guard first, procedure second

Two layers, cheapest first:

- **Setup-audit guard** — before creating anything, the setup audit searches *every* unit's `working/` for the slug, not just the new owner's. This turns the silent-duplicate failure into a visible one and is a one-sentence change.
- **Re-homing procedure** — the move itself: `git mv` the docs to the new owner's `working/`, rename the token on every doc, update the runbook's branch declaration, and re-run setup to fill anything the new home is missing. Small enough to live as a section in work setup rather than its own document.

## Alternatives considered

- **Defer ownership past intake** — don't settle the owner until the work's reach is known. Rejected: the owner decides where the docs live and which token they carry, so deferring it leaves the scaffold homeless from day one.

## What this doesn't solve

- Final knowledge placement is untouched: closeout already places each finding by reach, so an item that never re-homes still folds its knowledge to the right units. Re-homing is about the in-flight files and routing signals, not the destination of the knowledge.
