"""
Unit tests for Topic class.
"""

import pytest

from src.error.invalid_topic_error import InvalidTopicError
from src.model.topic import Topic


@pytest.mark.parametrize("value", [
    "a",
    "a" * 32
])
def test_tag_initialization_valid_values(value) -> None:
    """
    Tests that the Topic class initializes correctly with valid values.
    """
    topic_instance = Topic(value)
    assert value == topic_instance.value


@pytest.mark.parametrize("value", [
    "",
    "   ",
    "a" * 33,
])
def test_tag_initialization_invalid_values(value) -> None:
    """
    Tests that the Topic class raises InvalidTagError for invalid values.
    """
    with pytest.raises(InvalidTopicError) as excinfo:
        Topic(value)
    assert value in str(excinfo.value)


@pytest.mark.parametrize("one, two", [
    ("topic-1", "topic-1"),
    ("topic-1", "Topic-1"),
    ("topic-1", "TOPIC-1"),
])
def test_checking_for_equality_of_two_identical_values(one: str, two: str) -> None:
    """
    Tests the equality of two identical Topic objects.

    This test function creates two Topic objects with the same date and
    checks if they are equal by asserting their equality.
    """
    one_topic = Topic(one)
    two_topic = Topic(two)
    assert one_topic == two_topic


@pytest.mark.parametrize("one, two", [
    ("topic-1", "topic-2"),
    ("Topic-1", "Topic-2"),
    ("TOPIC-1", "TOPIC-2"),
])
def test_checking_for_equality_of_two_unequal_values(one: str, two: str) -> None:
    """
    Tests checking the equality operator for two unequal Topic objects.

    This function verifies that two Topic objects with different
    dates are not considered equal. The test ensures the correct
    behavior of the equality operator in such cases.
    """
    one_topic = Topic(one)
    two_topic = Topic(two)
    assert one_topic != two_topic


def test_checking_for_equality_of_two_unequal_type() -> None:
    """
    Tests the equality check for two objects of unequal types.

    This test ensures that attempting to compare an instance of the Topic
    class with an object of an unrelated type, such as an integer, raises a
    TypeError.
    """
    topic_instance = Topic("topic-1")
    with pytest.raises(TypeError):
        topic_instance == 42


@pytest.mark.parametrize("topic, expected_hash", [
    ("Topic-1", hash("Topic-1")),
    ("topic-2", hash("topic-2"))
])
def test_hash_function(topic, expected_hash: int) -> None:
    """
    Tests the correctness of the __hash__ implementation in the Topic class.
    Ensures that the hash of a Topic object matches the hash of its value.
    """
    topic_instance = Topic(topic)
    assert expected_hash == hash(topic_instance)
