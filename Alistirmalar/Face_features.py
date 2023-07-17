import math
import cv2
import numpy as np


# Callback function for trackbar
def nothing(x):
    pass


# Function to find contour with maximum area
def findMaxContour(contours):
    max_i = 0
    max_area = 0

    for i in range(len(contours)):
        face_area = cv2.contourArea(contours[i])

        if max_area < face_area:
            max_area = face_area
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

# Create trackbars for lower and upper HSV values
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("LS", "Trackbar", 82, 255, nothing)
cv2.createTrackbar("LV", "Trackbar", 54, 255, nothing)
cv2.createTrackbar("UH", "Trackbar", 22, 179, nothing)
cv2.createTrackbar("US", "Trackbar", 200, 255, nothing)
cv2.createTrackbar("UV", "Trackbar", 155, 255, nothing)

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

    # Define lower and upper HSV color thresholds
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
            extBottom = tuple(c[c[:, :, 1].argmax()][0])

            try:
                # Calculate and display the angle
                angle1 = int(math.atan2(extTop[1] - extLeft[1], extTop[0] - extLeft[0]) * 180 / math.pi)
                angle2 = int(math.atan2(extRight[1] - extTop[1], extRight[0] - extTop[0]) * 180 / math.pi)
                angle3 = int(math.atan2(extBottom[1] - extRight[1], extBottom[0] - extRight[0]) * 180 / math.pi)
                angle4 = int(math.atan2(extLeft[1] - extBottom[1], extLeft[0] - extBottom[0]) * 180 / math.pi)
            except:
                angle1, angle2, angle3, angle4 = "<>"
        except:
            # Handle case when no extreme points are found
            pass

    # Draw the contour and extreme points on the frame
    line_color = (255, 255, 0)
    cv2.line(roi, extLeft, extTop, line_color, 2)
    cv2.line(roi, extTop, extRight, line_color, 2)
    cv2.line(roi, extRight, extBottom, line_color, 2)
    cv2.line(roi, extBottom, extLeft, line_color, 2)
    # cv2.drawContours(roi, [c], -1, (0, 255, 255), 2)

    # Draw circles at extreme points
    circle_color = (150, 200, 5)
    cv2.circle(roi, extLeft, 8, circle_color, -1)
    cv2.circle(roi, extRight, 8, circle_color, -1)
    cv2.circle(roi, extTop, 8, circle_color, -1)
    cv2.circle(roi, extBottom, 8, circle_color, -1)

    text_color = (255, 255, 255)
    cv2.putText(roi, str(round(angle1, 1)), (extLeft[0] - 50, extLeft[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                text_color, 2)
    cv2.putText(roi, str(round(angle2, 1)), (extTop[0] + 10, extTop[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                text_color, 2)
    cv2.putText(roi, str(round(angle3, 1)), (extRight[0] + 10, extRight[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                text_color, 2)
    cv2.putText(roi, str(round(angle4, 1)), (extBottom[0] - 40, extBottom[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
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
1. Import the necessary libraries: `math`, `cv2` (OpenCV), and `numpy` (NumPy).

2. Define a callback function `nothing(x)` that does nothing. This function is used as a placeholder for the trackbar callback.

3. Define a function `findMaxContour(contours)` that takes a list of contours and returns the contour with the maximum area. It iterates through the contours, calculates the area of each contour using `cv2.contourArea()`, and keeps track of the contour with the maximum area.

4. Create a video capture object `cap` to capture video from the default camera (index 0).

5. Create a named window "Trackbar" to hold the trackbars.

6. Create six trackbars using `cv2.createTrackbar()` to adjust the lower and upper values for the HSV color thresholds. The trackbars are labeled as "LH" (lower hue), "LS" (lower saturation), "LV" (lower value), "UH" (upper hue), "US" (upper saturation), and "UV" (upper value). The initial values and the range for each trackbar are also specified.

7. Start an infinite loop to continuously read frames from the video capture.

8. Read a frame from the video capture using `cap.read()`. The returned values are stored in `ret` (a boolean indicating if the frame was read successfully) and `frame` (the captured frame).

9. If the frame was not read successfully (i.e., `ret` is 0), break the loop and exit.

10. Flip the frame horizontally using `cv2.flip()` to mirror the frame.

11. Define a region of interest (ROI) by extracting a portion of the frame using array slicing. The ROI is defined as the region between (100, 200) and (350, 400) pixels.

12. Convert the ROI from BGR color space to HSV color space using `cv2.cvtColor()`.

13. Get the current trackbar positions using `cv2.getTrackbarPos()` for each trackbar.

14. Create lower and upper HSV color thresholds using `np.array()` based on the trackbar positions.

15. Create a mask using `cv2.inRange()` to filter out pixels in the HSV image that are within the specified color range.

16. Apply morphological dilation to the mask using `cv2.dilate()` with a kernel size of (3, 3) to reduce noise.

17. Apply median blur to the mask using `cv2.medianBlur()` with a kernel size of 15 to further reduce noise.

18. Find contours in the mask using `cv2.findContours()`. The contours are retrieved along with the hierarchy information.

19. If there are contours found (i.e., `len(contours) > 0`), find the contour with the maximum area using the `findMaxContour()` function.

20. Find the extreme points of the contour using `tuple()` and NumPy array operations. These extreme points represent the corners of the detected shape.

21. Calculate the angles of the sides of the shape by using the `math.atan2()` function and convert the angles from radians to degrees.

22. Draw lines connecting the extreme points on the ROI using `cv2.line()`.

23. Draw circles at the extreme points using `cv2.circle()`.

24. Draw text displaying the calculated angles near each extreme point using `cv2.putText()`.

25. Draw a rectangle around the ROI on the original frame using `cv2.rectangle()`.

26. Display the original frame, ROI, and mask using `cv2.imshow()`.

27. Check for the '

q' key press to exit the loop. If 'q' is pressed, break the loop and exit.

28. Release the video capture object using `cap.release()` to free up resources.

29. Destroy all the windows created using `cv2.destroyAllWindows()`.
------------------------------------------------------------------------------------------------------------------------
1. Calculation of the contour area:
   - In the `findMaxContour()` function, the area of each contour is calculated using the `cv2.contourArea()` function. This function calculates the area enclosed by a contour.
   - The contour with the maximum area is determined by comparing the areas of all the contours and keeping track of the contour index (`max_i`) with the largest area (`max_area`).

2. Calculation of angles:
   - The angles are calculated using the `math.atan2()` function, which calculates the angle between the positive x-axis and the line connecting two points.
   - Four angles are calculated: `angle1`, `angle2`, `angle3`, and `angle4`.
   - `angle1` is the angle between `extLeft` and `extTop`.
   - `angle2` is the angle between `extTop` and `extRight`.
   - `angle3` is the angle between `extRight` and `extBottom`.
   - `angle4` is the angle between `extBottom` and `extLeft`.
   - The calculations are performed using the `math.atan2()` function and converted from radians to degrees using multiplication and division.

These calculations help determine the shape and orientation of the detected object. The contour area provides information about the size of the contour, and the angle calculations give insights into the orientation of the shape's sides.

'''