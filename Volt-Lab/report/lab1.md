# Lab 1

## Language design
The language is named Volt. It is a small language based on Lox. This lab
implements scanning: source text is converted into tokens, without executing it. It is implented via Python.

| Variable keyword | `let` replaces Lox's `var` |
| Output keyword | `say` replaces Lox's `print` | 
| Additional operator | `%`, with token type `PERCENT` | 

The other reserved words are `and`, `class`, `else`, `false`, `for`, `fun`, `if`,
`nil`, `or`, `return`, `super`, `this`, `true`, and `while`. Keywords are
case-sensitive. `var` and `print` are ordinary identifiers in Volt.

The scanner recognizes these token groups:

| Punctuation     | `(` `)` `{` `}` `,` `.` `;`           |
| Arithmetic      | `+` `-` `*` `/` `%`                   |
| Other operators | `!` `!=` `=` `==` `<` `<=` `>` `>=`   |
| Names           | Identifiers and the 16 reserved words |
| Values          | Numbers and double-quoted strings     |
| Number          |	[0-9]+(\.[0-9]+)?                     |
| String          |	"[^"]*"                               |
| Identifier      |	[A-Za-z_][A-Za-z0-9_]*                |
| End of input    | `EOF`                                 |

The leading `#` keeps the lab's `//` markers valid in Python. 


## Implementation
All implementation files are in `src/`:

- `tokens.py` defines 40 token types and the `Token` class.
- `scanner.py` recognizes tokens and records lexical errors.
- `main.py` defines the `Volt` entry-point class and `main()` function.

Each token stores its type, raw lexeme, converted literal and starting line.
The printed format is `TYPE lexeme literal (line N)`. Quotes and backslashes in
the output make empty strings and embedded newlines visible.


## Setup and commands
Use Python 3. No third-party packages are required. Open a terminal in the
repository folder, the folder containing `src`, `test`, and `report`.

Run a source file:
```text
python src/main.py test/example.volt
```

Start interactive mode:
```text
python src/main.py
```

Reproduce the tests and regenerate the detailed results:

```text
python test/lab1/run_tests.py
```

## AI assistance
The tests were prepared with AI assistance using the following comment inclusions:

```text
# // --- start AI code ---
# // --- end AI code ---
```