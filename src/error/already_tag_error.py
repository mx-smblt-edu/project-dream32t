"""
Defines a custom exception for handling cases where a tag already exists in the tag list.
"""


class AlreadyTagError(ValueError):
    """
    Custom exception to indicate that a tag already exists in the tag list.
    """

    def __init__(self, tag: str):
        self.message = f"Tag '{tag}' is already used."

    def __str__(self) -> str:
        return self.message
