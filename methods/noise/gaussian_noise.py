import numpy as np
import cv2
import os

def add_gaussian_noise(image, mean=0, stddev=25):
    """
    Adds Gaussian noise to a grayscale or RGB image.

    Args:
        image (numpy.ndarray): Input image (grayscale or RGB).
        mean (float): Mean of the Gaussian distribution.
        stddev (float): Standard deviation of the Gaussian distribution.

    Returns:
        numpy.ndarray: Noisy image with the same dimensions as the input.
    """
    #downscale_factor = 0.1
    #original_size = (image.shape[1], image.shape[0])  # (width, height)
    #original_shape = image.shape
    #new_size = (int(original_shape[1] * downscale_factor), int(original_shape[0] * downscale_factor))
    #image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

    # Ensure the input image is a NumPy array
    image = image.astype(np.float32)

    # Generate Gaussian noise
    noise = np.random.normal(mean, stddev, image.shape)

    # Add the noise to the image
    noisy_image = image + noise

    # Clip the pixel values to stay in the valid range [0, 255]
    noisy_image = np.clip(noisy_image, 0, 255)
    #noisy_image = cv2.resize(noisy_image, (original_shape[1], original_shape[0]), interpolation=cv2.INTER_NEAREST)
    return noisy_image.astype(np.uint8)
