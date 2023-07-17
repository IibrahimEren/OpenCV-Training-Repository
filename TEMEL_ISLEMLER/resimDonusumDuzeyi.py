import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread('media/helicopter.jpeg', 0)

# Downscale the image by a factor of 0.4
down = 0.4
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)

# Get the dimensions of the image
row, col = img.shape

# Define the transformation matrix
M = np.float32([[1, 0, 200], [0, 1, 200]])

# Apply the affine transformation to the image
dst = cv2.warpAffine(img, M, (row, col))

# Display the original and transformed images
cv2.imshow("original", img)
cv2.imshow("dst", dst)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Explanation:
1. The code reads an image in grayscale format using the `cv2.imread` function.
2. The image is then downscaled by a factor of 0.4 using the `cv2.resize` function.
3. The dimensions of the image are obtained using the `shape` attribute.
4. A transformation matrix `M` is defined using `np.float32` to specify the translation values.
5. The `cv2.warpAffine` function is used to apply the affine transformation to the image based on the provided matrix `M`.
6. The original and transformed images are displayed using `cv2.imshow`.
7. The code waits for a key press using `cv2.waitKey(0)` and then closes all windows using `cv2.destroyAllWindows()`.

The purpose of this code is to demonstrate how to apply an affine transformation to an image.
The transformation shifts the image by a specified amount in the x and y directions, 
creating a translated version of the original image.
'''