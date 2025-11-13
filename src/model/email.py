"""
Provides the Phone class.
"""
import re

from src.error.invalid_email_error import InvalidEmailError


class Email:
    """Class for storing email."""

    __pattern: re.Pattern = re.compile(r"^([a-zA-Z0-9]+[0-9._-]*)+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    def __init__(self, number: str):
        if re.fullmatch(Email.__pattern, number) is None:
            raise InvalidEmailError(number)
        self.__value = number

    @property
    def value(self) -> str:
        """Getter for the email"""
        return self.__value

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            raise TypeError(f"Cannot compare {self!r} and {other!r}")
        return self.value == other.value
