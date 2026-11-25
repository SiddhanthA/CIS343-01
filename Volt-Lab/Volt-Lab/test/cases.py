# // --- start AI code ---
# Expected results are written independently of the scanner.
# Raw strings keep backslashes in the expected printed representations.

CASES = [
    {
        "name": "01_empty_input",
        "purpose": "Empty input still produces an EOF token.",
        "source": "",
        "stdout": "EOF '' None (line 1)",
    },
    {
        "name": "02_whitespace",
        "purpose": "Spaces, tabs and carriage returns are ignored; newlines count.",
        "source": " \t\r\n\n",
        "stdout": "EOF '' None (line 3)",
    },
    {
        "name": "03_operators_and_punctuation",
        "purpose": "Every punctuation and operator token, including Volt's percent token.",
        "source": "(){} , . - + ; / * % ! != = == > >= < <=",
        "stdout": r'''LEFT_PAREN '(' None (line 1)
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
                    EOF '' None (line 1)''',
    },
    {
        "name": "04_all_keywords",
        "purpose": "Every reserved word has its own token type.",
        "source": "and class else false for fun if nil or say return super this true let while",
        "stdout": r'''AND 'and' None (line 1)
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
                    EOF '' None (line 1)''',
    },
    {
        "name": "05_identifiers_and_keyword_boundaries",
        "purpose": "Underscores, digits, case, keyword prefixes and old Lox words.",
        "source": "name _ _name name2 Name TRUE True var print orchid letter saySomething",
        "stdout": r'''IDENTIFIER 'name' None (line 1)
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
                    EOF '' None (line 1)''',
    },
    {
        "name": "06_numbers",
        "purpose": "Zero, integers, decimals and leading zeros become float literals.",
        "source": "0 123 45.67 007",
        "stdout": r'''NUMBER '0' 0.0 (line 1)
                    NUMBER '123' 123.0 (line 1)
                    NUMBER '45.67' 45.67 (line 1)
                    NUMBER '007' 7.0 (line 1)
                    EOF '' None (line 1)''',
    },
    {
        "name": "07_decimal_boundaries_and_minus",
        "purpose": "A dot needs a following digit to join a number; minus stays separate.",
        "source": ".5 5. 1.2.3 -12 1..2",
        "stdout": r'''DOT '.' None (line 1)
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
                    EOF '' None (line 1)''',
    },
    {
        "name": "08_number_identifier_boundary",
        "purpose": "Unsupported exponent forms and adjacent names split into ordinary tokens.",
        "source": "1e3 123abc",
        "stdout": r'''NUMBER '1' 1.0 (line 1)
                    IDENTIFIER 'e3' None (line 1)
                    NUMBER '123' 123.0 (line 1)
                    IDENTIFIER 'abc' None (line 1)
                    EOF '' None (line 1)''',
    },
    {
        "name": "09_strings",
        "purpose": "Empty strings, ordinary text and symbols inside strings are accepted.",
        "source": '"" "hello" "symbols @# // %"',
        "stdout": r'''STRING '""' '' (line 1)
            STRING '"hello"' 'hello' (line 1)
            STRING '"symbols @# // %"' 'symbols @# // %' (line 1)
            EOF '' None (line 1)''',
    },
    {
        "name": "10_multiline_string",
        "purpose": "Multiline strings use the opening line; later tokens keep correct lines.",
        "source": '"first\nsecond"\nsay 2;',
        "stdout": r'''STRING '"first\nsecond"' 'first\nsecond' (line 1)
                    SAY 'say' None (line 3)
                    NUMBER '2' 2.0 (line 3)
                    SEMICOLON ';' None (line 3)
                    EOF '' None (line 3)''',
    },
    {
        "name": "11_backslash_is_literal",
        "purpose": "Backslash-n remains two characters; no escape decoding is supported.",
        "source": r'"a\nb"',
        "stdout": r'''STRING '"a\\nb"' 'a\\nb' (line 1)
                    EOF '' None (line 1)''',
    },
    {
        "name": "12_comments_and_lines",
        "purpose": "Comments disappear and following token line numbers are correct.",
        "source": '// @#^ " ignored\nlet x = 1; // end\nsay x;\n',
        "stdout": r'''LET 'let' None (line 2)
                    IDENTIFIER 'x' None (line 2)
                    EQUAL '=' None (line 2)
                    NUMBER '1' 1.0 (line 2)
                    SEMICOLON ';' None (line 2)
                    SAY 'say' None (line 3)
                    IDENTIFIER 'x' None (line 3)
                    SEMICOLON ';' None (line 3)
                    EOF '' None (line 4)''',
    },
    {
        "name": "13_comment_at_eof",
        "purpose": "A comment may finish at EOF without a newline.",
        "source": "// comment without a newline",
        "stdout": "EOF '' None (line 1)",
    },
    {
        "name": "14_division_and_adjacent_comment",
        "purpose": "A slash is division unless the next character is another slash.",
        "source": "8/2//comment",
        "stdout": r'''NUMBER '8' 8.0 (line 1)
                    SLASH '/' None (line 1)
                    NUMBER '2' 2.0 (line 1)
                    EOF '' None (line 1)''',
    },
    {
        "name": "15_slash_at_eof",
        "purpose": "Looking for a second slash at EOF does not crash.",
        "source": "/",
        "stdout": r'''SLASH '/' None (line 1)
                    EOF '' None (line 1)''',
    },
    {
        "name": "16_longest_operator_match",
        "purpose": "Two-character operators win; spaces prevent combining operators.",
        "source": "!== === <== >== ! = < >",
        "stdout": r'''BANG_EQUAL '!=' None (line 1)
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
                    EOF '' None (line 1)''',
    },
    {
        "name": "17_unexpected_characters_and_recovery",
        "purpose": "Report multiple invalid characters and keep scanning later valid code.",
        "source": "say 1;\n@\n#\nsay 2;",
        "stdout": r'''SAY 'say' None (line 1)
                    NUMBER '1' 1.0 (line 1)
                    SEMICOLON ';' None (line 1)
                    SAY 'say' None (line 4)
                    NUMBER '2' 2.0 (line 4)
                    SEMICOLON ';' None (line 4)
                    EOF '' None (line 4)''',
        "stderr": r'''[line 2] Error: Unexpected character '@'.
[line 3] Error: Unexpected character '#'.''',
        "exit_code": 65,
    },
    {
        "name": "18_unterminated_string",
        "purpose": "An opening quote without a closing quote is a lexical error.",
        "source": '"oops',
        "stdout": "EOF '' None (line 1)",
        "stderr": "[line 1] Error: Unterminated string.",
        "exit_code": 65,
    },
    {
        "name": "19_unterminated_multiline_string",
        "purpose": "An unfinished multiline string reports its opening line.",
        "source": 'let x = "first\nsecond',
        "stdout": r'''LET 'let' None (line 1)
                    IDENTIFIER 'x' None (line 1)
                    EQUAL '=' None (line 1)
                    EOF '' None (line 2)''',
        "stderr": "[line 1] Error: Unterminated string.",
        "exit_code": 65,
    },
    {
        "name": "20_both_error_types",
        "purpose": "Both supported lexical error types can be reported in one file.",
        "source": '@\n"oops',
        "stdout": "EOF '' None (line 2)",
        "stderr": r'''[line 1] Error: Unexpected character '@'.
                    [line 2] Error: Unterminated string.''',
        "exit_code": 65,
    },
    {
        "name": "21_ascii_lexical_rules",
        "purpose": "Non-ASCII letters and digits outside strings are rejected.",
        "source": "caf\u00e9 \u0663",
        "stdout": r'''IDENTIFIER 'caf' None (line 1)
                    EOF '' None (line 1)''',
        "stderr": "[line 1] Error: Unexpected character 'é'.\n[line 1] Error: Unexpected character '٣'.",
        "exit_code": 65,
    },
    {
        "name": "22_unicode_inside_string",
        "purpose": "String contents may contain Unicode even though names are ASCII.",
        "source": '"caf\u00e9"',
        "stdout": '''STRING '"café"' 'café' (line 1)\nEOF '' None (line 1)''',
    },
    {
        "name": "23_windows_line_endings",
        "purpose": "Windows CRLF line endings count as one newline each.",
        "source": "let x=1;\r\nsay x;\r\n",
        "stdout": r'''LET 'let' None (line 1)
                    IDENTIFIER 'x' None (line 1)
                    EQUAL '=' None (line 1)
                    NUMBER '1' 1.0 (line 1)
                    SEMICOLON ';' None (line 1)
                    SAY 'say' None (line 2)
                    IDENTIFIER 'x' None (line 2)
                    SEMICOLON ';' None (line 2)
                    EOF '' None (line 3)''',
    },
    {
        "name": "24_interactive_error_recovery",
        "purpose": "Interactive mode accepts valid input after each kind of error and a blank line.",
        "mode": "interactive",
        "source": '@\nsay 7;\n"oops\nsay "ok";\n\n',
        "stdout": r'''Volt scanner. Press Ctrl+C to exit.
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
                    volt> ''',
        "stderr": r'''[line 1] Error: Unexpected character '@'.
                    [line 1] Error: Unterminated string.''',
    },
    {
        "name": "25_invalid_single_quotes",
        "purpose": "Single quotes do not delimit strings in Volt.",
        "source": "'bad'",
        "stdout": r'''IDENTIFIER 'bad' None (line 1)
EOF '' None (line 1)''',
        "stderr": '''[line 1] Error: Unexpected character "'".\n[line 1] Error: Unexpected character "'".''',
        "exit_code": 65,
    },
    {
        "name": "26_null_and_backslash_outside_strings",
        "purpose": "A null character is an error rather than EOF; bare backslashes are invalid.",
        "source": "\x00\\",
        "stdout": "EOF '' None (line 1)",
        "stderr": r'''[line 1] Error: Unexpected character '\x00'.
                    [line 1] Error: Unexpected character '\\'.''',
        "exit_code": 65,
    },
]
# // --- end AI code ---
