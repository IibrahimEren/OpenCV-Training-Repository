'''
Dış büke örtü demektir çizdiğimiz şekillerin şeklin üzerinden geçmesini
istemediğimiz zamanlarda kullanılarak çeklin çevresine bir örtü
serilmiş gibi hayal edilebilir
'''
import cv2
import numpy as np

img = cv2.imread('media/map.jpg')
down = 0.4
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the grayscale image
blur = cv2.blur(gray, (3, 3))

# Apply thresholding to obtain a binary image
ret, thresh = cv2.threshold(blur, 35, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty list to store the convex hulls
hull = []

# Compute the convex hull for each contour
for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False))# false gives us back indices of where contour is koyulduğu için contour'un bulunduğu indisin dönmesini sağlayacaktır

# Create a blank image
bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# Draw contours and convex hulls on the blank image
for i in range(len(contours)):
    cv2.drawContours(bg, contours, i, (255, 255, 0), 3, 8, hierarchy)
    cv2.drawContours(bg, hull, i, (255, 0, 0), 1, 8)

# Display the original image, grayscale image, blurred image, thresholded image, and the final image
cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("thresh", thresh)
cv2.imshow("Image", bg)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Explanation:
1. The code starts by reading an image using `cv2.imread()` and stores it in the `img` variable.
2. The image is resized by a scale factor (`down`) using `cv2.resize()` to reduce its size.
3. The image is then converted to grayscale using `cv2.cvtColor()` with the `cv2.COLOR_BGR2GRAY` flag.
4. The grayscale image is blurred using `cv2.blur()` to reduce noise. The kernel size for blurring is specified as `(3, 3)`.
5. Thresholding is applied to the blurred image using `cv2.threshold()`. Pixels with intensity values below the threshold (35) are set to 0, and those above the threshold are set to 255, creating a binary image.
6. Contours and hierarchy information are extracted from the binary image using `cv2.findContours()`, with retrieval mode `cv2.RETR_TREE` and contour approximation method `cv2.CHAIN_APPROX_SIMPLE`.
7. An empty list, `hull`, is created to store the convex hulls.
8. A `for` loop iterates over each contour. For each contour, `cv2.convexHull()` is applied to compute the convex hull and append it to the `hull` list.
9. A blank image, `bg`, is created using `np.zeros()` with the same dimensions as the thresholded image.
10. Another `for` loop is used to draw the contours and convex hulls on the blank image. `cv2.drawContours()` is called twice: once to draw the contours in blue and once to draw the convex hulls in red.
11. Finally, the original image, grayscale image, blurred image, thresholded image, and the final image with contours and convex hulls are displayed using `cv2.imshow()`.
12. The program waits for a key press using `cv2.waitKey(0)`.
13. After the key press, all windows are closed using `cv2.destroyAllWindows()`.

The purpose of this code is to demonstrate the application of convex hulls in image processing. The code performs image preprocessing steps such as resizing, grayscale conversion, blurring, and thresholding. Then it detects contours and computes the convex hull for each contour. The contours and convex hulls are visualized on a blank image, providing an understanding of the concept of convex hulls and their application in defining the boundaries of shapes.
'''

