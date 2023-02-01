#!/usr/bin/env python3

import sys
import cv2
import numpy as np
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


def sepia_filter(image):
    """
    Converts a given image to sepia using numpy.

    Args:
        image (Array): 3D array with image data

    Returns:
        Array: 3D array of the converted image
    """

    #Create empty array
    sepia_image = np.empty(image.shape)

    sepia_matrix = [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]

    #gets bgr on the third plane
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    #create a numpy array and calculate sepia values
    sepia = np.array(sepia_matrix)
    s_b = (sepia[0,0] * b) + (sepia[0,1] * g) + (sepia[0,2] * r)
    s_g = (sepia[1,0] * b) + (sepia[1,1] * g) + (sepia[1,2] * r)
    s_r = (sepia[2,0] * b) + (sepia[2,1] * g) + (sepia[2,2] * r)

    s_b[s_b > 255] = 255
    s_g[s_g > 255] = 255
    s_r[s_r > 255] = 255

    #applies values to pixels
    sepia_image[:,:,0] = s_b
    sepia_image[:,:,1] = s_g
    sepia_image[:,:,2] = s_r

    sepia_image = sepia_image.astype("uint8")

    return sepia_image


if __name__ == "__main__":
    main(sys.argv[1])