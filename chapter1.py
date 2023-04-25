import cv2

# print("Package Imported")

# Reading an image

# img = cv2.imread('./Resources/Photos/park.jpg')

# Displaying an image
# cv2.imshow('Boston Park Image', img)


# Importing a video

# capture = cv2.VideoCapture('./Resources/Videos/dog.mp4')  # Imports the video

# while True:
    # success, img = capture.read()
    # Captures the image into the img variable, and stores the result as true/false in success variable
    # cv2.imshow('Captured Video', img)

#     Adding Delay to exit the loop
#     if cv2.waitKey(5000) and 0xFF == ord('d'):
#         break

# capture.release()  # Releases the video capture pointer

# Accessing the webcam
capture = cv2.VideoCapture(0)
capture.set(3, 640)   # Here, 3 is the id for width
capture.set(4, 480)   # Here, 4 is the id for height
capture.set(10, 100)  # Here, 10 is the id for brightness.
while True:
    success, img = capture.read()
    cv2.imshow('WebCam Capture', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
