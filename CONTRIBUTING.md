# Contribution Guidelines

## Code Requirements

**Type Safety & Imports**

- Use Python typing hints for all functions, methods, and variables
- All class attributes must be defined with their type at the top of the class
- Use relative imports only (no absolute imports within the project)

**Documentation**

- Document all public classes, functions, methods, and modules using Google docstring format
- Private methods/functions: documentation optional unless logic is complex
- Write clear, verbose code over clever/obfuscated code

**Project Structure**

- Every module directory must contain `__init__.py`
- API request/response dataclasses must be suffixed with `Dto` (example: `GetUserRequestDto`)
- Use Pydantic validation for all external data and API models

## Development Commands

**Setup**

```bash
poetry install
```

**Quality Checks**

```bash
poetry run poe lint          # Run linter
poetry run poe typecheck     # Run type checker
poetry run poe test          # Run all tests
poetry run poe test_cov      # Run tests with coverage
poetry run pytest {args}     # Run specific test files
```

## Dependency Management

**Adding Dependencies**

```bash
poetry add dependency_name
```

- Do NOT edit `pyproject.toml` directly

**Updating Dependencies**

```bash
poetry update {package}      # Update specific package
poetry lock --no-update      # Update lock file only
```

- Only update dependency versions when strictly necessary
- Do NOT add subdependencies as direct dependencies to force versions
- Use `poetry update {package}` to manage subdependency versions in the lock file

## Code example

```python
"""Example module demonstrating proper Python coding style.

This module contains example classes that show how to implement
proper type hints, docstrings, and encapsulation following
the repository's coding standards.
"""

from .utils import capitalize


class PublicClass:
    """A class that demonstrates proper Python coding style.

    This class shows how to implement proper type hints, docstrings,
    and use private classes effectively.
    """

    name: str

    def __init__(self, name: str):
        """Initialize the class with a name.

        Args:
            name: The name to associate with this instance.

        Raises:
            ValueError: If the name is empty.
        """
        super().__init__()

        if name == "":
            raise ValueError("Name cannot be empty")

        self.name = capitalize(name)

    def public_method(self) -> str:
        """Return a greeting message.

        Returns:
            A greeting message using the instance name.
        """
        return self._generate_greeting()

    def _generate_greeting(self) -> str:
        return f"Hello, {self.name}!"
```
