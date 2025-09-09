from load_image import ft_load
import numpy as np
import os
import sys


def test_valid_image():
    """Test ft_load with a valid JPG image."""
    print("\n--- Test: Valid image ---")
    try:
        img = ft_load("landscape.jpg")
        if isinstance(img, np.ndarray) and img.size > 0:
            print(f"Image loaded successfully.\n{img}")
        else:
            print("Image failed to load or returned empty array.")
    except Exception as e:
        print(f"Unexpected exception: {e}")


def test_file_not_found():
    """Test ft_load with a non-existent file."""
    print("\n--- Test: File not found ---")
    try:
        ft_load("non_existent.jpg")
    except AssertionError as e:
        print("Caught expected error:", e)


def test_unsupported_extension():
    """Test ft_load with a file that has an unsupported extension."""
    print("\n--- Test: Unsupported file extension ---")
    try:
        ft_load("file.txt")
    except AssertionError as e:
        print("Caught expected error:", e)


def test_invalid_image_file():
    """Test ft_load with a corrupt / non-image file with an image extension."""
    print("\n--- Test: Invalid image content with valid extension ---")
    try:
        dummy_path = "fake_image.jpg"
        with open(dummy_path, "w") as f:
            f.write("This is not an image.")
        ft_load(dummy_path)
    except Exception as e:
        print("Caught expected error:", e)
    finally:
        if os.path.exists(dummy_path):
            os.remove(dummy_path)


def manual_test(path: str):
    """Test ft_load with a manual input."""
    print("\n--- Test: Manual input ---")
    try:
        img = ft_load(path)  # Replace with an actual image in your directory
        if isinstance(img, np.ndarray) and img.size > 0:
            print(f"Image loaded successfully.\n{img}")
        else:
            print("Image failed to load or returned empty array.")
    except Exception as e:
        print(f"Unexpected exception: {e}")


def main():
    """Runs all test cases for ft_load.
    You can specify a path to a file to run a manual test.
    """
    if (len(sys.argv) == 2 and isinstance(sys.argv[1], str)):
        manual_test(sys.argv[1])
    elif (len(sys.argv) == 1):
        test_valid_image()
        test_file_not_found()
        test_unsupported_extension()
        test_invalid_image_file()
    else:
        print("Usage: tester.py [input]")


if __name__ == "__main__":
    main()
