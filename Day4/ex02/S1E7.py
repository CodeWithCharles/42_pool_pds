from S1E9 import Character


class Baratheon(Character):
    """Class representing a Character of the Baratheon house"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of a Baratheon character. Calls super().__init__(args)

        Args:
            first_name (str): Name of the Baratheon character
            is_alive (bool, optional): Is the character alive. \
Defaults to True."""
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Override the __str__ attribute

        Returns:
            _type_: Returns a string describing the instance
        """
        return super().__str__()

    def __repr__(self):
        """Override the __repr__ attribute

        Returns:
            _type_: Returns the self.__str__ attribute, describing the instance
        """
        return self.__str__()


class Lannister(Character):
    """Class representing a Character of the Lannister house"""

    def __init__(self, first_name: str = "Lannister", is_alive: bool = True):
        """Constructor of a Lannister character. Calls super().__init__(args)

        Args:
            first_name (str): Name of the Lannister character
            is_alive (bool, optional): Is the character alive. \
Defaults to True."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive: bool = True):
        """Static function, creates a Lannister character instance

        Args:
            first_name (str): Name of the Lannister character
            is_alive (bool, optional): Is the character alive. \
Defaults to True.

        Returns:
            _type_: _description_
        """
        instance = cls(first_name, is_alive)
        return instance

    def __str__(self):
        """Override the __str__ attribute

        Returns:
            _type_: Returns a string describing the instance
        """
        return super().__str__()

    def __repr__(self):
        """Override the __repr__ attribute

        Returns:
            _type_: Returns the self.__str__ attribute, describing the instance
        """
        return self.__str__()
