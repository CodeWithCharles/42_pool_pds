def ft_filter(function, iterable):
    """ft_filter evaluates the members in iterable through
    the func "function", and returns a list of the members
    matching the function criterias.

    Args:
        function: Function used to evaluate the member
        iterable: List of members to evaluate, must be iterable

    Returns:
        list: A list of the members matching the condition
    """
    if (function is None):
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
