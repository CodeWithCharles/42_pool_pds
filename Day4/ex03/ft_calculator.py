class calculator:
    def __init__(self, vector):
        """Initialize the calculator instance with the given vector

        Args:
            vector (_type_): Vector to perform ops on
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds object to each elements of the vector

        Args:
            object (_type_): Object to add"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)


    def __sub__(self, object) -> None:
        """Substracts object to each elements of the vector

        Args:
            object (_type_): Object to substract
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)


    def __mul__(self, object) -> None:
        """Multiplies object with each elements of the vector

        Args:
            object (_type_): Object to mulitply"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)


    def __truediv__(self, object) -> None:
        """Divides object to each elements of the vector

        Args:
            object (_type_): Object to divide with

        Raises:
            ZeroDivisionError: If object is 0"""
        try:
            assert object != 0, "Division by zero is not allowed."
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except Exception as e:
            print(f"{Exception.__name__}: {e}")
