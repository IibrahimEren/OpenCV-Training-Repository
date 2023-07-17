import cv2
import numpy as np
import matplotlib.pyplot as plt
from Graph3D import Visulize3D_RGB as vis3d_rgb
from Graph3D import Visulize3D_HSV as vis3d_hsv
from Graph3D import hsvDisplayer as hsv_disp

# Load the image.
img = cv2.imread('media/blue_frog.jpg')

# Convert the image to RGB and HSV color spaces.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Visualize the RGB and HSV images as 3D scatter plots.
# This code is commented out because it is not necessary for this example.
# vis3d_rgb(img_rgb)
# vis3d_hsv(img_hsv)

# Create a mask for the blue color in HSV space.
# The lower and upper bounds of the blue color in HSV space are specified.
lower_blue = (55, 0, 0)
upper_blue = (118, 255, 255)
mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

# Apply the mask to the RGB image. The `bitwise_and()` function takes two images as input and returns a new image
# that contains the pixels that are common to both images.
result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)

# Display the mask and the result image. The `subplot()` function creates a subplot in a figure. The subplot is
# divided into two rows and two columns, and the first subplot is used to display the mask and the second subplot is
# used to display the result image.
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")

plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()

# Wait for the user to press a key.
cv2.waitKey(0)

# Destroy all windows that were created by the `cv2` library.
cv2.destroyAllWindows()
