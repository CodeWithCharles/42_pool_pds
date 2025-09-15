from typing import Callable, TypeVar
T = TypeVar("T", int, float)


def square(x: T) -> T:
    """Compute the square of a number.

    Args:
        x (int | float): The number to square.

    Returns:
        int | float: The square of `x`.
    """
    return x * x


def pow(x: T) -> T:
    """Compute the number raised to the power of itself.

    Args:
        x (int | float): The base and exponent.

    Returns:
        int | float: The value of `x` raised to the power of `x`.
    """
    return x ** x


def outer(x: T, function: Callable[[T], T]) -> Callable[[], T]:
    """Create a closure that applies a function to a variable and updates it.

    Args:
        x (int | float): Initial value to pass to `function`.
        function (Callable[[int | float], int | float]): Function to apply.

    Returns:
        Callable[[], int | float]: A function that, when called, applies\
`function`
        to the current value of `x`, updates `x`, and returns the result.
    """

    def inner() -> T:
        """Apply the outer function to `x`, update `x`, and return result.

        Returns:
            int | float: Result of applying `function` to current `x`.
        """
        nonlocal x
        result = function(x)
        x = result
        return result

    return inner
