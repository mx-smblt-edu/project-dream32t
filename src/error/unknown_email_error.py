"""
Defines a custom exception class for handling an unknown email address.
"""


class UnknownEmailError(ValueError):
    """Exception raised for errors related to an unknown email address."""

    def __init__(self, email: str):
        self.message = f"Email `{email}` does not exist."

    def __str__(self) -> str:
        return self.message
