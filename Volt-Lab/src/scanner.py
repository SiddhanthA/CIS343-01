from tokens import Token, TokenType

class Scanner:
    keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "say": TokenType.SAY,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "let": TokenType.LET,
        "while": TokenType.WHILE,
    }

    single_characters = {
        "(": TokenType.LEFT_PAREN,
        ")": TokenType.RIGHT_PAREN,
        "{": TokenType.LEFT_BRACE,
        "}": TokenType.RIGHT_BRACE,
        ",": TokenType.COMMA,
        ".": TokenType.DOT,
        "-": TokenType.MINUS,
        "+": TokenType.PLUS,
        ";": TokenType.SEMICOLON,
        "*": TokenType.STAR,
        "%": TokenType.PERCENT,
    }

    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.errors = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.start_line = 1

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.start_line = self.line
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        character = self.advance()

        if character in self.single_characters:
            self.add_token(self.single_characters[character])
        elif character == "!":
            token_type = TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG
            self.add_token(token_type)
        elif character == "=":
            token_type = TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
            self.add_token(token_type)
        elif character == "<":
            token_type = TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS
            self.add_token(token_type)
        elif character == ">":
            token_type = TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER
            self.add_token(token_type)
        elif character == "/":
            if self.match("/"):
                while not self.is_at_end() and self.peek() != "\n":
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif character in " \r\t":
            pass
        elif character == "\n":
            self.line += 1
        elif character == '"':
            self.string()
        elif self.is_digit(character):
            self.number()
        elif self.is_alpha(character):
            self.identifier()
        else:
            self.error(f"Unexpected character {character!r}.")

    def string(self):
        while not self.is_at_end() and self.peek() != '"':
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.is_at_end():
            self.error("Unterminated string.")
            return

        self.advance() 
        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()

        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    def identifier(self):
        while self.is_alpha(self.peek()) or self.is_digit(self.peek()):
            self.advance()

        text = self.source[self.start:self.current]
        token_type = self.keywords.get(text, TokenType.IDENTIFIER)
        self.add_token(token_type)

    def add_token(self, token_type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.start_line))

    def error(self, message):
        self.errors.append((self.start_line, message))

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        character = self.source[self.current]
        self.current += 1
        return character

    def peek(self):
        if self.is_at_end():
            return ""
        return self.source[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return ""
        return self.source[self.current + 1]

    def match(self, expected):
        if self.is_at_end() or self.peek() != expected:
            return False
        self.current += 1
        return True

    def is_digit(self, character):
        return "0" <= character <= "9"

    def is_alpha(self, character):
        return (
            "a" <= character <= "z"
            or "A" <= character <= "Z"
            or character == "_"
        )
