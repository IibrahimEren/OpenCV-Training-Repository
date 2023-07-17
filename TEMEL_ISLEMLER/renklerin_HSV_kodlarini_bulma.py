import cv2
import numpy as np

# Open video capture object
cap = cv2.VideoCapture(0)

# Callback function for the trackbar
def nothing(x):
    pass

# Create a named window for the trackbar
cv2.namedWindow("Trackbar")

# Resize the trackbar window
cv2.resizeWindow("Trackbar", 500, 500)

# Create trackbars for lower and upper HSV values
cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)  # Trackbar for lower hue value
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)  # Trackbar for lower saturation value
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)  # Trackbar for lower value value

cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)  # Trackbar for upper hue value
cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)  # Trackbar for upper saturation value
cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)  # Trackbar for upper value value

# Set initial values for upper HSV trackbars
cv2.setTrackbarPos("Upper - H", "Trackbar", 180)
cv2.setTrackbarPos("Upper - S", "Trackbar", 255)
cv2.setTrackbarPos("Upper - V", "Trackbar", 255)

while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame to HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current trackbar positions for lower and upper HSV values
    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")
    
    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")

    # Create lower and upper HSV color arrays
    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    # Create a mask based on the lower and upper HSV values
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

    # Display the original frame and the mask
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Release the video capture object and destroy windows
cap.release()
cv2.destroyAllWindows()

'''
Explanation:
1. The code starts by importing the necessary libraries, `cv2` for OpenCV and `numpy` for numerical operations.
2. A video capture object is created using `cv2.VideoCapture()` to capture video from the default camera.
3. The `nothing()` function is defined as a placeholder callback function for the trackbars.
4. A named window called "Trackbar" is created using `cv2.namedWindow()`.
5. The trackbars for lower and upper HSV values are created using `cv2.createTrackbar()`. The initial values are set to 0 for all trackbars.
6. The initial values for the upper HSV trackbars are set to their maximum values using `cv2.setTrackbarPos()`.
7. Inside the main loop, each frame is read from the video capture using `cap.read()`.
8. The frame is flipped horizontally using `cv2.flip()` to get a mirror-like effect.
9. The frame is converted from the BGR color space to the HSV color space using `cv2.cvtColor()`.
10. The current positions of the trackbars for lower and upper HSV values are obtained using `cv2.getTrackbarPos()`.
11. Lower and upper HSV color arrays are created using `np.array()`.
12. A mask is created using `cv2.inRange()` to filter out pixels that fall within the specified HSV range.
13. The original frame and the mask are displayed using `cv2.imshow()`.
14. If the 'q' key is pressed, the loop breaks and the program exits.
15. The video capture object is released using `cap.release()` and all windows are closed using `cv2.destroyAllWindows()`.
'''