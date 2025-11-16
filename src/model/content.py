"""
Provides the Content class.
"""
from src.error.invalid_content_error import InvalidContentError


class Content:
    """Class for storing the note content."""

    def __init__(self, value: str):
        clean_value = value.strip()
        if len(clean_value) < 1 or len(clean_value) > 512:
            raise InvalidContentError(value)
        self.__value = value

    @property
    def value(self) -> str:
        """Getter for the content value"""
        return self.__value

    def __str__(self) -> str:
        return f"Content: '{self.__value}'"
