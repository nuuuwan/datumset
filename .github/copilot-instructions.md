# Agent Guidelines & Python Rules

## Formatting

- Line length: 78 soft limit (black), 80 hard limit.
- No string quote normalization — keep quotes as written.
- No unused imports or variables, except re-exports in `__init__.py`.

## Structure

- All code lives in classes; one class per file, named after the class (`class Foo` → `Foo.py`).
- Max file length: 100 lines. Split oversized files into named Mixins; if a class has Mixins, put class + Mixins in their own folder.
- Max function length: 40 lines. Split oversized functions into helpers.
- Max cyclomatic complexity: 5. Split functions that exceed this limit.

## Style

- No prose comments or docstrings anywhere. Code must be self-explanatory.
- Exception: Linter and type-checker suppression comments (e.g., `# noqa`, `# type: ignore`) are permitted where required.

## Data & Pipeline Safety

- NEVER overwrite existing raw dataset files (`.json`, `.csv`, `.parquet`) without creating a backup or working in a temporary folder.
- Format all JSON dataset outputs with `indent=2` and `sort_keys=True` to maintain clean Git diffs.
- Always set explicit timeouts (minimum 10s) and handle potential network failures gracefully on remote HTTP calls.

## Verification

After writing or editing Python files, run the verification commands on every modified file using this script:

### Linter & Formatter Script (`verify.sh`)

Execute the following bash script on each modified file:

```bash
#!/usr/bin/env bash

set -e

if [ "$#" -eq 0 ]; then
    echo "Usage: ./verify.sh <path-to-python-file> [path-to-another-file...]"
    exit 1
fi

for FILE in "$@"; do
    if [ ! -f "$FILE" ]; then
        echo "Error: File '$FILE' does not exist."
        exit 1
    fi

    echo "==> Verifying $FILE..."

    echo "1/4 Running autoflake..."
    python3 -m autoflake -r --in-place \
        --remove-unused-variables \
        --remove-all-unused-imports \
        --ignore-init-module-imports \
        "$FILE"

    echo "2/4 Running autopep8..."
    python3 -m autopep8 --aggressive \
        --max-line-length 78 \
        --in-place -r \
        "$FILE"

    echo "3/4 Running black..."
    python3 -m black --quiet \
        --skip-string-normalization \
        --line-length 78 \
        "$FILE"

    echo "4/4 Running flake8..."
    python3 -m flake8 \
        --ignore="CFQ002,W503" \
        --per-file-ignores="__init__.py:F401" \
        --max-function-length 40 \
        --max-line-length 80 \
        --max-complexity 5 \
        "$FILE"

    echo "✓ $FILE passed verification."
done
```
