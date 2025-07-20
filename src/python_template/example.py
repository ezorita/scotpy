"""Example module demonstrating proper Python coding style.

This module contains example classes that show how to implement
proper type hints, docstrings, and encapsulation following
the repository's coding standards.
"""


class PublicClass:
    """A public class that demonstrates proper Python coding style.

    This class shows how to implement proper type hints, docstrings,
    and use private classes effectively.
    """

    def __init__(self, name: str) -> None:
        """Initialize the PublicClass with a name.

        Args:
            name: The name to associate with this instance.
        """
        self.name = name
        self._private_object: _PrivateClass = _PrivateClass(name)

    def public_method(self) -> str:
        """Return a public greeting message.

        Returns:
            A greeting message using the instance name.
        """
        return f"Hello, {self.name}!"

    def get_private_greeting(self) -> str:
        """Get a greeting from the private object.

        Returns:
            A greeting message from the private class instance.
        """
        return self._private_object.private_method()


class _PrivateClass:
    """A private class for internal use within this module.

    This class demonstrates proper encapsulation and private
    class implementation.
    """

    def __init__(self, name: str) -> None:
        """Initialize the private class with a name.

        Args:
            name: The name to associate with this instance.
        """
        self.name = name

    def private_method(self) -> str:
        """Return a private greeting message.

        Returns:
            A private greeting message using the instance name.
        """
        return f"Private hello, {self.name}!"
