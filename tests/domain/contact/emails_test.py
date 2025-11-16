"""
Unit tests for validating the behavior of adding and removing emails
in the `Emails` collection.
"""

import pytest

from src.domain.contact.email import Email
from src.domain.contact.emails import Emails
from src.error.already_phone_number_error import AlreadyPhoneNumberError
from src.error.unknown_phone_number_error import UnknownPhoneNumberError


def test_add_non_existing_email() -> None:
    """
    Tests adding unique email to Emails.
    """
    emails = Emails()
    email = Email("a@b.co")

    result = emails.add(email)

    assert result == email
    assert len(emails) == 1
    assert email in emails.data


def test_add_duplicate_phone_returns_none() -> None:
    """
    Tests that adding a duplicate email returns None.
    """
    emails = Emails()
    email = Email("a@b.co")

    emails.add(email)
    result = emails.add(email)

    assert result is None
    assert len(emails) == 1


def test_add_multiple_unique_email():
    """
    Test that multiple unique emails can be added to list emails.
    """
    emails = Emails()
    phone1 = Email("a@b.co")
    phone2 = Email("b@c.co")

    result1 = emails.add(phone1)
    result2 = emails.add(phone2)

    assert result1 == phone1
    assert result2 == phone2
    assert len(emails.data) == 2
    assert emails.data == [phone1, phone2]


def test_remove_phone_successful():
    """
    Test that remove successfully removes an existing email from the contact.
    """
    emails = Emails()
    email = Email("a@b.co")
    emails.add(email)

    removed_email = emails.remove(email)

    assert removed_email == email
    assert len(emails.data) == 0


def test_remove_nonexistent_email():
    """
    Test that remove returns None when trying to remove an email that does not exist.
    """
    emails = Emails()
    phone1 = Email("a@b.co")
    phone2 = Email("b@c.co")

    emails.add(phone1)
    removed_email = emails.remove(phone2)

    assert removed_email is None


def test_remove_email_from_empty_list():
    """
    Test that remove returns None when the contact has no email.
    """
    emails = Emails()
    email = Email("a@b.co")

    removed_email = emails.remove(email)

    assert removed_email is None


def test_change_email_successful():
    """
    Test if `replace` successfully replaces an old email with a new one.
    """
    emails = Emails()
    old_email = Email("a@b.co")
    new_email = Email("b@c.co")

    emails.add(old_email)
    replaced_email = emails.replace(old_email, new_email)

    assert replaced_email == new_email
    assert new_email in emails.data
    assert old_email not in emails.data


def test_change_email_old_email_not_found():
    """
    Test if `replace` raises error when the old email doesn't exist.
    """
    emails = Emails()
    old_email = Email("a@b.co")
    new_email = Email("b@c.co")

    with pytest.raises(UnknownPhoneNumberError):
        emails.replace(old_email, new_email)


def test_change_email_new_email_already_exists():
    """
    Test if `replace` raises error when the new email is already in the list.
    """
    emails = Emails()
    old_email = Email("a@b.co")
    another_email = Email("b@c.co")
    new_email = Email("b@c.co")

    emails.add(old_email)
    emails.add(another_email)

    with pytest.raises(AlreadyPhoneNumberError):
        emails.replace(old_email, new_email)
