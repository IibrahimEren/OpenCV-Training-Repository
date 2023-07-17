import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('media/clon.png')

# Split the image into its color channels (BGR)
b, g, r = cv2.split(img)

# Display the original image
cv2.imshow("img", img)

# Plot histograms for each color channel using matplotlib
# ravel() converts the 2D image into a 1D array for easier histogram calculation
# 256 represents the number of bins in the histogram
# [0, 256] defines the range of pixel values to be considered in the histogram (0 to 255)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])

# Show the plotted histograms
plt.show()

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Explanation:

1. Import the necessary libraries: `cv2` for image processing, `numpy` for array operations, and `pyplot` from `matplotlib` for plotting.
2. Read the image using `cv2.imread()` and assign it to the variable `img`.
3. Split the image into its color channels (Blue, Green, Red) using `cv2.split()`. The individual color channels are assigned to variables `b`, `g`, and `r`.
4. Display the original image using `cv2.imshow()`.
5. Plot histograms for each color channel using `plt.hist()`. The `ravel()` function is used to flatten the 2D image arrays into 1D arrays for histogram calculation. The `256` argument specifies the number of bins in the histogram, and `[0, 256]` defines the range of pixel values to be considered in the histogram.
6. Show the plotted histograms using `plt.show()`.
7. Wait for a key press using `cv2.waitKey(0)` and close all open windows using `cv2.destroyAllWindows()`.

This code calculates and displays histograms for each color channel of the image, providing insights into the distribution of pixel values and intensity levels.
'''