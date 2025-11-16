"""
Unit tests for the `PhoneNumberSearchTemplate` class
"""

import pytest

from src.domain.contact.phone_number_search_template import PhoneNumberSearchTemplate
from src.error.invalid_phone_number_search_template_error import InvalidPhoneNumberSearchTemplateError


def test_phone_number_search_template_valid():
    """Test creating a PhoneNumberSearchTemplate instance with a valid template."""
    template = "050"
    obj = PhoneNumberSearchTemplate(template)
    assert obj.value == "050"


def test_phone_number_search_template_whitespace_trimmed():
    """Test that leading and trailing whitespace in the template are trimmed."""
    template = "  050  "
    obj = PhoneNumberSearchTemplate(template)
    assert obj.value == "050"


def test_phone_number_search_template_empty_string_raises_error():
    """Test that an empty string raises InvalidPhoneNumberSearchTemplateError."""
    template = ""
    with pytest.raises(InvalidPhoneNumberSearchTemplateError) as excinfo:
        PhoneNumberSearchTemplate(template)
    assert "Invalid phone number search template:" in str(excinfo.value)


def test_phone_number_search_template_whitespace_only_raises_error():
    """Test that a string with only whitespace raises InvalidPhoneNumberSearchTemplateError."""
    template = "    "
    with pytest.raises(InvalidPhoneNumberSearchTemplateError) as excinfo:
        PhoneNumberSearchTemplate(template)
    assert "Invalid phone number search template:" in str(excinfo.value)
