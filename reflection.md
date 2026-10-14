# Lab 5 — Reflection

## 1. What is static code analysis, and how is it different from testing?
Static code analysis inspects source code without running the program. Tools such as Pylint and Flake8 identify potential maintainability, correctness, and style problems; Bandit looks for common security risks. Testing executes code with selected inputs to observe behaviour. Static analysis can flag risky code paths that a test never exercises, while tests help confirm the program's actual behaviour. They complement each other.

## 2. Which issues were most important, and why?
The SQL string interpolation was important because user-controlled values could change the meaning of the database query. The mutable default argument and broad exception handlers were also important: shared state can cause registrations to interfere with one another, and swallowed exceptions can conceal failed operations. Incorrect adoption counting was a logic problem because it could report an adoption even when no record changed. These were prioritized over cosmetic formatting.

## 3. How did the fixes improve code quality, security, and maintainability?
Parameterized SQL separates SQL instructions from data. Explicit validation rejects invalid records before they reach the database. A `None` default avoids sharing a list between calls, and removing broad silent exception handling makes unexpected failures visible. The adoption count now changes only when a database row is actually updated. Clear function names, docstrings, type hints, logging, and a main guard make the program easier to understand, reuse, and test.

## 4. What did you learn about using Pylint, Bandit, and Flake8, and what are their limitations?
The tools serve different purposes: Pylint checks code quality and likely programming mistakes, Flake8 checks style and common lint errors, and Bandit highlights patterns associated with security weaknesses. Their findings need interpretation rather than blind acceptance; a warning is a clue, not proof of an exploitable vulnerability, and passing a tool does not prove a program is correct or secure. Using the three tools alongside functional tests gives broader coverage than relying on only one approach. Before submission, run each tool against the final file and record the actual outputs and any remaining findings.

## Verification note

This reflection describes the fixes implemented in the cleaned file. The final Pylint, Bandit, and Flake8 reports should be generated locally with `run_analysis.sh`; tool execution was unavailable in the environment used to prepare these files because package downloads could not reach the network.
