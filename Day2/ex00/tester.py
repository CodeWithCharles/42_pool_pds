from give_bmi import give_bmi, apply_limit


def test_valid_case():
    """Test give_bmi and apply_limit with valid input data.

    Prints the calculated BMI list and the boolean list returned by apply_limit
    with a limit of 26.
    """
    print("\n--- Test: Valid input case ---")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print("BMI:", bmi, type(bmi))
    print("Apply limit 26:", apply_limit(bmi, 26))


def test_mismatched_lengths():
    """Test give_bmi with height and weight lists of different lengths.

    Expects an AssertionError indicating the arrays must be of the same length.
    """
    print("\n--- Test: Mismatched height/weight lengths ---")
    try:
        give_bmi([1.70, 1.80], [60])
    except AssertionError as e:
        print("Caught expected error:", e)


def test_invalid_height_type():
    """Test give_bmi with invalid types in the height list.

    Expects an AssertionError if any element of height is not int or float.
    """
    print("\n--- Test: Invalid type in height list ---")
    try:
        give_bmi(["1.75", 1.80], [70, 80])  # type: ignore
    except AssertionError as e:
        print("Caught expected error:", e)


def test_invalid_weight_type():
    """Test give_bmi with invalid types in the weight list.

    Expects an AssertionError if any element of weight is not int or float.
    """
    print("\n--- Test: Invalid type in weight list ---")
    try:
        give_bmi([1.75, 1.80], [70, "80"])  # type: ignore
    except AssertionError as e:
        print("Caught expected error:", e)


def test_invalid_bmi_type_in_apply_limit():
    """Test apply_limit with invalid types in the bmi list.

    Expects an AssertionError if any element of bmi is not int or float.
    """
    print("\n--- Test: Invalid type in BMI list for apply_limit ---")
    try:
        apply_limit([22.5, "29.0"], 25)  # type: ignore
    except AssertionError as e:
        print("Caught expected error:", e)


def test_invalid_limit_type():
    """Test apply_limit with an invalid type for the limit parameter.

    Expects an AssertionError if limit is not an int.
    """
    print("\n--- Test: Invalid type for limit ---")
    try:
        apply_limit([22.5, 29.0], "25")  # type: ignore
    except AssertionError as e:
        print("Caught expected error:", e)


def main():
    """Run all tests."""
    test_valid_case()
    test_mismatched_lengths()
    test_invalid_height_type()
    test_invalid_weight_type()
    test_invalid_bmi_type_in_apply_limit()
    test_invalid_limit_type()


if __name__ == "__main__":
    main()
