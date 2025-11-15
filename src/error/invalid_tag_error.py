"""
A module for defining custom exceptions related to tag validation.

This module introduces a specific exception, `InvalidTagError`, which
is used to raise an error when an invalid tag is encountered.
It provides a detailed error message highlighting the invalid input.
"""


class InvalidTagError(Exception):
    """
    Represents an error raised when an invalid tag is provided.

    This exception is specifically designed to notify about invalid
    tag during validation processes or other operations
    where valid tag input is required.

    :ivar message: The error message detailing the invalid tag information.
    :type message: str
    """

    def __init__(self, tag: str):
        self.message = (f"Invalid tag: '{tag}'. "
                        "Tag must not be empty and must be between 1 and 32 characters long.")

    def __str__(self) -> str:
        return self.message
