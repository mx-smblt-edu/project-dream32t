"""Provides the Topic class."""

from src.error.invalid_topic_error import InvalidTopicError


class Topic:
    """Class for storing the note topic."""

    def __init__(self, value: str):
        clean_value = value.strip()
        if len(clean_value) < 1 or len(clean_value) > 32:
            raise InvalidTopicError(value)
        self.__value = value

    @property
    def value(self) -> str:
        """Getter for the topic value"""
        return self.__value

    def __str__(self) -> str:
        return f"Topic: {self.__value}"

    def __hash__(self) -> int:
        return hash(self.__value)

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            raise TypeError(f"Cannot compare {self!r} and {other!r}")
        return self.value.casefold() == other.value.casefold()
