"""
A collection class for storing phone numbers.

This module provides the `Phones` class, which is a custom implementation
inheriting from the `UserList` collection that holds instances of the `Phone`
class.
"""
from collections import UserList

from src.error.already_phone_number_error import AlreadyPhoneNumberError
from src.error.unknown_phone_number_error import UnknownPhoneNumberError
from src.model.phone import Phone
from src.model.phone_number_search_template import PhoneNumberSearchTemplate


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

    def remove(self, phone: Phone) -> Phone | None:
        """
        Removes a phone number from the stored phone list, if it exists.

        Searches for the specified phone number in the list of stored phones. If the
        phone number is found, it is removed from the list and returned. If the phone
        number is not found, no operation is performed, and None is returned.

        :param phone: The phone number to be removed.
        :return: The removed phone instance if the phone number exists, otherwise None.
        """
        index_phone_number = self.__index_phone_number(phone)
        if index_phone_number is None:
            return None
        return self.data.pop(index_phone_number)

    def replace(self, old_phone: Phone, new_phone: Phone) -> Phone:
        """
        Replace an existing phone number in the phone list. Replaces the old phone number
        with a new one if the old number exists and the new number is not already in use.

        :param old_phone: The phone number currently stored in the list that
            needs to be replaced.
        :param new_phone: The new phone number to replace the old one. Must not
            already exist in the list.
        :return: The newly created Phone object representing the new phone number.
        :raises UnknownPhoneNumberError: If the old phone number is not found in the list.
        :raises ValueError: If the new phone number is already in the list.
        """
        index_old_phone_number = self.__index_phone_number(old_phone)
        if index_old_phone_number is None:
            raise UnknownPhoneNumberError(old_phone.value)

        if self.__index_phone_number(new_phone) is not None:
            raise AlreadyPhoneNumberError(new_phone.value)

        self.data[index_old_phone_number] = new_phone
        return new_phone

    def contains(self, template: PhoneNumberSearchTemplate) -> bool:
        """
        Determines if a given phone number is present in the data.

        This method iterates through a collection of phone numbers and checks
        if the provided phone_number exists within the `value` attribute of any
        phone object in the data.

        :param template: The phone number template to search for.
        :return: True if the phone number is found, False otherwise.
        """
        for phone in self.data:
            if template.value in phone.value:
                return True
        return False

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
