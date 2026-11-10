#!/usr/bin/env bash
# Run MAT's shell-sensitive script scenarios: 1 (each README install line, in zsh, bash and sh) and 14's find commands.
# Prints a PLATFORM line, then one PASS or FAIL line per case. Writes only inside <workdir>, and changes no git config.
# usage, on the host:  TK=<toolkit checkout> W=<new empty directory> bash tests/MBT_SHELL_CHECKS.sh
# usage, on Linux:     docker run --rm -v <toolkit checkout>:/tk:ro -v <new empty directory>:/work debian:stable-slim bash -c \
#                        'apt-get update -qq && apt-get install -y -qq --no-install-recommends git zsh ca-certificates >/dev/null && TK=/tk W=/work bash /tk/tests/MBT_SHELL_CHECKS.sh'
: "${TK:?set TK}" "${W:?set W}"
[ -d "$W" ] && [ -z "$(ls -A "$W")" ] || { echo "W must be an existing empty directory"; exit 1; }
# git settings for this process only; nothing global is written
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=safe.directory GIT_CONFIG_VALUE_0='*'
export GIT_AUTHOR_NAME=MAT GIT_AUTHOR_EMAIL=mat@example.invalid GIT_COMMITTER_NAME=MAT GIT_COMMITTER_EMAIL=mat@example.invalid
findv=$(find --version 2>/dev/null | head -1); [ -n "$findv" ] || findv="BSD find"
echo "PLATFORM $(uname -sm), git $(git --version | cut -d' ' -f3), bash $BASH_VERSION, zsh $(zsh --version | cut -d' ' -f2), $findv"

# Scenario 1: a bare clone of the checkout, tagged above any release, stands in for the remote.
git clone -q --bare "$TK" "$W/remote.git"; git -C "$W/remote.git" tag 0.99-mat HEAD; HEADC=$(git -C "$W/remote.git" rev-parse HEAD)
grep -n 'git clone' "$TK/README.md" | while IFS= read -r row; do
  n=${row%%:*}; line=${row#*:}
  for sh in zsh bash sh; do for case in fresh rerun moved badurl; do   # moved runs on an existing install, before badurl removes it
    d=$W/inst-$n-$sh; [ $case = fresh ] && rm -rf "$d"
    url=$W/remote.git; [ $case = badurl ] && { url=$W/nope.git; rm -rf "$d"; }
    [ $case = moved ] && mv "$W/remote.git" "$W/remote.moved"
    before=$( [ -d "$d" ] && { git -C "$d" rev-parse HEAD; git -C "$d" status --porcelain; } 2>/dev/null )
    l=$(printf '%s' "$line" | sed -E "s#^d=[^;]*;#d=$d;#; s#https://github.com/robfromboulder/mini-brain-toolkit#$url#")
    $sh -c "$l" >/dev/null 2>&1; rc=$?
    after=$( [ -d "$d" ] && { git -C "$d" rev-parse HEAD; git -C "$d" status --porcelain; } 2>/dev/null )
    [ $case = moved ] && mv "$W/remote.moved" "$W/remote.git"
    case $case in
      fresh)  ok=$([ $rc = 0 ] && [ "$(git -C "$d" rev-parse HEAD)" = "$HEADC" ] && echo PASS);;
      rerun)  ok=$([ $rc = 0 ] && [ "$before" = "$after" ] && echo PASS);;
      moved)  ok=$([ $rc != 0 ] && [ -n "$before" ] && [ "$before" = "$after" ] && echo PASS);;
      badurl) ok=$([ $rc != 0 ] && [ ! -e "$d" ] && echo PASS);;
    esac
    echo "1  line $n  $sh  $case  rc=$rc  ${ok:-FAIL}"
  done; done
done

# Scenario 14: work setup's two find commands, on a working/ that holds a prefix collision and a space, and on a missing working/.
mkdir -p "$W/s14/working" && cd "$W/s14" || exit 1
touch working/FIX_PLUM_PLAN.md working/FIX_PLUM_FINDINGS.md working/FIX_PLUM_JAM_PLAN.md working/FIX_OTHER_LOG.md working/ALPHA_X_PLAN.md "working/FIX_SP ACE_PLAN.md"
c1="find working -maxdepth 1 -name 'FIX_PLUM_*.md' 2>/dev/null"
c2="find working -maxdepth 1 \\( -name 'FIX_*_PLAN.md' -o -name 'FIX_*_FINDINGS.md' \\) 2>/dev/null"
c3="find nowhere -maxdepth 1 -name 'FIX_PLUM_*.md' 2>/dev/null"
i=0; for c in "$c1" "$c2" "$c3"; do i=$((i+1)); res=""; rcs=""
  for sh in zsh bash sh; do $sh -c "$c" | LC_ALL=C sort > "out.$sh"; rc=${PIPESTATUS[0]}; res="$res $sh:rc=$rc"; rcs="$rcs$rc"$'\n'; done
  same_rc=$(printf '%s' "$rcs" | sort -u | wc -l | tr -d ' ')
  cmp -s out.zsh out.bash && cmp -s out.bash out.sh && [ "$same_rc" = 1 ] && v=PASS || v=FAIL
  echo "14 find $i $res  lines=$(wc -l < out.sh | tr -d ' ')  $v"; cp out.sh "$W/s14-find$i.out"
done
