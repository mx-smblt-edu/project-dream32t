"""
Provides the Name class.
"""
from src.error.invalid_name_error import InvalidNameError


class Name:
    """Class for storing the contact name."""

    def __init__(self, value: str):
        clean_value = value.strip()
        if len(clean_value) < 2 or len(clean_value) > 64:
            raise InvalidNameError(value)
        self.__value = value

    @property
    def value(self) -> str:
        """Getter for the name value"""
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)

    def __hash__(self) -> int:
        return hash(self.__value)

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            raise TypeError(f"Cannot compare {self!r} and {other!r}")
        return self.value.casefold() == other.value.casefold()
