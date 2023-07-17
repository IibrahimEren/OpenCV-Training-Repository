# Import the OpenCV library
import cv2

# Load the image
img = cv2.imread('media/face.jpg')

# Resize the image
# This will reduce the size of the image, which will make face detection faster.
down = 0.4
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)

# Convert the image to grayscale
# This is necessary for face detection.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the cascade classifiers for face and eye detection
# These are XML files that contain the trained parameters for face and eye detection.
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
eye_cascade = cv2.CascadeClassifier('xml_files/haar_cascade_eye.xml')

# Perform face detection
# This will return a list of rectangles that represent the detected faces.
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Draw rectangles around the detected faces
# This will draw a rectangle around each detected face.
for (x, y, w, h) in faces:
    startPoint = (x, y)
    endPoint = (x + w, y + h)
    cv2.rectangle(img, startPoint, endPoint, (255, 0, 100), thickness=2)

# Detect eyes in the face area
# This will return a list of rectangles that represent the detected eyes.
face_area = img[y:y + h, x:x + w]
face_area_gray = gray[y:y + h, x:x + w]
eyes = eye_cascade.detectMultiScale3(face_area_gray)

# Draw rectangles around the detected eyes
# This will draw a rectangle around each detected eye.
for (ex, ey, ew, eh) in eyes:
    eyes_startPoint = (ex, ey)
    eyes_endPoint = (ex + ew, ey + eh)
    cv2.rectangle(face_area, eyes_startPoint, eyes_endPoint, (150, 120, 50), thickness=2)

# Show the image
# This will display the image with the detected faces and eyes.
cv2.imshow("eyes", img)

# Wait for a key press
# This will pause the execution of the code until a key is pressed.
cv2.waitKey(0)

# Close all windows
# This will close all the windows that were opened by the code.
cv2.destroyAllWindows()

'''
```
img = cv2.imread('media/face.jpg')
```
- Load the image `'media/face.jpg'` using `cv2.imread` function.

```
down = 0.4
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)
```
- Resize the image using `cv2.resize` function. The scaling factors `fx` and `fy` determine the resizing ratio, and 
`interpolation=cv2.INTER_LINEAR_EXACT` specifies the interpolation method for resizing.

```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
- Convert the resized image to grayscale using `cv2.cvtColor` function.

```
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
eye_cascade = cv2.CascadeClassifier('xml_files/haar_cascade_eye.xml')
```
- Load the Haar cascade classifier XML files for face detection and eye detection. These files contain pre-trained data 
to detect faces and eyes.

```
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
```
- Detect faces in the grayscale image using `detectMultiScale` method of the `face_cascade` object. The `scaleFactor` 
parameter specifies the scale reduction between successive image pyramids, and `minNeighbors` parameter specifies the 
minimum number of neighbors required for a region to be considered a face.

```
for (x, y, w, h) in faces:
    startPoint = (x, y)
    endPoint = (x + w, y + h)
    cv2.rectangle(img, startPoint, endPoint, (255, 0, 100), thickness=2)
```
- Iterate over the detected faces and draw rectangles around them on the original image using `cv2.rectangle` function. 
The rectangles are drawn with the specified color `(255, 0, 100)` and thickness 2.

```
face_area = img[y:y + h, x:x + w]
face_area_gray = gray[y:y + h, x:x + w]
eyes = eye_cascade.detectMultiScale(face_area_gray)
```
- Extract the region of interest (ROI) from the original image and grayscale image corresponding to the detected face area.
- Detect eyes in the face area using `detectMultiScale` method of the `eye_cascade` object.

```
for (ex, ey, ew, eh) in eyes:
    eyes_startPoint = (ex, ey)
    eyes_endPoint = (ex + ew, ey + eh)
    cv2.rectangle(face_area, eyes_startPoint, eyes_endPoint, (150, 120, 50), thickness=2)
```
- Iterate over the detected eyes and draw rectangles around them on the face area using `cv2.rectangle` function. 
The rectangles are drawn with the specified color `(150, 120, 50)` and thickness 2.

```
cv2.imshow("eyes", img)
```
- Display the image with the detected faces and eyes using `cv2.imshow` function.

```
cv2.waitKey(0)
```
- Wait for a key press. This will pause the execution of the code until a key is pressed.

```
cv2.destroyAllWindows()
```
- Close all windows that were opened by the code.

In summary, this code loads an image, resizes it, performs face detection, draws rectangles around the detected faces, 
extracts the face area, performs eye detection within the face area, draws rectangles around the detected eyes, and 
displays the image with the detected faces and eyes. The program waits for a key press before closing the windows.
'''
