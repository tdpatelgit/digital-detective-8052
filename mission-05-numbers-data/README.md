# Mission 5 — Numbers and data

## 1. Task / objective
Convert values between decimal, binary and hexadecimal by hand, verify every result with Python, build a small number-conversion program, and explain how text is stored.

## 2. Work completed

### Task 5.1 — Manual conversions (full working shown)

| Question | My working and answer |
|---|---|
| Decimal 13 → binary | 13÷2 = 6 r **1**; 6÷2 = 3 r **0**; 3÷2 = 1 r **1**; 1÷2 = 0 r **1**. Read remainders bottom-up: **1101** |
| Decimal 25 → binary | 25÷2 = 12 r **1**; 12÷2 = 6 r **0**; 6÷2 = 3 r **0**; 3÷2 = 1 r **1**; 1÷2 = 0 r **1**. Bottom-up: **11001** |
| Binary 1010 → decimal | 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 0 + 2 + 0 = **10** |
| Binary 1101 → decimal | 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = **13** |
| Hex A → decimal | In hex, A = **10** |
| Hex 1F → decimal | 1×16 + F(15)×1 = 16 + 15 = **31** |
| Binary 1111 → hex | 1111₂ = 8+4+2+1 = 15₁₀, and 15 is the hex digit **F**, so 1111₂ = **F**₁₆ |

### Task 5.2 — Python verification

| Expression I tested | Result | Matches manual? |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(13)` | `0xd` | Yes (13 = D in hex) |
| `hex(25)` | `0x19` | Yes (1×16 + 9 = 25) |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `bin(15)` | `0b1111` | Yes — confirms 1111₂ = F₁₆ |

### Task 5.3 — number_converter.py
The program reads typed text with `input()`, turns it into an integer with `int()`, then applies `bin()` and `hex()`. `bin()` returns the base-2 representation prefixed with `0b`, and `hex()` returns the base-16 representation prefixed with `0x` — the prefixes are Python's way of labelling which base a number is written in. Three test runs:

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 250 | `0b11111010` | `0xfa` |

(250 check by hand: 128+64+32+16+8+2 = 250 ✓ and 250 = 15×16 + 10 = FA₁₆ ✓)

### Task 5.4 — How is text stored?
- ASCII decimal code of uppercase **A = 65**, lowercase **a = 97** (verified with `ord('A')` and `ord('a')`).
- A computer only stores numbers, so an encoding standard is needed to agree which number stands for which character — without a shared standard, the same bytes written by one system would be read as different letters by another.
- A character outside basic ASCII: **₹** (the Indian rupee sign; so are é, ñ, Devanagari letters and emoji — all covered by wider standards like UTF-8).

## 3. Commands / tools used
`python3` (interactive verification and running my converter), `input()` (read user text), `int()` (text → integer, and `int('1010', 2)` / `int('1F', 16)` with a base argument), `bin()` (integer → binary), `hex()` (integer → hexadecimal), `ord()` (character → ASCII/Unicode code).

## 4. My understanding
Every base is just place-value with a different radix: decimal counts groups of 10, binary groups of 2, hexadecimal groups of 16. Manual conversion is repeated division (whole number side) or positional weighting (fraction-free expansion back to decimal). The hand results and Python results agreeing proves the rules are consistent — Python is not doing anything magical, it is applying the same division/weighting. Text storage follows the same principle one level up: characters are also just numbers, mapped through an agreed table.

## 5. Difficulties faced
Reading remainders in the wrong order (top-down instead of bottom-up) on the first attempt for decimal 25, which gave 10011 instead of 11001.

## 6. How I resolved them
Checked the reversed answer back into decimal by weighting positions (1×16+1×2+1 = 19 ≠ 25 vs 1×16+1×8+1 = 25 ✓), which confirmed the bottom-up order, and Python's `bin()` agreed.

## 7. Evidence / files
- `number_converter.py` — the working converter program.
- `evidence/mission-05/python-verification.txt` — three live test runs plus every Task 5.2 expression and result.

## 8. Commit details
Commit message: `Build number converter and practise data representation` — committed and pushed to GitHub.
