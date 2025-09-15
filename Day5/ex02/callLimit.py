from typing import Callable, TypeVar, Any
F = TypeVar("F", bound=Callable[..., Any])


def callLimit(limit: int) -> Callable[[F], F]:
    """Decorator factory that limits the number of times a function\
can be called.

    Args:
        limit (int): Maximum number of allowed calls to the decorated function.

    Returns:
        Callable[[Callable[..., Any]], Callable[..., Any]]: A decorator that
        enforces the call limit.
    """
    count = 0

    def callLimiter(function: F) -> F:
        """Decorator that wraps a function and enforces the call limit.

        Args:
            function (Callable[..., Any]): Function to decorate.

        Returns:
            Callable[..., Any]: Wrapped function with call limit enforcement.
        """
        def limit_function(*args: Any, **kwargs: Any) -> Any:
            """Call the wrapped function if limit not exceeded; otherwise,\
raise an error.

            Args:
                *args: Positional arguments to pass to the wrapped function.
                **kwargs: Keyword arguments to pass to the wrapped function.

            Returns:
                Any: Result of the wrapped function if within call limit.

            Raises:
                AssertionError: If the function is called more than `limit`\
times.
            """
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwargs)
            else:
                e = AssertionError(f"{function} call too many times")
                print("Error:", e)

        return limit_function  # type: ignore
    return callLimiter
