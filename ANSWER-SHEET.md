# The Digital Detective — Answer Sheet (fill-in fields for every page)

> Repo: https://github.com/tdpatelgit/digital-detective-8052 (public, verified)
> Everything below matches what is already committed and pushed in the repository.

---

## Page 1 — Student information

| Field | Write this |
|---|---|
| Name | Tejas Dharmendra Patel |
| USN | 2402608052 |
| Campus / Section | S-VYASA Campus, Section A-1 |
| GitHub username | tdpatelgit |
| GitHub repository name | digital-detective-8052 |
| GitHub repository URL | https://github.com/tdpatelgit/digital-detective-8052 |

---

## Mission 1 — Know your computer (page 4)

### Task 1.1 — IPOS trace (activity: typing and saving a document)

| Stage | What happens in my example | Hardware / component |
|---|---|---|
| Input | I press keys; each keypress becomes data | Keyboard |
| Processing | CPU runs the text editor, turns keypresses into characters, keeps the draft in memory | CPU / processor and RAM |
| Output | Characters appear on screen as I type | Display |
| Storage | On save, the file is written to disk and survives closing the program | SSD (internal storage) |

The activity moves input → output continuously (every keypress is processed and shown at once) and becomes permanent only at the storage stage, when I save.

### Task 1.2 — Hardware and software

| Item | Hardware or software? | Software type | Purpose |
|---|---|---|---|
| Keyboard | Hardware | Not applicable | Enter text |
| Trackpad | Hardware | Not applicable | Move the pointer |
| Display | Hardware | Not applicable | Show output |
| SSD | Hardware | Not applicable | Store files permanently |
| macOS | Software | Operating system software | Manages the computer and its resources |
| Safari | Software | Application software | Browse the web |
| Notes | Software | Application software | Writing and keeping notes |
| Disk Utility | Software | Utility software | Checks, repairs and manages the disk |

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
|---|---|---|---|
| ATM | Cash withdrawal and account services | Inserted card / keypad PIN | Dispensed cash / printed receipt |
| Traffic signal | Control vehicle flow at a junction | Timer or vehicle sensors | Red / yellow / green light |
| Smart TV | Streams video and apps | Remote control / voice command | Picture on screen and sound |

---

## Mission 2 — The Terminal (pages 5–6)

### Task 2.1 — Basic Terminal operations

| Operation / command name | Command | What I observed |
|---|---|---|
| Current-directory display | `pwd` | Full path of my current folder printed |
| Directory listing | `ls` | Mission folders and README listed by name |
| Detailed listing | `ls -l` | Added permissions, owner, size, date columns |
| Change directory | `cd ..` | Moved to parent; `pwd` path lost one level |
| Create directory | `mkdir terminal-practice` | Empty new folder appeared in `ls` |
| Create empty file | `touch notes.txt` | File appeared with 0-byte size |
| Copy file | `cp notes.txt backup.txt` | Duplicate created; original still present |
| Move / rename file | `mv backup.txt backup-renamed.txt` | Old name gone, new name present |
| Display file contents | `cat notes.txt` | Both original lines still present |

### Task 2.2 — Safe file practice (the four answers)

- **Replacing vs adding to the end:** `>` replaces the whole file's contents; `>>` appends a new line and keeps everything already there.
- **Copying vs moving:** `cp` leaves the original untouched and creates a duplicate; `mv` relocates the file, so the old name no longer exists.
- **What the current-directory display gives:** the complete absolute path of where I am, so I know exactly where other commands will act.
- **Why directory listing is useful:** it shows what actually exists in a folder — names, sizes, permissions, hidden files — without opening a graphical window, so I can confirm a command had the intended effect.

### Task 2.3 — Flags and pipes

- `ls` alone shows only names. `ls -lah` shows detailed rows (permission string, owner, human-readable sizes, dates) **plus hidden files** like `.git`.
  - `-l` = long/detailed format, `-a` = include hidden files, `-h` = human-readable sizes.
- `ls -lah | head -6` — the pipe `|` takes the **entire output of the command on the left** and feeds it as **input to the command on the right**. Left side produces the full listing; `head` accepts it and displays only the first 6 lines.

### Task 2.4 — Package managers (write 2–3 sentences)

A package manager installs, updates and removes software from one trusted catalogue, handles the extra pieces each program depends on, and keeps a single record of what is installed — far safer and more repeatable than downloading random installers from websites. Homebrew 7.0.13 is installed on my machine and manages 173 packages (checked with `brew --version` and `brew list`, nothing installed or removed).

---

## Mission 3 — The operating system (pages 6–7)

### Task 3.1 — System exploration (privacy-safe)

| Information explored | What it tells you | My observation |
|---|---|---|
| Operating system / system details | Which OS and version is running | macOS 27.2.1 (Darwin 27.2.0, arm64) |
| Current account identity | Which account is active | [redacted] |
| Available and used storage | Disk size, space used, space left | 1.8 Ti volume, ~197 Gi available |
| System activity snapshot | Programs currently running with PIDs | Dozens of processes; `launchd` at PID 1 |

