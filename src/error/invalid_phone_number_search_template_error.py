"""
Exception raised for invalid phone number search templates.

This exception is used to indicate that the provided phone number search
template does not meet the expected format or requirements.
"""


class InvalidPhoneNumberSearchTemplateError(ValueError):
    """
    Represents an error raised for an invalid phone number search template.

    This exception is specifically used to indicate that the provided phone number
    search template is not valid. It can be used in contexts where user-defined
    templates for searching phone numbers must adhere to a certain format.
    """

    def __init__(self, template: str):
        self.message = f"Invalid phone number search template: '{template}'."

    def __str__(self) -> str:
        return self.message
