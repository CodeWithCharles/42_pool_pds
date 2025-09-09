import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Display the shape of the family list truncates it & print the new shape.

    Args:
        family (list): Array to truncate
        start (int): Start index for truncation
        end (int): End index for truncation

    Raises:
        AssertionError: Input is not composed of a list and 2 integers
        AssertionError: Sub-arrays in input does not have same sizes

    Returns:
        list: A list matching the slice
    """
    try:
        if not isinstance(family, list) \
             or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Sub-arrays in input must have same sizes")
        print(f"My shape is : {np.array(family).shape}")
        print(f"my new shape is : {np.array(family)[start:end+1].shape}")
        return np.array(family)[start:end].tolist()
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
