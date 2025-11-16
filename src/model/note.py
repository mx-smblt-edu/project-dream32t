"""Provides the Topic class."""

from src.model.content import Content
from src.model.tags import Tags
from src.model.topic import Topic


class Note:
    """Class for storing the note."""

    def __init__(self, topic: Topic, content: Content, tags: Tags = Tags()):
        self.__topic = topic
        self.__content = content
        self.__tags: Tags = tags

    @property
    def topic(self) -> Topic:
        """Getter for the topic of the note."""
        return self.__topic

    @property
    def content(self) -> Content:
        """Getter for the content of the note."""
        return self.__content

    @property
    def tags(self) -> Tags:
        """Getter for the tags of the note."""
        return self.__tags

    def __str__(self):
        if len(self.tags) > 0:
            tags_str = ", ".join([tag.value for tag in self.tags.data])
            return f"Note topic: '{self.topic}', content: '{self.content}', {tags_str}."
        return f"Note topic: '{self.topic}', content: '{self.content}'."

    def __hash__(self) -> int:
        return hash(self.__topic)

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            raise TypeError(f"Cannot compare {self!r} and {other!r}")
        return self.topic == other.topic
