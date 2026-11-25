class VoltRuntimeError(Exception):
    def __init__(self, token, message):
        super().__init__(f"[line {token.line}] Runtime error: {message}")

class Environment:
    def __init__(self, enclosing=None):
        self.values = {}
        self.enclosing = enclosing

    def define(self, name, value):
        self.values[name.lexeme] = value

    def find(self, name):
        scope = self
        while scope is not None:
            if name.lexeme in scope.values:
                return scope
            scope = scope.enclosing
        raise VoltRuntimeError(name, f"Undefined variable '{name.lexeme}'.")

    def get(self, name):
        scope = self.find(name)
        return scope.values[name.lexeme]

    def assign(self, name, value):
        scope = self.find(name)
        scope.values[name.lexeme] = value