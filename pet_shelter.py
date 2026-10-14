"""Small in-memory animal shelter register used for Lab 5 static analysis.

The demo registers three pets, adopts one, prints the oldest available pet,
creates an adoption code, reports shelter status, and removes remaining pets.
"""

import logging
import secrets
import sqlite3
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
LOGGER = logging.getLogger(__name__)


def create_connection() -> sqlite3.Connection:
    """Create and initialize an in-memory SQLite database."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """CREATE TABLE pets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            age INTEGER NOT NULL CHECK (age >= 0),
            adopted INTEGER NOT NULL DEFAULT 0 CHECK (adopted IN (0, 1))
        )"""
    )
    return connection


conn = create_connection()
shelter_state = {"adoption_count": 0}


def register_pet(
    name: str, species: str, age: int, tags: Optional[list[str]] = None
) -> list[str]:
    """Register a pet safely and return its species tags.

    Parameterized SQL prevents user-provided strings from becoming SQL syntax.
    A fresh tag list is created for each call unless one is supplied.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Pet name must be a non-empty string.")
    if not isinstance(species, str) or not species.strip():
        raise ValueError("Pet species must be a non-empty string.")
    if isinstance(age, bool) or not isinstance(age, int) or age < 0:
        raise ValueError("Pet age must be a non-negative integer.")

    pet_tags = [] if tags is None else tags
    conn.execute(
        "INSERT INTO pets (name, species, age, adopted) VALUES (?, ?, ?, 0)",
        (name.strip(), species.strip(), age),
    )
    pet_tags.append(species.strip())
    return pet_tags


def adopt(pet_id: int) -> bool:
    """Mark an available pet as adopted; return whether it was updated."""
    if isinstance(pet_id, bool) or not isinstance(pet_id, int) or pet_id <= 0:
        raise ValueError("Pet ID must be a positive integer.")

    cursor = conn.execute(
        "UPDATE pets SET adopted = 1 WHERE id = ? AND adopted = 0",
        (pet_id,),
    )
    if cursor.rowcount == 1:
        shelter_state["adoption_count"] += 1
        return True
    LOGGER.warning("Pet ID %s was not found or was already adopted.", pet_id)
    return False


def adoption_code() -> str:
    """Return a harder-to-guess short adoption reference code."""
    return f"PET-{secrets.randbelow(9000) + 1000}"


def oldest_available() -> Optional[str]:
    """Return the name of the oldest unadopted pet, or None if none exist."""
    row = conn.execute(
        """
        SELECT name
        FROM pets
        WHERE adopted = 0
        ORDER BY age DESC, id ASC
        LIMIT 1
        """
    ).fetchone()
    return None if row is None else str(row[0])


def clear_unadopted() -> int:
    """Delete unadopted pets and return the number of deleted rows."""
    cursor = conn.execute("DELETE FROM pets WHERE adopted = 0")
    return cursor.rowcount


def shelter_status() -> str:
    """Report whether the shelter has recorded any successful adoptions."""
    return "active" if shelter_state["adoption_count"] > 0 else "quiet"


def main() -> None:
    """Run a small demonstration of the shelter register."""
    register_pet("Bruno", "dog", 7)
    register_pet("Mitzi", "cat", 3)
    register_pet("Kiwi", "parrot", 12)
    adopt(1)
    LOGGER.info(
        "Oldest available: %s | Adoption code: %s | Status: %s",
        oldest_available(),
        adoption_code(),
        shelter_status(),
    )
    removed = clear_unadopted()
    LOGGER.info("Removed %s unadopted pet record(s).", removed)


if __name__ == "__main__":
    main()
