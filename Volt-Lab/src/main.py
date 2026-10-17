import sys
from ast_printer import AstPrinter
from parser import ParseError, Parser
from scanner import Scanner

class Volt:
    def __init__(self, scan_only=False):
        self.had_error = False
        self.scan_only = scan_only

    def run(self, source):
        self.had_error = False
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        if self.scan_only:
            for token in tokens:
                print(token)

        if scanner.errors:
            for line, message in scanner.errors:
                print(f"[line {line}] Error: {message}", file=sys.stderr)
            self.had_error = True
            return

        if self.scan_only:
            return

        parser = Parser(tokens)
        try:
            expression = parser.parse()
            output = AstPrinter().print(expression)
        except ParseError as error:
            print(error, file=sys.stderr)
            self.had_error = True
            return
        except RecursionError:
            error = parser.error(parser.peek(), "Expression is nested too deeply.")
            print(error, file=sys.stderr)
            self.had_error = True
            return

        print(output)

    def run_file(self, path):
        try:
            with open(path, "r", encoding="utf-8", newline="") as source_file:
                source = source_file.read()
        except (OSError, UnicodeError):
            print(f"Cannot read file: {path}", file=sys.stderr)
            return 74

        self.run(source)
        return 65 if self.had_error else 0

    def run_prompt(self):
        mode = "scanner" if self.scan_only else "parser"
        print(f"Volt {mode}. Press Ctrl+C to exit.")
        while True:
            try:
                source = input("volt> ")
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            if self.scan_only or source.strip():
                self.run(source)

def main():
    arguments = sys.argv[1:]
    scan_only = False
    if arguments and arguments[0] == "--scan":
        scan_only = True
        arguments = arguments[1:]

    if len(arguments) > 1:
        print("Usage: python src/main.py [--scan] [source-file]", file=sys.stderr)
        return 64

    language = Volt(scan_only)
    if arguments:
        return language.run_file(arguments[0])
    return language.run_prompt()

if __name__ == "__main__":
    sys.exit(main())