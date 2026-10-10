from expr import Binary, Grouping, Literal, Unary

class AstPrinter:
    def print(self, expression):
        if isinstance(expression, Binary):
            left = self.print(expression.left)
            right = self.print(expression.right)
            return f"({expression.operator.lexeme} {left} {right})"

        elif isinstance(expression, Grouping):
            inside = self.print(expression.expression)
            return f"(group {inside})"

        elif isinstance(expression, Unary):
            right = self.print(expression.right)
            return f"({expression.operator.lexeme} {right})"

        elif isinstance(expression, Literal):
            value = expression.value

            if value is None:
                return "nil"
            if value is True:
                return "true"
            if value is False:
                return "false"
            if isinstance(value, str):
                return repr(value)
        
            return str(value)

        else:
            raise TypeError("Unknown expression type.")