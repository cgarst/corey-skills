#!/usr/bin/env python3
"""Cherry-pick one agent commit onto the current branch with a scheduled commit time.

usage: pick.py <commit-or-branch> [--start HH:MM] [--end HH] [--tz -05:00] [--state FILE]

Times are stored in FILE (default: ./.pick-last, keep it OUTSIDE the repo or gitignored).
First pick: --start plus 0-4 min, random seconds. Later picks: previous + 2-5 min, random seconds.
Stops (exit 1) when the time would reach --end hour. On a conflict it stages nothing and prints
the date to use; resolve, `git add`, then commit with
  GIT_COMMITTER_DATE=<d> git commit -C <commit> --date=<d>
and write the time into FILE yourself.
"""
import argparse, datetime, os, random, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("commit")
ap.add_argument("--start", default="06:00")
ap.add_argument("--end", type=int, default=9)
ap.add_argument("--tz", default="-05:00")
ap.add_argument("--state", default=".pick-last")
a = ap.parse_args()

if os.path.exists(a.state):
    t = datetime.datetime.fromisoformat(open(a.state).read().strip())
    t += datetime.timedelta(minutes=random.randint(2, 5), seconds=random.randint(0, 59))
else:
    h, m = map(int, a.start.split(":"))
    today = datetime.date.today()
    t = datetime.datetime(today.year, today.month, today.day, h, m, random.randint(0, 59))
    t += datetime.timedelta(minutes=random.randint(1, 4))
if t.hour >= a.end:
    sys.exit(f"past {a.end}:00, stop")
d = t.strftime("%Y-%m-%dT%H:%M:%S") + a.tz
if subprocess.run(["git", "cherry-pick", "--no-commit", a.commit]).returncode:
    sys.exit(f"conflict: resolve, git add, then commit with date {d} and update {a.state}")
subprocess.run(["git", "commit", "-q", "-C", a.commit, "--date", d],
               env=dict(os.environ, GIT_COMMITTER_DATE=d), check=True)
open(a.state, "w").write(t.isoformat())
print(d)
