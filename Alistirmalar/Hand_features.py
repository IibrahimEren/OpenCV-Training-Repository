import math
import cv2
import numpy as np


# Callback function for trackbar (used for thresholding)
def nothing(x):
    pass


# Function to find contour with maximum area
def findMaxContour(contours):
    max_i = 0
    max_area = 0

    # Iterate through all contours to find the one with maximum area
    for i in range(len(contours)):
        hand_area = cv2.contourArea(contours[i])

        if max_area < hand_area:
            max_area = hand_area
            max_i = i

    try:
        c = contours[max_i]
    except:
        # Handle case when no contours are found
        contours = [0]
        c = contours[0]

    return c


# Open video capture object
cap = cv2.VideoCapture(0)

# Create a named window for the trackbar
cv2.namedWindow("Trackbar")

# Create trackbars for lower and upper HSV values (used for color thresholding)
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)   # Lower hue
cv2.createTrackbar("LS", "Trackbar", 82, 255, nothing)  # Lower saturation
cv2.createTrackbar("LV", "Trackbar", 54, 255, nothing)  # Lower value
cv2.createTrackbar("UH", "Trackbar", 22, 179, nothing)   # Upper hue
cv2.createTrackbar("US", "Trackbar", 200, 255, nothing)  # Upper saturation
cv2.createTrackbar("UV", "Trackbar", 155, 255, nothing)  # Upper value

