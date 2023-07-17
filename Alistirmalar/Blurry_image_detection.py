import cv2

# Read the input image
img = cv2.imread("media/man.jpg")

# Apply median blur to the image
blurry_img = cv2.medianBlur(img, 9)  # The more we increase the kernel value, the lower the laplacian value

# Display the original image and the blurred image
cv2.imshow("man", img)
cv2.imshow("blur", blurry_img)

# Calculate the variance of the Laplacian of the blurred image
laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()
print("laplacian")

# Check if the image is blurry based on the Laplacian variance
if laplacian < 500:
    print("Blurry image")

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
```
img = cv2.imread("media/man.jpg")
```
- This line reads the image file "man.jpg" using the `cv2.imread()` function and stores it in the variable `img` as a 
NumPy array. The image is loaded in its original color format.

```
blurry_img = cv2.medianBlur(img, 9)
```
- This line applies median blurring to the image `img` using a kernel size of 9x9. The `cv2.medianBlur()` function is 
used for this operation, which helps to reduce noise and smooth out the image.

```
cv2.imshow("man", img)
cv2.imshow("blur", blurry_img)
```
- These lines display the original image and the blurred image using the `cv2.imshow()` function. The first argument is 
the window name, and the second argument is the image to be displayed.

```
laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()
```
The Laplacian is an image enhancement operator that is commonly used for edge detection. It calculates the second-order 
derivative of an image, which highlights regions of rapid intensity change, such as edges.

In OpenCV, the `cv2.Laplacian()` function is used to compute the Laplacian gradient of an image. Here's the syntax of the function:

***
dst = cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])
***

- `src`: This is the source image on which the Laplacian operation is performed. It should be a grayscale or 
single-channel image of type `cv2.CV_8U` or `cv2.CV_32F`.

- `ddepth`: This parameter specifies the desired depth of the output image. It can be set to `cv2.CV_64F` to obtain a 
floating-point representation of the Laplacian result.

- `dst` (optional): This is the output image where the Laplacian result is stored. If not provided, a new image will be 
created.

- `ksize` (optional): This parameter determines the size of the Laplacian kernel used for the operation. It should be an 
odd positive integer. The default value is 1, which corresponds to a 3x3 kernel.

- `scale` (optional): This parameter is used to scale the computed Laplacian values. It can be useful for adjusting the 
sensitivity of the edge detection. The default value is 1.

- `delta` (optional): This parameter is an offset applied to the computed Laplacian values. It can be useful for 
controlling the thresholding or visualization of the results. The default value is 0.

- `borderType` (optional): This parameter specifies the pixel extrapolation method when the image border is reached. The 
default value is `cv2.BORDER_DEFAULT`.

The `cv2.Laplacian()` function returns the Laplacian result as an output image or assigns it to the provided `dst` image.
The Laplacian image typically contains positive and negative values, representing edges with different orientations.

In the given code, the Laplacian function is used to compute the Laplacian gradient of the blurred image (`blurry_img`). 
By calculating the variance of the Laplacian image (`laplacian.var()`), the code determines the amount of detail or edge 
information present in the image, which can be used as a measure of image sharpness or blurriness.

```python
if laplacian < 500:
    print("blurry image")
```
- This code block checks if the computed Laplacian variance value (`laplacian`) is less than 500. If it is, it prints 
"blurry image", indicating that the image is likely blurry.

```python
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- These lines wait for a key press (`cv2.waitKey(0)`) and then close all open windows (`cv2.destroyAllWindows()`). This 
allows you to view the displayed images until a key is pressed, and then the windows are closed.

Overall, this code loads an image, applies median blurring to it, calculates the Laplacian variance, and determines if 
the image is blurry based on a threshold value.
'''