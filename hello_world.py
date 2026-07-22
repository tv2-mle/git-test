"""A simple Hello World program using object-oriented programming principles."""


class Greeter:
    """A class that generates greetings for a given recipient."""

    def __init__(self, name: str = "World") -> None:
        """Initialize the Greeter with the recipient's name.

        Args:
            name: The name of the person or entity to greet. Defaults to "World".
        """
        self._name = name

    @property
    def name(self) -> str:
        """Return the recipient's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the recipient's name."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name must be a non-empty string")
        self._name = value

    def greet(self) -> str:
        """Return a greeting message for the recipient."""
        return f"Hello, {self._name}!"

    def say_hello(self) -> None:
        """Print the greeting message to standard output."""
        print(self.greet())


def main() -> None:
    """Program entry point."""
    greeter = Greeter()
    greeter.say_hello()


if __name__ == "__main__":
    main()
