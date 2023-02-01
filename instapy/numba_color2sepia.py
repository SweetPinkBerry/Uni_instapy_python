#!/usr/bin/env python3

import sys
import cv2
import numpy as np
from numba import jit
import time

def main(file):
    #Start time of program
    t0 = time.time()

    #Convert image to sepia version
    image = cv2.imread(file)
    sepia_image = sepia_filter(image)

    #End time of program
    t1 = time.time()
    print("Runtime:", t1 - t0)

    #Create image file of scray image
    old_filename = file.split(".")
    new_filename = old_filename[0] + "_sepia." + old_filename[1]
    cv2.imwrite(new_filename, sepia_image)


@jit
def sepia_filter(image):
    """
    Converts a given image to sepia using numba.

    Args:
        image (Array): 3D array with image data

    Returns:
        Array: 3D array of the converted image
    """

    #Create empty array
    sepia_image = np.empty(image.shape)

    sepia_matrix = [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]

    #Change each pixel to sepia
    for x in range (0, image.shape[0]):
        for y in range (0, image.shape[1]):
            (b, g, r) = image[x][y]

            s_b = (sepia_matrix[0][0] * b) + (sepia_matrix[0][1] * g) + (sepia_matrix[0][2] * r)
            s_g = (sepia_matrix[1][0] * b) + (sepia_matrix[1][1] * g) + (sepia_matrix[1][2] * r)
            s_r = (sepia_matrix[2][0] * b) + (sepia_matrix[2][1] * g) + (sepia_matrix[2][2] * r)

            if s_b > 255:
                s_b = 255
            if s_g > 255:
                s_g = 255
            if s_r > 255:
                s_r = 255

            sepia_image[x][y] = (s_b, s_g, s_r)

    sepia_image = sepia_image.astype(np.uint8)

    return sepia_image


if __name__ == "__main__":
    main(sys.argv[1])