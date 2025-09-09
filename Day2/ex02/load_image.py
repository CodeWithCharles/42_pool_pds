from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """Load an image and prints its shape

    Args:
        path (str): Path to the image

    Raises:
        AssertionError: File not found
        AssertionError: Unsupported extension. Has to be jpg, jpeg, png, gif,\
            bmp, tiff, or ico

    Returns:
        np.ndarray: Empty if error or image pixels
    """
    image_ext = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".ico"}
    try:
        if not os.path.exists(path):
            raise AssertionError(f"File not found: {path}")
        _, ext = os.path.splitext(path)
        if not ext.lower() in image_ext:
            supported_ext = ', '.join(image_ext)
            raise AssertionError(f"Unsupported file extension. \
                                  Supported: {supported_ext}")
        img = Image.open(path)
        print(f"The shape of the image is: \
({img.size[1]},{img.size[0]},{img.layers})")  # type: ignore
        return np.array(img)
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
        return np.ndarray([])
