"""
A collection class for storing tags.

This module provides the `Phones` class, which is a custom implementation
inheriting from the `UserList` collection that holds instances of the `Phone`
class.
"""
from collections import UserList

from src.domain.note.tag import Tag
from src.domain.note.tag_search_template import TagSearchTemplate
from src.error.already_tag_error import AlreadyTagError
from src.error.unknown_tag_error import UnknownTagError


class Tags(UserList[Tag]):
    """A class for storing tags."""

    def __init__(self):
        self.data = []

    def add(self, tag: Tag) -> Tag | None:
        """
        Adds a tag to the list if it is not already present.

        :param tag: The tag to be added.
        :return: A new Phone object if the tag is successfully added,
            or None if the tag is already present in the list.
        """
        index_phone_number = self.__index_tag(tag)
        if index_phone_number is None:
            self.data.append(tag)
            return tag

        return None

    def remove(self, tag: Tag) -> Tag | None:
        """
        Removes a tag from the stored tag list, if it exists.

        Searches for the specified tag in the list of stored phones. If the
        tag is found, it is removed from the list and returned. If the tag
        is not found, no operation is performed, and None is returned.

        :param tag: The tag to be removed.
        :return: The removed tag instance if the tag exists, otherwise None.
        """
        index_phone_number = self.__index_tag(tag)
        if index_phone_number is None:
            return None
        return self.data.pop(index_phone_number)

    def replace(self, old_tag: Tag, new_tag: Tag) -> Tag:
        """
        Replace an existing tag in the tag list. Replaces the old tag
        with a new one if the old number exists and the new number is not already in use.

        :param old_tag: The tag currently stored in the list that
            needs to be replaced.
        :param new_tag: The new tag to replace the old one. Must not already exist in the list.
        :return: The newly created Phone object representing the new tag.
        :raises UnknownPhoneNumberError: If the old tag is not found in the list.
        :raises ValueError: If the new tag is already in the list.
        """
        index_old_tag = self.__index_tag(old_tag)
        if index_old_tag is None:
            raise UnknownTagError(old_tag.value)

        if self.__index_tag(new_tag) is not None:
            raise AlreadyTagError(new_tag.value)

        self.data[index_old_tag] = new_tag
        return new_tag

    def contains(self, template: TagSearchTemplate) -> bool:
        """
        Determines if a given tag is present in the data.

        This method iterates through a collection of tags and checks
        if the provided phone_number exists within the `value` attribute of any
        tag object in the data.

        :param template: The tag template to search for.
        :return: True if the tag is found, False otherwise.
        """
        for tag in self.data:
            if template.value in tag.value:
                return True
        return False

    def __index_tag(self, tag: Tag) -> int | None:
        """
        Searches for the index of a tag in the list of stored tags.

        This method iterates through the list of tags and checks if any of the
        numbers matches the provided tag. If a match is found, the index of the
        tag in the list is returned. If no match is found, the method returns None.

        :param tag: The tag to search for in the list.
        :return: The index of the tag if found, or None if no match is found.
        """
        for index, item in enumerate(self.data):
            if item == tag:
                return index
        return None

    def __str__(self):
        if len(self.data) == 0:
            return ""
        return f"Tags: [{'; '.join([f'{tag}' for tag in self.data])}]"
