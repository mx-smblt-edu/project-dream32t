"""Module for phone number search template."""
from src.error.invalid_phone_number_search_template_error import InvalidPhoneNumberSearchTemplateError


class PhoneNumberSearchTemplate:
    """Class for storing phone number search template."""

    def __init__(self, template: str):
        tripped_template = template.strip()
        if len(tripped_template) == 0:
            raise InvalidPhoneNumberSearchTemplateError(template)
        self.__value = tripped_template

    @property
    def value(self) -> str:
        """Getter for the phone number search template"""
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)
