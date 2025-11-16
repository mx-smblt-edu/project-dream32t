"""Module for tag search template."""
from src.error.invalid_tag_search_template_error import InvalidTagSearchTemplateError


class TagSearchTemplate:
    """Class for storing tag search template."""

    def __init__(self, template: str):
        tripped_template = template.strip()
        if len(tripped_template) == 0:
            raise InvalidTagSearchTemplateError(template)
        self.__value = tripped_template

    @property
    def value(self) -> str:
        """Getter for the tag search template"""
        return self.__value

    def __str__(self) -> str:
        return str(self.__value)
