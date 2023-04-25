import cv2 as cv
import numpy as np

# Creating a blank image
blank_image = np.zeros((512, 512, 3), np.uint8)  # Creates a blank image with BGR Color Channel.

# cv.imshow('Blank Image', blank_image)
blank_image[:] = 255, 0, 0
# Here, list slicing is done to fill the image with color.
# cv.imshow('Blue Filled Image', blank_image)

# Creating a line
cv.line(blank_image, (0, 0), (blank_image.shape[1], blank_image.shape[0]), (255, 255, 255), thickness=5)
# cv.imshow('Line Image', blank_image)

# Drawing a rectangle
cv.rectangle(blank_image, (100, 200), (300, 460), (0, 255, 0), cv.FILLED)
# cv.imshow('Rectangle', blank_image)

#  Drawing a circle
cv.circle(blank_image, (200, 350), 80, (255, 190, 154), cv.FILLED)
# cv.imshow('Circle', blank_image)

# Putting a text on image
cv.putText(blank_image, 'Open CV Basics', (130, 450), cv.FONT_HERSHEY_COMPLEX, 1, (220, 245, 230), 3)
# Syntax: (image_name, 'Text', (start_X, start_Y), cv.FONT_FAMILY, scale, color(BGR), thickness)
cv.imshow('Text On Image', blank_image)
cv.waitKey(0)
