import sys
from ft_filter import ft_filter


def main():
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
