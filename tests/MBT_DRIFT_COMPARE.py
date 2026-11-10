"""Check 10's two-way comparison: label each current-template paragraph current, missing, behind or own edit, and each unpaired brain paragraph dropped or own addition.
usage: python3 -I tests/MBT_DRIFT_COMPARE.py <toolkit> <template> <brain-file> <LS> <Project> <project> [--lobes] [-v]
       python3 -I tests/MBT_DRIFT_COMPARE.py <toolkit> --brain <brain-dir> <LS> <Project> <project> [--project-repo <dir>]... [--lobes] [-v]
<template> is relative to templates/, such as work/PLAN.md. <LS> is the brain's lobespace, its hub's in a multi-lobe brain (--lobes).
The first form compares one file as given. The second compares every file check 10 names, preparing each as check 10 does: it cuts
work setup's inline scaffolds out and compares each with its own work/ template, gathers each project repo's hook from its AGENTS.md
and CLAUDE.md, compares enforced terms' rules above the first --- only, and skips a multi-lobe brain's dream cycle."""
import os, re, subprocess, sys, difflib
args = [a for a in sys.argv[1:] if a not in ("--lobes", "-v")]; verbose = "-v" in sys.argv; lobes = "--lobes" in sys.argv
T = args[0]
git = lambda *a: subprocess.run(["git","-C",T,*a],capture_output=True,text=True).stdout
def paras(s):   # blank-line paragraphs, with a list split into its top-level items as an agent reads it; sub-items stay with their parent
    out = []
    for block in (b.strip() for b in re.split(r"\n\s*\n", s)):
        if not block: continue
        lines = block.split("\n")
        if block.startswith("|") or any(re.match(r"(`{3,}|~{3,})", l) for l in lines): out.append(block); continue
        cur = []
        for l in lines:
            if cur and re.match(r"(\d+\.|[-*]) ", l): out.append("\n".join(cur).strip()); cur = []
            cur.append(l)
        out.append("\n".join(cur).strip())
    return out
def compare(tmpl, text):
    owned = lambda p: tmpl in ("CLAUDE.md","LOBES_CLAUDE.md") and p.startswith("|")   # the brain's own table rows: read index, lobe registry, exemptions
    def versions():   # the template at every commit that changed it, each distinct blob read once
        blobs, c = set(), None
        for l in git("log","--follow","--format=%H","--name-only","--",f"templates/{tmpl}").splitlines():
            if re.fullmatch(r"[0-9a-f]{40}", l): c = l
            elif l: blobs.add(git("rev-parse","-q","--verify",f"{c}:{l}").strip())
        return [git("cat-file","-p",b) for b in blobs if b]
    def norm(s, t):   # t: a template text, whose creation-time placeholders are filled with the brain's values
        if t: s = s.replace("<Project>",PROJ).replace("<project>",proj).replace("<HUB>",LS).replace("<PREFIX>",LS)   # <PREFIX>: the pre-0.70 fixed namespace
        if not lobes: s = re.sub(rf"\b{LS}(?=_|`|\b)","<LOBESPACE>",s)   # single-lobe: <LOBESPACE> is filled; multi-lobe: it is runtime, so a literal hub name stays a difference
        s = re.sub(r"^> V\d+, .*\n","",s,flags=re.M)
        if tmpl=="PROJECT_HOOK.md": s = re.sub(r"\A<!--.*?-->\n+","",s,flags=re.S)
        if tmpl=="ENFORCED_TERMS.md": s = re.split(r"^---$", s, maxsplit=1, flags=re.M)[0]   # the rules above the entries
        return s
    vs = versions()
    old = set(p for v in vs for p in paras(norm(v,True)))
    if lobes:   # earlier creates filled <LOBESPACE> with the hub's lobespace in the hub's own copies: everywhere (0.70-0.72), or outside work-item slots (before 0.70)
        old |= set(p for v in vs for f in (r"<LOBESPACE>", r"<LOBESPACE>(?!_<WORK>)") for p in paras(re.sub(f, LS, norm(v,True))))
    raw = norm(open(f"{T}/templates/{tmpl}").read(),True)
    staged = set(p for c in re.findall(r"<!--(.*?)-->", raw, flags=re.S) for p in paras(c))   # create's staged text
    pointer = lambda q: q.startswith("Base templates for each doc live in the toolkit's `templates/work/`")
    namespace = lambda q: lobes and tmpl=="README.md" and q.startswith("Knowledge files in this mini-brain are")   # create rewords it
    now = [p for p in paras(re.sub(r"<!--.*?-->", "", raw, flags=re.S)) if not (owned(p) or pointer(p) or namespace(p))]
    brain = paras(norm(text,False)); bs = set(brain)
    now += [p for p in staged if p in bs]   # staged text the brain uncommented
    ns = set(now)
    sim = lambda a,b: difflib.SequenceMatcher(None,a.split(),b.split(),autojunk=False).ratio()
    out = {"missing":[], "behind":[], "own-edit":[], "dropped":[]}; paired = set(); out["brain-side"] = {}
    match = {}   # template paragraph -> the brain's version of it
    for p in now:
        if p in bs: paired.add(p); match[p] = p; continue
        cand = [q for q in brain if q not in ns and q not in paired and not owned(q)]
        best = max(cand, key=lambda q: sim(p,q), default=None)
        if best is not None and sim(p,best) >= 0.5: paired.add(best); match[p] = best
    # a rewrite too different to pass the similarity bar still pairs in place: the one unpaired brain paragraph between
    # the brain's versions of the template paragraph's neighbours that opens with the same four words
    pos = lambda q: brain.index(q)
    opening = lambda s: s.split()[:4]
    for i, p in enumerate(now):
        if p in match: continue
        lo = max((pos(match[x]) for x in now[:i] if x in match), default=-1)
        hi = min((pos(match[x]) for x in now[i+1:] if x in match), default=len(brain))
        cand = [q for q in brain[lo+1:hi] if q not in ns and q not in paired and not owned(q) and opening(q) == opening(p)]
        if len(cand) == 1: paired.add(cand[0]); match[p] = cand[0]
    for p in now:
        if p not in match: out["missing"].append(p)
        elif match[p] != p: out["behind" if match[p] in old else "own-edit"].append(p); out["brain-side"][p] = match[p]
    for q in paras(re.sub(r"<!--.*?-->", "", norm(text,False), flags=re.S)):   # the brain's still-staged comments are create's, not drift
        if pointer(q) or namespace(q): continue
        if q not in paired and q not in ns and q in old and q not in staged and not owned(q): out["dropped"].append(q)
    return out
