# PESU-Lab5-Static-Code-Analysis
PES University Lab 5: Python static code analysis using Pylint, Bandit, and Flake8. Includes corrected pet shelter code, issue documentation, analysis reports, and reflection answers.
# Lab 5 — Static Code Analysis

**Course:** Computer Science Engineering  
**Institution:** PES University  
**Project:** Pet Shelter Adoption Register

## Objective

To improve Python code quality, security, and style using static analysis tools: Pylint, Bandit, and Flake8.

## Tools Used

- **Pylint:** Checks code quality and potential programming errors.
- **Bandit:** Identifies common Python security issues.
- **Flake8:** Checks coding style and PEP 8 compliance.

## Project Files

| File | Description |
|---|---|
| `pet_shelter.py` | Cleaned and updated Python program |
| `issues.md` | Identified issues and their fixes |
| `reflection.md` | Answers to the lab reflection questions |
| `pylint_report.txt` | Pylint analysis results |
| `bandit_report.txt` | Bandit security analysis results |
| `flake8_report.txt` | Flake8 style analysis results |

## Improvements Made

- Replaced SQL string interpolation with parameterized queries.
- Fixed the mutable default argument.
- Removed broad and silent exception handling.
- Added input validation.
- Corrected adoption-counting logic.
- Improved adoption reference generation.
- Improved naming, formatting, and code readability.
- Added safe handling for an empty shelter and a main execution guard.

## Analysis Results

- **Pylint:** 10.00/10
- **Bandit:** No issues identified.
- **Flake8:** No violations reported in the latest run.

## How to Run

Run the program:

```bash
python pet_shelter.py
```

Run the analysis tools:

```bash
pylint pet_shelter.py > pylint_report.txt
bandit -r pet_shelter.py > bandit_report.txt 2>&1
flake8 pet_shelter.py > flake8_report.txt
```

## Conclusion

Static code analysis helped identify and address issues related to security, reliability, maintainability, and coding style. Using Pylint, Bandit, and Flake8 together provides complementary checks that improve code quality.

**Note:** Static analysis complements functional testing; a clean report does not guarantee that software is entirely free of bugs or vulnerabilities.
