# Merkl Dev Ops Intern Challenge (SAST)

This application is a simple command-line user manager backed by a local SQLite database. The code intentionally includes vulnerable patterns to practice SAST analysis with Semgrep.

## Arborescence

```
Merkl-TC/
	main.py
	README.md
	task1-semgrep-output.txt
	task2-triage.txt
	task3-suppressed-output.txt
	.github/workflows/sast.yml
```

## Application Behavior

The script [main.py](main.py) provides a password-protected CLI menu (`MERKL`):

1. `Display Users`: displays all users from the database.
2. `Insert User`: adds a user (name + entered birth date).
3. `Delete User`: deletes a user by ID.
4. `Exit`: exits the program.

At startup, `database.db` is created if needed

## Run the Project

From the root of the `Merkl-TC` folder:

```bash
python3 main.py
```

Expected password:

```text
MERKL
```

## Analyse Semgrep

## Known Vulnerabilities (Intentional)

The code includes intentionally unsafe patterns for educational purposes:

- `eval(...)` on user-influenced data (code execution risk).
- SQL string concatenation in user deletion (SQL injection risk).

Do not use this code as-is in production.

## Hardening Recommendations

- Replace `eval` with a native age calculation (date arithmetic).
- Use parameterized queries for all SQL operations.
- Strictly validate user inputs (types, ranges, date format).
- Add tests (unit + security) and CI linting.

