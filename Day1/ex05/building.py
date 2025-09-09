import sys


def analyze_text(text: str) -> None:
    """
    A function that will analyze the text.
    Outputs the result to terminal with this format :
    Prints the following information:
    1. The number of characters in the text
    2. The number of upper case letters
    3. The number of lower case letters
    4. The number of punctuation marks
    5. The number of spaces
    6. The number of digits

    :param str text: The text to analyze
    """
    PUNCTUATION_CHARS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    text_len = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punc_count = sum(1 for char in text if char in PUNCTUATION_CHARS)
    space_count = sum(1 for char in text if char.isspace())
    num_count = sum(1 for char in text if char.isdigit())

    print(f"The text contains {text_len} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punc_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{num_count} digits")


def main():
    """
    Main function. If not argument provided, will prompt the user.
    Will then analyze the text provided.

    :returns: Prints the analysis of the text
    :raises AssertionError: in case more than one argument is given
    """
    try:
        if (len(sys.argv) < 2):
            try:
                s = input("Input text to analyze :\n")
                s += "\n"
            except EOFError:
                sys.exit()
            except KeyboardInterrupt
                sys.exit()
        elif (len(sys.argv) == 2):
            s = sys.argv[1]
        elif (len(sys.argv) > 2):
            raise AssertionError("Too many arguments provided")
        analyze_text(s)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
