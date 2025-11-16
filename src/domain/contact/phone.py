"""
Provides the Phone class.
"""
import re

from src.error.invalid_phone_number_error import InvalidPhoneNumberError


class Phone:
    """Class for storing phone numbers. Has format validation (10-12 digits)"""

    __pattern: re.Pattern = re.compile(r"^\d{10,12}$")

    def __init__(self, number: str):
        if re.fullmatch(Phone.__pattern, number) is None:
            raise InvalidPhoneNumberError(number)
        self.__value = number

    @property
    def value(self) -> str:
        """Getter for the phone number"""
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            raise TypeError(f"Cannot compare {self!r} and {other!r}")
        return self.value == other.value
