"""
A module for defining custom exceptions related to email validation.

This module introduces a specific exception, `InvalidEmailError`, which
is used to raise an error when an invalid email address is encountered.
It provides a detailed error message highlighting the invalid input.
"""
from colorama import Fore, Style


class InvalidEmailError(Exception):
    """
    Represents an error raised when an invalid email is provided.

    This exception is specifically designed to notify about invalid
    email addresses during validation processes or other operations
    where valid email input is required.

    :ivar message: The error message detailing the invalid email information.
    :type message: str
    """
    def __init__(self, email: str):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid email: '{email}'."
