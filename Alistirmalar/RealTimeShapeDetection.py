import cv2
import numpy as np


# Callback function for trackbars (does nothing)
def nothing(x):
    pass


# Create a video capture object
cap = cv2.VideoCapture(0)

# Create a window to display trackbars for settings
cv2.namedWindow("Settings")

# Create trackbars for lower and upper HSV values
cv2.createTrackbar("Lower-Hue", "Settings", 0, 180, nothing)
cv2.createTrackbar("Lower-Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Lower-Value", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Hue", "Settings", 0, 180, nothing)
cv2.createTrackbar("Upper-Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Value", "Settings", 0, 255, nothing)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if ret == 0:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current trackbar positions for lower and upper HSV values
    lH = cv2.getTrackbarPos("Lower-Hue", "Settings")
    lS = cv2.getTrackbarPos("Lower-Saturation", "Settings")
    lV = cv2.getTrackbarPos("Lower-Value", "Settings")
    uH = cv2.getTrackbarPos("Upper-Hue", "Settings")
    uS = cv2.getTrackbarPos("Upper-Saturation", "Settings")
    uV = cv2.getTrackbarPos("Upper-Value", "Settings")

    # Create lower and upper color bounds based on trackbar values
    lower_color = np.array([lH, lS, lV])
    upper_color = np.array([uH, uS, uV])

    # Create a binary mask using color thresholding
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Create a kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Erode the mask to remove noise
    mask = cv2.erode(mask, kernel)

    # Find contours in the binary mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over contours and approximate shapes
    for cnt in contours:
        # Calculate contour area
        area = cv2.contourArea(cnt)

        # Approximate contour shape
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # Get the x and y coordinates of the first point in the approximated contour
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # Draw contours and display shape names
        if area > 400:  # It's returns Overload exceptions on bright zones
            try:
                cv2.drawContours(frame, [approx], 0, (255, 255, 255), 5)
                if len(approx) == 3:
                    cv2.putText(frame, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, (0, 0, 0))
                elif len(approx) == 4:
                    cv2.putText(frame, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, (0, 0, 0))
                elif len(approx) == 5:
                    cv2.putText(frame, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, (0, 0, 0))
                elif len(approx) == 6:
                    cv2.putText(frame, "Hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, (0, 0, 0))
            except:
                print("Overload Exception")

    # Display the frame with contours and shape names
    cv2.imshow("frame", frame)

    # Display the binary mask
    cv2.imshow("mask", mask)

    # Check for key press and break loop if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()

"""
Explanation of each line:

1. `import cv2`: This imports the OpenCV library, which provides various computer vision functionalities, 
including image and video processing.

2. `import numpy as np`: This imports the NumPy library, which is used for numerical computations. In this code, 
NumPy is used to create arrays for color thresholding.

3. `def nothing(x)`: This is a placeholder function that does nothing. It is used as a callback function for the 
trackbars created later in the code.

4. `cap = cv2.VideoCapture(0)`: This initializes a video capture object to access the default camera (index 0) or any 
connected camera. It will be used to read frames from the camera.

5. `cv2.namedWindow("Settings")`: This creates a named window called "Settings" that will be used to display 
trackbars for adjusting color threshold values.

6. `cv2.createTrackbar(trackbarName, windowName, value, count, onChange)`: This creates a trackbar within a window. 
It allows the user to interactively adjust a specific value. In this code, six trackbars are created to control the 
lower and upper HSV (Hue, Saturation, Value) values for color thresholding.

   - Trackbar names:
     - "Lower-Hue"
     - "Lower-Saturation"
     - "Lower-Value"
     - "Upper-Hue"
     - "Upper-Saturation"
     - "Upper-Value"
   
   - Window name: "Settings"
   - Initial value: 0
   - Maximum value: Count (180 for Hue, 255 for Saturation and Value)
   - onChange: Callback function (in this code, it is set to `nothing`)

7. The `while True:` loop is the main loop of the program that continuously reads frames from the camera and performs 
the following operations:

   - `ret, frame = cap.read()`: This reads a frame from the video capture object `cap`. The return value `ret` 
   indicates whether the frame was successfully read, and `frame` contains the captured image.
   
   - `frame = cv2.flip(frame, 1)`: This flips the frame horizontally using the `flip` function. It is commonly used 
   to mirror the captured image if needed.
   
   - `hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`: This converts the BGR image (`frame`) to the HSV color space 
   using the `cvtColor` function. HSV is often used for color thresholding because it separates color information 
   into hue, saturation, and value components.
   
   - The next few lines retrieve the current trackbar positions for lower and upper HSV values using 
   `cv2.getTrackbarPos` and store them in variables `lH`, `lS`, `lV`, `uH`, `uS`, `uV`.
   
   - `lower_color = np.array([lH, lS, lV])` and `upper_color = np.array([uH, uS, uV])`: These lines create NumPy 
   arrays to define the lower and upper bounds of the color range based on the trackbar values.
   
   - `mask = cv2.inRange(hsv, lower_color, upper_color)`: This applies color thresholding to the HSV image using the 
   lower and upper color bounds. It creates a binary mask where white pixels represent the colors within the 
   specified range, and black pixels represent the colors outside the range.
   
   - `kernel = np.ones((5, 5), np.uint8)`: This creates a 5x5 rectangular kernel using NumPy. It will

 be used for morphological operations like erosion.
   
   - `mask = cv2.erode(mask, kernel)`: This performs erosion on the mask image using the specified kernel. Erosion 
   helps remove noise and refine the binary mask.
   
   - `contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)`: This finds contours in the 
   binary mask image using the `findContours` function. Contours are the boundaries of connected components in the 
   image.
   
   - The code then loops over each contour and performs the following operations: - Calculates the contour area using 
   `cv2.contourArea`. - Approximates the contour shape using the Ramer-Douglas-Peucker algorithm with an epsilon 
   value of 0.02 times the contour perimeter using `cv2.approxPolyDP`. - Extracts the x and y coordinates of the 
   first point in the approximated contour. - Checks the area of the contour and draws the contour and displays the 
   corresponding shape name on the frame if the area is greater than 400.
   
   - `cv2.imshow("frame", frame)`: This displays the original frame with drawn contours and shape names.
   
   - `cv2.imshow("mask", mask)`: This displays the binary mask image.
   
   - `if cv2.waitKey(5) & 0xFF == ord("q"):`: This waits for a key press for 5 milliseconds. If the pressed key is 
   "q", it breaks out of the while loop and ends the program.
   
8. `cap.release()`: This releases the video capture object, allowing the camera resources to be freed.
   
9. `cv2.destroyAllWindows()`: This closes all windows created by OpenCV.

This code essentially captures video from a camera, applies color thresholding based on the trackbar values, 
detects contours, approximates their shapes, and displays the results in real-time.


"""