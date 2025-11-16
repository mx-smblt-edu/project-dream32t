"""Module for name search template class."""

from src.error.invalid_name_search_template_error import InvalidNameSearchTemplateError


class NameSearchTemplate:
    """Class for storing name search template."""

    def __init__(self, template: str):
        tripped_template = template.strip()
        if len(tripped_template) == 0:
            raise InvalidNameSearchTemplateError(template)
        self.__value = tripped_template.casefold()

    @property
    def value(self) -> str:
        """Getter for the name search template"""
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)
