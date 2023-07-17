import cv2
import numpy as np


def on_trackbar(val):
    # Callback function for trackbar
    th = cv2.getTrackbarPos("Threshold", "img-th1")  # Get the threshold value from the trackbar
    maxval = cv2.getTrackbarPos("Maxval", "img-th1")  # Get the maximum value from the trackbar

    # Apply thresholding to the image
    ret, th1 = cv2.threshold(img, th, maxval, cv2.THRESH_BINARY)

    # Display the original image and thresholded image
    cv2.imshow("original", img)
    cv2.imshow("img-th1", th1)


# Load the image as grayscale
img = cv2.imread('media/helicopter2.jpg', 0)

# Create a named window for displaying the thresholded image
cv2.namedWindow("img-th1")

# Create trackbars for threshold and maxval
cv2.createTrackbar("Threshold", "img-th1", 50, 255, on_trackbar)
cv2.createTrackbar("Maxval", "img-th1", 150, 255, on_trackbar)

# Call the trackbar callback function to initialize the thresholding
on_trackbar(0)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

'''
Explanation:
1. The code begins by importing the necessary libraries, OpenCV (`cv2`) and NumPy (`np`).
2. A callback function `on_trackbar` is defined to handle changes in the trackbar values. It takes a single argument `val`, which represents the current trackbar value.
3. Inside the `on_trackbar` function, the threshold value and maximum value are retrieved using `cv2.getTrackbarPos()` function based on the trackbar names specified in `cv2.createTrackbar()`.
4. The `cv2.threshold()` function is used to apply thresholding to the grayscale image (`img`). The threshold value and maximum value are passed as arguments, along with the thresholding method (`cv2.THRESH_BINARY`).
5. The original image (`img`) and thresholded image (`th1`) are displayed using `cv2.imshow()` function.
6. In the main part of the code, the image is loaded as grayscale using `cv2.imread()`.
7. A named window ("img-th1") is created for displaying the thresholded image.
8. Two trackbars are created using `cv2.createTrackbar()`, one for the threshold value and the other for the maximum value. The initial values, minimum value, maximum value, and the callback function (`on_trackbar`) are specified.
9. The `on_trackbar` function is called initially with `0` as the argument to set the initial thresholding.
10. The program waits for a key press using `cv2.waitKey()`.
11. After the key press, all windows are closed using `cv2.destroyAllWindows()`.

The purpose of this code is to demonstrate the use of trackbars in OpenCV for interactive 
thresholding. The user can adjust the threshold and maximum values using the trackbars, and 
the thresholding result is updated in real-time. The original image and the thresholded image 
are displayed side by side, allowing the user to visually observe the effect of changing the 
threshold parameters.
'''