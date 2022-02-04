# Libraries needed
from math import ceil, floor
import cv2
import numpy as np

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    h, w, c = image.shape

    # calculate the ratio of the width and construct the
    # dimensions
    r = width / float(w)
    dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

# Read the image using imread function
image = cv2.imread('image.png')
print(image.shape)

resized_image = image_resize(image, 299, 299)

# Calculate dominant color of the image
data = np.reshape(resized_image, (-1,3))
print(data.shape)
data = np.float32(data)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness,labels,centers = cv2.kmeans(data,1,None,criteria,10,flags)

dominant = centers[0].astype(np.int32)
temp = [ int(i) for i in dominant ]


# Add padding to the image
h, w, _ = resized_image.shape

top = 0 
bottom = 0
left = 0
right = 0

# Find top and bottom border
if h != 299:
    remainder = 299 - h
    top = ceil(remainder / 2)
    bottom = floor(remainder / 2)
# Eoi

# Find left and right border
if w != 299:
    remainder = 299 - w
    left = ceil(remainder / 2)
    right = floor(remainder / 2)
# Eoi

image_with_padding = cv2.copyMakeBorder(resized_image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=temp)

print(image_with_padding.shape)


cv2.imwrite("padding.png", image_with_padding)


# Resize => rescale, o transformación de algebra lineal
# Rellenar faltante de la imagen con padding, pixeles con el color promedio de la imagen
# Montar un microservicio con resize y otro con rescale