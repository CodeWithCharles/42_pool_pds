import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Computes a BMI list from height and weight list

    Args:
        height (list[int  |  float]): Height (m)
        weight (list[int  |  float]): Weight (kg)

    Raises:
        AssertionError: Height and weight are different size
        AssertionError: Height contains an element that is not int or float
        AssertionError: Weight contains an element that is not int or float

    Returns:
        list[int | float]: The list of computed BMIs
    """
    if (len(height) != len(weight)):
        raise AssertionError("Height and weight arrays must be of same length")
    if not all(isinstance(h, (int, float)) for h in height):
        raise AssertionError("Height must only contain ints or floats")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise AssertionError("Weight must only contain ints or floats")

    bmi = np.array(weight) / (np.array(height) ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit on a list of BMIs.

    Args:
        bmi (list[int  |  float]): The BMI list
        limit (int): The BMI limit

    Raises:
        AssertionError: Limit is not an integer
        AssertionError: BMI contains an element that is not int or float

    Returns:
        list[bool]: List of boolean whose index correspond to a BMI.
                    If a BMI is over limit, True, else, False
    """
    if not isinstance(limit, int):
        raise AssertionError("Limit must be an integer")

    if not all(isinstance(b, (int, float)) for b in bmi):
        raise AssertionError("BMI must only contain ints or floats")

    return [b > limit for b in bmi]
