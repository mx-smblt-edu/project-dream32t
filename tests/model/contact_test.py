"""
Unit tests for the Contact class.
"""
from src.model.contact import Contact
from src.model.name import Name


def test_contact_initialization():
    """
    Tests that a Contact object is correctly initialized with a valid Name instance.
    """
    name = Name("John")
    contact = Contact(name)
    assert contact.name == name
    assert len(contact.phones) == 0
