"""
A module for defining custom exceptions related to topic validation.

This module introduces a specific exception, `InvalidTopicError`, which
is used to raise an error when an invalid topic is encountered.
It provides a detailed error message highlighting the invalid input.
"""


class InvalidTopicError(ValueError):
    """
    Represents an error raised when an invalid topic is provided.

    This exception is specifically designed to notify about an invalid
    topic during validation processes or other operations
    where valid topic input is required.

    :ivar message: The error message detailing the invalid topic information.
    :type message: str
    """

    def __init__(self, topic: str):
        self.message = (f"Invalid topic: '{topic}'. "
                        "Topic must not be empty and must be between 1 and 32 characters long.")

    def __str__(self) -> str:
        return self.message
