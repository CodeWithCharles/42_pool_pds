from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class describing the King !"""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive=is_alive)

    def set_eyes(self, color: str) -> None:
        """Sets the eye color for the instance

        Args:
            color (str): New color of eyes"""
        self.eyes = color

    def set_hairs(self, color: str) -> None:
        """Sets the hair color for the instance

        Args:
            color (str): New color of hairs"""
        self.hairs = color

    def get_eyes(self) -> str:
        """Gets the color of the eyes"""
        return self.eyes

    def get_hairs(self) -> str:
        """Gets the color of the hairs"""
        return self.hairs
