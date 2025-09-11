import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts image colors (negative effect)

    Args:
        array (np.ndarray): The image array to invert

    Returns:
        np.ndarray: The inverted image array
    """
    return 255 - array  # Uses =, - only


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel

    Args:
        array (np.ndarray): The base image array

    Returns:
        np.ndarray: The array with only the red-channel
    """
    red_img = np.zeros_like(array)
    red_img[..., 0] = array[..., 0]
    return red_img  # Uses = only


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel

    Args:
        array (np.ndarray): The base image array

    Returns:
        np.ndarray: The array with only the green-channel
    """
    green_img = np.zeros_like(array)
    green_img[..., 1] = array[..., 1]
    return green_img  # Uses = only


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel

    Args:
        array (np.ndarray): The base image array

    Returns:
        np.ndarray: The array with only the blue-channel
    """
    blue_img = np.zeros_like(array)
    blue_img[..., 2] = array[..., 2]
    return blue_img  # Uses = only


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts image to grey scale

    Args:
        array (np.ndarray): The base image array

    Returns:
        np.ndarray: The image array to greyscale
    """
    return np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
