"""
Unit tests for Tag class.
"""

import pytest

from src.domain.note.content import Content
from src.domain.note.note import Note
from src.domain.note.tag import Tag
from src.domain.note.tags import Tags
from src.domain.note.topic import Topic


def test_checking_for_equality_of_two_identical_values() -> None:
    """
    Tests the equality of two identical Note objects.

    This test function creates two Note objects with the same date and
    checks if they are equal by asserting their equality.
    """
    one_topic_instance = Topic("topic-1")
    one_content_instance = Content("content-1")
    one_note_instance = Note(one_topic_instance, one_content_instance)

    two_topic_instance = Topic("topic-1")
    two_content_instance = Content("content-2")
    two_note_instance = Note(two_topic_instance, two_content_instance)

    assert one_note_instance == two_note_instance


def test_checking_for_equality_of_two_unequal_values() -> None:
    """
    Tests checking the equality operator for two unequal Note objects.

    This function verifies that two Note objects with different
    dates are not considered equal. The test ensures the correct
    behavior of the equality operator in such cases.
    """
    one_topic_instance = Topic("topic-1")
    one_content_instance = Content("content-1")
    one_note_instance = Note(one_topic_instance, one_content_instance)

    two_topic_instance = Topic("topic-2")
    two_content_instance = Content("content-1")
    two_note_instance = Note(two_topic_instance, two_content_instance)

    assert one_note_instance != two_note_instance


def test_checking_for_equality_of_two_unequal_type() -> None:
    """
    Tests the equality check for two objects of unequal types.

    This test ensures that attempting to compare an instance of the Note
    class with an object of an unrelated type, such as an integer, raises a
    TypeError.
    """
    topic_instance = Topic("topic-1")
    content_instance = Content("-1")
    note_instance = Note(topic_instance, content_instance)

    with pytest.raises(TypeError):
        note_instance == 42


@pytest.mark.parametrize("topic, content, tags, expected_hash", [
    ("topi1-1", "content-1", "tag-1", hash("topi1-1")),
    ("topi1-1", "content-1", "", hash("topi1-1")),
])
def test_hash_function(topic, content, tags, expected_hash: int) -> None:
    """
    Tests the correctness of the __hash__ implementation in the Note class.
    Ensures that the hash of a Note object matches the hash of its value.
    """
    topic_instance = Topic(topic)
    content_instance = Content(content)
    if len(tags) > 0:
        tags_instance = Tags()
        tag_instance = Tag(tags)
        tags_instance.append(tag_instance)
        note_instance = Note(topic_instance, content_instance, tags_instance)
    else:
        note_instance = Note(topic_instance, content_instance)

    assert expected_hash == hash(note_instance)
