"""
A module for defining custom exceptions related to name validation.

This module introduces a specific exception, `InvalidNameError`, which
is used to raise an error when an invalid name is encountered.
It provides a detailed error message highlighting the invalid input.
"""
from colorama import Fore, Style


class InvalidNameError(Exception):
    """
    Represents an error raised when an invalid name is provided.

    This exception is specifically designed to notify about invalid
    name during validation processes or other operations
    where valid name input is required.

    :ivar message: The error message detailing the invalid name information.
    :type message: str
    """

    def __init__(self, email: str):
        self.message = (f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid name: '{email}'. "
                        f"Name must not be empty and must be between 2 and 64 characters long.")
