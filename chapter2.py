import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/lady.jpg')
# Making a gray scale image
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('Gray Scale Image', img_gray)

# Making a blur of an image with Gaussian Blur Function
img_blur = cv.GaussianBlur(img_gray, (7, 7), 0,)  # Here, (7, 7) is the kernel size for the image
cv.imshow('Original Image', img)
# cv.imshow('Blurred Image', img_blur)


# Edge Detection (Canny Edge Detection)
img_canny = cv.Canny(img, 150, 200)
# cv.imshow('Edged Image', img_canny)

# Image Dilation
kernel = np.ones((5, 5), dtype=np.uint8)
img_dilation = cv.dilate(img_canny, kernel, iterations=5)
cv.imshow('Dilated Image', img_dilation)

# Eroding an image
img_erode = cv.erode(img_dilation, kernel, iterations=5)
cv.imshow('Eroded Image', img_erode)
cv.waitKey(3000)
