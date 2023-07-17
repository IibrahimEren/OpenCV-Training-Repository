import cv2

cap = cv2.VideoCapture('media/eye.mp4')

while True:
    # Read frame from video capture
    ret, frame = cap.read()

    if ret == 0:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Define the region of interest (ROI)
    roi = frame[80:250, 150:450]
    rows, cols, _ = roi.shape
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 20), 2)
        cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 30, 255), 2)
        cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 30, 255), 2)
        break
    roi = frame[80:250, 150:450] = roi

    cv2.imshow("frame", frame)
    cv2.imshow("Thresh", threshold)

    if cv2.waitKey(90) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

'''
```
import cv2
```
This line imports the OpenCV library, which provides functions for computer vision tasks.

```
cap = cv2.VideoCapture('media/eye.mp4')
```
This line creates a video capture object `cap` and opens the video file `'media/eye.mp4'` for reading.

```
while True:
```
This initiates an infinite loop that will continuously process each frame of the video.

``` ret, frame = cap.read() ``` This line reads the next frame from the video capture object `cap` and stores the 
frame in the variable `frame`. The return value `ret` indicates whether the frame was successfully read.

```
    if ret == 0:
        break
```
If the return value `ret` is 0, it means that there are no more frames to read from the video, so the loop is terminated 
using the `break` statement.

```
    frame = cv2.flip(frame, 1)
```
This line flips the frame horizontally using the `cv2.flip()` function. This is done to correct the mirror effect in the 
video.

```
    roi = frame[80:250, 150:450]
```
This line defines the region of interest (ROI) by extracting a rectangular portion from the frame. The ROI is specified 
as the range of rows (80 to 250) and columns (150 to 450) in the frame.

```
    rows, cols, _ = roi.shape
```
This line retrieves the dimensions of the ROI by calling the `shape` attribute of the `roi` array. The number of rows is 
stored in `rows` and the number of columns is stored in `cols`.

```
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
```
This line converts the ROI from the BGR color space to grayscale using the `cv2.cvtColor()` function. Grayscale images
 are often used for simplicity in image processing tasks.

```
    _, threshold = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY_INV)
```
This line applies thresholding to the grayscale image `gray` using the `cv2.threshold()` function. Pixels with intensity
 values less than 2 are set to 0 (black), and pixels with intensity values greater than or equal to 2 are set to
  255 (white). The resulting thresholded image is stored in the variable `threshold`.

```
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```
This line finds contours in the thresholded image using the `cv2.findContours()` function. The contours are stored in 
the variable `contours`. The optional arguments `cv2.RETR_TREE` and `cv2.CHAIN_APPROX_SIMPLE` specify the contour 
retrieval mode and contour approximation method, respectively.

```
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
```
This line sorts the contours in descending order based on their area using the `sorted()` function and the 
`cv2.contourArea()` function as the key for comparison. The sorted contours are stored back in the variable `contours`.

```
    for cnt in contours:
```
This line starts a loop to iterate over each contour in the `contours` list.

```
        (x, y, w, h) = cv2.boundingRect(cnt)
```
This line calculates the bounding rectangle for the current contour using the `cv2.boundingRect()` function. The

 top-left corner coordinates `(x, y)` and the width `w` and height `h` of the rectangle are stored in the respective 
 variables.

```
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 20), 2)
```
This line draws a green rectangle around the bounding rectangle on the `roi` image using the `cv2.rectangle()` function.
 The rectangle's top-left and bottom-right coordinates are specified as `(x, y)` and `(x + w, y + h)`, respectively.
  The color `(0, 255, 20)` represents green, and the thickness of the rectangle is set to 2.

```
        cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 30, 255), 2)
        cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 30, 255), 2)
```
These two lines draw vertical and horizontal lines through the center of the bounding rectangle. The first line draws a
 vertical line passing through the center of the rectangle, and the second line draws a horizontal line passing through 
 the center. The color `(0, 30, 255)` represents orange, and the thickness of the lines is set to 2.

```
        break
```
This line breaks the loop after processing the first contour. This is done to only focus on the largest contour or the 
contour with the highest area.

```
    roi = frame[80:250, 150:450] = roi
```
This line replaces the region of interest in the original frame with the modified `roi` image. This ensures that the 
processed ROI is displayed correctly in the final output.

```
    cv2.imshow("frame", frame)
    cv2.imshow("Thresh", threshold)
```
These two lines display the original frame with the bounding rectangle and the thresholded image in separate windows 
using the `cv2.imshow()` function.

```
    if cv2.waitKey(90) & 0XFF == ord('q'):
        break
```
This line waits for a key press for 90 milliseconds. If the pressed key is 'q', as indicated by `ord('q')`, the loop is 
terminated using the `break` statement.

```
cap.release()
cv2.destroyAllWindows()
```
These two lines release the video capture object `cap` and close all windows created by OpenCV using the 
`cap.release()` and `cv2.destroyAllWindows()` functions, respectively.

'''