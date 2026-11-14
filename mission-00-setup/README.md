# Mission 0 — Create your GitHub workspace

## 1. Task / objective
Create a correctly named public GitHub repository and prepare the folder structure for all nine missions.

## 2. Work completed
- Decided the repository name using the rule *assignment name + hyphen + last four USN digits*: **digital-detective-8052** (my USN ends in 8052). Lowercase, hyphen only, no spaces.
- Created the local project folder with the exact same name inside my Documents folder.
- Created every mission folder and its README, plus `mission-05-numbers-data/number_converter.py`, `mission-04-programs/hello.py` placeholders, and the `evidence/` folder.
- Wrote the root `README.md` with the project title, short description, mission index and links.

## 3. Commands / tools used
- `python3 --version` — checks Python 3 is installed (result: Python 3.9.6).
- `git --version` — checks Git is installed (result: git 2.54.0).
- `mkdir` — created the mission folders.
- `git init`, `git add`, `git commit`, `git push` — created the repository history and published it.

## 4. My understanding
A repository is a folder that Git watches: every saved state of its files is recorded as a commit, so earlier versions can be reviewed and mistakes can be undone. Organising the repository by mission folder keeps each task's evidence separate, so my instructor can review one mission at a time and match it to that mission's commit. Naming rules matter because the local folder name and the GitHub repository name must match exactly — otherwise the local project and the online repository would not connect cleanly.

## 5. Difficulties faced
No major difficulties. The only careful part was making sure the repository name followed the exact rule (assignment name + last four USN digits) and that I did not create a second README during the online GitHub setup, which would have conflicted with my local one.

## 6. How I resolved them
I created the repository empty on GitHub and connected the already-prepared local folder to it, then pushed. Verified on GitHub that all mission folders and the root README appeared.

## 7. Evidence / files
- Root `README.md` and all nine mission folders with `README.md` files.
- `evidence/mission-00/tool-versions.txt` — recorded Python 3.9.6, git 2.54.0 and Homebrew 7.0.13 versions.

## 8. Commit details
Commit message: `Set up Digital Detective mission structure` — staged, committed and pushed to GitHub.
