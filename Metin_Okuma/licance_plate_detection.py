import cv2
import numpy as np
import pytesseract
import imutils

# Load the image
img = cv2.imread('media/licence_plate2.jpg')

# Resize the image
# This will reduce the size of the image, which will make face detection faster.
down = 0.8
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a bilateral filter to smooth the image
# This will help to remove noise and make the edges of the license plate clearer.
d = 8
sigmaColor = 100
sigmaSpace = 200
filtered = cv2.bilateralFilter(gray, d, sigmaColor, sigmaSpace)

# Apply Canny edge detection to find the edges of the license plate
edged = cv2.Canny(filtered, 30, 150)

# Find all the contours in the image
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Keep only the largest 10 contours
cnts = imutils.grab_contours(contours)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

# Initialize a variable to store the license plate contour
screen = None

# Iterate over the contours and find the one that is a rectangle
for c in cnts:
    epsilon = 0.018 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4:
        # This is a rectangle!
        screen = approx
        break

# Create a mask that only shows the license plate area
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)
new_img = cv2.bitwise_and(img, img, mask=mask)

# Find the coordinates of the top-left and bottom-right corners of the license plate
(x, y) = np.where(mask == 255)
top_x, top_y = np.min(x), np.min(y)
bottom_x, bottom_y = np.max(x), np.max(y)

# Crop the license plate from the image
crop = gray[top_x:bottom_x + 1, top_y:bottom_y + 1]

# Use Tesseract to recognize the text in the license plate
text = pytesseract.image_to_string(crop, lang="eng")

# Print the detected text
print(f"detected text = {text}")

# Show the cropped license plate
cv2.imshow("crop", crop)

# Wait for the user to press a key
cv2.waitKey(0)

# Close all the windows
cv2.destroyAllWindows()

'''
```
import cv2
import numpy as np
import pytesseract
import imutils
```
- Import the required libraries: `cv2` for OpenCV, `numpy` for array operations, `pytesseract` for text recognition, 
and `imutils` for convenience functions.

```
img = cv2.imread('media/licence_plate2.jpg')
```
- Load the image of the license plate.

```
down = 0.8
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)
```
- Resize the image to a smaller size. This helps to speed up processing.

```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
- Convert the image to grayscale.

```
d = 8
sigmaColor = 100
sigmaSpace = 200
filtered = cv2.bilateralFilter(gray, d, sigmaColor, sigmaSpace)
```
- Apply a bilateral filter to the grayscale image. This helps to smooth the image while preserving the edges of the 
license plate.

```
edged = cv2.Canny(filtered, 30, 150)
```
- Apply Canny edge detection to find the edges of the license plate.

```
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
```
- Find all the contours in the edge-detected image using `cv2.findContours` function.
- Use `imutils.grab_contours` function to extract the actual contours from the result.
- Keep only the largest 10 contours based on their area.

```
screen = None
for c in cnts:
    epsilon = 0.018 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) == 4:
        screen = approx
        break
```
- Iterate over the contours and find the one that is a rectangle.
- Use the Ramer-Douglas-Peucker algorithm to approximate the contour with fewer points.
- Check if the approximated contour has four points, indicating a rectangle. If so, assign it to the `screen` variable.

```
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [screen], 0, (255, 255, 255), -1)
new_img = cv2.bitwise_and(img, img, mask=mask)
```
- Create a mask that only shows the area of the license plate using the `screen` contour.
- Apply the mask to the original image using `cv2.bitwise_and` function.

```
(x, y) = np.where(mask == 255)
top_x, top_y = np.min(x), np.min(y)
bottom_x, bottom_y = np.max(x), np.max(y)
crop = gray[top_x:bottom_x + 1, top_y:bottom_y + 1]
```
- Find the coordinates of the top-left and bottom-right corners of the license plate in the mask.
- Extract the corresponding region from the grayscale image.

```
text = pytesseract.image_to_string(crop, lang="eng")
```
- Use Tesseract OCR (`pytesseract`) to recognize the text in the license plate image.

```
print(f"detected text = {text}")
```
- Print the detected text.

```
cv2.imshow("crop", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- Display the cropped license plate image.
- Wait for a key press.
- Close all windows.

This code loads an image of a license plate, processes it to find the license plate area, crops the license plate, 
and performs text recognition on the cropped image using Tesseract OCR. The detected text is then printed, and the 
cropped license plate image is displayed.
'''
