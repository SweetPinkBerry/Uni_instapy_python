#!/usr/bin/env python3

import cv2
import sys
from instapy import numpy_color2gray
from instapy import numpy_color2sepia

def grayscale_image(input_filename, output_filename=None):
    """
    Takes an image and returns a grayscale array.
    Should a filename be added, the grayscale array will be stored with the name.
    
    Args:
        image (Array): 3D array with image data
        (optional) filename (String): Filename for returned image

    Returns:
        Array: 2D array of the converted image
        (optional) image: Converted image
    """

    image = cv2.imread(input_filename)
    image = numpy_color2gray.grayscale_filter(image)

    #Create image if a filename has been added
    if output_filename:
        cv2.imwrite(output_filename, image)

    return image

def sepia_image(input_filename, output_filename=None):
    """
    Takes an image and returns a sepia array.
    Should a filename be added, the sepia array will be stored with the name.
    
    Args:
        image (Array): 3D array with image data
        (optional) filename (String): Filename for returned image

    Returns:
        Array: 3D array of the converted image
        (optional) image: Converted image
    """

    image = cv2.imread(input_filename)
    image = numpy_color2sepia.sepia_filter(image)

    #Create image if a filename has been added
    if output_filename:
        cv2.imwrite(output_filename, image)

    return image