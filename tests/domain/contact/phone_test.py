"""
Unit tests for the `Phone` domain in the application.

These tests validate the behavior of the `Phone` class when provided with
both valid and invalid phone numbers. The tests ensure that valid phone
numbers are correctly accepted and assigned to `Phone.value`, while invalid
numbers raise the appropriate exception.

The test cases are parameterized to allow testing multiple inputs for both
valid and invalid scenarios.
"""

import pytest

from src.domain.contact.phone import Phone
from src.error.invalid_phone_number_error import InvalidPhoneNumberError


@pytest.mark.parametrize("number", [
    "1234567890",
    "12345678901",
    "123456789012",
])
def test_creating_phone_by_valid_value(number: str) -> None:
    """
    Tests the creation of a Phone object with valid number values through
    parameterized inputs. This function verifies whether the `value` attribute
    of the `Phone` object matches the input `number`.

    :param number: A string representing a valid phone number provided as
        parameterized input.
    :type number: str
    """
    phone = Phone(number)
    assert phone.value == number


@pytest.mark.parametrize("number", [
    "",
    "   ",
    "123456789",
    "-123456789",
    "abc",
])
def test_creating_phone_by_invalid_value(number: str) -> None:
    """
    Test the behavior of the Phone class constructor when provided with invalid phone
    number inputs. This test ensures that the Phone object raises an InvalidPhoneNumberError
    exception for invalid number values, such as non-numeric inputs or improperly
    formatted phone numbers.

    :param number: The invalid phone number value used for testing
    :type number: str
    :raises InvalidPhoneNumberError: If the provided phone number does not meet
        valid formatting and content requirements
    """
    with pytest.raises(InvalidPhoneNumberError):
        Phone(number)