### Task 3.2 — Processes

- **What is a process?** A program that is currently running — an active instance with its own memory and state.
- **What does the PID column represent?** The process identifier: the unique number the OS assigns each running process so it can be tracked, communicated with or stopped.
- **Two examples:** `launchd` (PID 1, the first process that starts everything else) and `logd` (background daemon recording system logs). Safari/editor would also appear when open.

### Task 3.3 — Paths and permissions

- **Absolute path:** full path from the root of the filesystem; works no matter where I am — e.g. the full `/Users/…/digital-detective-8052` path shown by `pwd`.
- **Relative path:** measured from my current location — e.g. from the repo root, `cd mission-03-operating-system`.
- My practice file listing showed **`-rw-r--r--`**: owner (me) can **read and write** but **not execute**; group and others can read only. No permissions were changed.

| Permission | Meaning | Example |
|---|---|---|
| r — Read | Contents can be read | Opening a text file |
| w — Write | File can be changed | Editing a text file |
| x — Execute | File can be run; on a directory allows traversal | Running a script |

### Task 3.4 — OS responsibilities

| OS responsibility | My explanation | Example |
|---|---|---|
| Process management | Starts, schedules and stops programs, deciding what runs and when | `launchd` at PID 1 boots the whole system |
| Memory management | Gives each running program its own working space so programs can't corrupt each other | Opening Safari and an editor gives each its own RAM region |
| Device management | Controls hardware access through drivers so apps never touch raw devices | My keyboard works in every app without per-app keyboard code |
| File management | Organises storage into folders and files and tracks where each lives | Reading `notes.txt` from `terminal-practice/` through its path |
| User interface / shell | The way the user gives instructions — GUI or command shell | Terminal is a shell: I typed commands, the OS carried them out |
| Security and permissions | Decides who may read, change or run each file using r/w/x bits | Group and others lacked `w` on my practice file |

---

## Mission 4 — How programs run (page 7)

### Task 4.2 — Compiler vs interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Before the program runs — the whole source is translated first | At runtime — instructions read and carried out one at a time |
| Typical output | A machine-code file / executable that can be run again | No separate output file; results appear only while running |
| One example | C / C++ compiled into a binary | Python run with `python3 hello.py` |
| One advantage | Runs faster — translation done once, ahead of time | Edit a line and run again instantly, no build step |

**Paragraph (3–4 sentences):** A compiler takes the entire source code and translates it into a lower-level form, usually machine code, before anything executes, so running the finished program is fast but a translation step comes first. An interpreter instead acts as the executor: it reads each instruction as the program runs and carries it out immediately, which makes experimenting quick but re-translates every run. Real languages mix both — Python compiles source to bytecode first, then an interpreter runs that bytecode — so the distinction is about the dominant approach, not a pure either/or.

---

## Mission 5 — Numbers and data (page 8)

### Task 5.1 — Manual conversions (write the working)

| Question | Working and answer |
|---|---|
| Decimal 13 → binary | 13÷2=6 r**1** · 6÷2=3 r**0** · 3÷2=1 r**1** · 1÷2=0 r**1** → read bottom-up: **1101** |
| Decimal 25 → binary | 25÷2=12 r**1** · 12÷2=6 r**0** · 6÷2=3 r**0** · 3÷2=1 r**1** · 1÷2=0 r**1** → **11001** |
| Binary 1010 → decimal | 1×8 + 0×4 + 1×2 + 0×1 = 8+0+2+0 = **10** |
| Binary 1101 → decimal | 1×8 + 1×4 + 0×2 + 1×1 = 8+4+0+1 = **13** |
| Hex A → decimal | A is **10** in hex |
| Hex 1F → decimal | 1×16 + F(15)×1 = 16+15 = **31** |
| Binary 1111 → hex | 1111₂ = 8+4+2+1 = 15₁₀ = **F**, so 1111₂ = **F**₁₆ |

### Task 5.2 — Python verification

