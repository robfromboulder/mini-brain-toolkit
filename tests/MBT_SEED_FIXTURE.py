"""Seed a fixture brain, and a project repo beside it, as the toolkit's create would have at a given ref, with every procedure file adopted.
usage: python3 -I tests/MBT_SEED_FIXTURE.py <toolkit> <ref> <outdir> [--lobes]
Writes <outdir>/mini-fix-brain and <outdir>/fix, each a git repo with one commit, named as the hook and README expect. The lobespace is FIX; --lobes adds child lobes ALPHA and BETA,
and the project repo maps to ALPHA. <ref> is any tag or commit, such as 0.72 or 8ad8deb. Nothing outside <outdir> is written."""
import os, re, subprocess, sys
T, REF, OUT = sys.argv[1:4]; lobes = "--lobes" in sys.argv
LS, PROJ, proj, DATE = "FIX", "Fix", "fix", "2026-01-01"
show = lambda p: subprocess.run(["git","-C",T,"show",f"{REF}:{p}"],capture_output=True,text=True).stdout
tmpl = lambda p: show(f"templates/{p}") or sys.exit(f"no templates/{p} at {REF}")
create = show("MBT_CREATE_BRAIN.md")
runtime = lobes and "In a multi-lobe brain, `<LOBESPACE>` in session closeout" in create   # create keeps the owning lobe's slot as a runtime variable
agents = bool(show("templates/AGENTS.md"))                                                    # the hook lives in AGENTS.md, imported by CLAUDE.md
both_keeps = "add a `.gitkeep` to each" in create
def fill(s, ls=LS, p=PROJ, pl=proj, keep=False):
    s = s.replace("<HUB>",LS).replace("<Project>",p).replace("<project>",pl).replace("<date>",DATE)
    return s if keep else s.replace("<LOBESPACE>",ls)
def put(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path,"w").write(s)
def unstage_index(c):   # move the staged lifecycle rows into the read index, and uncomment the boundary rule
    m = re.search(r"<!-- As the brain matures, add the lifecycle docs to this index:\n(.*?)-->\n\n?", c, flags=re.S)
    c = c.replace(m.group(0), "")
    anchor = re.search(r"^\| Session log update format.*\n", c, flags=re.M).group(0)
    c = c.replace(anchor, anchor + m.group(1), 1)
    return re.sub(r"<!-- As the brain matures and gains the lifecycle docs, add their boundary rule:\n(.*?)-->\n", r"\1", c, flags=re.S)
def inline_scaffolds(w):
    pointer = next(l for l in w.split("\n") if l.startswith("Base templates for each doc live"))
    blocks = "\n\n".join(f"### `<LOBESPACE>_<WORK>_{k}.md`\n\n````markdown\n{tmpl(f'work/{k}.md').rstrip()}\n````" for k in ["PLAN","FINDINGS","LOG","BURNDOWN","CLAUDE","TESTING"])
    return w.replace(pointer, "Each doc's base template follows; copy it when creating that doc.\n\n" + blocks)
def commit(d):
    run = lambda *a: subprocess.run(["git","-C",d,"-c","user.name=Fixture","-c","user.email=fixture@example.invalid",*a],check=True,capture_output=True)
    run("init","-q","-b","main"); run("add","-A"); run("commit","-q","-m",f"Seed fixture at {REF}")
B, P = f"{OUT}/mini-fix-brain", f"{OUT}/fix"
if os.path.exists(B) or os.path.exists(P): sys.exit(f"{B} or {P} exists")
# entrypoint
if lobes:
    c = tmpl("LOBES_CLAUDE.md")
    c = re.sub(r"^\| <Lobe> .*\n", "| Alpha | `alpha/` | `ALPHA` | alpha questions | — | `../fix` |\n| Beta | `beta/` | `BETA` | beta questions | — | |\n", c, flags=re.M)
    c = re.sub(r"^\| — <Sub-lobe>.*\n", "", c, flags=re.M)
    put(f"{B}/CLAUDE.md", fill(unstage_index(c), keep=True))   # its <LOBESPACE> is the doctype grammar's
else:
    put(f"{B}/CLAUDE.md", fill(unstage_index(tmpl("CLAUDE.md"))))
if agents: put(f"{B}/AGENTS.md", fill(tmpl("AGENTS.md")))
r = fill(tmpl("README.md"))
if lobes: r = re.sub(r"^Knowledge files in this mini-brain are .*$", f"Knowledge files in this mini-brain are namespaced per lobe: the hub's as `{LS}_*`, and each child lobe's with its own lobespace.", r, flags=re.M)
put(f"{B}/README.md", r)
# knowledge docs, per lobe
for d in ["SCOPE","APPROACH","FINDINGS","LOG"]:
    put(f"{B}/{LS}_{d}.md", fill(tmpl(f"{d}.md")))
    if lobes:
        for ls, p, pl, dir in [("ALPHA","Alpha","alpha","alpha"), ("BETA","Beta","beta","beta")]:
            put(f"{B}/{dir}/{ls}_{d}.md", fill(tmpl(f"{d}.md"), ls, p, pl))
# procedure files, at the hub
for d in ["SESSION_CLOSEOUT","WORK_CLOSEOUT","DREAM_CYCLE","DREAM_LOG","ENFORCED_TERMS"]:
    put(f"{B}/{LS}_{d}.md", fill(tmpl(f"{d}.md"), keep=runtime and d in ("SESSION_CLOSEOUT","WORK_CLOSEOUT")))
put(f"{B}/{LS}_WORK_SETUP.md", fill(inline_scaffolds(tmpl("WORK_SETUP.md")), keep=runtime))
put(f"{B}/working/.gitkeep", "")
if both_keeps: put(f"{B}/archive/.gitkeep", "")
# project repo and its hook
h = re.sub(r"\A<!--.*?-->\n+", "", tmpl("PROJECT_HOOK.md"), flags=re.S)
lobe = re.search(r"<!-- Multi-lobe brains only.*?:\n\n(.*?)\n-->\n\n", h, flags=re.S)
h = h.replace(lobe.group(0), (lobe.group(1).replace("<Lobe>","Alpha").replace("<dir>","alpha").replace("<LOBESPACE>","ALPHA") + "\n\n") if lobes else "")
h = re.sub(r"<!-- As the brain matures and gains work items \(stage 3\), add:\n\n(.*?)\n-->", r"\1", h, flags=re.S)
h = fill(h, keep=runtime)
own = f"# {PROJ}\n\nBuild with `make`, and run `make test` before every commit.\n"
if agents:
    put(f"{P}/AGENTS.md", h); put(f"{P}/CLAUDE.md", own + "\n@AGENTS.md\n")
else:
    put(f"{P}/CLAUDE.md", own + "\n" + h)
put(f"{P}/README.md", f"# {PROJ}\n")
commit(B); commit(P)
print(f"seeded {B} and {P} at {REF}" + (" (multi-lobe)" if lobes else ""))
