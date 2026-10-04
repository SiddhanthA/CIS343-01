# // --- start AI code ---
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from cases import CASES


# Support a runner stored in either test/ or test/lab1/.
ROOT = Path(__file__).resolve().parents[1]
if not (ROOT / "src" / "main.py").is_file():
    ROOT = ROOT.parent
MAIN = ROOT / "src" / "main.py"


def clean_expected(text):
    # Remove accidental indentation from expected-output strings only.
    # Keep trailing spaces, including the space after the interactive prompt.
    lines = []
    for line in text.split("\n"):
        lines.append(line.lstrip(" \t"))
    return "\n".join(lines).rstrip("\n")


def code_block(text):
    return "```text\n" + (text if text else "(no output)") + "\n```\n"


def main():
    if not MAIN.is_file():
        print(f"Cannot find the scanner: {MAIN}")
        print("Check that your project has src/main.py and the test folder.")
        return 1

    results = []
    seen_types = set()
    environment = os.environ.copy()
    environment["PYTHONIOENCODING"] = "utf-8"

    with TemporaryDirectory() as temporary_folder:
        for case in CASES:
            mode = case.get("mode", "file")
            command = [sys.executable, str(MAIN)]
            if mode == "file":
                path = Path(temporary_folder) / (case["name"] + ".volt")
                path.write_bytes(case["source"].encode("utf-8"))
                command.append(str(path))

            completed = subprocess.run(
                command,
                input=case["source"] if mode == "interactive" else None,
                capture_output=True,
                text=True,
                encoding="utf-8",
                env=environment,
                cwd=ROOT,
                timeout=10,
            )
            actual_stdout = completed.stdout.rstrip("\n")
            actual_stderr = completed.stderr.rstrip("\n")
            expected_stdout = clean_expected(case["stdout"])
            expected_stderr = clean_expected(case.get("stderr", ""))
            expected_code = case.get("exit_code", 0)
            passed = (
                actual_stdout == expected_stdout
                and actual_stderr == expected_stderr
                and completed.returncode == expected_code
            )
            expected_case = case.copy()
            expected_case["stdout"] = expected_stdout
            expected_case["stderr"] = expected_stderr
            results.append((expected_case, actual_stdout, actual_stderr, completed.returncode, passed))
            if mode == "file":
                seen_types.update(line.split()[0] for line in actual_stdout.splitlines())
            print(f"{'PASS' if passed else 'FAIL'} {case['name']}")
            if not passed:
                print("Expected tokens:\n" + expected_stdout)
                print("Actual tokens:\n" + actual_stdout)
                print("Expected errors:\n" + expected_stderr)
                print("Actual errors:\n" + actual_stderr)

    # Coverage is a separate check; all expected outputs above are independent.
    sys.path.insert(0, str(ROOT / "src"))
    from tokens import TokenType
    missing = {token_type.name for token_type in TokenType} - seen_types
    passed_count = sum(result[4] for result in results)
    summary = f"{passed_count}/{len(results)} tests passed."
    coverage = f"Token coverage: {len(seen_types)}/{len(TokenType)} token types."
    print(summary)
    print(coverage)
    if missing:
        print("Missing token types: " + ", ".join(sorted(missing)))

    runner_path = Path(__file__).resolve().relative_to(ROOT).as_posix()
    cases_path = Path(__file__).with_name("cases.py").relative_to(ROOT).as_posix()
    report = [
        "# Lab 1 test results\n",
        summary + "\n",
        coverage + "\n",
        f"Run `python {runner_path}` from the repository folder to reproduce "
        "these results. Each file test uses a real temporary UTF-8 source file. "
        "The interactive test sends several lines into one running prompt. "
        f"Expected results are stored in `{cases_path}`.\n",
        "Leading spaces or tabs in expected-output lines are removed before "
        "comparison. Actual scanner output is not changed except for trailing "
        "newline removal. Trailing prompt spaces are preserved.\n",
        "Tokens are stdout; diagnostics are stderr. These streams are recorded "
        "separately because their combined display order can vary.\n",
        "| Test | Mode | Result |\n| --- | --- | --- |",
    ]
    for case, stdout, stderr, exit_code, passed in results:
        report.append(
            f"| {case['name']} | {case.get('mode', 'file')} | "
            f"{'PASS' if passed else 'FAIL'} |"
        )

    for case, stdout, stderr, exit_code, passed in results:
        report.extend([
            "\n## " + case["name"] + "\n",
            "Purpose: " + case["purpose"] + "\n",
            "Mode: " + case.get("mode", "file") + "\n",
            "Source input (Python representation shows exact whitespace):\n",
            code_block(repr(case["source"])),
            "Expected tokens/stdout:\n",
            code_block(case["stdout"]),
            "Expected errors/stderr:\n",
            code_block(case.get("stderr", "")),
            "Actual tokens/stdout:\n",
            code_block(stdout),
            "Actual errors/stderr:\n",
            code_block(stderr),
            f"Expected exit code: {case.get('exit_code', 0)}. Actual exit code: {exit_code}.\n",
            "Matches expectations: " + ("Yes." if passed else "No.") + "\n",
        ])

    report_folder = ROOT / "report"
    report_folder.mkdir(exist_ok=True)
    (report_folder / "test_results.md").write_text("\n".join(report), encoding="utf-8")
    return 0 if passed_count == len(results) and not missing else 1


if __name__ == "__main__":
    sys.exit(main())
# // --- end AI code ---
