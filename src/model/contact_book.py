"""
Provides an AddressBook class for managing and storing contact information.
"""
from collections import UserDict

from src.model.contact import Contact
from src.model.name import Name


class ContactBook(UserDict[Name, Contact]):
    """A class for storing and managing contacts."""

    def add_contact(self, contact: Contact) -> None:
        """
        Add a contact to the data storage.

        This method adds a contact to the internal data storage only if the contact's name
        does not already exist in the storage. The name is determined using the contact's
        name attribute.

        :param contact: The contact to be added to the data storage
        :return: None
        """
        name: Name = contact.name
        if name not in self.data:
            self.data[name] = contact

    def __str__(self) -> str:
        return "ContactBook\n" + '\n'.join([f'{record}' for record in self.data.values()])
