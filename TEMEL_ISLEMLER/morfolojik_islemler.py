import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('media/helicopter2.jpg', 0)

# Downscale the image by a factor of 0.7 using resize
down = 0.7
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)

# Define a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Perform erosion on the image
erosion = cv2.erode(img, kernel, iterations=1)

# Perform dilation on the image
dilation = cv2.dilate(img, kernel, iterations=5)

# Perform opening morphological operation on the image
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Perform closing morphological operation on the image
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Perform gradient morphological operation on the image
gradiant = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Perform top hat morphological operation on the image
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display the original image and the processed images
cv2.imshow("original", img)
cv2.imshow("erosioned", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gradiant", gradiant)
cv2.imshow("tophat", tophat)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

'''
Explanation:
1. Import the `cv2` and `numpy` modules.
2. Load the image 'media/helicopter2.jpg' in grayscale using `cv2.imread` with `0` flag.
3. Downscale the image by a factor of 0.7 using the `cv2.resize` function.
4. Define a 5x5 kernel using `np.ones` to be used in morphological operations.
5. Perform erosion on the image using `cv2.erode` with the defined kernel and 1 iteration.
6. Perform dilation on the image using `cv2.dilate` with the defined kernel and 5 iterations.
7. Perform opening morphological operation on the image using `cv2.morphologyEx` with `cv2.MORPH_OPEN` as the operation.
8. Perform closing morphological operation on the image using `cv2.morphologyEx` with `cv2.MORPH_CLOSE` as the operation.
9. Perform gradient morphological operation on the image using `cv2.morphologyEx` with `cv2.MORPH_GRADIENT` as the operation.
10. Perform top hat morphological operation on the image using `cv2.morphologyEx` with `cv2.MORPH_TOPHAT` as the operation.
11. Display the original image and the processed images using `cv2.imshow`.
12. Wait for a key press using `cv2.waitKey`.
13. Close all windows using `cv2.destroyAllWindows`.

This code performs various morphological operations such as erosion, dilation, opening, 
closing, gradient, and top hat on an image. The resulting images are displayed to visualize 
the effects of these operations.
'''