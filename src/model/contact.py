"""
Provides the Contact class.
"""
from src.model.name import Name
from src.model.phone import Phone
from src.model.phones import Phones


class Contact:
    """A class for storing contact information."""

    def __init__(self, name: Name):
        self.__name = name
        self.__phones = Phones()

    @property
    def name(self) -> Name:
        """Getter for the name"""
        return self.__name

    def add_phone(self, phone: Phone) -> Phone | None:
        """
        Adds a phone number to the list of phones.

        :param phone: The phone number to be added.
        :return: A new Phone object if the phone number is successfully added,
            or None if the phone number is already present in the list.
        """
        return self.__phones.add(phone)

    def __str__(self):
        """Returns a string representation of the contact."""
        result = f"Contact name: {self.name}"
        phones_str = str(self.__phones)
        if len(phones_str) > 0:
            result += f", {phones_str}"
        return result
