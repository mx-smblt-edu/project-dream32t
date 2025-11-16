"""
Unit tests for Birthday creation validity.

This module contains tests for verifying the correct behavior of the
Birthday class and ensuring that the InvalidBirthdayError exception
is raised when invalid date values are provided. The Birthday class
is validated to accept correctly formatted date inputs and reject
invalid ones.
"""

from datetime import datetime

import pytest

from src.domain.contact.birthday import Birthday
from src.error.invalid_birthday_error import InvalidBirthdayError


@pytest.mark.parametrize("value", [
    "01.01.2025",
    "31.01.2025",
    "29.02.2028",
])
def test_creating_birthday_by_valid_value(value: str) -> None:
    """
    Test function to validate birthday creation using a valid date value. This function
    verifies that the Birthday object correctly initializes and retains the provided
    value when the input date format is valid.

    :param value: Input string representing a valid date
    :type value: str
    """
    birthday = Birthday(value)
    expected = datetime.strptime(value, "%d.%m.%Y").date()
    assert birthday.value == expected
    assert birthday.to_string() == value


@pytest.mark.parametrize("value", [
    "",
    "   ",
    "10.30.2025",
    "2025.10.30",
    "29.02.2025",
])
def test_creating_birthday_by_invalid_value(value: str) -> None:
    """
    Tests email creation with invalid birthday values.

    This test ensures that creating Birthday objects with the provided invalid
    date values raises the `InvalidBirthdayError` as expected. It validates
    various cases of invalid input.

    :param value: A string that represents the potentially invalid date
        input to be tested.
    :type value: str
    """
    with pytest.raises(InvalidBirthdayError):
        Birthday(value)


def test_checking_for_equality_of_two_identical_values() -> None:
    """
    Tests the equality of two identical Birthday objects.

    This test function creates two Birthday objects with the same date and
    checks if they are equal by asserting their equality.
    """
    one_birthday = Birthday("01.01.2025")
    two_birthday = Birthday("01.01.2025")
    assert one_birthday == two_birthday


def test_checking_for_equality_of_two_unequal_values() -> None:
    """
    Tests checking the equality operator for two unequal Birthday objects.

    This function verifies that two Birthday objects with different
    dates are not considered equal. The test ensures the correct
    behavior of the equality operator in such cases.
    """
    one_birthday = Birthday("01.01.2025")
    two_birthday = Birthday("10.10.2025")
    assert one_birthday != two_birthday


def test_checking_for_equality_of_two_unequal_type() -> None:
    """
    Tests the equality check for two objects of unequal types.

    This test ensures that attempting to compare an instance of the Birthday
    class with an object of an unrelated type, such as an integer, raises a
    TypeError.
    """
    birthday = Birthday("01.01.2025")
    with pytest.raises(TypeError):
        birthday == 42
