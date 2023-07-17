import cv2
import numpy as np

# Load the input images
img_filter = cv2.imread("media/cupcakes.jpg")  # Load the image to be filtered
img_median = cv2.imread("media/noisycupcakes.jpg")  # Load the noisy image

# Downscale the images
down = 0.4  # Scale factor for downscaling
img_filter = cv2.resize(img_filter, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)  # Downscale the filtered image
img_median = cv2.resize(img_median, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)  # Downscale the noisy image

# Apply different blur filters
blur = cv2.blur(img_filter, (5, 5))  # Apply a simple averaging blur filter to the filtered image
blur2 = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)  # Apply a Gaussian blur filter to the filtered image
blur_m = cv2.medianBlur(img_median, 5)  # Apply a median blur filter to the noisy image (the second argument must be an odd number)

# Display the images
cv2.imshow("original", img_median)  # Display the original noisy image
cv2.imshow("blur", blur)  # Display the image filtered with the simple averaging blur
cv2.imshow("blur2", blur2)  # Display the image filtered with the Gaussian blur
cv2.imshow("median", blur_m)  # Display the image filtered with the median blur

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Explanation of each line:

import cv2 - Imports the OpenCV library for image processing.
import numpy as np - Imports the NumPy library for numerical operations.
img_filter = cv2.imread("media/cupcakes.jpg") - Loads the image named "cupcakes.jpg" to be filtered.
img_median = cv2.imread("media/noisycupcakes.jpg") - Loads the noisy image named "noisycupcakes.jpg".
down = 0.4 - Specifies the scaling factor for downscaling the images.
img_filter = cv2.resize(img_filter, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR) - Downscales the filtered image using the specified scaling factor.
img_median = cv2.resize(img_median, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR) - Downscales the noisy image using the specified scaling factor.
blur = cv2.blur(img_filter, (5, 5)) - Applies a simple averaging blur filter with a kernel size of 5x5 to the filtered image.
blur2 = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT) - Applies a Gaussian blur filter with a kernel size of 5x5 to the filtered image.
blur_m = cv2.medianBlur(img_median, 5) - Applies a median blur filter with a kernel size of 5x5 to the noisy image.
cv2.imshow("original", img_median) - Displays the original noisy image in a window titled "original".
cv2.imshow("blur", blur) - Displays the image filtered with the simple averaging blur in a window titled "blur".
cv2.imshow("blur2", blur2) - Displays the image filtered

"""