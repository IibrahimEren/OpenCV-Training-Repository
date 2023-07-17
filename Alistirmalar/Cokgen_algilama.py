# Import the OpenCV library
import cv2

# Read the image from the media folder
img = cv2.imread('media/polygons.png')

# Set the font for the text to be added to the image
font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX_SMALL

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image to create a binary image
ret, thresh = cv2.threshold(gray, 230, 260, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop through each contour
for cnt in contours:
    # Approximate the contour with a polygon
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # Draw the approximated polygon on the image
    cv2.drawContours(img, [approx], 0, 0, 2)

    # Get the coordinates of the first point of the polygon
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    # Check the number of vertices of the polygon and add text to the image accordingly
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font1, 1, 0)
    if len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font1, 1, 0)
    if len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font1, 1, 0)
    if len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), font1, 1, 0)
    else:
        cv2.putText(img, "Ellipse", (x, y), font, 1, 0)

# Show the image with the detected polygons and added text
cv2.imshow("polygons", img)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Explanation of each line:

import cv2 - Imports the OpenCV library for image and video processing.
img = cv2.imread('media/polygons.png') - Reads the image "polygons.png" from the file system and assigns it to the variable img.
font = cv2.FONT_HERSHEY_SIMPLEX - Defines the font type for displaying text as FONT_HERSHEY_SIMPLEX.
font1 = cv2.FONT_HERSHEY_COMPLEX_SMALL - Defines a smaller font type for displaying text as FONT_HERSHEY_COMPLEX_SMALL.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) - Converts the image img from BGR color space to grayscale using the cv2.cvtColor() function and assigns it to the variable gray.
ret, thresh = cv2.threshold(gray, 230, 260, cv2.THRESH_BINARY) - Applies thresholding to the grayscale image gray using the cv2.threshold() function. It converts the image into a binary image where pixel values above 230 are set to 260 and pixel values below 230 are set to 0. The resulting binary image is assigned to the variables ret and thresh.
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) - Finds contours in the binary image thresh using the cv2.findContours() function. The contours are retrieved using the RETR_TREE retrieval mode, and the contour approximation method is set to CHAIN_APPROX_SIMPLE. The resulting contours are assigned to the variable contours.
for cnt in contours: - Iterates over each contour in the contours list.
epsilon = 0.01 * cv2.arcLength(cnt, True) - Calculates the approximation accuracy as a fraction (0.01) of the contour perimeter using the cv2.arcLength() function. The perimeter is closed (True) since the contour represents a closed shape. The result is assigned to the variable epsilon.
approx = cv2.approxPolyDP(cnt, epsilon, True) - Approximates the contour cnt with a polygonal curve using the Ramer-Douglas-Peucker algorithm. The approximation accuracy is specified by epsilon, and the resulting polygonal curve is assigned to the variable approx.
cv2.drawContours(img, [approx], 0, 0, 2) - Draws the contour approx on the image img using the cv2.drawContours() function. The contour is represented as a list [approx], and the contour color is set to 0 (black) with a line thickness of 2 pixels.
x = approx.ravel()[0] and y = approx.ravel()[1] - Extracts the x and y coordinates of the first vertex of the polygon by flattening the approx array and accessing the respective elements.
33-39. Determines the shape of the polygon based on the number of vertices (len(approx)) and displays the corresponding shape name at the position (x, y) using the cv2.putText() function.
42-44. Displays the image with labeled polygons in a window titled "polygons" using the cv2.imshow() function.
47-48. Waits for a key press and closes all the open windows using the cv2.waitKey() and cv2.destroyAllWindows() functions, respectively.

"""