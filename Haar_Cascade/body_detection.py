import cv2

# Load the image
img = cv2.imread('media/man.jpg')

# Load the cascade classifiers for body detection
# These are XML files that contain the trained parameters for fullbody detection.
body_cascade = cv2.CascadeClassifier('xml_files/full_body_cascade.xml')

# Convert the image to grayscale
# This is necessary for face detection.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=1)


for (x, y, w, h) in bodies:
    startPoint = (x, y)
    endPoint = (x + w, y + h)
    cv2.rectangle(img, startPoint, endPoint, (255, 255, 255), thickness=2)

# Display the image with detected faces
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()