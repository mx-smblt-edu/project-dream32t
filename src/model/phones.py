"""
A collection class for storing phone numbers.

This module provides the `Phones` class, which is a custom implementation
inheriting from the `UserList` collection that holds instances of the `Phone`
class.
"""
from collections import UserList

from src.model.phone import Phone


class Phones(UserList[Phone]):
    """A class for storing phone numbers."""
    pass


def __str__(self):
    if len(self.data) == 0:
        return ""
    return f"phones: {'; '.join([f'{phone}' for phone in self.data])}"
