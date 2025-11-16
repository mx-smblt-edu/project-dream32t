"""
Defines a custom exception class for handling unknown contacts.
"""


class UnknownContactError(ValueError):
    """Exception raised for errors related to unknown contacts."""

    def __init__(self, name: str):
        self.message = f"Contact `{name}` does not exist."

    def __str__(self) -> str:
        return self.message
