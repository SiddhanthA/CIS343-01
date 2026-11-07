## Language design
The language is named Volt. It is a small language based on Lox, implemented in Python. Lab 1 implements scanning, which converts source text into tokens. Lab 2 adds expression classes and an AST printer that displays hard-coded expressions using parentheses. Lab 3 adds a parser that builds expression trees from source text instead of hard-coded expressions. 

| Variable keyword | `let` replaces Lox's `var` |
| Output keyword | `say` replaces Lox's `print` | 
| Additional operator | `%`, with token type `PERCENT` | 

The other reserved words are `and`, `class`, `else`, `false`, `for`, `fun`, `if`,
`nil`, `or`, `return`, `super`, `this`, `true`, and `while`. Keywords are
case-sensitive. `var` and `print` are ordinary identifiers in Volt.

The scanner recognizes these token groups:

| Category        | Symbols                               |
| --------------- | ------------------------------------- |
| Punctuation     | `(` `)` `{` `}` `,` `.` `;`           |
| Arithmetic      | `+` `-` `*` `/` `%`                   |
| Other operators | `!` `!=` `=` `==` `<` `<=` `>` `>=`   |
| Names           | Identifiers and the 16 reserved words |
| Values          | Numbers and double-quoted strings     |
| Number          |	[0-9]+(\.[0-9]+)?                     |
| String          |	"[^"]*"                               |
| Identifier      |	[A-Za-z_][A-Za-z0-9_]*                |
| End of input    | `EOF`                                 |

| Expression | Grammar                                                                            |
| ---------- | ---------------------------------------------------------------------------------- |
| Expression | `expression → equality ;`                                                          |
| Equality   | `equality → comparison ( ( "!=" \| "==" ) comparison )* ;`                         |
| Comparison | `comparison → term ( ( ">" \| ">=" \| "<" \| "<=" ) term )* ;`                     |
| Term       | `term → factor ( ( "-" \| "+" ) factor )* ;`                                       |
| Factor     | `factor → unary ( ( "/" \| "*" \| "%" ) unary )* ;`                                |
| Unary      | `unary → ( "!" \| "-" ) unary \| primary ;`                                        |
| Primary    | `primary → NUMBER \| STRING \| "true" \| "false" \| "nil" \| "(" expression ")" ;` |

The leading `#` keeps the lab's `//` markers valid in Python. 
Volt follows Lox's expression grammar and adds `%` for remainder.
Supported literals are numbers, strings, booleans, and nil.

Precedence from highest to lowest is: literals and grouping; unary operators; multiplication, division, and remainder; addition and subtraction; comparisons; and equality. Binary operators associate to the left, while unary operators associate to the right.

Lab 3 requires the complete input to follow input -> expression EOF, so extra tokens are rejected. Each input contains one expression without a semicolon.

Lab 4 allows multiple statements in one input. Each statement ends with a semicolon. A `say` statement prints an expression's value, while an expression statement evaluates the expression without printing its result. The expression grammar and operator precedence remain the same.

```text
program        → statement* EOF ;
statement      → expressionStmt | printStmt ;
expressionStmt → expression ";" ;
printStmt      → "say" expression ";" ;
```


## Implementation
All implementation files are in `src/`:

- `tokens.py` defines 40 token types and the `Token` class.
- `scanner.py` recognizes tokens and records lexical errors.
- `main.py` defines the `Volt` entry-point class and `main()` function. It also connects the scanner, parser, and AST printer, and interpreter. The optional --scan mode prints tokens for earlier scanner tests.
- `expr.py` defines Literal, Unary, Binary, and Grouping expressions.
- `ast_printer.py` prints expressions using parentheses to show their hierarchy.
- `parser.py` builds expression and statement trees. It records syntax errors and skips tokens to a likely statement boundary so parsing can continue.
- `stmt.py` defines the Expression and Print statement classes.
- `interpreter.py` evaluates expressions and executes statements. It checks operand types and reports runtime errors. 

Each token stores its type, raw lexeme, converted literal and starting line.
The printed format is `TYPE lexeme literal (line N)`. Quotes and backslashes in
the output make empty strings and embedded newlines visible.

The expression classes store literal values, operators, operands, and
grouped expressions.


## Setup and commands
Use Python 3. No third-party packages are required. Open a terminal in the
repository folder, the folder containing `src`, `test`, and `report`.

| Purpose             | Command                                       |
|---------------------|-----------------------------------------------|
| Lab 4 error test    | `python src/main.py test/errors.volt`         |
| Lab 4 valid test    | `python src/main.py test/statements.volt`     |
| Interactive mode    | `python src/main.py`                          |
| Old scanner example | `python src/main.py --scan test/example.volt` |
| Scanner tests       | `python test/tests.py`                        |
| AST examples        | `python test/ast_examples.py`                 |



## Tests and Results
**Results for tests.py:**
PASS 01_empty_input
PASS 02_whitespace
PASS 03_operators_and_punctuation
PASS 04_all_keywords
PASS 05_identifiers_and_keyword_boundaries
PASS 06_numbers
PASS 07_decimal_boundaries_and_minus
PASS 08_number_identifier_boundary
PASS 09_strings
PASS 10_multiline_string
PASS 11_backslash_is_literal
PASS 12_comments_and_lines
PASS 13_comment_at_eof
PASS 14_division_and_adjacent_comment
PASS 15_slash_at_eof
PASS 16_longest_operator_match
PASS 17_unexpected_characters_and_recovery
PASS 18_unterminated_string
PASS 19_unterminated_multiline_string
PASS 20_both_error_types
PASS 21_ascii_lexical_rules
PASS 22_unicode_inside_string
PASS 23_windows_line_endings
PASS 24_interactive_error_recovery
PASS 25_invalid_single_quotes
PASS 26_null_and_backslash_outside_strings
26/26 tests passed.
Token coverage: 40/40 token types.
[Detailed Lab 1 test results](test_results.md)

**Result for ast_examples.py:**
Test 1: All four expression classes
(* (- 123) (group 45.67))

Test 2: Addition
(+ 2 3)

Test 3: Subtraction
(- 10 4)

Test 4: Division
(/ 12 3)

Test 5: Volt remainder operator
(% 10 3)

Test 6: Equality and boolean literals
(== true false)

Test 7: Inequality, string, and nil
(!= 'Volt (lab)' nil)

Test 8: Less than
(< 2 5)

Test 9: Less than or equal
(<= 5 5)

Test 10: Greater than
(> 5 2)

Test 11: Greater than or equal
(>= 5 5)

Test 12: Unary not
(! true)

Test 13: Empty string
''

Test 14: Nested grouping and zero
(group (group 0))

Test 15: Nested binary expressions
(+ 1 (* 2 3))

Test 16: Nested unary expressions
(- (- 5))

**example results for parser.py**
input: 1 + 2 * 3
output: (+ 1.0 (* 2.0 3.0))

**Lab 4 test results**
PS C:\Users\Sid\Desktop\Volt-Lab> python src/main.py test/errors.volt
[line 2] Error at 'true': Expected ';' after expression.
[line 3] Error at end: Expected an expression.

PS C:\Users\Sid\Desktop\Volt-Lab> python src/main.py test/statements.volt 
one
true
3
nil

## AI assistance
The tests were prepared with AI assistance using the following comment inclusions:

```text
# // --- start AI code ---
# // --- end AI code ---
```
This also includes test_results.md