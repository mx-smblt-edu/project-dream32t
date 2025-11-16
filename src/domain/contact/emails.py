"""
A collection class for storing email addresses.

This module provides the `Emails` class, which is a custom implementation
inheriting from the `UserList` collection that holds instances of the `Email`
class.
"""

from collections import UserList

from src.domain.contact.email import Email
from src.error.already_email_error import AlreadyEmailError
from src.error.unknown_email_error import UnknownEmailError


class Emails(UserList[Email]):
    """A class for storing email addresses."""

    def __init__(self):
        self.data = []
        super().__init__()

    def add(self, email: Email) -> bool:
        """
        Adds an email object to the internal data list if it does not already
        exist.

        This method checks if the provided email object is already indexed in
        the internal storage. If not, the email is appended to the data list.
        """
        index_email = self.__index_email(email)
        if index_email is None:
            self.data.append(email)
            return True

        return False

    def remove(self, email: Email) -> None:
        """
        Removes an email from the data.

        This method removes the specified email from the collection of data. If the
        email is not found in the collection, an exception is raised.
        """
        index_email = self.__index_email(email)
        if index_email is None:
            raise UnknownEmailError(email.value)

        self.data.pop(index_email)

    def replace(self, old_email: Email, new_email: Email) -> None:
        """
        Replaces an existing email with a new one in the email collection.

        Searches for the given old email within the collection. If found,
        replaces it with the new email while ensuring no duplicate entries
        exist. Raises an error if the old email is not found or if the
        new email already exists in the collection.
        """
        index_old_email = self.__index_email(old_email)
        if index_old_email is None:
            raise UnknownEmailError(old_email.value)

        if self.__index_email(new_email) is not None:
            raise AlreadyEmailError(new_email.value)

        self.data[index_old_email] = new_email

    def __index_email(self, email: Email) -> int | None:
        """
        Searches for an email object in the data collection and returns its index if found.

        This method iterates through the collection of email objects stored in the `data`
        attribute to identify if a given email object exists in the collection. If the
        email object matches an item in the collection, it returns the index of the first
        occurrence. Otherwise, it returns None.
        """
        for index, item in enumerate(self.data):
            if item == email:
                return index
        return None

    def __str__(self):
        if len(self.data) == 0:
            return ""
        return f"Emails: [{', '.join([f'{email.value}' for email in self.data])}]"
