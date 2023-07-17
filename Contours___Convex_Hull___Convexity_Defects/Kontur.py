import cv2

# Read the image
img = cv2.imread('media/contour1.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain a binary image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

# Display the image with contours
cv2.imshow("contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
``` 
img = cv2.imread('media/contour1.png')
```
This line reads an image file named 'contour1.png' and stores it in the variable `img`.

``` 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
This line converts the image from BGR (Blue-Green-Red) color space to grayscale using the `cvtColor` function. Grayscale images have only one channel representing the intensity values.

``` 
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```
This line applies thresholding to the grayscale image using the `threshold` function. Pixels with intensity values greater than 127 are set to 255 (white), and the rest are set to 0 (black). The thresholded image is stored in the variable `thresh`.

``` 
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```
This line finds contours in the thresholded image using the `findContours` function. It returns a list of contours and a hierarchy. The contour retrieval mode is set to `RETR_TREE`, which retrieves all contours and reconstructs the full hierarchy of nested contours. The contour approximation method is set to `CHAIN_APPROX_SIMPLE`, which compresses horizontal, vertical, and diagonal segments into their endpoints.

``` 
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
```
This line draws the contours on the original image using the `drawContours` function. It takes the original image (`img`), the list of contours, contour index (-1 for all contours), the color of the contours (in BGR format), and the thickness of the contour lines.

``` 
cv2.imshow("contours", img)
```
This line displays the image with the contours in a window titled "contours" using the `imshow` function.

```
cv2.waitKey(0)
cv2.destroyAllWindows()
```
These lines wait for a key press and then close all windows when a key is pressed. They are used to keep the image window open until a key is pressed, allowing the user to view the image.
'''