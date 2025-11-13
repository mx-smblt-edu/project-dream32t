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

    def find(self, name: Name) -> Contact | None:
        """
        Searches for a contact by its name in the data mapping.

        This method attempts to retrieve a contact from the internal data mapping.
        If the name exists in the mapping, the corresponding contact is returned.
        If the name does not exist, `None` is returned.

        :param name: The name of the contact to search for.
        :return: The associated contact if found, otherwise `None`.
        """
        return self.data.get(name, None)
