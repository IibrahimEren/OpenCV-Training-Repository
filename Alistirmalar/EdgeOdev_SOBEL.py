import cv2
import numpy as np

# <editor-fold decs= "SOBEL">
# Load the image
image = cv2.imread('image/gul.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Sobel operator
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
sobel = np.sqrt(sobelx ** 2 + sobely ** 2)


# Function to apply thresholding to the Sobel image
def apply_threshold(threshold):
    # Threshold the Sobel image to create a binary image
    _, edges = cv2.threshold(sobel, threshold, 255, cv2.THRESH_BINARY)

    # Find the contours in the binary image
    contours, _ = cv2.findContours(edges.astype(np.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create a copy of the original image
    result = image.copy()

    # Draw the largest contour (boundary) on the image
    if len(contours) > 0:
        cv2.drawContours(result, [max(contours, key=cv2.contourArea)], -1, (102, 0, 0), 3)

        # Create a mask with the same size as the image
        '''''
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        redMask = cv2.inRange(hsv, lower_red, upper_red)

        image[np.where(redMask == 255)] = [0, 255, 0]

        cv2.imshow("redMask",image)
        '''''
        mask = np.zeros_like(image[:, :, 0])
        # Fill the area inside the boundary with white color
        cv2.fillPoly(mask, [max(contours, key=cv2.contourArea)], 255)

        # Change the color of the region inside the boundary >> WHite To Blue
        result[np.where(mask == 255)] = [255, 0, 0]

        # Make the background black
        result[np.where(mask == 0)] = [0, 0, 0]



    # Resize the images
    scale_percent = 60  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Resize The Result
    scale_percent = 60  # percent of original size
    width = int(result.shape[1] * scale_percent / 100)
    height = int(result.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_result = cv2.resize(result, dim, interpolation=cv2.INTER_AREA)

    # Tresult = 0.5
    # Timage = 1- alpha
    # trans = cv2.addWeighted(resized_image,alpha,resized_result,beta,0)

    # Show the images
    # cv2.imshow("mask", mask)
    cv2.imshow("Image", resized_image)
    cv2.imshow('Result', resized_result)
    # cv2.imshow("trans",trans)


# Create a window to display the result
cv2.namedWindow('resizedResult')

# Create a trackbar to adjust the threshold value of the Sobel image
cv2.createTrackbar('threshold', 'resizedResult', 165, 255, apply_threshold)

# Show the result with the initial threshold value >> threshold startup value
apply_threshold(165)

# Wait for a key press
cv2.waitKey(0)
# </editor-fold>

# <editor-fold desc= "LAPLACIAN">
# # Load the image
# image = cv2.imread('image/gul.jpeg')
#
# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Function to apply the Laplacian operator with the given kernel size
# def apply_laplacian(ksize):
#     # Apply the Laplacian operator
#     laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
#
#     # Threshold the Laplacian image to create a binary image
#     _, edges = cv2.threshold(laplacian, 30, 255, cv2.THRESH_BINARY)
#
#     # Find the contours in the binary image
#     contours, _ = cv2.findContours(edges.astype(np.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Create a copy of the original image
#     result = image.copy()
#
#     # Draw the largest contour (boundary) on the image
#     if len(contours) > 0:
#         cv2.drawContours(result, [max(contours, key=cv2.contourArea)], -1, (0, 255, 0), 3)
#
#         # Create a mask with the same size as the image
#         mask = np.zeros_like(image[:,:,0])
#
#         # Fill the area inside the boundary with white color
#         cv2.fillPoly(mask, [max(contours, key=cv2.contourArea)], 255)
#
#         # Change the color of the region inside the boundary
#         result[np.where(mask == 255)] = [255, 0, 0]
#
#         # Make the background black
#         result[np.where(mask == 0)] = [0, 0, 0]
#
#     # Show the result
#     cv2.imshow('Result', result)
#
# # Create a window to display the result
# cv2.namedWindow('Result')
#
# # Create a trackbar to adjust the kernel size of the Laplacian operator
# cv2.createTrackbar('ksize', 'Result', 1, 31, lambda ksize: apply_laplacian(2 * ksize + 1))
#
# # Show the result with the initial kernel size
# apply_laplacian(1)
#
# # Wait for a key press
# cv2.waitKey(0)
# </editor-fold>