from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from sys import argv
import os


def crop_image(image: Image.Image) -> Image.Image:
    """Crops an image to a square

    Args:
        image (Image.Image): The image to crop

    Returns:
        Image.Image: The cropped image
    """
    # crop_size = min(image.height // 1.5, image.width // 1.5)
    # crop_left = (image.width // 1.5 - crop_size) // 2
    # crop_top = (image.height // 1.5 - crop_size) // 2
    # crop_right = crop_left + crop_size
    # crop_bottom = crop_top + crop_size
    return image.crop((400, 100, 800, 500))


def transpose_image(image: Image.Image) -> Image.Image:
    """Transpose an image, rotating it 90 degree

    Args:
        image (Image.Image): The image to transpose

    Returns:
        Image.Image: The transposed image
    """
    src_pixels = image.load()
    width, height = image.size
    rotated_image = Image.new("RGB", (height, width))
    dst_pixels = rotated_image.load()

    if (src_pixels and dst_pixels):
        for y in range(height):
            for x in range(width):
                dst_pixels[y, width - 1 - x] = src_pixels[x, y]

    return rotated_image if rotated_image and dst_pixels else image


def main():
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
        cropped_image = crop_image(img)
        _, ext = os.path.splitext(path)
        cropped_image.save(f"cropped_image{ext}")
        a1, a2 = ft_load(f"cropped_image{ext}", True)

        if (len(a1) and a2):
            array = a1
            img = a2
        transposed_image = transpose_image(img)

        plt.imshow(transposed_image)
        plt.title("Transposed Image")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"Unexpected exception: {e}")


if __name__ == "__main__":
    main()
