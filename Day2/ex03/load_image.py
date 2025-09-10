from typing import Tuple, Optional
from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> Tuple[np.ndarray, Optional[Image.Image]]:
    """Load an image and print its shape

    Args:
        path (str): Path to the image

    Raises:
        AssertionError: - File not found
            - Unsupported extension. Has to be jpg, jpeg, png, gif,\
 bmp, tiff, or ico
            - Failed to load image
    Returns:
        Tuple[np.ndarray,Optional[Image.Image]]: (pixels array, image object\
or None on error)
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
        if (img is None):
            raise AssertionError("Failed to load image.")
        print(f"The shape of the image is: \
({img.size[0]},{img.size[1]},{img.layers})")  # type: ignore
        return np.array(img), img
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
        return np.ndarray([]), None
