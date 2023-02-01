#!/usr/bin/env python3

import sys
import cv2
import numpy as np
from numba import jit
import time

def main(file):
    #Start time of program
    t0 = time.time()

    #Convert image to grayscale version
    image = cv2.imread(file)
    gray_image = grayscale_filter(image)

    #End time of program
    t1 = time.time()
    print("Runtime:", t1 - t0)

    #Create image file of scrayscale image
    old_filename = file.split(".")
    new_filename = old_filename[0] + "_grayscale." + old_filename[1]
    cv2.imwrite(new_filename, gray_image)


@jit
def grayscale_filter(image):
    """
    Converts a given image to grayscale using numba decoration jit.

    Args:
        image (Array): 3D array with image data

    Returns:
        Array: 2D array of the converted image
    """

    #Create empty array
    gray_image = np.empty(image.shape[:2])

    #Change each pixel to grayscale
    for x in range (0, image.shape[0]):
        for y in range (0, image.shape[1]):
            (b, g, r) = image[x][y]
            weigth = (b * 0.07) + (g * 0.72) + (r * 0.21)
            gray_image[x][y] = weigth

    gray_image = gray_image.astype(np.uint8)

    return gray_image


if __name__ == "__main__":
    main(sys.argv[1])