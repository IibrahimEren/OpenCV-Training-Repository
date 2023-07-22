import face_recognition
import cv2

path = "media/face.jpg"

img = cv2.imread(path)

# Find the faces in the image
faceLocations = face_recognition.face_locations(img)

# Draw a rectangle around each face
for (top, right, bottom, left) in faceLocations:
    cv2.rectangle(img, (left, top), (right, bottom), (250, 180, 250), 2)

# Display the image
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the face locations
print(faceLocations)
