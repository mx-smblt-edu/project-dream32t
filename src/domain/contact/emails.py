"""
A collection class for storing phone numbers.

This module provides the `Phones` class, which is a custom implementation
inheriting from the `UserList` collection that holds instances of the `Phone`
class.
"""

from collections import UserList

from src.domain.contact.email import Email
from src.error.already_phone_number_error import AlreadyPhoneNumberError
from src.error.unknown_phone_number_error import UnknownPhoneNumberError


class Emails(UserList[Email]):
    """A class for storing phone numbers."""

    def __init__(self):
        self.data = []

    def add(self, email: Email) -> Email | None:
        """
        Adds a email to the list if it is not already present.

        :param email: The email to be added.
        :return: A new Phone object if the email is successfully added,
            or None if the email is already present in the list.
        """
        index_phone_number = self.__index_phone_number(email)
        if index_phone_number is None:
            self.data.append(email)
            return email

        return None

    def remove(self, email: Email) -> Email | None:
        """
        Removes a email from the stored phone list, if it exists.

        Searches for the specified email in the list of stored phones. If the
        email is found, it is removed from the list and returned. If the phone
        number is not found, no operation is performed, and None is returned.

        :param email: The email to be removed.
        :return: The removed phone instance if the email exists, otherwise None.
        """
        index_phone_number = self.__index_phone_number(email)
        if index_phone_number is None:
            return None
        return self.data.pop(index_phone_number)

    def replace(self, old_email: Email, new_email: Email) -> Email:
        """
        Replace an existing email in the phone list. Replaces the old email
        with a new one if the old number exists and the new number is not already in use.

        :param old_email: The email currently stored in the list that
            needs to be replaced.
        :param new_email: The new email to replace the old one. Must not
            already exist in the list.
        :return: The newly created Phone object representing the new email.
        :raises UnknownPhoneNumberError: If the old email is not found in the list.
        :raises ValueError: If the new email is already in the list.
        """
        index_old_phone_number = self.__index_phone_number(old_email)
        if index_old_phone_number is None:
            raise UnknownPhoneNumberError(old_email.value)

        if self.__index_phone_number(new_email) is not None:
            raise AlreadyPhoneNumberError(new_email.value)

        self.data[index_old_phone_number] = new_email
        return new_email

    def __index_phone_number(self, email: Email) -> int | None:
        """
        Searches for the index of a email in the list of stored phone numbers.

        This method iterates through the list of phone numbers and checks if any of the
        numbers matches the provided email. If a match is found, the index of the
        email in the list is returned. If no match is found, the method returns None.

        :param email: The email to search for in the list.
        :return: The index of the email if found, or None if no match is found.
        """
        for index, item in enumerate(self.data):
            if item == email:
                return index
        return None

    def __str__(self):
        if len(self.data) == 0:
            return ""
        return f"emails: {'; '.join([f'{phone}' for phone in self.data])}"
