import sys
from scanner import Scanner

class Volt:
    def __init__(self):
        self.had_error = False

    def run(self, source):
        self.had_error = False
        scanner = Scanner(source)

        for token in scanner.scan_tokens():
            print(token)

        for line, message in scanner.errors:
            print(f"[line {line}] Error: {message}", file=sys.stderr)
            self.had_error = True

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
        print("Volt scanner. Press Ctrl+C to exit.")
        while True:
            try:
                source = input("volt> ")
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            self.run(source)


def main():
    arguments = sys.argv[1:]
    if len(arguments) > 1:
        print("Usage: python src/main.py [source-file]", file=sys.stderr)
        return 64

    interpreter = Volt()
    if arguments:
        return interpreter.run_file(arguments[0])
    return interpreter.run_prompt()


if __name__ == "__main__":
    sys.exit(main())