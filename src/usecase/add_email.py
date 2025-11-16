"""
Provides functionality to add an email to a contact in a contact book.
"""

from src.domain.contact.contact import Contact
from src.domain.contact.contact_book import ContactBook
from src.domain.contact.email import Email
from src.domain.contact.name import Name
from src.error.unknown_contact_error import UnknownContactError


def add_email(contact_book: ContactBook, name: Name, email: Email) -> Contact | None:
    contact = contact_book.find(name)
    if contact is None:
        raise UnknownContactError(name.value)

    if contact.emails.add(email):
        return contact
    return None
