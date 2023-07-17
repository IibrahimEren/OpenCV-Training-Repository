import cv2

# Load the video
cap = cv2.VideoCapture('media/crowd.mp4')
# cap = cv2.VideoCapture(0)

# Load the Haar cascade classifier XML file for face detection
# It seems to been used front side of human bodies while preparing the xml file
body_cascade = cv2.CascadeClassifier('xml_files/full_body_cascade.xml')

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if no frame is read
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection on the grayscale frame
    body = body_cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=2)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in body:
        startPoint = (x, y)
        endPoint = (x + w, y + h)
        cv2.rectangle(frame, startPoint, endPoint, (255, 255, 255), thickness=2)

    # Display the frame with detected faces
    cv2.imshow("frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(5) & 0XFF == ord("q"):
        break

# Close all windows
cv2.destroyAllWindows()

'''
```
import cv2
```
- Import the OpenCV library.

```
cap = cv2.VideoCapture('media/crowd.mp4')
# cap = cv2.VideoCapture(0)
```
- Load the video using `cv2.VideoCapture`. You can specify a file path or use `0` for 
capturing video from a webcam.

```
body_cascade = cv2.CascadeClassifier('xml_files/full_body_cascade.xml')
```
- Load the Haar cascade classifier XML file for full body detection.

```
while True:
    ret, frame = cap.read()

    if ret == 0:
        break
```
- Enter a loop to read frames from the video. The loop breaks if no frame is read 
(`ret == 0`).

```
    frame = cv2.flip(frame, 1)
```
- Flip the frame horizontally using `cv2.flip` function.

```
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
- Convert the frame to grayscale using `cv2.cvtColor` function.

```
    body = body_cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=2)
```
- Perform full body detection on the grayscale frame using `detectMultiScale` method 
of the `body_cascade` object.

```
    for (x, y, w, h) in body:
        startPoint = (x, y)
        endPoint = (x + w, y + h)
        cv2.rectangle(frame, startPoint, endPoint, (255, 255, 255), thickness=2)
```
- Iterate over the detected full bodies and draw rectangles around them on the frame 
using `cv2.rectangle` function.

```
    cv2.imshow("frame", frame)

    if cv2.waitKey(5) & 0XFF == ord("q"):
        break
```
- Display the frame with detected full bodies using `cv2.imshow` function.
- Break the loop if the 'q' key is pressed.

```
cv2.destroyAllWindows()
```
- Close all windows.

In summary, this code reads frames from a video, performs full body detection on each 
frame, and displays the frames with rectangles around the detected full bodies. 
The loop continues until the 'q' key is pressed.
'''