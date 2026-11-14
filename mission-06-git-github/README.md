# Mission 6 — Git and GitHub

## 1. Task / objective
Understand version control in practice: inspect status, stage and commit changes, review history, create a branch, open a Pull Request and explain the collaboration workflow.

## 2. Work completed

### Task 6.1 — Basic Git workflow

| Git operation | What it does in my own words |
|---|---|
| `git status` | Reports the current state: which branch I am on, which files changed since the last commit, and which changes are staged but not yet recorded |
| `git add <file>` | Stages the chosen file — marks its current changes as the next candidate to be recorded |
| `git commit -m "..."` | Records every staged change permanently as one snapshot with my message |
| `git log --oneline` | Lists recent commits, newest first, so I can review the recorded history |

**Staging vs committing:** staging (`git add`) only selects which changes will be included — it prepares them but nothing is recorded yet; committing takes exactly those selected changes and writes them into history as a permanent, described snapshot. Staging is choosing, committing is recording.

### Task 6.2 — Branch `update-about`
Created the branch `update-about` with `git switch -c update-about`, added a short **"My Learning"** section to the root `README.md`, staged and committed it, then published the branch with `git push origin update-about`.

### Task 6.3 — Pull Request
Opened a Pull Request on GitHub comparing `update-about` against `main`, with a description explaining the README change. **Status: the PR is currently OPEN and not merged** — the assignment says to merge only if the instructor asks, and it has not been asked yet.

- A **branch** is a separate line of development: I can add and test changes without disturbing `main` until they are ready.
- A **Pull Request** is a formal request to bring a branch's changes into another branch, with a visible review of exactly what changed before anything is accepted. They are useful in a shared project because people work in parallel on their own branches, and changes are discussed and reviewed before joining the main line, instead of everyone overwriting one folder.

### Task 6.4 — Git command glossary

| Operation | One-line explanation |
|---|---|
| Initialise a repository | `git init` — starts Git tracking in a folder |
| Check status | `git status` — show what changed and what is staged |
| Stage changes | `git add` — select changes for the next commit |
| Commit changes | `git commit -m "..."` — record the staged changes permanently with a message |
| View history | `git log` — list the recorded commits |
| Create / list branches | `git switch -c <name>` / `git branch` — start or show lines of development |
| Switch branches | `git switch <name>` — move my working folder onto another line |
| Publish changes | `git push` — send my local commits to GitHub |
| Retrieve remote changes | `git pull` — bring commits from GitHub into my local copy |

## 3. Commands / tools used
`git init`, `git status`, `git add`, `git commit`, `git log --oneline`, `git switch -c update-about`, `git switch main`, `git push`, `git pull`, and the GitHub website for the Pull Request.

## 4. My understanding
Git has two layers: the local layer (status → add → commit → log) where I decide and record changes on my own machine, and the shared layer (push, pull, branch, PR) where recorded history is exchanged with GitHub. The staging step exists so one commit contains exactly the work I mean to describe, not whatever happened to be dirty. The branch + PR cycle is how teams keep one shared main line trustworthy: proposals are isolated, compared and reviewed before merging.

## 5. Difficulties faced
Understanding why my `My Learning` edit did not appear on `main` after I switched back — it only lived on the `update-about` branch until the PR is merged.

## 6. How I resolved them
Checked `git log --oneline` on each branch and compared them, and reviewed the changed-files tab of the PR on GitHub, which showed the edit waiting there for merge review.

## 7. Evidence / files
- `evidence/mission-06/git-history.txt` — commit history showing each mission's dedicated commit, and the branch listing including `update-about`.
- This README documents the staging/commit distinction, glossary, and PR status.

## 8. Commit details
Commit message: `Complete Git and GitHub collaboration mission` — committed and pushed to GitHub. The `update-about` branch commit is `Add My Learning section to root README`, pushed and open as a Pull Request.
