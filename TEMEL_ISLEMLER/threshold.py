import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = 'media/helicopter2.jpg'
img = cv2.imread(image_path, 0)  # Read the image as grayscale

# Apply global thresholding
ret, th1 = cv2.threshold(img, 150, 200, cv2.THRESH_BINARY)

# Apply adaptive thresholding using mean of neighborhood
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)

# Apply adaptive thresholding using Gaussian-weighted sum of neighborhood
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

# Display the original image and thresholded images
cv2.imshow("Original Image", img)
cv2.imshow("Global Thresholding", th1)
cv2.imshow("Adaptive Thresholding (Mean)", th2)
cv2.imshow("Adaptive Thresholding (Gaussian)", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Explanation:
1. The code begins by importing the necessary libraries, OpenCV (`cv2`), NumPy (`np`), and pyplot submodule from Matplotlib (`plt`).
2. The image path is specified, pointing to the 'helicopter2.jpg' file.
3. The image is loaded using `cv2.imread()` function with the additional argument `0` to read the image as grayscale.
4. Global thresholding is applied using `cv2.threshold()` function, which takes the grayscale image, threshold values (`150` and `200`), and thresholding method (`cv2.THRESH_BINARY`) as arguments. The result is stored in `th1`.
5. Adaptive thresholding using the mean of the neighborhood is applied using `cv2.adaptiveThreshold()` function. It takes the grayscale image, maximum pixel value (`255`), adaptive thresholding method (`cv2.ADAPTIVE_THRESH_MEAN_C`), thresholding type (`cv2.THRESH_BINARY`), block size (`21`), and constant value subtracted from the mean (`2`) as arguments. The result is stored in `th2`.
6. Adaptive thresholding using the Gaussian-weighted sum of the neighborhood is applied similarly to step 5, with the adaptive thresholding method changed to `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`. The result is stored in `th3`.
7. The original image and thresholded images are displayed using `cv2.imshow()`.
8. The program waits for a key press using `cv2.waitKey()`. After the key press, the windows are closed using `cv2.destroyAllWindows()`.
9. The code is executed sequentially, resulting in the display of the original image and different thresholded images using global and adaptive thresholding methods.
'''