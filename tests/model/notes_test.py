"""
Unit tests for validating the behavior of adding and removing phone numbers
in the `Phones` collection.
"""

from src.model.content import Content
from src.model.note import Note
from src.model.notes import Notes
from src.model.topic import Topic


def test_add_non_existing_note() -> None:
    """
    Tests the addition of a non-existing note to the collection.

    This function creates a Notes instance, along with a single Topic and
    Content instance. It then creates a Note object from the provided Topic
    and Content instances and appends this note to the Notes collection.
    The test verifies that the note is correctly added, the collection's size
    is updated accordingly, and that the note exists in the data of the Notes
    collection.
    """
    notes = Notes()
    one_topic_instance = Topic("topic-1")
    one_content_instance = Content("content-1")
    one_note = Note(one_topic_instance, one_content_instance)

    result = notes.append(one_note)

    assert result == one_note
    assert len(notes) == 1
    assert one_note in notes.data


def test_add_exist_note() -> None:
    """
    Tests the behavior of adding duplicate notes to a Notes collection.

    This test ensures that attempting to add a duplicate note to a Notes
    collection returns None and does not increase the length of the Notes
    collection.
    """
    notes = Notes()
    one_topic_instance = Topic("topic-1")
    one_content_instance = Content("content-1")
    one_note = Note(one_topic_instance, one_content_instance)

    two_topic_instance = Topic("topic-1")
    two_content_instance = Content("content-1")
    two_note = Note(two_topic_instance, two_content_instance)

    result1 = notes.append(one_note)
    result2 = notes.append(two_note)

    assert result1 == one_note
    assert result2 is None
    assert len(notes) == 1


def test_add_multiple_unique_note():
    """
    Test the addition of multiple unique notes to the Notes collection.

    This function verifies that when adding two distinct notes to the Notes collection,
    both notes are successfully appended, and the notes data structure is updated
    correctly. It tests the integrity of the append operation, ensuring the notes are
    stored in the expected order, and the total count of notes is validated.
    """
    notes = Notes()
    one_topic_instance = Topic("topic-1")
    one_content_instance = Content("content-1")
    one_note = Note(one_topic_instance, one_content_instance)

    two_topic_instance = Topic("topic-2")
    two_content_instance = Content("content-2")
    two_note = Note(two_topic_instance, two_content_instance)

    result1 = notes.append(one_note)
    result2 = notes.append(two_note)

    assert result1 == one_note
    assert result2 == two_note
    assert len(notes.data) == 2
    assert notes.data == [one_note, two_note]


def test_find_existing_note() -> None:
    """
    Tests finding an existing note by topic.
    """
    notes = Notes()
    topic_instance = Topic("Test Topic 1")
    content_instance = Content("Test Content 1")
    one_note = Note(topic_instance, content_instance)
    notes.append(one_note)

    result = notes.find(topic_instance)

    assert result == one_note


def test_find_non_existing_note() -> None:
    """
    Tests searching for a note with a topic that does not exist.
    """
    notes = Notes()
    one_topic_instance = Topic("topic-1")
    content_instance = Content("content 1")
    one_note = Note(one_topic_instance, content_instance)

    two_topic_instance = Topic("topic-2")
    notes.append(one_note)

    result = notes.find(two_topic_instance)

    assert result is None


def test_find_in_empty_notes() -> None:
    """
    Tests finding a note in an empty Notes instance.
    """
    notes = Notes()
    topic_instance = Topic("Empty Topic")

    result = notes.find(topic_instance)

    assert result is None


def test_remove_successful():
    """
    Tests the successful removal of a note from the Notes collection.

    The function verifies that when a note is removed from the Notes collection using
    a topic instance as a key, the removed note matches the expected note. It also
    checks that the collection no longer contains the removed note.
    """
    notes = Notes()
    one_topic_instance = Topic("topic-1")
    one_content_instance = Content("content-1")
    one_note = Note(one_topic_instance, one_content_instance)
    notes.append(one_note)

    removed_note = notes.remove(one_topic_instance)

    assert removed_note == one_note
    assert len(notes.data) == 0


def test_remove_nonexistent_note():
    """
    Test the removal of a topic that does not exist in the notes list.

    This function tests the behavior of the `remove` method when attempting to
    remove a note associated with a topic that has already been removed or does not
    exist in the collection. The expected result is that the method returns `None`.
    """
    notes = Notes()
    one_topic_instance = Topic("topic-1")
    one_content_instance = Content("content-1")
    one_note = Note(one_topic_instance, one_content_instance)
    notes.append(one_note)

    result1 = notes.remove(one_topic_instance)
    result2 = notes.remove(one_topic_instance)

    assert result1 == one_note
    assert result2 is None


def test_remove_from_empty_list():
    """
    Test the removal of a topic from an empty notes list.

    This test function ensures that attempting to remove a topic from an
    empty notes list correctly returns None, indicating no topic was removed.
    """
    notes = Notes()
    topic_instance = Topic("topic-1")

    removed_note = notes.remove(topic_instance)

    assert removed_note is None
