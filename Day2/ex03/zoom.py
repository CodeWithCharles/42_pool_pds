from sys import argv
from PIL import Image
import numpy as np
import os
from load_image import ft_load
import matplotlib.pyplot as plt

def main():
    """Loads an image, zoom on it and displays it.
    If no arguments are given, will default to animal.jpeg
    """
    try:
        path = "animal.jpeg"
        if (len(argv) == 2):
            path = argv[1]
        array: np.ndarray
        img: Image.Image
        a1, a2 = ft_load(path)
        if (len(a1) and a2):
            array = a1
            img = a2
        print(array)
        zoomed_image = img.crop((400, 100, 800, 500))
        _, ext = os.path.splitext(path)
        zoomed_image.save(f"zoomed_image{ext}")
        print(f"New shape after cropping: {zoomed_image.size}")

        grayscale_img = zoomed_image.convert("L")
        print(np.array(grayscale_img))

        plt.imshow(zoomed_image)
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"Unexpected exception: {e}")


if __name__ == "__main__":
    main()