while True:
    # Read frame from video capture
    ret, frame = cap.read()

    if ret == 0:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Define the region of interest (ROI)
    roi = frame[100:350, 200:400]

    # Convert the ROI to HSV color space
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Get current trackbar positions
    lh = cv2.getTrackbarPos("LH", "Trackbar")
    ls = cv2.getTrackbarPos("LS", "Trackbar")
    lv = cv2.getTrackbarPos("LV", "Trackbar")
    uh = cv2.getTrackbarPos("UH", "Trackbar")
    us = cv2.getTrackbarPos("US", "Trackbar")
    uv = cv2.getTrackbarPos("UV", "Trackbar")

    # Define lower and upper HSV color thresholds based on trackbar positions
    lower_color = np.array([lh, ls, lv])
    upper_color = np.array([uh, us, uv])

    # Create a mask based on the HSV color thresholds
    mask = cv2.inRange(hsv_roi, lower_color, upper_color)

    # Apply dilation to reduce noise
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Apply median blur to further reduce noise
    mask = cv2.medianBlur(mask, 15)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        try:
            # Find contour with maximum area
            c = findMaxContour(contours)

            # Find extreme points of the contour
            extLeft = tuple(c[c[:, :, 0].argmin()][0])
            extRight = tuple(c[c[:, :, 0].argmax()][0])
            extTop = tuple(c[c[:, :, 1].argmin()][0])

            try:
                # Calculate and display the angle of each side
                angle1 = int(math.atan2(extTop[1] - extLeft[1], extTop[0] - extLeft[0]) * 180 / math.pi)
                angle2 = int(math.atan2(extRight[1] - extTop[1], extRight[0] - extTop[0]) * 180 / math.pi)
                angle3 = int(math.atan2(extLeft[1] - extRight[1], extLeft[0] - extRight[0]) * 180 / math.pi)

            except:
                angle1, angle2, angle3 = "<>"
        except:
            # Handle case when no extreme points are found
            pass

    # Draw the contour and extreme points on the ROI
    line_color = (255, 255, 0)
    cv2.line(roi, extLeft, extTop, line_color, 2)
    cv2.line(roi, extTop, extRight, line_color, 2)
    cv2.line(roi, extRight, extLeft, line_color, 2)
    # cv2.drawContours(roi, [c], -1, (0, 255, 255), 2)

    # Draw circles at extreme points
    circle_color = (150, 200, 5)
    cv2.circle(roi, extLeft, 8, circle_color, -1)
    cv2.circle(roi, extRight, 8, circle_color, -1)
    cv2.circle(roi, extTop, 8, circle_color, -1)

    text_color = (255, 255, 255)
    # Display the calculated angle for each side
    cv2.putText(roi, str(round(angle1, 1)), (extLeft[0] - 50, extLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                text_color, 2)
    cv2.putText(roi, str(round(angle2, 1)), (extTop[0] + 10, extTop[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                text_color, 2)
    cv2.putText(roi, str(round(angle3, 1)), (extRight[0] + 10, extRight[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                text_color, 2)

    # Draw a rectangle around the ROI on the original frame
    rectangle_color = (255, 230, 60)
    cv2.rectangle(frame, (200, 100), (400, 350), rectangle_color, 0)

    # Display the original frame, ROI, and mask
    cv2.imshow("Frame", frame)
    cv2.imshow("ROI", roi)
    cv2.imshow("Mask", mask)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy windows
cap.release()
cv2.destroyAllWindows()

'''
1. Import necessary libraries:
   - `math` for mathematical operations.
   - `cv2` for OpenCV functions.
   - `numpy` as `np` for array operations.

2. Define a callback function `nothing()` for the trackbar. This function doesn't perform any operation and acts as a placeholder.

3. Define a function `findMaxContour()` to find the contour with the maximum area:
   - Initialize variables `max_i` and `max_area` to keep track of the contour index and maximum area, respectively.
   - Iterate through all the contours:
     - Calculate the area of each contour using `cv2.contourArea()`.
     - If the current contour's area is greater than the maximum area, update `max_area` and `max_i` with the current values.
   - Return the contour with the maximum area (`c`).

4. Open a video capture object (`cap`) to read frames from the webcam.

5. Create a named window for the trackbar.

6. Create trackbars for the lower and upper HSV values used for color thresholding.

7. Enter a loop to continuously read frames from the video capture object:
   - Read the frame using `cap.read()`.
   - Flip the frame horizontally using `cv2.flip()` to get a mirror image.
   - Define the region of interest (ROI) by selecting a specific area of the frame.
   - Convert the ROI from BGR color space to HSV color space using `cv2.cvtColor()`.
   - Get the current positions of the trackbars using `cv2.getTrackbarPos()`.
   - Define the lower and upper HSV color thresholds based on the trackbar positions.
   - Create a mask based on the HSV color thresholds using `cv2.inRange()`.
   - Apply dilation to reduce noise using a square kernel and `cv2.dilate()`.
   - Apply median blur to further reduce noise using `cv2.medianBlur()`.
   - Find contours in the mask using `cv2.findContours()`.
   - If contours are found:
     - Find the contour with the maximum area using the `findMaxContour()` function.
     - Find the extreme points (left, right, and top) of the contour.
     - Calculate the angles of the sides using `math.atan2()` and convert them from radians to degrees.
   - Draw the contour and extreme points on the ROI using `cv2.line()` and `cv2.circle()`.
   - Display the calculated angles for each side using `cv2.putText()`.
   - Draw a rectangle around the ROI on the original frame using `cv2.rectangle()`.
   - Display the original frame, ROI, and mask using `cv2.imshow()`.
   - Check for the 'q' key press to exit the loop.

8. Release the video capture object and destroy the windows.

This code captures video from the webcam, allows the user to adjust HSV color thresholds using trackbars, 
performs color thresholding, detects contours, finds extreme points of the contour, calculates angles for each side, 
and displays the results in real-time.
------------------------------------------------------------------------------------------------------------------------
1. Finding the contour with maximum area:
   - The `findMaxContour()` function calculates the area of each contour using `cv2.contourArea()` and keeps track of the contour with the maximum area.
   - The contour with the maximum area is determined by comparing the current contour's area with the maximum area stored in the variables `max_area` and `max_i`.

2. Calculating the angles of the sides:
   - The code calculates the angles of each side of the detected hand shape using the `math.atan2()` function.
   - The `atan2()` function takes the y-coordinate difference and the x-coordinate difference between two points and returns the angle in radians.
   - The angles are then converted from radians to degrees by multiplying them with `(180 / math.pi)`.
   - The angles are calculated for the following sides:
     - `angle1`: Angle between the top and left sides of the hand.
     - `angle2`: Angle between the top and right sides of the hand.
     - `angle3`: Angle between the left and right sides of the hand.

These calculations are essential for analyzing the hand shape and determining the angles between the fingers. The 
results are then displayed on the screen using `cv2.putText()` to provide real-time feedback to the user.
'''