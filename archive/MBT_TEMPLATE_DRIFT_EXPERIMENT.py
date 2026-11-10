"""Three-way drift experiment with placeholder normalization and WORK_SETUP scaffold splitting.
usage: python3 -I MBT_TEMPLATE_DRIFT_EXPERIMENT.py <toolkit> <base-ref> <brain-dir> <LS> <Project> <project> <outdir> [--show] tmpl:brainfile ...
"""
import os, re, subprocess, sys

T, BASE, B, LS, PROJ, proj, OUT = sys.argv[1:8]
args = sys.argv[8:]
show = "--show" in args
pairs = [a for a in args if a != "--show"]
os.makedirs(OUT, exist_ok=True)
SCAFFOLDS = ["PLAN", "FINDINGS", "LOG", "BURNDOWN", "CLAUDE", "TESTING"]

def git_show(ref, path):
    return subprocess.run(["git", "-C", T, "show", f"{ref}:{path}"], capture_output=True, text=True, check=True).stdout

def norm(s, template):
    """Normalize: fill names, then fold the lobespace back to one token so filled and unfilled copies compare equal."""
    if template:
        s = s.replace("<Project>", PROJ).replace("<project>", proj)
    s = s.replace("<HUB>", "<LOBESPACE>")
    s = re.sub(rf"\b{LS}(?=_|`|\b)", "<LOBESPACE>", s)
    s = re.sub(r"^> V\d+, .*\n", "", s, flags=re.M)          # version line
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s

def split_setup(s):
    """Return (procedure text, {scaffold: text}) from a WORK_SETUP copy with inlined fenced scaffolds."""
    scaff = {}
    def grab(m):
        scaff[m.group(1)] = m.group(3).strip() + "\n"
        return ""
    proc = re.sub(r"### (?:`<LOBESPACE>_<WORK>_)?([A-Z]+)(?:\.md`| template)\s*\n(?:.*\n)*?(~~~~|````|```)markdown\n((?:.*\n)*?)\2\n", grab, s)
    return proc, scaff

def write(name, text):
    p = os.path.join(OUT, name); open(p, "w").write(text); return p

def count(a, b):
    r = subprocess.run(["diff", a, b], capture_output=True, text=True).stdout
    return sum(1 for l in r.splitlines() if l[:1] in "<>")

def three(name, base, now, brain):
    pb, pn, pr = write(name + ".base", base), write(name + ".now", now), write(name + ".brain", brain)
    pm = write(name + ".merged", brain)
    c = subprocess.run(["git", "merge-file", "-q", pm, pb, pn]).returncode
    print(f"{name:34} brain={brain.count(chr(10)):4} 2way={count(pn, pr):4} local={count(pb, pr):4} upstream={count(pb, pn):4} conflicts={c}")
    if show:
        for label, a, b in (("LOCAL", pb, pr), ("CONFLICT-FREE MERGE vs NOW", pn, pm)):
            d = subprocess.run(["git", "diff", "--no-index", "--word-diff=plain", "-U0", a, b], capture_output=True, text=True).stdout
            hunks = [l[:300] for l in d.splitlines() if ("[-" in l or "{+" in l)]
            if hunks:
                print(f"   -- {label}:"); [print("     " + h) for h in hunks]

for pair in pairs:
    t, f = pair.split(":")
    base, now = norm(git_show(BASE, f"templates/{t}"), True), norm(git_show("HEAD", f"templates/{t}"), True)
    if t == "PROJECT_HOOK.md":
        base, now = [re.sub(r"\A<!--.*?-->\n+", "", x, flags=re.S) for x in (base, now)]
    brain = norm(open(os.path.join(B, f)).read(), False)
    stem = os.path.basename(f)[:-3]
    if t == "WORK_SETUP.md":
        bp, bs = split_setup(brain)
        three(stem + ".proc", base, now, bp)
        for k in SCAFFOLDS:
            sb = norm(git_show(BASE, f"templates/work/{k}.md"), True).strip() + "\n"
            sn = norm(git_show("HEAD", f"templates/work/{k}.md"), True).strip() + "\n"
            if k in bs:
                three(f"{stem}.work.{k}", sb, sn, bs[k])
            else:
                print(f"{stem}.work.{k}: not found in brain copy")
    else:
        three(stem, base, now, brain)
