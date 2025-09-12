from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character"""

    @abstractmethod
    def __init__(self, first_name: str,
                 family_name: str,
                 is_alive: bool = True):
        """Character's constructor

        Args:
            first_name (str): Name of the character
            is_alive (bool, optional): Is the character alive. \
Defaults to True."""
        self.first_name: str = first_name
        self.is_alive: bool = is_alive
        self.family_name: str = family_name
        self.eyes: str
        self.hairs: str

    def die(self):
        """Changes is_alive to False"""
        self.is_alive = False

    def __str__(self):
        """Override the __str__ attribute

        Returns:
            _type_: Returns a string describing the instance
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Override the __repr__ attribute

        Returns:
            _type_: Returns the self.__str__ attribute, describing the instance
        """
        return self.__str__()


class Stark(Character):
    """Class representing a Character of the Stark house"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of a stark character. Calls super().__init__(args)

        Args:
            first_name (str): Name of the stark character
            is_alive (bool, optional): Is the character alive. \
Defaults to True."""
        super().__init__(first_name, "Stark", is_alive)
