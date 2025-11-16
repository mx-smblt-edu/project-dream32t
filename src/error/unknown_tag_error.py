"""
Defines a custom exception class for handling unknown tag.
"""


class UnknownTagError(ValueError):
    """
    Exception raised for referencing an unknown tag.
    """

    def __init__(self, tag: str):
        self.message = f"Tag '{tag}' is unknown."

    def __str__(self) -> str:
        return self.message
