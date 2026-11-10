"""Infer a brain file's base by check 10's rule, merge it with the current template, and list recommendations and conflicts.
usage: python3 -I MBT_TEMPLATE_DRIFT_INFER.py <toolkit> <template> <brain-file> <LS> <Project> <project> [new|old]
new (default) is the bounded rule from PR #22's review; old is the earlier most-paragraphs, newest-on-tie rule."""
import re, subprocess, sys, tempfile, os
T, tmpl, bf, LS, PROJ, proj = sys.argv[1:7]
rule = sys.argv[7] if len(sys.argv) > 7 else "new"
def show(ref):
    r = subprocess.run(["git","-C",T,"show",f"{ref}:templates/{tmpl}"],capture_output=True,text=True)
    return r.stdout if r.returncode == 0 else None
def norm(s, template):
    if template: s = s.replace("<Project>",PROJ).replace("<project>",proj)
    s = s.replace("<HUB>","<LOBESPACE>")
    s = re.sub(rf"\b{LS}(?=_|`|\b)","<LOBESPACE>",s)
    s = re.sub(r"^> V\d+, .*\n","",s,flags=re.M)
    if tmpl == "PROJECT_HOOK.md": s = re.sub(r"\A<!--.*?-->\n+","",s,flags=re.S)
    return re.sub(r"\n{3,}","\n\n",s)
import difflib
def near(p, ps):
    w=p.split()
    return any(difflib.SequenceMatcher(None,w,q.split(),autojunk=False).ratio()>=0.5 for q in ps)
def lacks(ps, bp): return sum(1 for p in ps-bp if not near(p, bp-ps))
def paras(s): return {p.strip() for p in re.split(r"\n\s*\n",s) if p.strip()}
tags = subprocess.run(["git","-C",T,"tag","--sort=v:refname"],capture_output=True,text=True).stdout.split()
cands = [(c, show(c)) for c in tags+["HEAD"]]
cands = [(c, norm(t,True)) for c,t in cands if t is not None]
brain = norm(open(bf).read(), False); bp = paras(brain)
P = [(c, paras(t)) for c,t in cands]
idx = {c:i for i,(c,_) in enumerate(P)}
if rule == "old":
    base = max(P, key=lambda x:(len(bp & x[1]), idx[x[0]]))[0]; bound=None
else:
    lasts = [max(i for i,(c,ps) in enumerate(P) if p in ps) for p in bp if any(p in ps for _,ps in P)]
    bound = min(lasts) if lasts else len(P)-1
    base = max(P[:bound+1], key=lambda x:(len(bp & x[1]), -lacks(x[1],bp), idx[x[0]]))[0]
print(f"{tmpl}: scores " + " ".join(f"{c}={len(bp&ps)}/-{lacks(ps,bp)}" for c,ps in P) + f" | bound={P[bound][0] if bound is not None else '-'} base={base}")
d = tempfile.mkdtemp()
def w(n,t): p=os.path.join(d,n); open(p,"w").write(t); return p
pb, pn, pr = w("base",dict(cands)[base]), w("now",dict(cands)["HEAD"]), w("brain",brain)
m = subprocess.run(["git","merge-file","-p",pr,pb,pn],capture_output=True,text=True)
merged = m.stdout; conflicts = merged.count("<<<<<<<")
recs = [p for p in paras(re.sub(r"<<<<<<<.*?>>>>>>>[^\n]*","",merged,flags=re.S)) - bp]
print(f"   conflicts={conflicts} recommendations={len(recs)}")
for r in recs: print("   + " + r[:110].replace("\n"," / "))
