import cv2
import numpy as np

# Load the images
img1 = cv2.imread('media/coin.png')
img2 = cv2.imread('media/balls.png')

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# Apply a median blur to the images
blur1 = cv2.medianBlur(gray1, 5)
blur2 = cv2.medianBlur(gray2, 5)

# Detect circles in the images
circles1 = cv2.HoughCircles(blur1, cv2.HOUGH_GRADIENT, 1, img1.shape[0] / 2, param1=200, param2=10, minRadius=40,
                            maxRadius=50)
circles2 = cv2.HoughCircles(blur2, cv2.HOUGH_GRADIENT, 1, img1.shape[0] / 3, param1=200, param2=10, minRadius=40,
                            maxRadius=42)

# Check if any circles were detected
if circles1 is not None:
    # Convert the circles to integers
    circles1 = np.uint16(np.around(circles1))

    # Draw the circles on the image
    for i in circles1[0, :]:
        cv2.circle(img1, (i[0], i[1]), i[2], (0, 0, 255), 2)

if circles2 is not None:
    circles2 = np.uint16(np.around(circles2))

    for i in circles2[0, :]:
        cv2.circle(img2, (i[0], i[1]), i[2], (0, 0, 255), 2)

# Display the images
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

"""
Explanation of each lines

import cv2 imports the OpenCV library.
import numpy as np imports the NumPy library.
img1 = cv2.imread('media/coin.png') loads the image coin.png into the variable img1.
gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY) converts the image img1 to grayscale.
blur1 = cv2.medianBlur(gray1, 5) applies a median blur to the image gray1.
circles1 = cv2.HoughCircles(blur1, cv2.HOUGH_GRADIENT, 1, img1.shape[0] / 2, param1=200, param2=10, minRadius=40, maxRadius=50) detects circles in the image blur1.
if circles1 is not None: checks if any circles were detected.
circles1 = np.uint16(np.around(circles1)) converts the circles to integers.
for i in circles1[0, :] iterates over the circles.
cv2.circle(img1, (i[0], i[1]), i[2], (0, 0, 255), 2) draws a circle on the image img1 at the coordinates (i[0], i[1]) with radius i[2].
cv2.imshow("img1", img1) displays the image img1.
cv2.waitKey(0) waits for a key press.
cv2.destroyAllWindows() closes all windows.

"""