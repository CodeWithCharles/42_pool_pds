import sys
from Loading import ft_tqdm
from tqdm import tqdm


def main():
    """
    Tests the ft_tqdm progress bar against tqdm for visual comparison.

    Expects:
        A single command-line argument:
            - An integer > 0 (used as the max range for iteration)

    Runs:
        - ft_tqdm over range(0, arg)
        - tqdm over range(0, arg)

    Raises:
        AssertionError if:
            - No argument or more than one is provided
            - Argument is not a positive integer

    Displays:
        Progress bars from both ft_tqdm and tqdm to standard output.
    """
    try:
        if (len(sys.argv) != 2):
            raise AssertionError("bad argument: tester.py <max_range: int>")

        max_range = 0
        try:
            max_range = int(sys.argv[1])
        except ValueError:
            raise ValueError("bad argument: max_range must be an int")

        if max_range <= 0:
            raise AssertionError("bad argument: must be positive non-null")

        for _ in ft_tqdm(range(0, max_range)):
            pass
        for _ in tqdm(range(0, max_range)):
            pass

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
