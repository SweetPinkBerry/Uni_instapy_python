#Instapy

Instapy is a package for image modification, where you can add a filter (grayscale or sepia), scale the image, and add the filter using an implementation of choice.

##Installation

Instapy required the package manager pip.
It also requires for the user to install the packages:
-Numpy
-openCV
-Numba

This can be done like this:

```python
pip install [package]
```

##Usage

With the required packages available, download the package.

The package must be installed with pip install -e . and virtualenv must be installed and active to access instapy from outside /bin

This is done as follows:

```python
cd ~
pip3 install --user virtualenv
export PATH=$PATH:~/.local/bin
virtualenv -p python3 venv-in3110
source venv-in3110/bin/activate

pip install -e .
```

To use instapy, you apply flags to indicate which function you wish to use.
Instapy comes with the following flags:

-h / --help - lets the user see which flags are available and how to use them
-f FILE / --file FILE - lets the user enter an image to be modified
-se / --sepia - adds the sepia filter to the image
-g / --gray - adds the grayscale filter to the image
NOTE: if the user tries to add both filters, only grayscale will be applied
-sc SCALE / --scale SCALE - lets the user scale the image with a float (decimal) value over 0. The image will be scaled according to the percentage of the inputted value
-i IMPLEMENTATIOM / --implement IMPLEMENTATION - lets the user choose which implementation to run the filter with. The user has the input options "python", "numpy" and "numba"
-o OUT / --out OUT - lets the user add a filename to write the modified image to. If there is no filename added, the modified image won't be created

Example on how to use:

```python
pip install -e .

instapy -h
instapy -f FILE #example.jpg 400x600
instapy -se
instapy -g
instapy -sc SCALE #0.5
instapy -i #python
instapy -o #example_grayscale.jpg

instapy -f example.jpg -g -sc 0.5 -i python -o example_grayscale.jpg #returns grayscale image example_grayscale.jpg with pixels 200x300
```