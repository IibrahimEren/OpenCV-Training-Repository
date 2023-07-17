import cv2
import numpy as np

# Function used as a placeholder for the trackbar callback function
def nothing(x):
    pass

# Open the video file for capturing frames
cap = cv2.VideoCapture('media/eraser.mp4')

# Create a window for trackbars
cv2.namedWindow("Trackbar")

# Create trackbars for setting lower and upper HSV values
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)  # Lower Hue 97
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)  # Lower Saturation 106
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)  # Lower Value 74
cv2.createTrackbar("UH", "Trackbar", 179, 179, nothing)  # Upper Hue 179
cv2.createTrackbar("US", "Trackbar", 255, 255, nothing)  # Upper Saturation 255
cv2.createTrackbar("UV", "Trackbar", 255, 255, nothing)  # Upper Value 255

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the video has ended, restart from the beginning
    if ret == 0:
        cap = cv2.VideoCapture('media/eraser.mp4')
        ret, frame = cap.read()

    # Resize the frame to the desired size
    frame = cv2.resize(frame, (320, 240))

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the current positions of the trackbars
    lh = cv2.getTrackbarPos("LH", "Trackbar")  # Lower Hue
    ls = cv2.getTrackbarPos("LS", "Trackbar")  # Lower Saturation
    lv = cv2.getTrackbarPos("LV", "Trackbar")  # Lower Value
    uh = cv2.getTrackbarPos("UH", "Trackbar")  # Upper Hue
    us = cv2.getTrackbarPos("US", "Trackbar")  # Upper Saturation
    uv = cv2.getTrackbarPos("UV", "Trackbar")  # Upper Value

    # Define the lower and upper HSV values based on trackbar positions
    lower_blue = np.array([lh, ls, lv])
    upper_blue = np.array([uh, us, uv])

    # Create a mask using the defined lower and upper HSV values
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, the mask, and the result
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(20) & 0XFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
