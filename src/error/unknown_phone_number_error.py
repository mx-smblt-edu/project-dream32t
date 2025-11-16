"""
Defines a custom exception class for handling unknown phone numbers.
"""


class UnknownPhoneNumberError(ValueError):
    """
    Exception raised for referencing an unknown phone number.
    """

    def __init__(self, phone: str):
        self.message = f"Phone '{phone}' is unknown."

    def __str__(self) -> str:
        return self.message
