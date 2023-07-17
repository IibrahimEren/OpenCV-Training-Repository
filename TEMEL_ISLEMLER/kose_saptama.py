import cv2
import numpy as np

# Callback function for the trackbar
def on_trackbar(val):
    # Get the current positions of the trackbars
    cornerMetin = cv2.getTrackbarPos("corner", "metin")
    cornerSekil = cv2.getTrackbarPos("corner", "sekil")

    # Read the images
    img = cv2.imread('media/metin.png')
    img1 = cv2.imread('media/triangle.png')

    # Convert the images to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale images to float32
    gray = np.float32(gray)
    gray1 = np.float32(gray1)

    # Find corners in the images using the goodFeaturesToTrack function
    corners = cv2.goodFeaturesToTrack(gray, cornerMetin, 0.01, 10)
    corners1 = cv2.goodFeaturesToTrack(gray1, cornerSekil, 0.01, 10)

    # Convert the corner coordinates to integers
    corners = np.int0(corners)
    corners1 = np.int0(corners1)

    # Draw circles at the detected corners
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    for corner1 in corners1:
        x, y = corner1.ravel()
        cv2.circle(img1, (x, y), 3, (0, 0, 255), -1)

    # Display the images with the detected corners
    cv2.imshow("metin", img)
    cv2.imshow("sekil", img1)

# Create named windows for the images
cv2.namedWindow("metin")
cv2.namedWindow("sekil")

# Create trackbars to control the number of corners
cv2.createTrackbar("corner", "metin", 50, 100, on_trackbar)
cv2.createTrackbar("corner", "sekil", 50, 100, on_trackbar)

# Wait for a key press to exit
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

'''
Explanation:

1. Import the `cv2` and `numpy` modules.
2. Define a callback function `on_trackbar` that will be called when the trackbar positions change.
3. Inside the callback function, retrieve the current positions of the trackbars using `cv2.getTrackbarPos`.
4. Read the images `'media/metin.png'` and `'media/triangle.png'` using `cv2.imread`.
5. Convert the images to grayscale using `cv2.cvtColor`.
6. Convert the grayscale images to `float32` using `np.float32`.
7. Use `cv2.goodFeaturesToTrack` to find corners in the images. The `cornerMetin` and `cornerSekil` variables control the maximum number of corners to be detected.
8. Convert the corner coordinates to integers using `np.int0`.
9. Draw circles at the detected corners using `cv2.circle`.
10. Display the images with the detected corners using `cv2.imshow`.
11. Create named windows for the images using `cv2.namedWindow`.
12. Create trackbars to control the number of corners using `cv2.createTrackbar`. The callback function `on_trackbar` will be called when the trackbar positions change.
13. Wait for a key press using `cv2.waitKey`.
14. Close all windows using `cv2.destroyAllWindows`.

This code allows you to control the number of corners to be detected in two images using trackbars. The images are read, converted to grayscale, and the `goodFeaturesToTrack` function is used to find corners. The detected corners are then visualized by drawing circles on the images. The number of corners can be adjusted using the trackbars in the windows.
'''