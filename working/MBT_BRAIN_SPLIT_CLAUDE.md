# Brain Split: Claude Runbook

Instructions for branch: `brain-split*`

## Running Tests

Run the steps from the brain's canonical runbook first (if it has one), verifying results match the expectations documented there. Then run the work-specific step(s) below.

### Step 1 — install line upgrades a full install to a product-only tag ← NEW in this branch

```bash
# fill in once the work item has tests
```

**Expected:** Each README line exits 0 on a clean 0.73 install and lands on the post-split tag, with only the product's tracked files and no brain file left; `git log --follow -- templates/<file>` from that tag still lists the template's earlier commits.

### Step 2 — existing test scripts from the brain against a sibling product checkout ← NEW in this branch

```bash
# fill in once the work item has tests
```

**Expected:** <runtime, pass/fail expectations, which tests are active>
