"""
Provides the Contact class.
"""
from src.model.name import Name


class Contact:
    """A class for storing contact information."""

    def __init__(self, name: Name):
        self.name = name

    def __str__(self):
        return f"Contact name: {self.name}"
