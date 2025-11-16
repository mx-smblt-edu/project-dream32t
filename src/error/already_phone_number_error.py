"""
Defines a custom exception for handling cases where a phone number already exists in the phone list.
"""


class AlreadyPhoneNumberError(ValueError):
    """
    Custom exception to indicate that a phone number already exists in the phone list.
    """

    def __init__(self, phone: str):
        self.message = f"Phone '{phone}' is already used."

    def __str__(self) -> str:
        return self.message
