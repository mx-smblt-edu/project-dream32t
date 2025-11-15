"""
Unit tests for Tag class.
"""

import pytest

from src.error.invalid_tag_error import InvalidTagError
from src.model.tag import Tag


@pytest.mark.parametrize("value", [
    "a",
    "a" * 32
])
def test_tag_initialization_valid_values(value) -> None:
    """
    Tests that the Tag class initializes correctly with valid values.
    """
    tag_instance = Tag(value)
    assert value == tag_instance.value


@pytest.mark.parametrize("value", [
    "",
    "   ",
    "a" * 33,
])
def test_tag_initialization_invalid_values(value) -> None:
    """
    Tests that the Tag class raises InvalidTagError for invalid values.
    """
    with pytest.raises(InvalidTagError) as excinfo:
        Tag(value)
    assert value in str(excinfo.value)


@pytest.mark.parametrize("one, two", [
    ("tag-1", "tag-1"),
    ("tag-1", "Tag-1"),
    ("tag-1", "TAG-1"),
])
def test_checking_for_equality_of_two_identical_values(one: str, two: str) -> None:
    """
    Tests the equality of two identical Tag objects.

    This test function creates two Tag objects with the same date and
    checks if they are equal by asserting their equality.
    """
    one_tag = Tag(one)
    two_tag = Tag(two)
    assert one_tag == two_tag


@pytest.mark.parametrize("one, two", [
    ("tag-1", "tag-2"),
    ("Tag-1", "Tag-2"),
    ("TAG-1", "TAG-2"),
])
def test_checking_for_equality_of_two_unequal_values(one: str, two: str) -> None:
    """
    Tests checking the equality operator for two unequal Tag objects.

    This function verifies that two Tag objects with different
    dates are not considered equal. The test ensures the correct
    behavior of the equality operator in such cases.
    """
    one_tag = Tag(one)
    two_tag = Tag(two)
    assert one_tag != two_tag


def test_checking_for_equality_of_two_unequal_type() -> None:
    """
    Tests the equality check for two objects of unequal types.

    This test ensures that attempting to compare an instance of the Tag
    class with an object of an unrelated type, such as an integer, raises a
    TypeError.
    """
    tag = Tag("John")
    with pytest.raises(TypeError):
        tag == 42


@pytest.mark.parametrize("tag, expected_hash", [
    ("John", hash("John")),
    ("Dan", hash("Dan"))
])
def test_hash_function(tag, expected_hash: int) -> None:
    """
    Tests the correctness of the __hash__ implementation in the Tag class.
    Ensures that the hash of a Tag object matches the hash of its value.
    """
    tag_instance = Tag(tag)
    assert expected_hash == hash(tag_instance)
