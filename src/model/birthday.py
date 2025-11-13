"""
Provides the Birthday class.
"""
from datetime import datetime, date

from src.error.invalid_birthday_error import InvalidBirthdayError


class Birthday:
    """
    Represents a birthday field.

    This class provides functionality to store and handle a birthday
    date in a specific format. It ensures that the provided date string
    adheres to the expected format and converts it to a date object for
    further use.
    """
    format = "%d.%m.%Y"

    def __init__(self, value: str):
        try:
            date_of_birthday: date = datetime.strptime(value, Birthday.format).date()
            self.__value = date_of_birthday
        except ValueError as vex:
            raise InvalidBirthdayError(value) from vex

    @property
    def value(self) -> date:
        """Getter for the value of the birthday."""
        return self.__value

    def to_string(self) -> str:
        """Returns the birthday as a string in the expected format."""
        return self.__value.strftime(Birthday.format)

    def __str__(self) -> str:
        return f"Birthday: {self.to_string()}"

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            raise TypeError(f"Cannot compare {self!r} and {other!r}")
        return self.value == other.value
