import cv2
import numpy as np
import math

def nothing(x):
    pass

# Open the video capture object to read frames from the default camera (index 0)
vid = cv2.VideoCapture(0)

# Create a named window to display the trackbars
cv2.namedWindow("Trackbar")

# Create trackbars for lower and upper HSV color ranges
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)   # Lower hue trackbar (0-179)
cv2.createTrackbar("LS", "Trackbar", 84, 255, nothing)  # Lower saturation trackbar (0-255)
cv2.createTrackbar("LV", "Trackbar", 20, 255, nothing)  # Lower value trackbar (0-255)
cv2.createTrackbar("UH", "Trackbar", 178, 179, nothing)   # Upper hue trackbar (0-179)
cv2.createTrackbar("US", "Trackbar", 255, 255, nothing)  # Upper saturation trackbar (0-255)
cv2.createTrackbar("UV", "Trackbar", 155, 255, nothing)  # Upper value trackbar (0-255)

while True:
    try:
        # Read a frame from the video capture
        ret, frame = vid.read()

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Create a 3x3 kernel for image dilation
        kernel = np.ones((3, 3), np.uint8)

        # Define a region of interest (ROI) within the frame
        roi = frame[100:300, 100:300]

        # Draw a rectangle on the frame to visualize the ROI
        cv2.rectangle(frame, (100, 100), (300, 300), 255, 0)

        # Convert the ROI from BGR to HSV color space
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Get the current positions of the trackbars
        lh = cv2.getTrackbarPos("LH", "Trackbar")  # Lower hue value
        ls = cv2.getTrackbarPos("LS", "Trackbar")  # Lower saturation value
        lv = cv2.getTrackbarPos("LV", "Trackbar")  # Lower value value
        uh = cv2.getTrackbarPos("UH", "Trackbar")  # Upper hue value
        us = cv2.getTrackbarPos("US", "Trackbar")  # Upper saturation value
        uv = cv2.getTrackbarPos("UV", "Trackbar")  # Upper value value

        # Define lower and upper HSV color thresholds based on trackbar positions
        lower_skin = np.array([lh, ls, lv])
        upper_skin = np.array([uh, us, uv])

        # Create a binary mask based on the color thresholds
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Dilate the mask to fill gaps and remove noise
        mask = cv2.dilate(mask, kernel, iterations=4)

        # Apply Gaussian blur to smoothen the mask
        mask = cv2.GaussianBlur(mask, (5, 5), 100)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Find the contour with the largest area
        cnt_max = max(contours, key=lambda x: cv2.contourArea(x))

        # Calculate the epsilon value for contour approximation
        epsilon = 0.0005 * cv2.arcLength(cnt_max, True)

        # Approximate the contour with fewer points
        approx = cv2.approxPolyDP(cnt_max, epsilon, True)

        # Calculate the convex hull of the contour
        hull = cv2.convexHull(cnt_max)

        # Calculate the area of the convex hull and the contour
        area_hull = cv2.contourArea(hull)
        area_cnt = cv2.contourArea(cnt_max)

        # Calculate the area ratio between the hull and the contour
        area_ratio = ((area_hull - area_cnt) / area_cnt) * 100

        # Compute the convex hull indices for the simplified contour
        hull = cv2.convexHull(approx, returnPoints=False)

        # Calculate the convexity defects of the simplified contour
        defects = cv2.convexityDefects(approx, hull)

        # Initialize finger count
        l = 0

        # Iterate over the convexity defects
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])

            # Calculate the lengths of sides of a triangle formed by the defects
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

            # Calculate the semi-perimeter, area, and depth of the triangle using Heron's formula
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            d = (2 * area) / a

            # Calculate the angle between sides a and b using the law of cosines
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

            # If the angle is less than or equal to 90 degrees and depth is above a certain threshold, increment finger count
            if angle <= 90 and d > 30:
                l += 1
                # Draw a circle at the farthest point
                cv2.circle(roi, far, 3, 255, -1)

            # Draw lines connecting start and end points
            cv2.line(roi, start, end, [100, 0, 100], 2)

        # Increment finger count by 1 to account for the thumb
        l += 1

        # Define the font for displaying text
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Display gesture based on the finger count
        if l == 1:
            if area_cnt < 2000:
                cv2.putText(frame, "elinizi gösterin", (0, 50), font, 2, (50, 50, 200), 1, cv2.LINE_AA)
            else:
                if area_ratio < 12:
                    cv2.putText(frame, "<>", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
                elif area_ratio < 17.5:
                    cv2.putText(frame, "Noice", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
                else:
                    cv2.putText(frame, "1", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
        elif l == 2:
            cv2.putText(frame, "Noice", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
        elif l == 3:
            if area_ratio < 27:
                cv2.putText(frame, "2 + 1", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
        elif l == 4:
            cv2.putText(frame, "2+2/2*2", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
        elif l == 5:
            cv2.putText(frame, "hey", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
        elif l == 6:
            cv2.putText(frame, "<___*__*___>", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "<>", (0, 50), font, 2, (50, 50, 200), 2, cv2.LINE_AA)
    except:
        pass

    # Display the frame and mask
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    # Wait for the ESC key to be pressed to exit the loop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Release the video capture object and destroy all windows
vid.release()
cv2.destroyAllWindows()
'''
```
def nothing(x):
    pass
```
- This line defines an empty function `nothing` that is used as a placeholder for the trackbar callbacks.

```
vid = cv2.VideoCapture(0)
```
- This line initializes the video capture object to read frames from the default camera (index 0).

```
cv2.namedWindow("Trackbar")
```
- This line creates a named window to display the trackbars.

```python
cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("LS", "Trackbar", 84, 255, nothing)
cv2.createTrackbar("LV", "Trackbar", 20, 255, nothing)
cv2.createTrackbar("UH", "Trackbar", 178, 179, nothing)
cv2.createTrackbar("US", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("UV", "Trackbar", 155, 255, nothing)
```
- These lines create trackbars with specific names and initial values in the "Trackbar" window. These trackbars will 
control the lower and upper HSV color thresholds for skin detection.

```
while True:
    try:
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)
```
- This is the start of the main loop that reads frames from the video capture object (`vid.read()`) and flips each frame 
horizontally (`cv2.flip(frame, 1)`).

```
kernel = np.ones((3, 3), np.uint8)
```
- This line creates a 3x3 kernel of ones (`np.ones((3, 3), np.uint8)`) which will be used for image dilation.

```
roi = frame[100:300, 100:300]
cv2.rectangle(frame, (100, 100), (300, 300), 255, 0)
```
- These lines define a region of interest (ROI) by extracting a rectangular portion from the frame 
(`frame[100:300, 100:300]`). They also draw a rectangle on the frame to visualize the ROI using `cv2.rectangle()`.

```
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
```
- This line converts the ROI from the BGR color space to the HSV color space using `cv2.cvtColor()`.

```
lh = cv2.getTrackbarPos("LH", "Trackbar")
ls = cv2.getTrackbarPos("LS", "Trackbar")
lv = cv2.getTrackbarPos("LV", "Trackbar")
uh = cv2.getTrackbarPos("UH", "Trackbar")
us = cv2.getTrackbarPos("US", "Trackbar")
uv = cv2.getTrackbarPos("UV", "Trackbar")
```
- These lines get the current positions of the trackbars using `cv2.getTrackbarPos()`. They store the values in 
variables representing the lower and upper HSV color thresholds.

```
lower_skin = np.array([lh, ls, lv])
upper_skin = np.array([uh, us, uv])
```
- These lines create NumPy arrays representing the lower and upper HSV color thresholds based on the trackbar positions.

```
mask = cv2.inRange(hsv, lower_skin, upper_skin)
mask = cv2.dilate(mask, kernel, iterations=4)
mask = cv2.GaussianBlur(mask, (5, 5), 100)
```
- These lines create a binary mask by thresholding the HSV image using the lower and upper skin color thresholds 
(`cv2.inRange()`). Then, they perform image dilation to fill gaps and remove noise (`cv2.dilate()`). Finally, they apply 
Gaussian blur to smoothen the mask (`cv2.GaussianBlur()`).

```
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt_max = max(contours, key=lambda x: cv2.contourArea(x))
```
- These lines find contours in the mask using `cv2.findContours()`. The contours are retrieved along with the contour
hierarchy. The largest contour with the maximum area is obtained using `max()` and stored in `cnt_max`.

```
epsilon = 0.0005 * cv2.arcLength(cnt_max, True)
approx = cv2.approxPolyDP(cnt_max, epsilon, True)
```
- These lines calculate the epsilon value for contour approximation based on the contour perimeter using 
`cv2.arcLength()`. Then, the contour is approximated with fewer points using the Ramer-Douglas-Peucker algorithm 
(`cv2.approxPolyDP()`), and the simplified contour is stored in `approx`.

```
hull = cv2.convexHull(cnt_max)
area_hull = cv2.contourArea(hull)
area_cnt = cv2.contourArea(cnt_max)
area_ratio = ((area_hull - area_cnt) / area_cnt) * 100
```
- These lines calculate the convex hull of the contour using `cv2.convexHull()`. The area of the hull and the contour 
are calculated using `cv2.contourArea()`. The area ratio between the hull and the contour is computed.

```
hull = cv2.convexHull(approx, returnPoints=False)
defects = cv2.convexityDefects(approx, hull)
```
- These lines compute the convex hull indices for the simplified contour (`cv2.convexHull()`) and calculate the 
convexity defects of the simplified contour (`cv2.convexityDefects()`).

```
l = 0
```
- This line initializes the finger count to zero.

```
for i in range(defects.shape[0]):
```
- This line starts a loop over the number of defects (convexity defects) detected in the hand.

```
    s, e, f, d = defects[i, 0]
    start = tuple(approx[s][0])
    end = tuple(approx[e][0])
    far = tuple(approx[f][0])
```
- These lines extract the defect information for the current iteration. `s` represents the start point index, 
`e` represents the end point index, `f` represents the farthest point index, and `d` represents the approximate distance 
between the contour and the convex hull. They also convert the indices to tuples representing the corresponding points.

```
    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
```
- These lines calculate the lengths of the sides of the triangles formed by the start, end, and far points using the 
Euclidean distance formula.

```
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    d = (2 * area) / 2
```
- These lines calculate the semi-perimeter (`s`) of the triangle, the area of the triangle using Heron's formula, and 
the depth (`d`) of the triangle (half of its area).

```
    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
```
- This line calculates the angle between sides `b` and `c` of the triangle using the Law of Cosines. The angle is 
converted from radians to degrees.

```
    if angle <= 90 and d > 30:
        l += 1
        cv2.circle(roi, far, 3, 255, -1)
    cv2.line(roi, start, end, [100, 0, 100], 2)
```
- If the angle is less than or equal to 90 degrees and the depth is greater than 30, it increments the finger count 
(`l`) by 1 and draws a circle at the farthest point on the ROI. It also draws lines connecting the start and end 
points on the ROI.

```
l += 1
```
- This line increments the finger count by 1 to account for the thumb.

```
font = cv2.FONT_HERSHEY_SIMPLEX
```
- This line defines the font to be used for displaying text.

```
if l == 1:
    # ...
elif l == 2:
    # ...
elif l == 3:
    # ...
elif l == 4:
    # ...
elif l == 5:
    # ...
elif l == 6:
    # ...
else:
    # ...
```
- These lines perform different actions based on the finger count (`l`). They use `cv2.putText()` to display different 
 gesture text on the frame depending on the finger count.

```
cv2.imshow("frame", frame)
cv2.imshow("mask", mask)
```
- These lines display the original frame with gestures and the binary mask on separate windows using `cv2.imshow()`.

```
k = cv2.waitKey(5) & 0xFF
if k == 27:
    break
```
- These lines wait for a key press for 5 milliseconds (`cv2.waitKey(5)`) and check if the pressed key is the "Esc" key 
(ASCII code 27). If so, it breaks the loop and exits the program.

```
vid.release()
cv2.destroyAllWindows()
```
- These lines release the video capture object (`vid.release()`) and destroy all windows (`cv2.destroyAllWindows()`) to
clean up the resources.
'''