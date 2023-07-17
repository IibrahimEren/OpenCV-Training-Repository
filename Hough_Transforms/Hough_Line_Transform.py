import cv2
import numpy as np

# Load the image
img = cv2.imread('media/h_line.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection to find edges in the grayscale image
edges = cv2.Canny(gray, 80, 200)
# The Canny edge detection algorithm detects edges in an image using gradient information.
# The second and third arguments specify the lower and upper thresholds for edge detection.

# Apply probabilistic Hough transform to detect lines in the edge image
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=200)
# The HoughLinesP function applies a probabilistic Hough transform to detect lines in an edge image.
# The second argument is the distance resolution in pixels.
# The third argument is the angle resolution in radians.
# The fourth argument is the minimum number of votes (threshold) required to consider a line.
# The maxLineGap parameter specifies the maximum allowed gap between line segments to link them as a single line.

# Iterate over the detected lines and draw them on the original image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    # Draws a line segment on the original image using the starting and ending points of the line.

# Display the grayscale image, edge image, and the original image with the detected lines
cv2.imshow("gray", gray)
cv2.imshow("edges", edges)
cv2.imshow("img", img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

``` 
import cv2
import numpy as np

img = cv2.imread('media/h_line.png')
```

- Import the required libraries: `cv2` for OpenCV and `numpy` for array operations.
- Load the image using `cv2.imread`, specifying the path to the image file.

``` 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

- Convert the loaded image from BGR color space to grayscale using `cv2.cvtColor` function.

``` 
edges = cv2.Canny(gray, 80, 200)
```

- Apply the Canny edge detection algorithm to the grayscale image using `cv2.Canny` function.
- The second and third arguments represent the lower and upper thresholds for edge detection.

``` 
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=200)
```

- Apply the probabilistic Hough transform to detect lines in the edge image using `cv2.HoughLinesP` function.
- The second argument is the distance resolution in pixels.
- The third argument is the angle resolution in radians.
- The fourth argument is the minimum number of votes (threshold) required to consider a line.
- The `maxLineGap` parameter specifies the maximum allowed gap between line segments to link them as a single line.

``` 
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
```

- Iterate over the detected lines and draw them on the original image using `cv2.line` function.
- Extract the starting and ending points of each line and draw a line segment on the image.

``` 
cv2.imshow("gray", gray)
cv2.imshow("edges", edges)
cv2.imshow("img", img)
```

- Display the grayscale image, edge image, and the original image with the detected lines using `cv2.imshow`.

``` 
cv2.waitKey(0)
cv2.destroyAllWindows()
```

- Wait for a key press using `cv2.waitKey(0)`.
- Close all windows using `cv2.destroyAllWindows` to clean up resources and close the program properly.

This code performs edge detection on the grayscale image using the Canny algorithm, applies the probabilistic Hough transform to detect lines in the edge image, and draws the detected lines on the original image. The resulting grayscale image, edge image, and the original image with the detected lines are displayed.
'''