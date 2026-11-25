# Lab 1 test results

26/26 tests passed.

Token coverage: 40/40 token types.

Run `python test/tests.py` from the repository folder to reproduce these results. Each file test uses a real temporary UTF-8 source file. The interactive test sends several lines into one running prompt. Expected results are stored in `test/cases.py`.

Leading spaces or tabs in expected-output lines are removed before comparison. Actual scanner output is not changed except for trailing newline removal. Trailing prompt spaces are preserved.

Tokens are stdout; diagnostics are stderr. These streams are recorded separately because their combined display order can vary.

| Test | Mode | Result |
| --- | --- | --- |
| 01_empty_input | file | PASS |
| 02_whitespace | file | PASS |
| 03_operators_and_punctuation | file | PASS |
| 04_all_keywords | file | PASS |
| 05_identifiers_and_keyword_boundaries | file | PASS |
| 06_numbers | file | PASS |
| 07_decimal_boundaries_and_minus | file | PASS |
| 08_number_identifier_boundary | file | PASS |
| 09_strings | file | PASS |
| 10_multiline_string | file | PASS |
| 11_backslash_is_literal | file | PASS |
| 12_comments_and_lines | file | PASS |
| 13_comment_at_eof | file | PASS |
| 14_division_and_adjacent_comment | file | PASS |
| 15_slash_at_eof | file | PASS |
| 16_longest_operator_match | file | PASS |
| 17_unexpected_characters_and_recovery | file | PASS |
| 18_unterminated_string | file | PASS |
| 19_unterminated_multiline_string | file | PASS |
| 20_both_error_types | file | PASS |
| 21_ascii_lexical_rules | file | PASS |
| 22_unicode_inside_string | file | PASS |
| 23_windows_line_endings | file | PASS |
| 24_interactive_error_recovery | interactive | PASS |
| 25_invalid_single_quotes | file | PASS |
| 26_null_and_backslash_outside_strings | file | PASS |

## 01_empty_input

Purpose: Empty input still produces an EOF token.

Mode: file

Source input (Python representation shows exact whitespace):

```text
''
```

Expected tokens/stdout:

```text
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 02_whitespace

Purpose: Spaces, tabs and carriage returns are ignored; newlines count.

Mode: file

Source input (Python representation shows exact whitespace):

```text
' \t\r\n\n'
```

Expected tokens/stdout:

```text
EOF '' None (line 3)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
EOF '' None (line 3)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 03_operators_and_punctuation

Purpose: Every punctuation and operator token, including Volt's percent token.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'(){} , . - + ; / * % ! != = == > >= < <='
```

Expected tokens/stdout:

```text
LEFT_PAREN '(' None (line 1)
RIGHT_PAREN ')' None (line 1)
LEFT_BRACE '{' None (line 1)
RIGHT_BRACE '}' None (line 1)
COMMA ',' None (line 1)
DOT '.' None (line 1)
MINUS '-' None (line 1)
PLUS '+' None (line 1)
SEMICOLON ';' None (line 1)
SLASH '/' None (line 1)
STAR '*' None (line 1)
PERCENT '%' None (line 1)
BANG '!' None (line 1)
BANG_EQUAL '!=' None (line 1)
EQUAL '=' None (line 1)
EQUAL_EQUAL '==' None (line 1)
GREATER '>' None (line 1)
GREATER_EQUAL '>=' None (line 1)
LESS '<' None (line 1)
LESS_EQUAL '<=' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
LEFT_PAREN '(' None (line 1)
RIGHT_PAREN ')' None (line 1)
LEFT_BRACE '{' None (line 1)
RIGHT_BRACE '}' None (line 1)
COMMA ',' None (line 1)
DOT '.' None (line 1)
MINUS '-' None (line 1)
PLUS '+' None (line 1)
SEMICOLON ';' None (line 1)
SLASH '/' None (line 1)
STAR '*' None (line 1)
PERCENT '%' None (line 1)
BANG '!' None (line 1)
BANG_EQUAL '!=' None (line 1)
EQUAL '=' None (line 1)
EQUAL_EQUAL '==' None (line 1)
GREATER '>' None (line 1)
GREATER_EQUAL '>=' None (line 1)
LESS '<' None (line 1)
LESS_EQUAL '<=' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 04_all_keywords

