"""
Exception raised for invalid tag search templates.

This exception is used to indicate that the provided tag search
template does not meet the expected format or requirements.
"""


class InvalidTagSearchTemplateError(Exception):
    """
    Represents an error raised for an invalid tag search template.

    This exception is specifically used to indicate that the provided tag
    search template is not valid. It can be used in contexts where user-defined
    templates for searching tags must adhere to a certain format.
    """

    def __init__(self, template: str):
        self.message = f"Invalid tag search template: '{template}'."

    def __str__(self) -> str:
        return self.message
