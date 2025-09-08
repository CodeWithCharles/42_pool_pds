import sys


def convert_to_morse(text: str) -> str:
    MORSE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    morse_text = []
    for char in text.upper():
        if char in MORSE_DICT:
            morse_text.append(MORSE_DICT[char])
        else:
            raise AssertionError("Unrecognized char: {}".format(char))
    return ' '.join(morse_text)


def main():
    try:
        if (len(sys.argv) != 2 or len(sys.argv[1]) == 0 or
        not isinstance(sys.argv[1], str)):
            raise AssertionError("Usage: sos.py \"<text>\"")
        input_text = sys.argv[1]
        result = convert_to_morse(input_text)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
