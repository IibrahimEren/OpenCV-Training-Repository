import cv2

img = cv2.imread('media/triangle.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply thresholding to obtain a binary image
_, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)

# Calculate the moments of the binary image
M = cv2.moments(thresh)

# Calculate the centroid coordinates of the shape
X = int(M["m10"] / M["m00"])
Y = int(M["m01"] / M["m00"])

# Draw a circle at the centroid position on the original image
cv2.circle(img, (X, Y), 5, (255, 0, 255), -1)

# Display the image with the centroid circle
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Explanation:
1. The code starts by reading an image using `cv2.imread()` and stores it in the `img` variable.
2. The image is then converted to grayscale using `cv2.cvtColor()` with the `cv2.COLOR_RGB2GRAY` flag.
3. Thresholding is applied to the grayscale image using `cv2.threshold()`. Pixels with intensity values below the threshold (125) are set to 0, and those above the threshold are set to 255, creating a binary image. The threshold value and other parameters are passed as input to the function.
4. The moments of the binary image are calculated using `cv2.moments()`. This function calculates various moments, such as the area, centroid, and spatial moments of the image.
5. The centroid coordinates of the shape are calculated using the spatial moments from the previous step. The x-coordinate is obtained by dividing the "m10" moment by the "m00" moment, and the y-coordinate is obtained by dividing the "m01" moment by the "m00" moment. These values represent the center of mass or centroid of the shape.
6. A circle is drawn at the centroid position on the original image using `cv2.circle()`. The center coordinates (X, Y), radius (5), color (255, 0, 255), and thickness (-1 for a filled circle) are specified.
7. Finally, the image with the centroid circle is displayed using `cv2.imshow()`.
8. The program waits for a key press using `cv2.waitKey(0)`.
9. After the key press, all windows are closed using `cv2.destroyAllWindows()`.

The purpose of this code is to demonstrate the calculation and visualization of the centroid 
of a shape in an image. The code performs image processing steps such as grayscale conversion 
and thresholding to obtain a binary image. Then it calculates the moments of the binary image 
to find the centroid coordinates. The centroid is marked on the original image using a circle,
allowing for visual verification of the centroid position.
'''