Purpose: Every reserved word has its own token type.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'and class else false for fun if nil or say return super this true let while'
```

Expected tokens/stdout:

```text
AND 'and' None (line 1)
CLASS 'class' None (line 1)
ELSE 'else' None (line 1)
FALSE 'false' None (line 1)
FOR 'for' None (line 1)
FUN 'fun' None (line 1)
IF 'if' None (line 1)
NIL 'nil' None (line 1)
OR 'or' None (line 1)
SAY 'say' None (line 1)
RETURN 'return' None (line 1)
SUPER 'super' None (line 1)
THIS 'this' None (line 1)
TRUE 'true' None (line 1)
LET 'let' None (line 1)
WHILE 'while' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
AND 'and' None (line 1)
CLASS 'class' None (line 1)
ELSE 'else' None (line 1)
FALSE 'false' None (line 1)
FOR 'for' None (line 1)
FUN 'fun' None (line 1)
IF 'if' None (line 1)
NIL 'nil' None (line 1)
OR 'or' None (line 1)
SAY 'say' None (line 1)
RETURN 'return' None (line 1)
SUPER 'super' None (line 1)
THIS 'this' None (line 1)
TRUE 'true' None (line 1)
LET 'let' None (line 1)
WHILE 'while' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 05_identifiers_and_keyword_boundaries

Purpose: Underscores, digits, case, keyword prefixes and old Lox words.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'name _ _name name2 Name TRUE True var print orchid letter saySomething'
```

Expected tokens/stdout:

```text
IDENTIFIER 'name' None (line 1)
IDENTIFIER '_' None (line 1)
IDENTIFIER '_name' None (line 1)
IDENTIFIER 'name2' None (line 1)
IDENTIFIER 'Name' None (line 1)
IDENTIFIER 'TRUE' None (line 1)
IDENTIFIER 'True' None (line 1)
IDENTIFIER 'var' None (line 1)
IDENTIFIER 'print' None (line 1)
IDENTIFIER 'orchid' None (line 1)
IDENTIFIER 'letter' None (line 1)
IDENTIFIER 'saySomething' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
IDENTIFIER 'name' None (line 1)
IDENTIFIER '_' None (line 1)
IDENTIFIER '_name' None (line 1)
IDENTIFIER 'name2' None (line 1)
IDENTIFIER 'Name' None (line 1)
IDENTIFIER 'TRUE' None (line 1)
IDENTIFIER 'True' None (line 1)
IDENTIFIER 'var' None (line 1)
IDENTIFIER 'print' None (line 1)
IDENTIFIER 'orchid' None (line 1)
IDENTIFIER 'letter' None (line 1)
IDENTIFIER 'saySomething' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 06_numbers

