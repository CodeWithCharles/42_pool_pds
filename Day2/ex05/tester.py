from sys import argv
import numpy as np
from PIL import Image
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def main():
    """Takes the file in argument and displays in a graph :
    - Base image
    - Inverted image
    - Red channel image
    - Green channel image
    - Blue channel image
    - Greyscale image
    """

    try:
        if (len(argv) != 2):
            raise AssertionError("Usage: tester.py <path>")
        path = argv[1]
        a1, a2 = ft_load(path, True)
        if not (len(a1) and a2):
            raise AssertionError("Image failed to load")
        array = a1
        img = a2
        print(array)

        for name, func in [
            ("Inverted", ft_invert),
            ("Red", ft_red),
            ("Green", ft_green),
            ("Blue", ft_blue),
            ("Greyscale", ft_grey),
        ]:
            out = func(array)
            print(f"{name} shape: {out.shape}")
        images = [
            ("Base", img),
            ("Inverted", Image.fromarray(ft_invert(array))),
            ("Red", Image.fromarray(ft_red(array))),
            ("Green", Image.fromarray(ft_green(array))),
            ("Blue", Image.fromarray(ft_blue(array))),
            ("Greyscale", Image.fromarray(ft_grey(array))),
        ]
        fig, axs = plt.subplots(2, 3, figsize=(12, 8))

        for ax, (title, data) in zip(axs.flat, images):
            ax.imshow(data)
            ax.set_title(title)
            ax.axis("off")

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Unexpected exception: {e}")


if __name__ == "__main__":
    main()
