"""
Unit tests for Address class.
"""

import pytest

from src.domain.contact.address import Address


@pytest.mark.parametrize("one, two", [
    ("Kyiv city, Ukraine", "Kyiv city, Ukraine"),
    ("Kyiv city, Ukraine", "kyiv city, ukraine")
])
def test_checking_for_equality_of_two_identical_values(one: str, two: str) -> None:
    """
    Tests the equality of two identical Address objects.

    This test function creates two Address objects with the same date and
    checks if they are equal by asserting their equality.
    """
    one_address = Address(one)
    two_address = Address(two)
    assert one_address == two_address


def test_checking_for_equality_of_two_unequal_values() -> None:
    """
    Tests checking the equality operator for two unequal Address objects.

    This function verifies that two Address objects with different
    dates are not considered equal. The test ensures the correct
    behavior of the equality operator in such cases.
    """
    one_address = Address("Kyiv city, Ukraine")
    two_address = Address("Lviv city, Ukraine")
    assert one_address != two_address


def test_checking_for_equality_of_two_unequal_type() -> None:
    """
    Tests the equality check for two objects of unequal types.

    This test ensures that attempting to compare an instance of the Birthday
    class with an object of an unrelated type, such as an integer, raises a
    TypeError.
    """
    address = Address("Kyiv city, Ukraine")
    with pytest.raises(TypeError):
        address == 42
