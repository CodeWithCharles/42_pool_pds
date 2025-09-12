from ft_calculator import calculator


def main():
    """Tests the ft_calculator class"""
    a: list[float] = [5, 10, 2]  # : list[float] is just for my linter
    b: list[float] = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
