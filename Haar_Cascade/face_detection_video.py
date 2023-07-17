import cv2

# Load the video
cap = cv2.VideoCapture('media/face_video.mp4')
# cap = cv2.VideoCapture(0)

# Load the Haar cascade classifier XML file for face detection
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if no frame is read
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)

    # Resize the frame
    down = 0.2
    frame = cv2.resize(frame, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection on the grayscale frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=4)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
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
cap = cv2.VideoCapture('media/face_video.mp4')
```
- Create a `VideoCapture` object to read the video file specified by the path `'media/face_video.mp4'`.

```
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
```
- Load the Haar cascade classifier XML file for face detection. This file contains pre-trained data to detect frontal 
faces.

```
while True:
    ret, frame = cap.read()
    if ret == 0:
        break
```
- Enter a loop to read frames from the video. `cap.read()` reads a frame from the video and returns `ret` (a boolean 
indicating if the frame was successfully read) and `frame` (the actual frame). If no frame is read (`ret == 0`), break 
the loop.

```
down = 0.2
frame = cv2.resize(frame, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)
```
- Resize the frame to a smaller size using `cv2.resize` function. The scaling factors `fx` and `fy` determine the 
resizing ratio, and `interpolation=cv2.INTER_LINEAR_EXACT` specifies the interpolation method for resizing.

```
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
- Convert the resized frame to grayscale using `cv2.cvtColor` function.

```
faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=4)
```
- Detect faces in the grayscale frame using `detectMultiScale` method of the `face_cascade` object. The `scaleFactor` 
parameter specifies the scale reduction between successive image pyramids, and `minNeighbors` parameter specifies the 
minimum number of neighbors required for a region to be considered a face.

```
for (x, y, w, h) in faces:
    startPoint = (x, y)
    endPoint = (x + w, y + h)
    cv2.rectangle(frame, startPoint, endPoint, (255, 255, 255), thickness=2)
```
- Iterate over the detected faces and draw rectangles around them on the original frame using `cv2.rectangle` function. 
The rectangles are drawn with the specified color `(255, 255, 255)` (white) and thickness 2.

```
cv2.imshow("frame", frame)
```
- Display the frame with the detected faces using `cv2.imshow` function.

```
if cv2.waitKey(5) & 0XFF == ord("q"):
    break
```
- Wait for a key press and check if the pressed key is 'q'. If true, break the loop.

```
cv2.destroyAllWindows()
```
- Close all windows.

In summary, this code reads frames from a video, resizes each frame, performs face detection on the resized frames, 
draws rectangles around the detected faces, and displays the frames with the detected faces. The program exits when the 
'q' key is pressed.
'''
