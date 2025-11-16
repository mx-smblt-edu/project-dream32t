"""
Unit tests for Name class.
"""

import pytest

from src.domain.contact.name import Name
from src.error.invalid_name_error import InvalidNameError


@pytest.mark.parametrize("value", [
    "Li",
    "a" * 64
])
def test_name_initialization_valid_values(value) -> None:
    """
    Tests that the Name class initializes correctly with valid values.
    """
    name_instance = Name(value)
    assert value == name_instance.value


@pytest.mark.parametrize("value", [
    "",
    "   ",
    "a",
    "a" * 65,
])
def test_name_initialization_invalid_values(value) -> None:
    """
    Tests that the Name class raises InvalidNameError for invalid values.
    """
    with pytest.raises(InvalidNameError) as excinfo:
        Name(value)
    assert value in str(excinfo.value)


@pytest.mark.parametrize("one, two", [
    ("John", "John"),
    ("John", "john")
])
def test_checking_for_equality_of_two_identical_values(one: str, two: str) -> None:
    """
    Tests the equality of two identical Name objects.

    This test function creates two Name objects with the same date and
    checks if they are equal by asserting their equality.
    """
    one_name = Name(one)
    two_name = Name(two)
    assert one_name == two_name


def test_checking_for_equality_of_two_unequal_values() -> None:
    """
    Tests checking the equality operator for two unequal Name objects.

    This function verifies that two Name objects with different
    dates are not considered equal. The test ensures the correct
    behavior of the equality operator in such cases.
    """
    one_name = Name("John")
    two_name = Name("Dan")
    assert one_name != two_name


def test_checking_for_equality_of_two_unequal_type() -> None:
    """
    Tests the equality check for two objects of unequal types.

    This test ensures that attempting to compare an instance of the Birthday
    class with an object of an unrelated type, such as an integer, raises a
    TypeError.
    """
    name = Name("John")
    with pytest.raises(TypeError):
        name == 42


@pytest.mark.parametrize("name, expected_hash", [
    ("John", hash("John")),
    ("Dan", hash("Dan"))
])
def test_name_hash_function(name, expected_hash: int) -> None:
    """
    Tests the correctness of the __hash__ implementation in the Name class.
    Ensures that the hash of a Name object matches the hash of its value.
    """
    name_instance = Name(name)
    assert expected_hash == hash(name_instance)