| Expression tested | Result | Matches manual? |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(13)` | `0xd` | Yes (13 = D) |
| `hex(25)` | `0x19` | Yes (16+9 = 25) |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `bin(15)` | `0b1111` | Yes — confirms 1111₂ = F₁₆ |

### Task 5.3 — number_converter.py test runs

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 250 | `0b11111010` | `0xfa` |

`bin()` returns the base-2 form of an integer prefixed with `0b`; `hex()` returns the base-16 form prefixed with `0x`. The prefixes are how Python labels which base a number is written in.

### Task 5.4 — How is text stored?

- ASCII decimal codes: uppercase **A = 65**, lowercase **a = 97** (checked with `ord('A')`, `ord('a')`).
- **Why an encoding standard is needed:** a computer stores only numbers, so an agreed standard is required to define which number stands for which character — without a shared standard the same bytes would be read as different letters on different systems.
- **Character outside basic ASCII:** **₹** (the Indian rupee sign — like é, ñ, Devanagari letters and emoji; covered by wider standards such as UTF-8).

---

## Mission 6 — Git and GitHub (page 9)

### Task 6.1 — Basic Git workflow

| Git operation | What it does in my own words |
|---|---|
| Check repository status | `git status` — shows my branch, which files changed since the last commit, and which changes are staged |
| Stage selected changes | `git add <file>` — marks the file's changes as the next candidate to be recorded |
| Create a commit | `git commit -m "..."` — records every staged change permanently as one snapshot with my message |
| View commit history | `git log --oneline` — lists recent commits, newest first |

**Staging vs committing:** staging (`git add`) only *selects* which changes will be included — it prepares them but records nothing; committing *records* exactly those selected changes into history as a permanent, described snapshot. Staging is choosing, committing is recording.

### Task 6.2 — Branch (done on GitHub)

Created branch `update-about` with `git switch -c update-about`, added a short **"My Learning"** section to the root README, committed with message `Add My Learning section to root README` and pushed with `git push origin update-about`.

### Task 6.3 — Pull Request

- **Branch:** a separate line of development — changes can be added and tested without disturbing `main` until ready.
- **Pull Request:** a formal request to bring a branch's changes into another branch, showing exactly what changed for review before anything is accepted.
- **Why useful in a shared project:** people work in parallel on their own branches, and changes are discussed and reviewed before joining the main line instead of everyone overwriting one folder.
- **Status to write in the README:** the PR from `update-about` into `main` is **OPEN — created but NOT merged**, because the assignment says to merge only if the instructor asks. (It is PR #1 on GitHub.)

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

---

## Mission 7 — How computers communicate (page 10)

### Task 7.1 — Network concepts (your-words + example column)

| Concept | Explain in your own words | Example |
|---|---|---|
| LAN | A network covering a small area like a home, lab or office | My laptop, phone and router on home Wi-Fi |
| MAN | A network covering a city or large campus, linking many LANs | A city-wide network connecting government buildings |
| WAN | A network covering large geographical areas; a network of networks | The internet carrying traffic between countries |
| DNS | The directory service that turns a domain name into the IP address machines use | Looking up `example.org` and receiving its address |
| Router | A device joining networks and forwarding data, choosing where each packet goes | My home router passing traffic from my LAN to my internet provider |
| Protocol | Agreed rules devices follow so they understand each other | HTTP/HTTPS between a browser and a website |
| Packet switching | Data split into packets that travel independently and reassemble at the destination | Parts of a video call taking different routes yet arriving together |
| Client-server | A client requests a service, a server provides it | My browser (client) asking GitHub (server) for a page |

### Task 7.2 — Network observations (answers to the three questions)

- **What a connectivity test checks:** whether my computer can actually reach a destination at all — `ping -c 4 example.com` sent four test packets and got four replies (~20–26 ms each, 0% loss). If this fails the problem is in my network path, not the website.
- **What a DNS lookup displays:** the name I queried and the IP address(es) that name maps to (`nslookup example.org`).
- **Role of DNS when I type a website name:** my machine doesn't know where the site lives; DNS answers "which IP address belongs to this name?" so the browser then knows which machine to talk to.

### Task 7.3 — What happens when you open a website (6 steps)

1. The **client** (my browser) receives the address I typed and first needs the site's IP address.
2. The browser asks **DNS**, which looks up the name and replies with the **server's** IP address.
3. My request leaves the computer through my home network (LAN) and the **router**, which forwards it across the wider network.
4. The request follows the rules of the **protocol** (HTTPS) and reaches the server hosting the site.
5. The server processes the request and sends a response — the page's files — as data **packets**.
6. The packets are reassembled on my side and the browser reads them and displays the page to me.

---

## Mission 8 — Final report (pages 11–12)

No blank tables to fill on these pages — it's the verification checklist, and every item is already satisfied:

- All 9 mission folders present, each with its own README in the required format ✓
- One dedicated meaningful commit per mission, all pushed (verified in `git log`) ✓
- IPOS, hardware/software, systems examples ✓ · Terminal, flags, pipes ✓ · OS, processes, paths, permissions ✓
- Compiler vs interpreter compared ✓ · Conversions with working + Python verification ✓
- `number_converter.py` ran with 3 test values (13, 25, 250) ✓
- Commit history, `update-about` branch and Pull Request visible on GitHub (PR #1, OPEN) ✓
- Personal details redacted in all evidence; repository public ✓
- **URL to submit through the instructor's form:** https://github.com/tdpatelgit/digital-detective-8052

---

## Commit messages used (for reference)

| Mission | Commit message |
|---|---|
| 0 | Set up Digital Detective mission structure |
| 1 | Complete computer basics and IPOS mission |
| 2 | Complete Terminal and file management mission |
| 3 | Document operating system and file management |
| 4 | Compare compilers and interpreters |
| 5 | Build number converter and practise data representation |
| 6 | Complete Git and GitHub collaboration mission |
| 7 | Explain networking concepts and website communication |
| 8 | Complete final report and verify assignment submission |
| 6 (branch) | Add My Learning section to root README |
| evidence | Record Git history evidence for missions 6 and 8 |
