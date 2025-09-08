import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words from a string based on length.

    Expects exactly two command-line arguments:
    1. A string containing words separated by spaces.
    2. An integer N.

    The function splits the string into words and filters out those whose
    length is less than or equal to N using a custom filter
    function `ft_filter`.

    Prints the list of words longer than N.

    Raises:
        AssertionError: If the number of arguments is incorrect or if the
                        arguments are not of the expected type
                        (string and digit).
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        S, N = sys.argv[1], sys.argv[2]
        assert isinstance(S, str) and N.isdigit(), "the arguments are bad"
        N = int(N)

        words = S.split()
        # use ft_filter with lambda
        res = list(ft_filter(lambda w: len(w) > N, words))
        print(res)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
