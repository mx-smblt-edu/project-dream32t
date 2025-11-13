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


def test_find_contact_existing() -> None:
    """
    Test that the `find` method returns the correct Contact object
    when the corresponding Name exists in the ContactBook.
    """
    contact_book = ContactBook()
    contact_name = Name("John")
    contact = Contact(contact_name)

    contact_book.add_contact(contact)
    result = contact_book.find(contact_name)

    assert result == contact


def test_find_contact_non_existing() -> None:
    """
    Test that the `find` method returns None when the Name does not exist
    in the ContactBook.
    """
    contact_book = ContactBook()
    non_existent_name = Name("John")

    result = contact_book.find(non_existent_name)

    assert result is None


def test_delete_existing_contact():
    """
    Test that delete successfully removes and returns a Contact object
    if the contact's name exists in the ContactBook.
    """
    contact_book = ContactBook()
    contact_name = Name("John")
    contact = Contact(contact_name)
    contact_book.add_contact(contact)

    deleted_contact = contact_book.delete(contact_name)

    assert deleted_contact == contact
    assert contact_name not in contact_book.data


def test_delete_non_existing_contact():
    """
    Test that delete returns None if the contact's name does not exist
    in the ContactBook.
    """
    contact_book = ContactBook()
    contact_name = Name("NonExisting")

    deleted_contact = contact_book.delete(contact_name)

    assert deleted_contact is None


def test_find_by_name_single_result():
    """
    Tests that find_by_name returns a single contact when the name matches exactly.
    """
    book = ContactBook()
    name = Name("John Doe")
    contact = Contact(name)
    book.add_contact(contact)

    result = book.find_by_name("John")
    assert result == [contact]


def test_find_by_name_multiple_results():
    """
    Tests that find_by_name returns multiple contacts when the name substring matches multiple.
    """
    book = ContactBook()
    contact1 = Contact(Name("John Smith"))
    contact2 = Contact(Name("Johnny Depp"))
    book.add_contact(contact1)
    book.add_contact(contact2)

    result = book.find_by_name("John")
    assert result == [contact1, contact2]


def test_find_by_name_no_matches():
    """
    Tests that find_by_name returns None when no contacts match the name substring.
    """
    book = ContactBook()
    contact = Contact(Name("Alice Wonderland"))
    book.add_contact(contact)

    result = book.find_by_name("John")
    assert result is None


def test_find_by_name_case_insensitivity():
    """
    Tests that find_by_name is case-insensitive when searching for name substrings.
    """
    book = ContactBook()
    contact = Contact(Name("John Doe"))
    book.add_contact(contact)

    result = book.find_by_name("john")
    assert result == [contact]


def test_find_by_name_empty_substring():
    """
    Tests that find_by_name returns all contacts when an empty substring is provided.
    """
    book = ContactBook()
    contact1 = Contact(Name("John Smith"))
    contact2 = Contact(Name("Jane Doe"))
    book.add_contact(contact1)
    book.add_contact(contact2)

    result = book.find_by_name("")
    assert result == [contact1, contact2]
