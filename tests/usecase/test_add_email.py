import pytest

from src.domain.contact.contact import Contact
from src.domain.contact.contact_book import ContactBook
from src.domain.contact.email import Email
from src.domain.contact.name import Name
from src.error.unknown_contact_error import UnknownContactError
from src.usecase.add_email import add_email


def test_add_email_to_existing_contact():
    """
    Test that `add_email` adds an email to an existing contact.
    """
    contact_book = ContactBook()
    name = Name("John")
    email = Email("a@b.com")
    contact = Contact(name)
    contact_book.add(contact)

    updated_contact = add_email(contact_book, name, email)

    assert updated_contact is not None
    assert email in updated_contact.emails


def test_add_email_to_non_existent_contact():
    """
    Test that `add_email` raises `UnknownContactError` if contact does not exist.
    """
    contact_book = ContactBook()
    name = Name("Jane")
    email = Email("a@b.com")

    with pytest.raises(UnknownContactError, match=r"Contact `Jane` does not exist."):
        add_email(contact_book, name, email)


def test_add_duplicate_email():
    """
    Test that `add_email` does not add a duplicate email to a contact.
    """
    contact_book = ContactBook()
    name = Name("Jane")
    email = Email("a@b.com")
    contact = Contact(name)
    contact.emails.add(email)  # Add the email initially
    contact_book.add(contact)

    updated_contact = add_email(contact_book, name, email)

    assert updated_contact is None
    assert len(contact.emails) == 1
