"""
Provides the Contact class.
"""
from src.model.emails import Emails
from src.model.name import Name
from src.model.phone import Phone
from src.model.phone_number_search_template import PhoneNumberSearchTemplate
from src.model.phones import Phones


class Contact:
    """A class for storing contact information."""

    def __init__(self, name: Name):
        self.__name = name
        self.__phones = Phones()
        self.__emails = Emails()

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

    def remove_phone(self, phone: Phone) -> Phone | None:
        """
        Removes a phone number from the stored phone list, if it exists.

        Searches for the specified phone number in the list of stored phones. If the
        phone number is found, it is removed from the list and returned. If the phone
        number is not found, no operation is performed, and None is returned.

        :param phone: The phone number to be removed.
        :return: The removed phone instance if the phone number exists, otherwise None.
        """

        return self.__phones.remove(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone) -> Phone:
        """
        Edits an existing phone number in the phone list. Replaces the old phone number
        with a new one if the old number exists and the new number is not already in use.

        :param old_phone: The phone number currently stored in the list that
            needs to be replaced.
        :param new_phone: The new phone number to replace the old one. Must not
            already exist in the list.
        :return: The newly created Phone object representing the new phone number.
        :raises UnknownPhoneNumberError: If the old phone number is not found in the list.
        :raises AlreadyPhoneNumberError: If the new phone number is already in the list.
        """
        return self.__phones.replace(old_phone, new_phone)

    def contains(self, template: PhoneNumberSearchTemplate) -> bool:
        """
        Determines if a given phone number is present in the phone list.

        :param template: The phone number template to search for.
        :return: True if the phone number is found, False otherwise.
        """
        return self.__phones.contains(template)

    def __str__(self):
        """Returns a string representation of the contact."""
        result = f"Contact name: {self.name}"
        phones_str = str(self.__phones)
        if len(phones_str) > 0:
            result += f", {phones_str}"
        return result
