"""
Defines a custom exception class for handling unknown note.
"""


class UnknownNoteError(ValueError):
    """
    Exception raised for referencing an unknown note.
    """

    def __init__(self, topic: str):
        self.message = f"Note with topic: '{topic}' is unknown."

    def __str__(self) -> str:
        return self.message