def report(tmpl, name, out):
    side = out.pop("brain-side")
    print(f"{tmpl:20} {name:28} " + " ".join(f"{k}={len(v)}" for k,v in out.items()))
    if verbose:
        for k,v in out.items():
            for p in v:
                print(f"   {k:8} {p[:110]!r}")
                if k == "own-edit": print(f"   {'  brain':8} {side[p][:110]!r}")   # the brain's version, beside the template's
SCAFFOLDS = ["PLAN","FINDINGS","LOG","BURNDOWN","CLAUDE","TESTING"]
def cut_scaffolds(s):   # each scaffold sits under a heading naming its doc (`X_<WORK>_PLAN.md`, or before 0.70 just PLAN), in a fenced block of ``` or ~~~, three or more
    found, rest = {}, s
    for k in SCAFFOLDS:
        m = re.search(rf"^#+ [^\n]*(?:_<WORK>_{k}\.md|\b{k}\b)[^\n]*\n+(?P<f>`{{3,}}|~{{3,}})[^\n]*\n(?P<body>.*?)\n(?P=f)[ \t]*$\n?", rest, flags=re.M|re.S)
        if m: found[k] = m.group("body") + "\n"; rest = rest.replace(m.group(0), "")
    return found, rest
if args[1] == "--brain":
    D, LS, PROJ, proj = args[2:6]
    repos = [a for i,a in enumerate(sys.argv) if i and sys.argv[i-1] == "--project-repo"]
    read = lambda p: open(p).read() if os.path.exists(p) else None
    files = [("LOBES_CLAUDE.md" if lobes else "CLAUDE.md", "CLAUDE.md"), ("README.md", "README.md")] + \
            [(f"{d}.md", f"{LS}_{d}.md") for d in ["SESSION_CLOSEOUT","WORK_SETUP","WORK_CLOSEOUT","DREAM_CYCLE","ENFORCED_TERMS"]]
    for tmpl, name in files:
        text = read(f"{D}/{name}")
        if text is None: print(f"{tmpl:20} {name:28} not adopted"); continue
        if tmpl == "DREAM_CYCLE.md" and lobes: print(f"{tmpl:20} {name:28} skipped: a multi-lobe brain adapts the whole file"); continue
        if tmpl == "WORK_SETUP.md":
            found, text = cut_scaffolds(text)
            for k in SCAFFOLDS:
                if k in found: report(f"work/{k}.md", f"{name} ({k} scaffold)", compare(f"work/{k}.md", found[k]))
                else: print(f"{'work/'+k+'.md':20} {name:28} scaffold not found inline")
        report(tmpl, name, compare(tmpl, text))
    for r in repos:
        text = "\n\n".join(t for t in (read(f"{r}/AGENTS.md"), read(f"{r}/CLAUDE.md")) if t)
        report("PROJECT_HOOK.md", f"{os.path.basename(r.rstrip('/'))} hook", compare("PROJECT_HOOK.md", text))
else:
    tmpl, bf, LS, PROJ, proj = args[1:6]
    report(tmpl, bf.split('/')[-1], compare(tmpl, open(bf).read()))
