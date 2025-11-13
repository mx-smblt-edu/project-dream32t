from src.model.phone import Phone
from src.model.phones import Phones


def test_add_non_existing_phone() -> None:
    """
    Tests adding unique phone number to Phones.
    """
    phones = Phones()
    phone = Phone("1234567890")

    result = phones.add(phone)

    assert result == phone
    assert len(phones) == 1
    assert phone in phones.data


def test_add_duplicate_phone_returns_none() -> None:
    """
    Tests that adding a duplicate phone number returns None.
    """
    phones = Phones()
    phone = Phone("1234567890")

    phones.add(phone)
    result = phones.add(phone)

    assert result is None
    assert len(phones) == 1


def test_add_multiple_unique_phone_numbers():
    """
    Test that multiple unique phone numbers can be added to list phones.
    """
    phones = Phones()
    phone1 = Phone("1234567890")
    phone2 = Phone("0987654321")

    result1 = phones.add(phone1)
    result2 = phones.add(phone2)

    assert result1 == phone1
    assert result2 == phone2
    assert len(phones.data) == 2
    assert phones.data == [phone1, phone2]
