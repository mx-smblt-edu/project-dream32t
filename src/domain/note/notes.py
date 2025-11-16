"""A class for storing notes."""

from collections import UserList

from src.domain.note.note import Note
from src.domain.note.topic import Topic


class Notes(UserList[Note]):
    """A class for storing notes."""

    def add(self, note: Note) -> Note | None:
        """
        Adds a note to the data storage if it does not already exist by topic.

        If a note with the same topic already exists in the storage, the method does
        not append the note and returns None. Otherwise, it appends the note and
        returns the added note.

        """
        index_note = self.__index_note(note.topic)
        if index_note is None:
            self.data.append(note)
            return note
        return None

    def remove(self, topic: Topic) -> Note | None:
        """
        Removes a specific note associated with the given topic.

        This method searches for the note corresponding to the provided topic.
        If a note is found, it is removed from the data storage and returned.
        If no matching note is found, the method returns None.
        """
        index_note = self.__index_note(topic)
        if index_note is None:
            return None
        return self.data.pop(index_note)

    def find(self, topic: Topic) -> Note | None:
        """
        Searches for a note related to a given topic.

        This method attempts to locate the note corresponding to the provided topic
        from the internal data storage. If no match is found, it returns None.
        """
        index_note = self.__index_note(topic)
        if index_note is None:
            return None
        return self.data[index_note]

    def __index_note(self, topic: Topic) -> int | None:
        """
        Searches for the index of a note in the list of stored notes.
        """
        for index, item in enumerate(self.data):
            if item.topic == topic:
                return index
        return None
