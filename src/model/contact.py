"""
Provides the Contact class.
"""
from src.model.name import Name
from src.model.phones import Phones


class Contact:
    """A class for storing contact information."""

    def __init__(self, name: Name):
        self.name = name
        self.phones = Phones()

    def __str__(self):
        """Returns a string representation of the contact."""
        result = f"Contact name: {self.name}"
        phones_str = str(self.phones)
        if len(phones_str) > 0:
            result += f", {phones_str}"
        return result
