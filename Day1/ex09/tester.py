from ft_package.utils import count_in_list


def main():
    """Tests the count_in_list function from ft_package
    """
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0


if __name__ == "__main__":
    main()
