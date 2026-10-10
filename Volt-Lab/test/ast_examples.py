# // --- start AI code ---
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ast_printer import AstPrinter
from expr import Binary, Grouping, Literal, Unary
from tokens import Token, TokenType


# Each entry contains a test label and a hard-coded AST.
EXAMPLES = [
    (
        "Test 1: All four expression classes",
        Binary(
            Unary(Token(TokenType.MINUS, "-", None, 1), Literal(123)),
            Token(TokenType.STAR, "*", None, 1),
            Grouping(Literal(45.67)),
        ),
    ),
    (
        "Test 2: Addition",
        Binary(Literal(2), Token(TokenType.PLUS, "+", None, 1), Literal(3)),
    ),
    (
        "Test 3: Subtraction",
        Binary(Literal(10), Token(TokenType.MINUS, "-", None, 1), Literal(4)),
    ),
    (
        "Test 4: Division",
        Binary(Literal(12), Token(TokenType.SLASH, "/", None, 1), Literal(3)),
    ),
    (
        "Test 5: Volt remainder operator",
        Binary(Literal(10), Token(TokenType.PERCENT, "%", None, 1), Literal(3)),
    ),
    (
        "Test 6: Equality and boolean literals",
        Binary(Literal(True), Token(TokenType.EQUAL_EQUAL, "==", None, 1), Literal(False)),
    ),
    (
        "Test 7: Inequality, string, and nil",
        Binary(
            Literal("Volt (lab)"),
            Token(TokenType.BANG_EQUAL, "!=", None, 1),
            Literal(None),
        ),
    ),
    (
        "Test 8: Less than",
        Binary(Literal(2), Token(TokenType.LESS, "<", None, 1), Literal(5)),
    ),
    (
        "Test 9: Less than or equal",
        Binary(Literal(5), Token(TokenType.LESS_EQUAL, "<=", None, 1), Literal(5)),
    ),
    (
        "Test 10: Greater than",
        Binary(Literal(5), Token(TokenType.GREATER, ">", None, 1), Literal(2)),
    ),
    (
        "Test 11: Greater than or equal",
        Binary(Literal(5), Token(TokenType.GREATER_EQUAL, ">=", None, 1), Literal(5)),
    ),
    (
        "Test 12: Unary not",
        Unary(Token(TokenType.BANG, "!", None, 1), Literal(True)),
    ),
    (
        "Test 13: Empty string",
        Literal(""),
    ),
    (
        "Test 14: Nested grouping and zero",
        Grouping(Grouping(Literal(0))),
    ),
    (
        "Test 15: Nested binary expressions",
        Binary(
            Literal(1),
            Token(TokenType.PLUS, "+", None, 1),
            Binary(Literal(2), Token(TokenType.STAR, "*", None, 1), Literal(3)),
        ),
    ),
    (
        "Test 16: Nested unary expressions",
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Unary(Token(TokenType.MINUS, "-", None, 1), Literal(5)),
        ),
    ),
]


def main():
    printer = AstPrinter()

    for label, expression in EXAMPLES:
        print(label)
        print(printer.print(expression))
        print()


if __name__ == "__main__":
    main()
# // --- end AI code ---