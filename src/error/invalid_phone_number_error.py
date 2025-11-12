"""
Defines a custom exception class `InvalidPhoneNumberError` for handling
invalid phone number inputs.

This module introduces an exception specifically tailored to indicate that
a provided phone number string is invalid.
"""
from colorama import Fore, Style


class InvalidPhoneNumberError(Exception):
    """
    Exception raised for invalid phone numbers.

    This class is designed to handle cases where a provided phone
    number does not match the required format or specification.

    :param phone: The invalid phone number string.
    """

    def __init__(self, phone: str):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid phone number: '{phone}'."
