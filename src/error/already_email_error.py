"""
Defines a custom exception for handling cases where an email address
already exists in the email list.
"""


class AlreadyEmailError(ValueError):
    """
    Custom exception to indicate that an email address already exists in the email list.
    """

    def __init__(self, email: str):
        self.message = f"Email '{email}' is already used."

    def __str__(self) -> str:
        return self.message
