import cv2
import numpy as np

# Read the input images
img1 = cv2.imread("media/puppy.jpg", 0)  # Read the first image (grayscale)
template = cv2.imread("media/puppy_paws.jpg", 0)  # Read the template image (grayscale)

# Get the width and height of the template image
w, h = template.shape[::-1]

# Perform template matching using the TM_CCOEFF_NORMED method
result = cv2.matchTemplate(img1, template, cv2.TM_CCOEFF_NORMED)

# Find the locations where the template matches with high similarity (threshold = 0.99)
locations = np.where(result >= 0.99)

# Draw rectangles around the matched locations on the original image
for point in zip(*locations[::-1]):
    cv2.rectangle(img1, point, (point[0] + w, point[1] + h), 255, 2)

cv2.imshow("dog", img1)  # Display the original image with rectangles
cv2.imshow("template", template)  # Display the template image
cv2.imshow("result", result)  # Display the result of template matching

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
```
img1 = cv2.imread("media/puppy.jpg", 0)
template = cv2.imread("media/puppy_paws.jpg", 0)
```
Here, we read the two input images, "puppy.jpg" and "puppy_paws.jpg", using the `cv2.imread()` function. The second argument `0` specifies that the images should be loaded in grayscale.

```
w, h = template.shape[::-1]
```
We obtain the width (`w`) and height (`h`) of the template image using its shape. The `[::-1]` indexing is used to 
reverse the order of dimensions, as `shape` returns the number of rows and columns, but we need width and height.

```
result = cv2.matchTemplate(img1, template, cv2.TM_CCOEFF_NORMED)
```
This line performs template matching using the `cv2.matchTemplate()` function. It takes the input image `img1`, template 
image `template`, and the method `cv2.TM_CCOEFF_NORMED` as arguments. The method `cv2.TM_CCOEFF_NORMED` calculates the 
correlation coefficient between the template and image regions. The function returns a result map indicating the similarity 
between the template and different regions of the input image.

```
locations = np.where(result >= 0.99)
```
Here, we use `np.where()` to find the locations in the result map where the similarity is greater than or equal to 0.99. 
This line returns a tuple of arrays representing the row and column indices of the matched locations.

```
for point in zip(*locations[::-1]):
    cv2.rectangle(img1, point, (point[0] + w, point[1] + h), 255, 2)
```
This `for` loop iterates over the matched locations obtained from the `zip(*locations[::-1])` expression. It unpacks the 
`locations` tuple and iterates over the x and y coordinates of each match. For each match, a rectangle is drawn on the 
`img1` image using the `cv2.rectangle()` function. The `point` represents the top-left corner of the rectangle, and 
`(point[0] + w, point[1] + h)` represents the bottom-right corner. The color `(255)` and thickness `2` arguments are 
used to specify the color and thickness of the rectangle.

```
cv2.imshow("dog", img1)
cv2.imshow("template", template)
cv2.imshow("result", result)
```
These lines display the original image (`img1`), template image (`template`), and the result of template matching 
(`result`) using the `cv2.imshow()` function. The first argument is the window name, and the second argument is the 
corresponding image.

```
cv2.waitKey(0)
cv2.destroyAllWindows()
```
The `cv2.waitKey(0)` function waits for a key press and returns the key code. Here, we pass `0` as the argument to wait 
indefinitely until a key is pressed. The `cv2.destroyAllWindows()` function is used to close all open windows after the 
execution of the program.
'''
