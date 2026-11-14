# Mission 4 — How programs run

## 1. Task / objective
Create and run a simple Python program, then compare how compilers and interpreters translate or execute programs.

## 2. Work completed
- Created `hello.py` in this folder containing one line that displays the message `Hello from Python`.
- Ran it from Terminal with `python3 hello.py` and confirmed the message appeared.
- Completed the compiler vs interpreter comparison below.

### Task 4.2 — Compiler vs interpreter comparison

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Before the program runs — the whole source is translated first | At runtime — instructions are read and carried out one at a time |
| Typical output | A separate machine-code file / executable that can be run again on its own | No separate output file; results appear only while the program runs |
| One example | C / C++ compiled into a runnable binary | Python run line by line with `python3 program.py` |
| One advantage | Runs faster because translation happened once, ahead of time | Try changes instantly — edit a line and run again without a separate build step |

**In my own words:** A compiler takes the entire source code and translates it into a lower-level form, usually machine code, before anything executes, so running the finished program is fast but requires a translation step first. An interpreter instead acts as the executor itself: it reads each instruction as the program runs and carries it out immediately, which makes experimenting quick but re-translates every single run. Real languages mix both — Python actually compiles source to bytecode first, then an interpreter runs that bytecode — which is why the distinction is about the dominant approach rather than a pure either/or.

## 3. Commands / tools used
- `python3 hello.py` — the interpreter reads and executes the file; this is the tool that ran my program.
- A plain text editor to create `hello.py`.

## 4. My understanding
Running `python3 hello.py` meant the Python interpreter handled everything: it read the file, translated it internally, and executed it, all in one step. That is why no compiled binary appeared in the folder afterwards. A language like C would instead need a build command producing a separate executable before anything could run. The trade-off is preparation versus speed of iteration.

## 5. Difficulties faced
No major difficulties — the program ran on the first attempt.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `hello.py` — the working one-line program.
- `evidence/mission-04/run.txt` — Terminal output confirming `Hello from Python` was displayed.

## 8. Commit details
Commit message: `Compare compilers and interpreters` — committed and pushed to GitHub.
