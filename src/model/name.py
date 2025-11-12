"""
Provides the Name class.
"""


class Name:
    """Class for storing the contact name."""

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)
