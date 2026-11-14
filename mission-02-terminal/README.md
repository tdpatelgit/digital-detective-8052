# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use the command-line interface to inspect folders, create and manage practice files safely, understand flags and pipes, and explain what a package manager is.

## 2. Work completed

### Task 2.1 — Basic Terminal operations (all performed inside my repository)

| Operation / command | What it does | What I observed |
|---|---|---|
| `pwd` | Prints the full path of the folder I am currently in | Showed my full assignment folder path |
| `ls` | Lists files and folders here | Showed the mission folders and README |
| `ls -l` | Detailed listing: permissions, owner, size, modified date | Added columns for permissions, byte sizes and timestamps |
| `cd ..` | Moves to the parent folder | `pwd` afterwards showed one folder level removed from the path |
| `mkdir terminal-practice` | Creates a new folder | Empty folder appeared in `ls` |
| `touch notes.txt` | Creates an empty file | File appeared with 0-byte size |
| `echo "..." >> notes.txt` | Adds a line to the end of the file | Two lines present after two `echo >>` commands |
| `cp notes.txt backup.txt` | Copies a file into a second file | Both files listed; backup had identical content |
| `mv backup.txt backup-renamed.txt` | Moves/renames a file | Original name gone from `ls`, new name present |
| `cat notes.txt` | Displays the file's contents | Both original lines were still intact |

### Task 2.2 — Safe file practice in `terminal-practice/`
- **Replacing vs adding to the end:** `>` replaces the whole file contents, while `>>` appends a new line and keeps everything already there. My two `echo >>` operations proved both lines survived.
- **Copying vs moving:** `cp` leaves the original untouched and creates a duplicate; `mv` relocates the file, so after `mv` the old name no longer exists — copying duplicates, moving transfers.
- **What `pwd` provides:** the complete absolute path of my current location, so I always know exactly where relative commands will act.
- **Why directory listing is useful:** it shows what actually exists in a folder (names, sizes, permissions, hidden files) without opening a graphical window, which is how you verify a command had the effect you intended.

### Task 2.3 — Flags and pipes
- `ls` alone printed only names. `ls -lah` printed long-format rows with permission strings, owner, human-readable sizes and dates, and included hidden entries such as `.git`. The `-l` flag switches on the detailed format, `-a` includes hidden files, `-h` makes sizes readable (Ki/Mi/Gi). Flags change how the same command behaves without changing what it is.
- `ls -lah | head -6` — the pipe symbol `|` takes the entire output produced on the left side and feeds it as input to the command on the right side. The left side produced the full listing; `head` accepted it and displayed only the first six lines. The pipe chains small tools into a pipeline.

### Task 2.4 — Package managers
Homebrew 7.0.13 is installed on my machine; I checked its version and package list without installing or removing anything. A package manager is useful because it installs, updates and removes software for you from a trusted catalogue, handles the extra pieces each program depends on, and keeps a single record of what is installed — far safer and more reproducible than downloading random installers from websites.

## 3. Commands / tools used
`pwd` (current directory), `ls` (list), `ls -l` / `ls -lah` (detailed listing), `cd` (change directory), `mkdir` (create directory), `touch` (create empty file), `echo >>` (append a line), `cat` (display file), `cp` (copy), `mv` (move/rename), `|` pipe into `head` (limit output), `brew --version` and `brew list` (package manager inspection).

## 4. My understanding
The Terminal is just another way to do everything Finder does — but each action is an explicit instruction I typed, so I can see exactly what happened and repeat it. Appending versus redirecting is the difference between adding to a document and throwing the document away and starting a new one. Flags are options that modify a command's behaviour, and pipes let one command's output become the next command's input, which is how small commands compose into bigger workflows.

## 5. Difficulties faced
At first hidden files confused the listing comparison — I did not know why `.git` appeared only with `-a`. I also nearly used `>` when I meant `>>`.

## 6. How I resolved them
I re-ran each listing side by side and compared columns, and checked the append by `cat`-ing the file after every change to confirm nothing was erased.

## 7. Evidence / files
- `evidence/mission-02/terminal-operations.txt` — recorded output of the full command sequence (username redacted).
- `evidence/mission-02/flags-pipes.txt` — plain `ls` vs `ls -lah` vs `ls -lah | head -6`.
- `evidence/mission-02/brew-list.txt` — recorded the packages Homebrew manages.
- `evidence/mission-00/tool-versions.txt` — Homebrew version check.

## 8. Commit details
Commit message: `Complete Terminal and file management mission` — committed and pushed to GitHub.
