"""
Provides the Contact class.
"""
from src.domain.contact.birthday import Birthday
from src.domain.contact.emails import Emails
from src.domain.contact.name import Name
from src.domain.contact.phones import Phones


class Contact:
    """A class for storing contact information."""

    def __init__(self, name: Name):
        self.__name = name
        self.__phones = Phones()
        self.__emails = Emails()
        self.__birthday: Birthday | None = None

    @property
    def name(self) -> Name:
        """Getter for the name"""
        return self.__name

    @property
    def phones(self) -> Phones:
        """Getter for the phones"""
        return self.__phones

    @property
    def emails(self) -> Emails:
        """Getter for the emails"""
        return self.__emails

    @property
    def birthday(self) -> Birthday | None:
        """Getter for the birthday"""
        return self.__birthday

    def add_birthday(self, birthday: Birthday) -> None:
        """Adds a birthday to the contact."""
        self.__birthday = birthday

    def delete_birthday(self) -> None:
        """Deletes the birthday from the contact."""
        self.__birthday = None

    def __str__(self):
        """Returns a string representation of the contact."""
        result = f"Contact name: {self.name}"
        phones_str = str(self.__phones)
        if len(phones_str) > 0:
            result += f", {phones_str}"
        return result