Purpose: Zero, integers, decimals and leading zeros become float literals.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'0 123 45.67 007'
```

Expected tokens/stdout:

```text
NUMBER '0' 0.0 (line 1)
NUMBER '123' 123.0 (line 1)
NUMBER '45.67' 45.67 (line 1)
NUMBER '007' 7.0 (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
NUMBER '0' 0.0 (line 1)
NUMBER '123' 123.0 (line 1)
NUMBER '45.67' 45.67 (line 1)
NUMBER '007' 7.0 (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 07_decimal_boundaries_and_minus

Purpose: A dot needs a following digit to join a number; minus stays separate.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'.5 5. 1.2.3 -12 1..2'
```

Expected tokens/stdout:

```text
DOT '.' None (line 1)
NUMBER '5' 5.0 (line 1)
NUMBER '5' 5.0 (line 1)
DOT '.' None (line 1)
NUMBER '1.2' 1.2 (line 1)
DOT '.' None (line 1)
NUMBER '3' 3.0 (line 1)
MINUS '-' None (line 1)
NUMBER '12' 12.0 (line 1)
NUMBER '1' 1.0 (line 1)
DOT '.' None (line 1)
DOT '.' None (line 1)
NUMBER '2' 2.0 (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
DOT '.' None (line 1)
NUMBER '5' 5.0 (line 1)
NUMBER '5' 5.0 (line 1)
DOT '.' None (line 1)
NUMBER '1.2' 1.2 (line 1)
DOT '.' None (line 1)
NUMBER '3' 3.0 (line 1)
MINUS '-' None (line 1)
NUMBER '12' 12.0 (line 1)
NUMBER '1' 1.0 (line 1)
DOT '.' None (line 1)
DOT '.' None (line 1)
NUMBER '2' 2.0 (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 08_number_identifier_boundary

Purpose: Unsupported exponent forms and adjacent names split into ordinary tokens.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'1e3 123abc'
```

Expected tokens/stdout:

```text
NUMBER '1' 1.0 (line 1)
IDENTIFIER 'e3' None (line 1)
NUMBER '123' 123.0 (line 1)
IDENTIFIER 'abc' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
NUMBER '1' 1.0 (line 1)
IDENTIFIER 'e3' None (line 1)
NUMBER '123' 123.0 (line 1)
IDENTIFIER 'abc' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 09_strings

Purpose: Empty strings, ordinary text and symbols inside strings are accepted.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'"" "hello" "symbols @# // %"'
```

Expected tokens/stdout:

```text
STRING '""' '' (line 1)
STRING '"hello"' 'hello' (line 1)
STRING '"symbols @# // %"' 'symbols @# // %' (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
STRING '""' '' (line 1)
STRING '"hello"' 'hello' (line 1)
STRING '"symbols @# // %"' 'symbols @# // %' (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 10_multiline_string

Purpose: Multiline strings use the opening line; later tokens keep correct lines.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'"first\nsecond"\nsay 2;'
```

Expected tokens/stdout:

```text
STRING '"first\nsecond"' 'first\nsecond' (line 1)
SAY 'say' None (line 3)
NUMBER '2' 2.0 (line 3)
SEMICOLON ';' None (line 3)
EOF '' None (line 3)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
STRING '"first\nsecond"' 'first\nsecond' (line 1)
SAY 'say' None (line 3)
NUMBER '2' 2.0 (line 3)
SEMICOLON ';' None (line 3)
EOF '' None (line 3)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 11_backslash_is_literal

Purpose: Backslash-n remains two characters; no escape decoding is supported.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'"a\\nb"'
```

Expected tokens/stdout:

```text
STRING '"a\\nb"' 'a\\nb' (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
STRING '"a\\nb"' 'a\\nb' (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 12_comments_and_lines

Purpose: Comments disappear and following token line numbers are correct.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'// @#^ " ignored\nlet x = 1; // end\nsay x;\n'
```

Expected tokens/stdout:

```text
LET 'let' None (line 2)
IDENTIFIER 'x' None (line 2)
EQUAL '=' None (line 2)
NUMBER '1' 1.0 (line 2)
SEMICOLON ';' None (line 2)
SAY 'say' None (line 3)
IDENTIFIER 'x' None (line 3)
SEMICOLON ';' None (line 3)
EOF '' None (line 4)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
LET 'let' None (line 2)
IDENTIFIER 'x' None (line 2)
EQUAL '=' None (line 2)
NUMBER '1' 1.0 (line 2)
SEMICOLON ';' None (line 2)
SAY 'say' None (line 3)
IDENTIFIER 'x' None (line 3)
SEMICOLON ';' None (line 3)
EOF '' None (line 4)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 13_comment_at_eof

Purpose: A comment may finish at EOF without a newline.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'// comment without a newline'
```

Expected tokens/stdout:

```text
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 14_division_and_adjacent_comment

Purpose: A slash is division unless the next character is another slash.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'8/2//comment'
```

Expected tokens/stdout:

```text
NUMBER '8' 8.0 (line 1)
SLASH '/' None (line 1)
NUMBER '2' 2.0 (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
NUMBER '8' 8.0 (line 1)
SLASH '/' None (line 1)
NUMBER '2' 2.0 (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 15_slash_at_eof

Purpose: Looking for a second slash at EOF does not crash.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'/'
```

Expected tokens/stdout:

```text
SLASH '/' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
SLASH '/' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 16_longest_operator_match

Purpose: Two-character operators win; spaces prevent combining operators.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'!== === <== >== ! = < >'
```

Expected tokens/stdout:

```text
BANG_EQUAL '!=' None (line 1)
EQUAL '=' None (line 1)
EQUAL_EQUAL '==' None (line 1)
EQUAL '=' None (line 1)
LESS_EQUAL '<=' None (line 1)
EQUAL '=' None (line 1)
GREATER_EQUAL '>=' None (line 1)
EQUAL '=' None (line 1)
BANG '!' None (line 1)
EQUAL '=' None (line 1)
LESS '<' None (line 1)
GREATER '>' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
BANG_EQUAL '!=' None (line 1)
EQUAL '=' None (line 1)
EQUAL_EQUAL '==' None (line 1)
EQUAL '=' None (line 1)
LESS_EQUAL '<=' None (line 1)
EQUAL '=' None (line 1)
GREATER_EQUAL '>=' None (line 1)
EQUAL '=' None (line 1)
BANG '!' None (line 1)
EQUAL '=' None (line 1)
LESS '<' None (line 1)
GREATER '>' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 17_unexpected_characters_and_recovery

Purpose: Report multiple invalid characters and keep scanning later valid code.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'say 1;\n@\n#\nsay 2;'
```

Expected tokens/stdout:

```text
SAY 'say' None (line 1)
NUMBER '1' 1.0 (line 1)
SEMICOLON ';' None (line 1)
SAY 'say' None (line 4)
NUMBER '2' 2.0 (line 4)
SEMICOLON ';' None (line 4)
EOF '' None (line 4)
```

Expected errors/stderr:

```text
[line 2] Error: Unexpected character '@'.
[line 3] Error: Unexpected character '#'.
```

Actual tokens/stdout:

```text
SAY 'say' None (line 1)
NUMBER '1' 1.0 (line 1)
SEMICOLON ';' None (line 1)
SAY 'say' None (line 4)
NUMBER '2' 2.0 (line 4)
SEMICOLON ';' None (line 4)
EOF '' None (line 4)
```

Actual errors/stderr:

```text
[line 2] Error: Unexpected character '@'.
[line 3] Error: Unexpected character '#'.
```

Expected exit code: 65. Actual exit code: 65.

Matches expectations: Yes.


## 18_unterminated_string

Purpose: An opening quote without a closing quote is a lexical error.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'"oops'
```

Expected tokens/stdout:

```text
EOF '' None (line 1)
```

Expected errors/stderr:

```text
[line 1] Error: Unterminated string.
```

Actual tokens/stdout:

```text
EOF '' None (line 1)
```

Actual errors/stderr:

```text
[line 1] Error: Unterminated string.
```

Expected exit code: 65. Actual exit code: 65.

Matches expectations: Yes.


## 19_unterminated_multiline_string

Purpose: An unfinished multiline string reports its opening line.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'let x = "first\nsecond'
```

Expected tokens/stdout:

```text
LET 'let' None (line 1)
IDENTIFIER 'x' None (line 1)
EQUAL '=' None (line 1)
EOF '' None (line 2)
```

Expected errors/stderr:

```text
[line 1] Error: Unterminated string.
```

Actual tokens/stdout:

```text
LET 'let' None (line 1)
IDENTIFIER 'x' None (line 1)
EQUAL '=' None (line 1)
EOF '' None (line 2)
```

Actual errors/stderr:

```text
[line 1] Error: Unterminated string.
```

Expected exit code: 65. Actual exit code: 65.

Matches expectations: Yes.


## 20_both_error_types

Purpose: Both supported lexical error types can be reported in one file.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'@\n"oops'
```

Expected tokens/stdout:

```text
EOF '' None (line 2)
```

Expected errors/stderr:

```text
[line 1] Error: Unexpected character '@'.
[line 2] Error: Unterminated string.
```

Actual tokens/stdout:

```text
EOF '' None (line 2)
```

Actual errors/stderr:

```text
[line 1] Error: Unexpected character '@'.
[line 2] Error: Unterminated string.
```

Expected exit code: 65. Actual exit code: 65.

Matches expectations: Yes.


## 21_ascii_lexical_rules

Purpose: Non-ASCII letters and digits outside strings are rejected.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'café ٣'
```

Expected tokens/stdout:

```text
IDENTIFIER 'caf' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
[line 1] Error: Unexpected character 'é'.
[line 1] Error: Unexpected character '٣'.
```

Actual tokens/stdout:

```text
IDENTIFIER 'caf' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
[line 1] Error: Unexpected character 'é'.
[line 1] Error: Unexpected character '٣'.
```

Expected exit code: 65. Actual exit code: 65.

Matches expectations: Yes.


## 22_unicode_inside_string

Purpose: String contents may contain Unicode even though names are ASCII.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'"café"'
```

Expected tokens/stdout:

```text
STRING '"café"' 'café' (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
STRING '"café"' 'café' (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 23_windows_line_endings

Purpose: Windows CRLF line endings count as one newline each.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'let x=1;\r\nsay x;\r\n'
```

Expected tokens/stdout:

```text
LET 'let' None (line 1)
IDENTIFIER 'x' None (line 1)
EQUAL '=' None (line 1)
NUMBER '1' 1.0 (line 1)
SEMICOLON ';' None (line 1)
SAY 'say' None (line 2)
IDENTIFIER 'x' None (line 2)
SEMICOLON ';' None (line 2)
EOF '' None (line 3)
```

Expected errors/stderr:

```text
(no output)
```

Actual tokens/stdout:

```text
LET 'let' None (line 1)
IDENTIFIER 'x' None (line 1)
EQUAL '=' None (line 1)
NUMBER '1' 1.0 (line 1)
SEMICOLON ';' None (line 1)
SAY 'say' None (line 2)
IDENTIFIER 'x' None (line 2)
SEMICOLON ';' None (line 2)
EOF '' None (line 3)
```

Actual errors/stderr:

```text
(no output)
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 24_interactive_error_recovery

Purpose: Interactive mode accepts valid input after each kind of error and a blank line.

Mode: interactive

Source input (Python representation shows exact whitespace):

```text
'@\nsay 7;\n"oops\nsay "ok";\n\n'
```

Expected tokens/stdout:

```text
Volt scanner. Press Ctrl+C to exit.
volt> EOF '' None (line 1)
volt> SAY 'say' None (line 1)
NUMBER '7' 7.0 (line 1)
SEMICOLON ';' None (line 1)
EOF '' None (line 1)
volt> EOF '' None (line 1)
volt> SAY 'say' None (line 1)
STRING '"ok"' 'ok' (line 1)
SEMICOLON ';' None (line 1)
EOF '' None (line 1)
volt> EOF '' None (line 1)
volt> 
```

Expected errors/stderr:

```text
[line 1] Error: Unexpected character '@'.
[line 1] Error: Unterminated string.
```

Actual tokens/stdout:

```text
Volt scanner. Press Ctrl+C to exit.
volt> EOF '' None (line 1)
volt> SAY 'say' None (line 1)
NUMBER '7' 7.0 (line 1)
SEMICOLON ';' None (line 1)
EOF '' None (line 1)
volt> EOF '' None (line 1)
volt> SAY 'say' None (line 1)
STRING '"ok"' 'ok' (line 1)
SEMICOLON ';' None (line 1)
EOF '' None (line 1)
volt> EOF '' None (line 1)
volt> 
```

Actual errors/stderr:

```text
[line 1] Error: Unexpected character '@'.
[line 1] Error: Unterminated string.
```

Expected exit code: 0. Actual exit code: 0.

Matches expectations: Yes.


## 25_invalid_single_quotes

Purpose: Single quotes do not delimit strings in Volt.

Mode: file

Source input (Python representation shows exact whitespace):

```text
"'bad'"
```

Expected tokens/stdout:

```text
IDENTIFIER 'bad' None (line 1)
EOF '' None (line 1)
```

Expected errors/stderr:

```text
[line 1] Error: Unexpected character "'".
[line 1] Error: Unexpected character "'".
```

Actual tokens/stdout:

```text
IDENTIFIER 'bad' None (line 1)
EOF '' None (line 1)
```

Actual errors/stderr:

```text
[line 1] Error: Unexpected character "'".
[line 1] Error: Unexpected character "'".
```

Expected exit code: 65. Actual exit code: 65.

Matches expectations: Yes.


## 26_null_and_backslash_outside_strings

Purpose: A null character is an error rather than EOF; bare backslashes are invalid.

Mode: file

Source input (Python representation shows exact whitespace):

```text
'\x00\\'
```

Expected tokens/stdout:

```text
EOF '' None (line 1)
```

Expected errors/stderr:

```text
[line 1] Error: Unexpected character '\x00'.
[line 1] Error: Unexpected character '\\'.
```

Actual tokens/stdout:

```text
EOF '' None (line 1)
```

Actual errors/stderr:

```text
[line 1] Error: Unexpected character '\x00'.
[line 1] Error: Unexpected character '\\'.
```

Expected exit code: 65. Actual exit code: 65.

Matches expectations: Yes.
