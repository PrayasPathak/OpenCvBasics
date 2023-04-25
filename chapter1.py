import cv2

print("Package Imported")

# Reading an image

img = cv2.imread('./Resources/Photos/park.jpg')

# Displaying an image
cv2.imshow('Boston Park Image', img)
cv2.waitKey(3000)
