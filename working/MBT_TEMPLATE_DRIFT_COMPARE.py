"""Check 10's two-way comparison: label each current-template paragraph current, missing, behind or own edit, and each unpaired brain paragraph dropped or own addition.
usage: python3 -I MBT_TEMPLATE_DRIFT_COMPARE.py <toolkit> <template> <brain-file> <LS> <Project> <project> [--lobes] [-v]"""
import re, subprocess, sys, difflib
T, tmpl, bf, LS, PROJ, proj = sys.argv[1:7]; verbose = "-v" in sys.argv; lobes = "--lobes" in sys.argv
git = lambda *a: subprocess.run(["git","-C",T,*a],capture_output=True,text=True).stdout
def versions():   # the template at every commit that changed it, each distinct blob read once
    blobs, c = set(), None
    for l in git("log","--follow","--format=%H","--name-only","--",f"templates/{tmpl}").splitlines():
        if re.fullmatch(r"[0-9a-f]{40}", l): c = l
        elif l: blobs.add(git("rev-parse","-q","--verify",f"{c}:{l}").strip())
    return [git("cat-file","-p",b) for b in blobs if b]
def norm(s, t):
    if t: s = s.replace("<Project>",PROJ).replace("<project>",proj)
    s = s.replace("<HUB>","<LOBESPACE>"); s = re.sub(rf"\b{LS}(?=_|`|\b)","<LOBESPACE>",s)
    s = re.sub(r"^> V\d+, .*\n","",s,flags=re.M)
    if tmpl=="PROJECT_HOOK.md": s = re.sub(r"\A<!--.*?-->\n+","",s,flags=re.S)
    return s
paras = lambda s: [p.strip() for p in re.split(r"\n\s*\n",s) if p.strip()]
old = set(p for v in versions() for p in paras(norm(v,True)))
raw = norm(open(f"{T}/templates/{tmpl}").read(),True)
staged = set(p for c in re.findall(r"<!--(.*?)-->", raw, flags=re.S) for p in paras(c))   # create's staged text
now = [p for p in paras(re.sub(r"<!--.*?-->", "", raw, flags=re.S))
       if not (tmpl in ("CLAUDE.md","LOBES_CLAUDE.md") and p.startswith("|"))           # brain-owned table rows
       and not p.startswith("Base templates for each doc live in the toolkit's `templates/work/`")
       and not (lobes and tmpl=="README.md" and p.startswith("Knowledge files in this mini-brain are"))]   # create rewords it
now += [p for p in staged if p in set(paras(norm(open(bf).read(),False)))]           # staged text the brain uncommented
brain = paras(norm(open(bf).read(),False)); bs=set(brain); ns=set(now)
sim = lambda a,b: difflib.SequenceMatcher(None,a.split(),b.split(),autojunk=False).ratio()
out = {"missing":[], "behind":[], "own-edit":[], "dropped":[]}; paired=set()
for p in now:
    if p in bs: paired.add(p); continue
    cand = [q for q in brain if q not in ns and q not in paired and not q.startswith('|')]
    best = max(cand, key=lambda q: sim(p,q), default=None)
    if best is None or sim(p,best) < 0.5: out["missing"].append(p)
    else:
        paired.add(best); out["behind" if best in old else "own-edit"].append(p)
pointer = lambda q: q.startswith("Base templates for each doc live in the toolkit's `templates/work/`")
for q in paras(re.sub(r"<!--.*?-->", "", norm(open(bf).read(),False), flags=re.S)):   # the brain's still-staged comments are create's, not drift
    if pointer(q) or (lobes and tmpl=="README.md" and q.startswith("Knowledge files in this mini-brain are")): continue
    if q not in paired and q not in ns and q in old and q not in staged and not q.startswith('|'): out["dropped"].append(q)
print(f"{tmpl:20} {bf.split('/')[-1]:28} " + " ".join(f"{k}={len(v)}" for k,v in out.items()))
if verbose:
    for k,v in out.items():
        for p in v: print(f"   {k:8} {p[:110]!r}")
