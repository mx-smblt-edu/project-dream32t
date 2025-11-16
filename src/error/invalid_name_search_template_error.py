"""
Exception raised for invalid name search templates.

This exception is used to indicate that the provided name search
template does not meet the expected format or requirements.
"""


class InvalidNameSearchTemplateError(ValueError):
    """
    Represents an error raised for invalid name search templates.

    This exception is used to signal that a given name search template
    does not conform to the expected or required format.
    """

    def __init__(self, template: str):
        self.message = f"Invalid name search template: '{template}'."

    def __str__(self) -> str:
        return self.message
