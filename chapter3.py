import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/lady.jpg')

# Resizing an image
# In order to resize an image, we need to determine it's size first.
# print(img.shape)  # The output is in the format of result is (height, width, channels for color i.e. (BGR))

img_resize = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))  # (width, height) format
# Here, img.shape[0] means height of image, shape[1] means width of image
cv.imshow('Original Image', img)
cv.imshow('Resized Image', img_resize)

# Cropping an image
img_cropped = img[0:200, 200:500]  # height, width format
cv.imshow('Cropped Image', img_cropped)
cv.waitKey(0)