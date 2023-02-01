#!/usr/bin/env python3

import sys
import cv2
import numpy as np
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


def grayscale_filter(image):
    """
    Converts a given image to grayscale using numpy.

    Args:
        image (Array): 3D array with image data

    Returns:
        Array: 2D array of the converted image
    """

    #Create empty array
    gray_image = np.empty(image.shape[:2])

    #gets bgr on the third plane
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]
    #calculates weigth
    weigth = (b * 0.07) + (g * 0.72) + (r * 0.21)
    gray_image[:,:] = weigth

    gray_image = gray_image.astype("uint8")

    return gray_image


if __name__ == "__main__":
    main(sys.argv[1])