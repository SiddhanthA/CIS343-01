from expr import Binary, Grouping, Literal, Unary
from stmt import Expression, Print
from tokens import TokenType

class ParseError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.errors = []

    def parse(self):
        statements = []
        while not self.check(TokenType.EOF):
            try:
                statements.append(self.statement())
            except ParseError as error:
                self.errors.append(error)
                self.synchronize()
        return statements

    def statement(self):
        if self.match(TokenType.SAY):
            return self.print_statement()
        return self.expression_statement()

    def print_statement(self):
        expression = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after value.")
        return Print(expression)

    def expression_statement(self):
        expression = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after expression.")
        return Expression(expression)

    def synchronize(self):
        self.advance()
        while not self.check(TokenType.EOF):
            if self.previous().type == TokenType.SEMICOLON:
                return
            if self.check(TokenType.SAY):
                return
            self.advance()

    def expression(self):
        return self.equality()

    def equality(self):
        expression = self.comparison()
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expression = Binary(expression, operator, right)
        return expression

    def comparison(self):
        expression = self.term()
        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL,
                         TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expression = Binary(expression, operator, right)
        return expression

    def term(self):
        expression = self.factor()
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expression = Binary(expression, operator, right)
        return expression

    def factor(self):
        expression = self.unary()
        while self.match(TokenType.SLASH, TokenType.STAR, TokenType.PERCENT):
            operator = self.previous()
            right = self.unary()
            expression = Binary(expression, operator, right)
        return expression

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)
        if self.match(TokenType.LEFT_PAREN):
            expression = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression.")
            return Grouping(expression)
        raise self.error(self.peek(), "Expected an expression.")

    def match(self, *types):
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def consume(self, token_type, message):
        if self.check(token_type):
            return self.advance()
        raise self.error(self.peek(), message)

    def check(self, token_type):
        return self.peek().type == token_type

    def advance(self):
        if not self.check(TokenType.EOF):
            self.current += 1
        return self.previous()

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def error(self, token, message):
        location = "at end" if token.type == TokenType.EOF else f"at {token.lexeme!r}"
        return ParseError(f"[line {token.line}] Error {location}: {message}")