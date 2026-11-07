from expr import Binary, Grouping, Literal, Unary
from stmt import Expression, Print
from tokens import TokenType

class VoltRuntimeError(Exception):
    def __init__(self, token, message):
        super().__init__(f"[line {token.line}] Runtime error: {message}")

class Interpreter:
    def interpret(self, statements):
        for statement in statements:
            self.execute(statement)

    def execute(self, statement):
        if isinstance(statement, Print):
            value = self.evaluate(statement.expression)
            print(self.stringify(value))
        elif isinstance(statement, Expression):
            self.evaluate(statement.expression)

    def evaluate(self, expression):
        if isinstance(expression, Literal):
            return expression.value

        if isinstance(expression, Grouping):
            return self.evaluate(expression.expression)

        if isinstance(expression, Unary):
            right = self.evaluate(expression.right)
            operator = expression.operator

            if operator.type == TokenType.BANG:
                return not self.is_truthy(right)
            if operator.type == TokenType.MINUS:
                if not self.is_number(right):
                    raise VoltRuntimeError(operator, "Operand must be a number.")
                return -right

        if isinstance(expression, Binary):
            left = self.evaluate(expression.left)
            right = self.evaluate(expression.right)
            operator = expression.operator
            token_type = operator.type

            if token_type == TokenType.EQUAL_EQUAL:
                return self.is_equal(left, right)
            if token_type == TokenType.BANG_EQUAL:
                return not self.is_equal(left, right)

            if token_type == TokenType.PLUS:
                if self.is_number(left) and self.is_number(right):
                    return left + right
                if isinstance(left, str) and isinstance(right, str):
                    return left + right
                raise VoltRuntimeError(
                    operator, "Operands must be two numbers or two strings."
                )

            if not self.is_number(left) or not self.is_number(right):
                raise VoltRuntimeError(operator, "Operands must be numbers.")

            if token_type == TokenType.MINUS:
                return left - right
            if token_type == TokenType.STAR:
                return left * right
            if token_type == TokenType.SLASH:
                if right == 0:
                    raise VoltRuntimeError(operator, "Cannot divide by zero.")
                return left / right
            if token_type == TokenType.PERCENT:
                if right == 0:
                    raise VoltRuntimeError(operator, "Cannot take remainder with zero.")
                return left % right
            if token_type == TokenType.GREATER:
                return left > right
            if token_type == TokenType.GREATER_EQUAL:
                return left >= right
            if token_type == TokenType.LESS:
                return left < right
            if token_type == TokenType.LESS_EQUAL:
                return left <= right

        raise TypeError("Unknown expression type.")

    def is_number(self, value):
        return type(value) in (int, float)

    def is_truthy(self, value):
        return value is not None and value is not False

    def is_equal(self, left, right):
        if self.is_number(left) and self.is_number(right):
            return left == right
        if type(left) is not type(right):
            return False
        return left == right

    def stringify(self, value):
        if value is None:
            return "nil"
        if value is True:
            return "true"
        if value is False:
            return "false"

        text = str(value)
        if isinstance(value, float) and text.endswith(".0"):
            return text[:-2]
        return text