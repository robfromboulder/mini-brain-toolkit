# Enforce the Work-Item Token Prefix: Decision Record

## Problem

When a new work item is created, its filenames inconsistently carry the namespace token: most runs produce `MBT_<WORK>_*`, but some produce a bare `<WORK>_*`. The inconsistency surfaces only at creation — everywhere else a bare name is accepted and mapped back to the prefixed file, so setup is the one place the optionality bites.

Root cause is in the instruction, not the convention. `WORK_SETUP.md` does say to prepend the token, but only inside dense prose (§2's prefix-distinctness discussion, §3's "substituting `<TOKEN>`"), never as a crisp imperative at the one decision point that matters: the moment a name is handed in and turned into filenames. It also never resolves the ambiguity there — given "BLAH_BLAH", is that the `<WORK>` slug to be prefixed, or a compound already? §2 further muddies it by saying the slug is "*not* a mechanical transform of the work-item name," which pushes toward inventing a slug but says nothing about whether the token is then mandatory on the filename. So the model sometimes emits the slug as the filename and sometimes prepends.

## Preferred approach: enforce the prefix in WORK_SETUP (Option B)

Make the name → slug → filename transform an explicit, unmissable step in `WORK_SETUP.md`, with the handed-name ambiguity resolved in the instruction:

- The produced filenames are **always** `<TOKEN>_<WORK>_*`.
- Derive `<WORK>` from the work-item name; a bare name like `BLAH_BLAH` always becomes `<TOKEN>_BLAH_BLAH`.
- If the handed name already leads with the unit's token, strip it before treating the rest as `<WORK>` — never double-prefix.

| Aspect | Detail |
|---|---|
| Blast radius | One file: `templates/WORK_SETUP.md` (§2/§3). |
| Invariants touched | None. The glob `<TOKEN>_<WORK>_*`, the component ownership model, and the universal-token naming law all already assume this outcome. |
| Reach | New brains only — `WORK_SETUP` is inlined at seed time, so existing brains keep their copy until re-seeded or hand-patched. |

- **Confined** — sharpens an instruction the doc already intends; nothing downstream moves.
- **Invariant-preserving** — keeps working files inside the "every mini-brain filename carries its owning token" law rather than carving a third exemption into it.

## Alternatives considered

- **Drop the token from working files (Option A)** — rejected. The token is genuinely redundant with the directory in component brains and pure redundancy in single-unit brains, so the scannability complaint is real. But dropping it is not confined: the glob `<TOKEN>_<WORK>_*` is threaded through `WORK_SETUP`, `WORK_CLOSEOUT`, `SESSION_CLOSEOUT`, `PROJECT_HOOK`, and `templates/work/{PLAN,BURNDOWN}.md`, and it punctures two invariants — the universal-token naming law in `CLAUDE.md` (two named exemptions become three, conditionally) and the longest-match ownership cross-check in `MBT_COMPONENTS.md` that catches misfiled work files. Six-doc change, foundational invariants disturbed, and the benefit fully materializes only in single-unit brains.

## What this doesn't solve

- The token stays redundant-with-directory in component brains and redundant in single-unit brains; the file-listing scannability tax persists. Retiring that redundancy pattern-wide (make the directory the sole ownership signal) is a deliberate redesign of `MBT_COMPONENTS.md`, deferred to its own work item, not this one.
- Existing exemplar brains are not fixed by this change — they carry inlined copies of `WORK_SETUP` and only pick it up on re-seed or hand-patch.

## Reversals

None. `WORK_SETUP` already intends the prefix; this makes the existing intent enforceable. No canonical claim becomes false.
