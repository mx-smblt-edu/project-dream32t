"""
Provides the Address class.
"""


class Address:
    """Class for storing the address."""

    def __init__(self, value: str):
        self.__value = value

    @property
    def value(self) -> str:
        """Getter for the value of the address."""
        return self.__value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            raise TypeError(f"Cannot compare {self!r} and {other!r}")
        return self.value.casefold() == other.value.casefold()
