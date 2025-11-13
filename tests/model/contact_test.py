"""
Unit tests for the Contact class.
"""
from src.model.contact import Contact
from src.model.name import Name
from src.model.phone import Phone


def test_contact_initialization():
    """
    Tests that a Contact object is correctly initialized with a valid Name instance.
    """
    name = Name("John")
    contact = Contact(name)
    assert contact.name == name
    assert len(contact._Contact__phones) == 0


def test_add_unique_phone_number():
    """
    Test that a new phone number is successfully added to the contact.
    """
    contact_name = Name("John")
    contact = Contact(contact_name)
    phone = Phone("1234567890")

    result = contact.add_phone(phone)

    assert result == phone
    assert len(contact._Contact__phones.data) == 1  # Accessing private attribute for validation
    assert contact._Contact__phones.data[0] == phone


def test_add_duplicate_phone_numbers():
    """
    Test that duplicate phone numbers cannot be added to a contact.
    """
    contact_name = Name("John")
    contact = Contact(contact_name)
    phone = Phone("1234567890")
    contact.add_phone(phone)

    result = contact.add_phone(phone)

    assert result is None
    assert len(contact._Contact__phones.data) == 1
    assert contact._Contact__phones.data[0] == phone


def test_add_multiple_unique_phone_numbers():
    """
    Test that multiple unique phone numbers can be added to a contact.
    """
    contact_name = Name("John")
    contact = Contact(contact_name)
    phone1 = Phone("1234567890")
    phone2 = Phone("0987654321")

    result1 = contact.add_phone(phone1)
    result2 = contact.add_phone(phone2)

    assert result1 == phone1
    assert result2 == phone2
    assert len(contact._Contact__phones.data) == 2
    assert contact._Contact__phones.data == [phone1, phone2]


def test_remove_phone_successful():
    """
    Test that remove_phone successfully removes an existing phone from the contact.
    """
    name = Name("John")
    contact = Contact(name)
    phone = Phone("1234567890")
    contact.add_phone(phone)

    removed_phone = contact.remove_phone(phone)

    assert removed_phone == phone
    assert len(contact._Contact__phones.data) == 0


def test_remove_nonexistent_phone():
    """
    Test that remove_phone returns None when trying to remove a phone that does not exist.
    """
    name = Name("John")
    contact = Contact(name)
    phone1 = Phone("1234567890")
    phone2 = Phone("0987654321")

    contact.add_phone(phone1)
    removed_phone = contact.remove_phone(phone2)

    assert removed_phone is None


def test_remove_phone_from_empty_list():
    """
    Test that remove_phone returns None when the contact has no phone numbers.
    """
    name = Name("John")
    contact = Contact(name)
    phone = Phone("1234567890")

    removed_phone = contact.remove_phone(phone)

    assert removed_phone is None
