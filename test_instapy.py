import pytest
import importlib
import cv2
import numpy as np
from random import seed
from random import randint

def test_import():
    import instapy
    from instapy.python_color2gray import grayscale_filter
    from instapy.python_color2sepia import sepia_filter
    from instapy.numpy_color2gray import grayscale_filter
    from instapy.numpy_color2sepia import sepia_filter
    from instapy.numba_color2gray import grayscale_filter
    from instapy.numba_color2sepia import sepia_filter

@pytest.mark.parametrize("implementation", ("python", "numpy", "numba"))
def test_grayscale(implementation):
    mod = importlib.import_module(f"instapy.{implementation}_color2gray")
    grayscale_image = getattr(mod, "grayscale_filter")
    image = cv2.imread("rain.jpg")
    result = grayscale_image(image)
    assert (len(image.shape) - len(result.shape)) == 1
    seed(1)
    row = randint(0, image.shape[0] - 1)
    seed(2)
    col = randint(0, image.shape[1] - 1)
    test = image[row][col]
    (b, g, r) = test
    weigth = (b * 0.07) + (g * 0.72) + (r * 0.21)
    test = weigth
    assert result[row][col] == int(test)
    

@pytest.mark.parametrize("implementation", ("python", "numpy", "numba"))
def test_sepia(implementation):
    mod = importlib.import_module(f"instapy.{implementation}_color2sepia")
    sepia_image = getattr(mod, "sepia_filter")
    image = cv2.imread("rain.jpg")
    result = sepia_image(image)
    seed(1)
    row = randint(0, image.shape[0] - 1)
    seed(2)
    col = randint(0, image.shape[1] - 1)
    test = image[row][col]
    (b, g, r) = test
    s_b = (b * 0.272) + (g * 0.534) + (r * 0.131)
    s_g = (b * 0.349) + (g * 0.686) + (r * 0.168)
    s_r = (b * 0.393) + (g * 0.769) + (r * 0.189)
    if s_b > 255:
        s_b = 255
    if s_g > 255:
        s_g = 255
    if s_r > 255:
        s_r = 255
    test = (int(s_b), int(s_g), int(s_r))
    assert (result[row][col][0] == int(s_b)) and (result[row][col][1] == int(s_g)) and (result[row][col][2] == int(s_r))