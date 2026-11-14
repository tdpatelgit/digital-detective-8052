# Mission 3 — Understand the operating system

## 1. Task / objective
Explore my operating system, observe running processes, understand paths and file permissions, and explain the operating system's responsibilities.

## 2. Work completed

### Task 3.1 — System exploration (privacy-safe)

| Information explored | What it tells you | My observation |
|---|---|---|
| `sw_vers` / `uname -srm` | Which OS and version is running | macOS 27.2.1 (Darwin 27.2.0, arm64) |
| `whoami` | Which account is currently active | [redacted] |
| `df -h` | Disk sizes, used space and available space | Main volume: 1.8 Ti total, ~197 Gi available |
| `ps -ax -o pid,comm` | Snapshot of running programs with their PIDs | launchd at PID 1 plus many system daemons and my shell |

### Task 3.2 — Processes
- A **process** is a program that is currently running — an active instance of an executable, with its own memory and state.
- The **PID** column is the process identifier: the unique number the operating system assigns to each running process so it can be tracked, communicated with or stopped.
- Two examples running on my machine: `launchd` (the very first process, PID 1, which starts everything else) and `logd` (a background daemon that records system logs). A browser or text editor would also appear when open.

### Task 3.3 — Paths and permissions
- **Absolute path:** the full path starting from the root of the filesystem, e.g. `/Users/[redacted]/Documents/Newton School Of Technology/digital-detective-8052` (shown by `pwd`). It works no matter where you currently are.
- **Relative path:** a path measured from your current location, e.g. from the repository root, `cd mission-03-operating-system` reaches this folder without repeating the whole path.
- Detailed listing of my practice file showed `-rw-r--r--`: the owner (me) has **r** (read) and **w** (write) but **not** **x** (execute); the group and others have read only. I did not change any permissions.

| Permission | Meaning | Example |
|---|---|---|
| r — Read | Contents can be read | Opening a text file |
| w — Write | File can be changed | Editing a text file |
| x — Execute | File can be run; on a directory it allows traversal | Running a script |

### Task 3.4 — Operating-system responsibilities

| OS responsibility | My explanation | Example |
|---|---|---|
| Process management | Starts, schedules and stops programs, deciding which ones run and when | `ps` shows dozens of processes the OS keeps running; `launchd` at PID 1 boots the system |
| Memory management | Allocates each running program its own working space so programs cannot corrupt each other | Opening Safari and a text editor gives each its own RAM region |
| Device management | Controls access to hardware through drivers so applications never talk to raw devices | My keyboard works in every app without each app having its own keyboard code |
| File management | Organises storage into folders and files and tracks where each one physically lives | Reading `notes.txt` from `terminal-practice/` through a path |
| User interface / shell | Provides the way the user gives instructions — graphical interface or a command shell | Terminal itself is a shell: I typed commands and the OS carried them out |
| Security and permissions | Decides which user may read, change or run each file using the r/w/x permission bits | Group and others could not write my `notes.txt` because they lack `w` |

## 3. Commands / tools used
`sw_vers` and `uname -srm` (system identity), `whoami` (account identity), `df -h` (storage report), `ps -ax -o pid,comm` (process snapshot), `cd` (navigation between paths), `ls -l` (permission strings).

## 4. My understanding
The OS sits between me and the hardware. Nothing a normal program does — reading a file, using the keyboard, allocating memory — happens directly; the operating system performs it on the program's behalf and enforces the permission model at every step. Seeing PID 1 as `launchd` made that concrete: on macOS everything the OS starts is organised as a tree of processes rooted at one first process.

## 5. Difficulties faced
The `ps` snapshot was long and full of unfamiliar daemon names, which made it hard to pick meaningful examples.

## 6. How I resolved them
I trimmed the output to just PID and command name columns and took the first few rows, then used a file-listing command to inspect permissions on my own practice file where I knew exactly what to expect. I redacted my username from the evidence.

## 7. Evidence / files
- `evidence/mission-03/system-info.txt` — OS version, storage report, process snapshot, permission listing, absolute vs relative path demonstration (personal details redacted).

## 8. Commit details
Commit message: `Document operating system and file management` — committed and pushed to GitHub.
