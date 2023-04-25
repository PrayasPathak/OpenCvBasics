import cv2 as cv
import numpy as np

# Joining Images
img = cv.imread('./Resources/Photos/cat.jpg')

# Numpy horizontal and vertical stack function
horizontal = np.hstack((img, img))
vertical = np.vstack((img, img))
cv.imshow('Original Image', img)
cv.imshow('Horizontal Stacking', horizontal)
cv.imshow('Vertical Stacking', vertical)

# The Drawbacks of this method is as follows:
# 1. Image Resizing is not possible
# 2. Both images must have the same color channel.
cv.waitKey(0)
