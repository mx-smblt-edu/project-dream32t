"""
A collection class for storing phone numbers.

This module provides the `Phones` class, which is a custom implementation
inheriting from the `UserList` collection that holds instances of the `Phone`
class.
"""
from collections import UserList

from src.model.phone import Phone


class Phones(UserList[Phone]):
    """A class for storing phone numbers."""

    def __init__(self):
        self.data = []

    def add(self, phone: Phone) -> Phone | None:
        """
        Adds a phone number to the list if it is not already present.

        :param phone: The phone number to be added.
        :return: A new Phone object if the phone number is successfully added,
            or None if the phone number is already present in the list.
        """
        index_phone_number = self.__index_phone_number(phone)
        if index_phone_number is None:
            self.data.append(phone)
            return phone

        return None

    def __index_phone_number(self, phone: Phone) -> int | None:
        """
        Searches for the index of a phone number in the list of stored phone numbers.

        This method iterates through the list of phone numbers and checks if any of the
        numbers matches the provided phone number. If a match is found, the index of the
        phone number in the list is returned. If no match is found, the method returns None.

        :param phone: The phone number to search for in the list.
        :return: The index of the phone number if found, or None if no match is found.
        """
        for index, item in enumerate(self.data):
            if item == phone:
                return index
        return None


def __str__(self):
    if len(self.data) == 0:
        return ""
    return f"phones: {'; '.join([f'{phone}' for phone in self.data])}"
