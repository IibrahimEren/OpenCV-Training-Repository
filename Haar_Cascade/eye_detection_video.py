import cv2

# Load the video
# cap = cv2.VideoCapture('media/face_video2.mp4')
cap = cv2.VideoCapture(0)

# Load the Haar cascade classifier XML file for face detection
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
eye_cascade = cv2.CascadeClassifier('xml_files/haar_cascade_eye.xml')

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
    faces = face_cascade.detectMultiScale3(gray_frame, scaleFactor=1.3, minNeighbors=4)

    # Try to draw rectangles around the detected faces
    try:
        for (x, y, w, h) in faces:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

            # Get the face region of interest (ROI)
            roi_frame = frame[y: y + h, x:x + w]
            roi_gray = gray_frame[y:y + h, x:x + w]

            # Detect eyes in the ROI
            eyes = eye_cascade.detectMultiScale3(roi_gray, scaleFactor=1.1, minNeighbors=50)

            # Try to draw rectangles around the detected eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (150, 120, 50), 2)

    # If no faces or eyes are detected, print a message
    except:
        if len(faces) == 0:
            print("No face detected!")
        elif len(eyes) == 0:
            print("No eyes detected!")
        else:
            print("Neither face nor eyes detected")

    # Display the frame with detected faces
    cv2.imshow("frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
# Close all windows
cv2.destroyAllWindows()

'''
```
cap = cv2.VideoCapture('media/face_video2.mp4')
# cap = cv2.VideoCapture(0)
```
- Load the video using `cv2.VideoCapture`. You can specify a file path or use `0` for capturing video from a webcam.

```
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
eye_cascade = cv2.CascadeClassifier('xml_files/haar_cascade_eye.xml')
```
- Load the Haar cascade classifier XML files for face detection and eye detection.

```
while True:
    ret, frame = cap.read()

    if ret == 0:
        break
```
- Enter a loop to read frames from the video. The loop breaks if no frame is read (`ret == 0`).

```
    frame = cv2.flip(frame, 1)
```
- Flip the frame horizontally using `cv2.flip` function.

```
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
- Convert the frame to grayscale using `cv2.cvtColor` function.

```
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=4)
```
- Perform face detection on the grayscale frame using `detectMultiScale` method of the `face_cascade` object.

```
    try:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

            roi_frame = frame[y: y + h, x:x + w]
            roi_gray = gray_frame[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=50)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (150, 120, 50), 2)
```
- Iterate over the detected faces and draw rectangles around them on the frame using `cv2.rectangle` function.
- Extract the region of interest (ROI) for each face.
- Perform eye detection within the ROI and draw rectangles around the detected eyes.

```
    except:
        if len(faces) == 0:
            print("No face detected!")
        elif len(eyes) == 0:
            print("No eyes detected!")
        else:
            print("Neither face nor eyes detected")

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
```
- Handle exceptions in case no faces or eyes are detected, and print corresponding messages.
- Display the frame with detected faces and eyes using `cv2.imshow` function.
- Break the loop if the 'q' key is pressed.

```
cap.release()
cv2.destroyAllWindows()
```
- Release the video capture and close all windows.

In summary, this code reads frames from a video, performs face detection and eye detection on each frame, and displays 
the frames with rectangles around the detected faces and eyes. It also provides feedback messages if no faces or eyes 
are detected. The loop continues until the 'q' key is pressed.
'''
