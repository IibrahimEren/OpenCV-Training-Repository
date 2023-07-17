import cv2

# Load the image
img = cv2.imread('media/clon.png')

# Scaling Down the image 0.2 times specifying a single scale factor
down = 0.4
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)

# Convert the image to RGB color space
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert the image to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the original image in BGR, RGB, HSV, and grayscale formats
cv2.imshow("clon BGR", img)
cv2.imshow("clon RGB", img_rgb)
cv2.imshow("clon HSV", img_hsv)
cv2.imshow("clon GRAY", img_gray)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

'''
Explanation:
1. Import the `cv2` module.
2. Load the image 'media/clon.png' using `cv2.imread`.
3. Scale down the image by a factor of 0.4 using `cv2.resize` with `fx` and `fy` parameters.
4. Convert the image to RGB color space using `cv2.cvtColor` with `cv2.COLOR_BGR2RGB` conversion flag.
5. Convert the image to HSV color space using `cv2.cvtColor` with `cv2.COLOR_BGR2HSV` conversion flag.
6. Convert the image to grayscale using `cv2.cvtColor` with `cv2.COLOR_BGR2GRAY` conversion flag.
7. Display the original image in BGR format using `cv2.imshow` with the window name "clon BGR".
8. Display the image in RGB format using `cv2.imshow` with the window name "clon RGB".
9. Display the image in HSV format using `cv2.imshow` with the window name "clon HSV".
10. Display the image in grayscale format using `cv2.imshow` with the window name "clon GRAY".
11. Wait for a key press using `cv2.waitKey`.
12. Close all windows using `cv2.destroyAllWindows`.

The code demonstrates how to convert an image between different color spaces, including BGR, 
RGB, HSV, and grayscale. The resulting images in each color space are displayed to visualize 
the color transformations.
'''