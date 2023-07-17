import cv2

# Load the image
img = cv2.imread('media/faces.jpg')

# Resize the image
down = 0.4
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale3(gray, scaleFactor=1.3, minNeighbors=4)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    startPoint = (x, y)
    endPoint = (x + w, y + h)
    cv2.rectangle(img, startPoint, endPoint, (255, 255, 255), thickness=2)

# Display the image with detected faces
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
```
img = cv2.imread('media/face.jpg')
```
- Load the image `'media/face.jpg'` using `cv2.imread`, which reads an image file and returns a NumPy array representing 
the image.

```
down = 0.4
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)
```
- Define a scale factor `down` to resize the image.
- Resize the image using `cv2.resize`, specifying the image, scale factors (`fx` for width and `fy` for height), and 
interpolation method (`cv2.INTER_LINEAR_EXACT`).

```
face_cascade = cv2.CascadeClassifier('xml_files/frontal_face_cascade.xml')
```
- Load the Haar cascade classifier XML file for face detection using `cv2.CascadeClassifier`, specifying the path to the 
XML file `'xml_files/frontal_face_cascade.xml'`.

```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
- Convert the resized image from BGR color space to grayscale using `cv2.cvtColor`, specifying the image and the 
conversion code `cv2.COLOR_BGR2GRAY`.

```
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
```
- Perform face detection on the grayscale image using `cv2.CascadeClassifier.detectMultiScale`, specifying the grayscale 
image, `scaleFactor` (specifies how much the image size is reduced at each image scale), and `minNeighbors` (specifies 
the minimum number of neighbors required for a region to be considered a face).

```
for (x, y, w, h) in faces:
    startPoint = (x, y)
    endPoint = (x + w, y + h)
    cv2.rectangle(img, startPoint, endPoint, (255, 255, 255), thickness=2)
```
- Iterate over the detected faces, where each face is represented by a rectangle with `(x, y, w, h)` coordinates.
- Define the starting point and ending point of the rectangle.
- Draw a rectangle around each detected face on the original image using `cv2.rectangle`, specifying the image, starting 
point, ending point, color `(255, 255, 255)` (white), and thickness `2`.

```
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- Display the image with the detected faces using `cv2.imshow`, specifying the window name and the image.
- Wait for a key press using `cv2.waitKey`, which waits indefinitely until a key is pressed. `0` as the argument means 
it waits until any key is pressed.
- Close all windows using `cv2.destroyAllWindows`, which destroys all created windows.

This code loads an image, resizes it, performs face detection using the Haar cascade classifier, draws rectangles around 
the detected faces, and displays the resulting image with the detected faces.
'''
