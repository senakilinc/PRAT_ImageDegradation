import numpy as np
import cv2
import os

def add_salt_and_pepper_noise(image, probability=0.01):
    """
    Adds salt and pepper noise to a grayscale or RGB image.

    Args:
        image (numpy.ndarray): Input image (grayscale or RGB).
        probability (float): Probability of a pixel being altered by noise (value between 0 and 1).

    Returns:
        numpy.ndarray: Noisy image with the same dimensions as the input.
    """
    #downscale_factor = 0.4
    #original_size = (image.shape[1], image.shape[0])  # (width, height)
    #original_shape = image.shape
    #new_size = (int(original_shape[1] * downscale_factor), int(original_shape[0] * downscale_factor))
    #image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
    # Ensure the input image is a NumPy array
    image = image.astype(np.uint8)
    noisy_image = np.copy(image)

    # Generate a random matrix the same size as the image
    random_matrix = np.random.rand(*image.shape[:2])

    # Salt (white pixels)
    noisy_image[random_matrix < (probability / 2)] = 255

    # Pepper (black pixels)
    noisy_image[random_matrix > (1 - probability / 2)] = 0
    #noisy_image = cv2.resize(noisy_image, (original_shape[1], original_shape[0]), interpolation=cv2.INTER_NEAREST)
    return noisy_image
