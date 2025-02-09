import numpy as np
import cv2
import os

def floyd_steinberg_halftoning(image, block_size=8):
    """
    Applies Floyd-Steinberg error diffusion halftoning with enhanced visibility for a newspaper-style effect.

    Args:
        image (numpy.ndarray): Grayscale input image.
        block_size (int): Size of the grid for coarser halftone visibility.

    Returns:
        numpy.ndarray: Halftoned binary image.
    """
    # Ensure the image is a NumPy array and in float format for processing
    image = image.astype(np.float32)
    height, width = image.shape

    # Create the output halftoned image
    halftoned_image = np.zeros_like(image, dtype=np.uint8)

    # Process the image in blocks
    for y_start in range(0, height, block_size):
        for x_start in range(0, width, block_size):
            # Define the block region
            block_end_y = min(y_start + block_size, height)
            block_end_x = min(x_start + block_size, width)
            block = image[y_start:block_end_y, x_start:block_end_x]

            # Apply Floyd-Steinberg error diffusion within the block
            for y in range(block.shape[0]):
                for x in range(block.shape[1]):
                    old_pixel = block[y, x]
                    new_pixel = 255 if old_pixel > 127 else 0
                    halftoned_image[y_start + y, x_start + x] = new_pixel
                    error = old_pixel - new_pixel

                    # Distribute error to neighboring pixels in the block
                    if x + 1 < block.shape[1]:  # Right
                        block[y, x + 1] += error * (7 / 16)
                    if y + 1 < block.shape[0]:  # Bottom
                        if x > 0:  # Bottom-left
                            block[y + 1, x - 1] += error * (3 / 16)
                        block[y + 1, x] += error * (5 / 16)  # Bottom-center
                        if x + 1 < block.shape[1]:  # Bottom-right
                            block[y + 1, x + 1] += error * (1 / 16)

    return halftoned_image