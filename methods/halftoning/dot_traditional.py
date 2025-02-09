import numpy as np
from PIL import Image, ImageDraw
import cv2

def dot_halftoning(image, cell_size=32, max_radius_factor=1.0, non_linear=False):
    """
    Applies dot-based halftoning to a grayscale image.

    Args:
        image (numpy.ndarray): Grayscale input image (values in 0–255).
        cell_size (int): Size of each halftoning cell.
        max_radius_factor (float): Factor to scale the maximum dot radius.
        non_linear (bool): Apply a non-linear intensity transformation.

    Returns:
        numpy.ndarray: Halftoned image.
    """
    # Ensure the input is grayscale
    if len(image.shape) != 2:
        raise ValueError("Input image must be grayscale.")

    height, width = image.shape
    halftoned_image = np.ones_like(image, dtype=np.uint8) * 255  # White background

    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            # Extract the current cell
            cell = image[y:y + cell_size, x:x + cell_size]

            # Compute the average intensity of the cell
            intensity = np.mean(cell)

            # Calculate the radius based on intensity
            max_radius = (cell_size // 2) * max_radius_factor
            if non_linear:
                radius = (1 - (intensity / 255) ** 2) * max_radius
            else:
                radius = (1 - intensity / 255) * max_radius

            # Ensure the radius is non-negative
            radius = max(0, int(round(radius)))

            # Determine the center of the circle
            center_x = x + cell_size // 2
            center_y = y + cell_size // 2

            # Draw the circle if the radius is greater than 0
            if radius > 0:
                cv2.circle(halftoned_image, (center_x, center_y), radius, 0, -1)  # Black dot

    return halftoned_image