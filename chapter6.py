import cv2 as cv
import numpy as np


def empty(a):
    pass

img = cv.imread('./Resources/Photos/park.jpg')

# Create trackbars
cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 640, 240)  # The name should be same as that of the namedWindow()
cv.createTrackbar("Hue Minimum", "Trackbars", 10, 179, empty)
cv.createTrackbar("Hue Maximum", "Trackbars", 19, 179, empty)
cv.createTrackbar("Saturation Minimum", "Trackbars", 77, 255, empty)
cv.createTrackbar("Saturation Maximum", "Trackbars", 247, 255, empty)
cv.createTrackbar("Value Minimum", "Trackbars", 60, 255, empty)
cv.createTrackbar("Value Maximum", "Trackbars", 226, 255, empty)

# Color Detection from an image
while True:
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min =cv.getTrackbarPos("Hue Minimum", "Trackbars")
    h_max =cv.getTrackbarPos("Hue Maximum", "Trackbars")
    s_min =cv.getTrackbarPos("Saturation Minimum", "Trackbars")
    s_max =cv.getTrackbarPos("Saturation Maximum", "Trackbars")
    v_min=cv.getTrackbarPos("Value Minimum", "Trackbars")
    v_max =cv.getTrackbarPos("Value Maximum", "Trackbars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(img_hsv, lower, upper)

    img_result = cv.bitwise_and(img, img, mask=mask)

    cv.imshow('Original Image', img)
    cv.imshow('HSV Image', img_hsv)
    cv.imshow('Masked Image', mask)
    cv.imshow('Result Image', img_result)
    stacked_image = np.hstack((img, img_result))
    cv.imshow('Stacked image', stacked_image)
    cv.waitKey(1)
