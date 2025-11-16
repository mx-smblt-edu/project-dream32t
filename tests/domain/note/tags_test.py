"""
Unit tests for validating the behavior of adding and removing tags
in the `Tags` collection.
"""

import pytest

from src.domain.note.tag import Tag
from src.domain.note.tag_search_template import TagSearchTemplate
from src.domain.note.tags import Tags
from src.error.already_tag_error import AlreadyTagError
from src.error.unknown_tag_error import UnknownTagError


def test_add_non_existing_tag() -> None:
    """
    Tests adding unique tag to Tags.
    """
    tags = Tags()
    tag = Tag("tag-1")

    result = tags.add(tag)

    assert result == tag
    assert len(tags) == 1
    assert tag in tags.data


def test_add_duplicate_tag_returns_none() -> None:
    """
    Tests that adding a duplicate tag returns None.
    """
    tags = Tags()
    tag = Tag("tag-1")

    tags.add(tag)
    result = tags.add(tag)

    assert result is None
    assert len(tags) == 1


def test_add_multiple_unique_tag():
    """
    Test that multiple unique tag can be added to list tags.
    """
    tags = Tags()
    phone1 = Tag("tag-1")
    phone2 = Tag("tag-2")

    result1 = tags.add(phone1)
    result2 = tags.add(phone2)

    assert result1 == phone1
    assert result2 == phone2
    assert len(tags.data) == 2
    assert tags.data == [phone1, phone2]


def test_remove_successful():
    """
    Test that remove successfully removes an existing tag from the note.
    """
    tags = Tags()
    tag = Tag("tag-1")
    tags.add(tag)

    removed_tag = tags.remove(tag)

    assert removed_tag == tag
    assert len(tags.data) == 0


def test_remove_nonexistent_tag():
    """
    Test that remove returns None when trying to remove a tag that does not exist.
    """
    tags = Tags()
    phone1 = Tag("tag-1")
    phone2 = Tag("tag-2")

    tags.add(phone1)
    removed_tag = tags.remove(phone2)

    assert removed_tag is None


def test_remove_from_empty_list():
    """
    Test that remove returns None when the contact has no tags.
    """
    tags = Tags()
    tag = Tag("tag-1")

    removed_tag = tags.remove(tag)

    assert removed_tag is None


def test_change_tag_successful():
    """
    Test if `replace` successfully replaces an old tag with a new one.
    """
    tags = Tags()
    old_tag = Tag("tag-1")
    new_tag = Tag("tag-2")

    tags.add(old_tag)
    replaced_tag = tags.replace(old_tag, new_tag)

    assert replaced_tag == new_tag
    assert new_tag in tags.data
    assert old_tag not in tags.data


def test_change_tag_old_number_not_found():
    """
    Test if `replace` raises error when the old tag doesn't exist.
    """
    tags = Tags()
    old_tag = Tag("tag-1")
    new_tag = Tag("tag-2")

    with pytest.raises(UnknownTagError):
        tags.replace(old_tag, new_tag)


def test_change_tag_new_number_already_exists():
    """
    Test if `replace` raises error when the new tag is already in the list.
    """
    tags = Tags()
    old_tag = Tag("tag-1")
    another_tag = Tag("tag-2")
    new_tag = Tag("tag-2")

    tags.add(old_tag)
    tags.add(another_tag)

    with pytest.raises(AlreadyTagError):
        tags.replace(old_tag, new_tag)


def test_contains_existing_tag_number():
    """
    Tests that the `contains` method returns True for a tag already in the list.
    """
    tags = Tags()
    tag = Tag("tag-1")
    tags.add(tag)
    template = TagSearchTemplate("tag-1")

    assert tags.contains(template) is True


def test_contains_non_existing_tag_number():
    """
    Tests that the `contains` method returns False for a tag not in the list.
    """
    tags = Tags()
    tag = Tag("tag-1")
    tags.add(tag)
    template = TagSearchTemplate("tag-2")

    assert tags.contains(template) is False


def test_contains_partial_match_within_tag_number():
    """
    Tests that the `contains` method can find a partial match of a tag.
    """
    tags = Tags()
    tag = Tag("tag-1")
    tags.add(tag)
    template = TagSearchTemplate("tag")

    assert tags.contains(template) is True


def test_contains_empty_tag_list():
    """
    Tests that the `contains` method of a `Contact` instance returns False
    when the tag list is empty.
    """
    tags = Tags()
    template = TagSearchTemplate("tag-1")

    assert tags.contains(template) is False
