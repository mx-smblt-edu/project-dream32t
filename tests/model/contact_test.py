"""
Unit tests for the Contact class.
"""
import pytest

from src.error.already_phone_number_error import AlreadyPhoneNumberError
from src.error.unknown_phone_number_error import UnknownPhoneNumberError
from src.model.contact import Contact
from src.model.name import Name
from src.model.phone import Phone
from src.model.phone_number_search_template import PhoneNumberSearchTemplate


def test_contact_initialization():
    """
    Tests that a Contact object is correctly initialized with a valid Name instance.
    """
    name = Name("John")
    contact = Contact(name)
    assert contact.name == name
    assert len(contact._Contact__phones) == 0
    assert len(contact._Contact__emails) == 0


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


def test_change_phone_successful():
    """
    Test if `change_phone` successfully replaces an old phone number with a new one.
    """
    contact = Contact(Name("John"))
    old_phone = Phone("1234567890")
    new_phone = Phone("0987654321")

    contact.add_phone(old_phone)
    replaced_phone = contact.change_phone(old_phone, new_phone)

    assert replaced_phone == new_phone
    assert new_phone in contact._Contact__phones.data
    assert old_phone not in contact._Contact__phones.data


def test_change_phone_old_number_not_found():
    """
    Test if `change_phone` raises error when the old phone number doesn't exist.
    """
    contact = Contact(Name("John"))
    old_phone = Phone("1234567890")
    new_phone = Phone("0987654321")

    with pytest.raises(UnknownPhoneNumberError):
        contact.change_phone(old_phone, new_phone)


def test_change_phone_new_number_already_exists():
    """
    Test if `change_phone` raises error when the new phone number is already in the list.
    """
    contact = Contact(Name("John Doe"))
    old_phone = Phone("1234567890")
    another_phone = Phone("1122334455")
    new_phone = Phone("1122334455")

    contact.add_phone(old_phone)
    contact.add_phone(another_phone)

    with pytest.raises(AlreadyPhoneNumberError):
        contact.change_phone(old_phone, new_phone)


def test_contains_existing_phone_number():
    """
    Tests that the `contains` method of a `Contact` instance returns True
    when a phone number exists in the contact's phone list.
    """
    name = Name("John")
    contact = Contact(name)
    phone = Phone("1234567890")
    contact.add_phone(phone)
    template = PhoneNumberSearchTemplate("1234567890")

    assert contact.contains(template) is True


def test_contains_non_existing_phone_number():
    """
    Tests that the `contains` method of a `Contact` instance returns False
    for a phone number that is not in the contact's phone list.
    """
    name = Name("John")
    contact = Contact(name)
    phone = Phone("1234567890")
    contact.add_phone(phone)
    template = PhoneNumberSearchTemplate("9876543210")

    assert contact.contains(template) is False


def test_contains_partial_match_within_phone_number():
    """
    Tests that the `contains` method of a `Contact` instance can find a
    partial match of a phone number.
    """
    name = Name("John")
    contact = Contact(name)
    phone = Phone("1234567890")
    contact.add_phone(phone)
    template = PhoneNumberSearchTemplate("456")

    assert contact.contains(template) is True


def test_contains_empty_phone_list():
    """
    Tests that the `contains` method of a `Contact` instance returns False
    when the phone list is empty.
    """
    name = Name("John")
    contact = Contact(name)
    template = PhoneNumberSearchTemplate("1234567890")

    assert contact.contains(template) is False
