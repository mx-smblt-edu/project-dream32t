"""
Unit tests for Email creation validity.

This module contains tests for creating `Email` instances with valid and
invalid values.
"""
import pytest

from src.error.invalid_email_error import InvalidEmailError
from src.model.email import Email


@pytest.mark.parametrize("value", [
    "a@b.co",
    "a9@b.co",
    "a9b@c.co",
    "a.9@b.co",
    "a.9.b@c.co",
    "a-9@b.co",
    "a-9-b@c.co",
    "a_9@b.co",
    "a_9_b@c.co",
    "a.b@c.co",
    "a-b@c.co",
    "a_b@c.co",
    "a@0.co",
    "a@b.c.co",
    "9@a.co",
])
def test_creating_email_by_valid_value(value: str) -> None:
    """
    Test function to validate email creation using a valid email value. This function
    verifies that the Email object correctly initializes and retains the provided
    value when the input email format is valid.

    :param value: Input string representing a valid email address
    :type value: str
    """
    email = Email(value)
    assert email.value == value


@pytest.mark.parametrize("value", [
    "",
    "   ",
    "-@com",
    "-@b.com",
    "a@com",
    "a-b.com",
    "a@b.c",
    "abc",
    "123",
])
def test_creating_email_by_invalid_value(value: str) -> None:
    """
    Tests email creation with invalid email values.

    This test ensures that creating Email objects with the provided invalid
    email values raises the `InvalidEmailError` as expected. It validates
    various cases of invalid input.

    :param value: A string that represents the potentially invalid email
        input to be tested.
    :type value: str
    """
    with pytest.raises(InvalidEmailError):
        Email(value)
