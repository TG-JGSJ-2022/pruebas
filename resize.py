# let's start with the Imports 
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
image = cv2.imread('image.jpeg')
print(image.shape)

resized_image = image_resize(image, 299, 299)
print(resized_image.shape)
cv2.imwrite("resized.jpg", resized_image)


# Resize => rescale, o transformación de algebra lineal
# Rellenar faltante de la imagen con padding, pixeles con el color promedio de la imagen
# Montar un microservicio con resize y otro con rescale