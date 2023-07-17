# Import the OpenCV library
import cv2

# Load the image
img = cv2.imread('media/smile.jpg')

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
smile_cascade = cv2.CascadeClassifier('xml_files/smile_cascade.xml')

# Perform face detection
# This will return a list of rectangles that represent the detected faces.
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

try:

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
    smile = smile_cascade.detectMultiScale3(face_area_gray, scaleFactor=0.1, minNeighbors=2)

    # Draw rectangles around the detected eyes
    # This will draw a rectangle around each detected eye.
    for (ex, ey, ew, eh) in smile:
        eyes_startPoint = (ex, ey)
        eyes_endPoint = (ex + ew, ey + eh)
        cv2.rectangle(face_area, eyes_startPoint, eyes_endPoint, (150, 120, 50), thickness=2)

except:
    print("no smile detected")

# Show the image
# This will display the image with the detected faces and eyes.
cv2.imshow("smile", img)
cv2.imshow("roi img", face_area)

# Wait for a key press
# This will pause the execution of the code until a key is pressed.
cv2.waitKey(0)

# Close all windows
# This will close all the windows that were opened by the code.
cv2.destroyAllWindows()
