import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.colors import hsv_to_rgb

# This function visualizes an RGB image as a 3D scatter plot.
def Visulize3D_RGB(img_rgb):

    # Split the image into its R, G, and B channels.
    r, g, b = cv2.split(img_rgb)

    # Reshape each channel into a 1D array.
    pixel_colors = img_rgb.reshape((np.shape(img_rgb)[0] * np.shape(img_rgb)[1], 3))

    # Scale the pixel values to the range [-1, 1].
    norm = colors.Normalize(vmin=-1, vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    # Create a 3D scatter plot of the pixel values.
    axis = plt.figure().add_subplot(1, 1, 1, projection="3d")
    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")

    # Label the axes of the plot.
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")

    # Show the plot.
    plt.show()

# This function visualizes an HSV image as a 3D scatter plot.
def Visulize3D_HSV(img_hsv):

    # Convert the HSV image to RGB.
    rgb = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

    # Visualize the RGB image as a 3D scatter plot.
    Visulize3D_RGB(rgb)

# This function displays two 10x10 square images, one with a light black value and one with a dark black value.
def hsvDisplayer(light_black, dark_black):

    # Create two 10x10 square images.
    lo_square = np.full((10, 10, 3), light_black, dtype=np.uint8) / 255.0
    do_square = np.full((10, 10, 3), dark_black, dtype=np.uint8) / 255.0

    # Display the images in a subplot.
    plt.subplot(1, 2, 1)
    plt.imshow(hsv_to_rgb(do_square))
    plt.subplot(1, 2, 2)
    plt.imshow(hsv_to_rgb(lo_square))

    # Show the plot.
    plt.show()
