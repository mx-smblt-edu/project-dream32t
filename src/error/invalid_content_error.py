"""
A module for defining custom exceptions related to content validation.

This module introduces a specific exception, `InvalidContentError`, which
is used to raise an error when an invalid content is encountered.
It provides a detailed error message highlighting the invalid input.
"""


class InvalidContentError(ValueError):
    """
    Represents an error raised when an invalid content is provided.

    This exception is specifically designed to notify about an invalid
    content during validation processes or other operations
    where valid content input is required.

    :ivar message: The error message detailing the invalid content information.
    :type message: str
    """

    def __init__(self, content: str):
        self.message = (f"Invalid content: '{content}'. "
                        "Content must not be empty and must be between 1 and 512 characters long.")

    def __str__(self) -> str:
        return self.message
