import cv2

# Load the video
# cap = cv2.VideoCapture('media/smile.mp4')
# Alternatively, you can use the webcam by setting
cap = cv2.VideoCapture(0)

# Load the Haar cascade classifier XML file for face detection
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
smile_cascade = cv2.CascadeClassifier('xml_files/smile_cascade.xml')

# This loop will run until the user presses 'q'
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If no frame is read, break the loop
    if ret == 0:
        break

    # Flip the frame horizontally (this is just for visualization purposes)
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=4)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

        # Get the face region of interest (ROI)
        roi_frame = frame[y: y + h, x:x + w]
        roi_gray = gray_frame[y:y + h, x:x + w]

        # Detect smiles in the ROI
        smile = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.9, minNeighbors=10)

        # Draw rectangles around the detected smiles
        for (ex, ey, ew, eh) in smile:
            cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (150, 120, 50), 2)

    # Display the frame with detected faces
    cv2.imshow("frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()

'''
```
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('media/smile.mp4')
```
- Create a video capture object using `cv2.VideoCapture`. It can capture video from a webcam (`0`) or from a video file 
specified by the file path.

```
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
smile_cascade = cv2.CascadeClassifier('xml_files/smile_cascade.xml')
```
- Load the Haar cascade classifier XML files for face and smile detection.

```
while True:
    ret, frame = cap.read()

    if ret == 0:
        break
```
- Enter a loop to read frames from the video capture object. The loop breaks if no frame is read (`ret == 0`).

```
    frame = cv2.flip(frame, 1)
```
- Flip the frame horizontally using `cv2.flip` function for visualization purposes.

```
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
- Convert the frame to grayscale using `cv2.cvtColor` function.

```
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=4)
```
- Detect faces in the grayscale frame using `detectMultiScale` method of the `face_cascade` object.

```
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

        roi_frame = frame[y: y + h, x:x + w]
        roi_gray = gray_frame[y:y + h, x:x + w]

        smile = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.9, minNeighbors=10)

        for (ex, ey, ew, eh) in smile:
            cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (150, 120, 50), 2)
```
- Iterate over the detected faces and draw rectangles around them on the frame using `cv2.rectangle` function.
- Extract the region of interest (ROI) for each detected face.
- Convert the ROI to grayscale.
- Detect smiles in the ROI using `detectMultiScale` method of the `smile_cascade` object.
- Draw rectangles around the detected smiles on the ROI.

```
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
```
- Display the frame with detected faces and smiles using `cv2.imshow` function.
- Break the loop if the 'q' key is pressed.

```
cap.release()
cv2.destroyAllWindows()
```
- Release the video capture object.
- Close all windows.

In summary, this code captures video frames either from a webcam or a video file, 
detects faces and smiles in each frame using Haar cascade classifiers, and displays 
the frames with rectangles around the detected faces and smiles. The loop continues 
until the 'q' key is pressed.
'''