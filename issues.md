# Lab 5 — Static Code Analysis Issue Log

**Repository:** [SETAPESU26/L5_16_pet_shelter](https://github.com/SETAPESU26/L5_16_pet_shelter)  
**Source analyzed:** original `pet_shelter.py` from the assigned repository  
**Note:** line numbers below refer to the original starter file; line numbers in the cleaned file differ.

| Issue | Type / Tool | Original line(s) | Description and impact | Fix approach |
|---|---|---:|---|---|
| SQL query built with string interpolation | Security / Bandit-style finding | 10 | `name` and `species` were interpolated directly into an SQL statement. Input containing SQL syntax could alter the query. | Replaced string interpolation with parameterized SQL placeholders (`?`) and a tuple of values. |
| Mutable default argument | Bug / Pylint | 9 | `tags=[]` was created once and reused across calls, so separate registrations could unintentionally share state. | Changed the default to `None` and initialize a new list inside the function. |
| Bare `except` | Reliability / Pylint | 27 | The handler caught every exception, including programming errors, and obscured the real cause. | Removed the broad handler; the database query is designed to return `None` when no pet exists. |
| Silent broad exception handling | Reliability / Pylint | 34–35 | `except Exception: pass` hid failures during deletion, making a failed operation appear successful. | Removed the catch-and-ignore block and return the number of deleted rows. Database errors can now surface instead of being hidden. |
| Incorrect empty-result handling in oldest-pet lookup | Bug | 26–28 | The query fetched a row without `LIMIT 1`; when no pet was available, `row[0]` raised an exception which was swallowed. | Query only the required columns, add `LIMIT 1`, and explicitly return `None` when no row exists. |
| Adoption count incremented even if no pet was adopted | Logic bug | 19–22 | The count increased even when the supplied ID matched no row or an already-adopted pet. | Validate the ID and increment only when the `UPDATE` affects exactly one row. |
| Weak predictable random adoption code | Security / design improvement | 24–25 | The standard pseudo-random generator is not intended for security-sensitive tokens. | Used Python's `secrets` module to generate a less predictable short reference code. |
| Non-PEP 8 naming and formatting | Style / Flake8 / Pylint | 9–38 | CamelCase function names and a one-line conditional made the code less consistent and harder to read. | Renamed functions to `snake_case`, formatted branches across lines, and added docstrings and type hints. |
| No input validation | Reliability | 9–10 | Blank names/species and invalid/negative ages could be stored. | Added validation for name, species, age, and adoption ID; added database constraints for core fields. |
| Program executed on import | Maintainability | 48–50 | Importing the module immediately ran the demo, making it harder to reuse or test functions. | Added an `if __name__ == "__main__":` guard. |

## Verification status

The cleaned program was checked with Python compilation and a functional smoke test (see `verification.txt`). The Pylint, Bandit, and Flake8 commands are included in `run_analysis.sh`. Their actual reports must be generated on a machine with the tools installed; those tools could not be installed in this execution environment because package-network access was unavailable. Do not treat the included placeholder report files as analyzer output.
