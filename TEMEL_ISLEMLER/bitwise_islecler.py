import cv2
import numpy as np

# Read and load the first image
img1 = cv2.imread('media/bitwise1.png')

# Read and load the second image
img2 = cv2.imread('media/bitwise2.png')

# Perform bitwise AND operation between the two images
bit_and = cv2.bitwise_and(img2, img1)

# Perform bitwise OR operation between the two images
bit_or = cv2.bitwise_or(img2, img1)

# Perform bitwise NOT operation on the second image
bit_not = cv2.bitwise_not(img2)

# Perform bitwise XOR operation between the two images
bit_xor = cv2.bitwise_xor(img2, img1)

# Display the first image
cv2.imshow("img1", img1)

# Display the second image
cv2.imshow("img2", img2)

# Display the result of bitwise AND operation
cv2.imshow("bit_and", bit_and)

# Wait for a key press to close the windows
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

'''
- `cv2.imread('media/bitwise1.png')`: This function is used to read an image file and load it into memory. It takes the file path as input and returns a NumPy array representing the image.

- `cv2.bitwise_and(img2, img1)`: This function performs a bitwise AND operation between two images. It takes two input images of the same size and applies the logical AND operation on each corresponding pixel. The result is a new image where each pixel value is the bitwise AND of the corresponding pixels in the input images.

- `cv2.bitwise_or(img2, img1)`: This function performs a bitwise OR operation between two images. Similar to bitwise AND, it takes two input images and performs the logical OR operation on each corresponding pixel. The result is a new image where each pixel value is the bitwise OR of the corresponding pixels in the input images.

- `cv2.bitwise_not(img2)`: This function performs a bitwise NOT operation on a single image. It takes one input image and applies the logical NOT operation on each pixel. The result is a new image where each pixel value is the bitwise NOT of the corresponding pixel in the input image. In other words, it inverts the binary representation of the image.

- `cv2.bitwise_xor(img2, img1)`: This function performs a bitwise XOR (exclusive OR) operation between two images. It takes two input images and applies the logical XOR operation on each corresponding pixel. The result is a new image where each pixel value is the bitwise XOR of the corresponding pixels in the input images.

- `cv2.imshow(window_name, image)`: This function is used to display an image in a named window. It takes the window name as the first argument and the image to be displayed as the second argument.

- `cv2.waitKey(0)`: This function waits for a key press. It takes an integer argument representing the delay in milliseconds. Here, `0` is passed to wait indefinitely until a key is pressed.

- `cv2.destroyAllWindows()`: This function is used to close all open windows created by `cv2.imshow()`. It releases the resources associated with the windows and frees up memory.

These functions are part of the OpenCV library and they are commonly used for various operations such as image manipulation, blending, masking, and more.
'''