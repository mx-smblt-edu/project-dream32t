"""
Unit tests for verifying the behavior of the ContactBook class methods.
"""
from src.model.contact import Contact
from src.model.contact_book import ContactBook
from src.model.name import Name


def test_add_contact_adds_new_contact():
    """
    Test that add_contact successfully adds a new Contact object
    to the ContactBook when the contact's name does not already exist.
    """
    contact_book = ContactBook()
    contact_name = Name("John")
    new_contact = Contact(contact_name)

    contact_book.add_contact(new_contact)

    assert contact_name in contact_book.data
    assert contact_book.data[contact_name] == new_contact


def test_add_contact_does_not_add_duplicate_contact():
    """
    Test that add_contact does not add a Contact object
    if a contact with the same name already exists.
    """
    contact_book = ContactBook()
    contact_name = Name("John")
    contact = Contact(contact_name)

    # Add a contact
    contact_book.add_contact(contact)

    # Try adding a duplicate contact
    duplicate_contact = Contact(contact_name)
    contact_book.add_contact(duplicate_contact)

    # The duplicate should not be added
    assert len(contact_book.data) == 1
    assert contact_name in contact_book.data
    assert contact_book.data[contact_name] == contact
