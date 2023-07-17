import cv2
import numpy as np

# Path to the input images
path1 = "media/puppy.jpg"
path2 = "media/puppyKopya.jpg"

# Read the input images
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# Apply median blur to img1 with a kernel size of 15x15
img3 = cv2.medianBlur(img1, 15)

# Check if the shapes of img1 and img2 are the same
if img1.shape == img2.shape:
    print("Same size")
else:
    print("Not the same size")

# Compute the absolute difference between img1 and img3
diff = cv2.subtract(img1, img3)
b, g, r = cv2.split(diff)

# Check if all channels (B, G, R) have zero differences
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("Completely equal")
else:
    print("Not equal")

# Display the original image (img1), the median-blurred image (img3), and the difference image (diff)
cv2.imshow("dog", img1)
cv2.imshow("dog2", img3)
cv2.imshow("diff", diff)

# Wait for a key press to exit
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

'''

```
path1 = "media/puppy.jpg"
path2 = "media/puppyKopya.jpg"
```
- These lines define the file paths of two images, `puppy.jpg` and `puppyKopya.jpg`.

```
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
```
- These lines use the `cv2.imread()` function to read the images from the file paths and store them as NumPy arrays, `img1` and `img2`.

```
img3 = cv2.medianBlur(img1, 15)
```
- This line applies median filtering to `img1` using a kernel size of 15. The result is stored in `img3`, which helps to reduce noise in the image.

```
if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")
```
- This code block checks if the shapes (dimensions) of `img1` and `img2` are the same. If they are the same, it prints 
"same size"; otherwise, it prints "not same".

```
diff = cv2.subtract(img1, img3)
b, g, r = cv2.split(diff)
```
- These lines calculate the absolute difference between `img1` and `img3` using the `cv2.subtract()` function. The result 
is stored in `diff`. Then, `cv2.split()` function splits `diff` into separate color channels, `b`, `g`, and `r`.

```
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("completely equal")
else:
    print("Not Equal")
```
- This code block checks if all three color channels (`b`, `g`, and `r`) have zero non-zero (non-black) pixels. If all 
channels have zero non-zero pixels, it prints "completely equal"; otherwise, it prints "Not Equal".

```
cv2.imshow("dog", img1)
cv2.imshow("dog2", img3)
cv2.imshow("diff", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- These lines display the images using `cv2.imshow()` function. The images are displayed in separate windows with the 
given names. `cv2.waitKey(0)` waits for a key press, and `cv2.destroyAllWindows()` closes all open windows.

These lines demonstrate image loading, image processing operations, and image display using OpenCV functions.
'''
