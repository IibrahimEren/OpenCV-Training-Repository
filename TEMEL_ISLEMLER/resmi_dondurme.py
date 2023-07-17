import cv2
import numpy as np

# Load the image
image_path = 'media/helicopter.jpeg'
img = cv2.imread(image_path, 0)  # Read the image as grayscale

# Downscale the image
scale_factor = 0.4
downscaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

# Get the dimensions of the downscaled image
height, width = downscaled_img.shape

# Define the rotation transformation matrix
center = (width // 2, height // 2)
angle = 180
scale = 1
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Apply the rotation transformation to the image
rotated_img = cv2.warpAffine(downscaled_img, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow("Original Image", downscaled_img)
cv2.imshow("Rotated Image", rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Explanation:
1. The code begins by importing the necessary libraries, OpenCV (`cv2`) and NumPy (`np`).
2. The image path is specified, pointing to the 'helicopter.jpeg' file.
3. The image is loaded using `cv2.imread()` function with the additional argument `0` to read the image as grayscale.
4. The image is downscaled by a factor of 0.4 using `cv2.resize()` function, which takes the image, scale factors (`fx` and `fy`), and interpolation method (`cv2.INTER_LINEAR`) as arguments.
5. The dimensions (height and width) of the downscaled image are obtained using the `.shape` attribute.
6. The rotation transformation matrix is defined using `cv2.getRotationMatrix2D()`, specifying the center of rotation (`center`), rotation angle (`angle`), and scale factor (`scale`).
7. The rotation transformation is applied to the downscaled image using `cv2.warpAffine()`, providing the downscaled image, rotation matrix, and dimensions of the resulting image.
8. Finally, the original and rotated images are displayed using `cv2.imshow()`, and the program waits for a key press using `cv2.waitKey()`. After the key press, the windows are closed using `cv2.destroyAllWindows()`.
9. The code is executed sequentially, resulting in the display of the original and rotated images.
'''