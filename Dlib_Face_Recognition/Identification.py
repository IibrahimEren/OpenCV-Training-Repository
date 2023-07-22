import cv2
import face_recognition

# Load the image of Jensen for training.
path = 'media/jensen.png'
jensenImage = cv2.imread(path)
jensenImage_encoding = face_recognition.face_encodings(jensenImage)[0]

# Load the image of Michael for testing.
testPath = 'media/michael.png'
image = cv2.imread(testPath)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Find the faces in the image of Michael.
# The `face_locations()` function returns a list of tuples, where each tuple represents the coordinates of a face in the image.
face_loc = face_recognition.face_locations(image)
face_enc = face_recognition.face_encodings(image, face_loc)

# Compare the face encodings of Jensen and Michael.
# The `compare_faces()` function returns a list of boolean values, where each value indicates whether the corresponding face in the image of Michael matches the face of Jensen.
matched_faces = face_recognition.compare_faces(jensenImage_encoding, face_enc)

# If the faces match, draw a rectangle around the face and label it "Jensen".
# The `rectangle()` function draws a rectangle around the face, and the `putText()` function labels the rectangle with the text "Jensen".
if True in matched_faces:
    for (topLeftY, bottomRightX, bottomRightY, topLeftX) in face_loc:
        cv2.rectangle(image, (topLeftX, topLeftY), (bottomRightX, bottomRightY), (30, 180, 90), 2)
        cv2.putText(image, "Jensen", (topLeftX, topLeftY), cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 180, 90), 2)

# If the faces do not match, draw a rectangle around the face and label it "Unknown".
# The `rectangle()` function draws a rectangle around the face, and the `putText()` function labels the rectangle with the text "Unknown".
else:
    for (topLeftY, bottomRightX, bottomRightY, topLeftX) in face_loc:
        cv2.rectangle(image, (topLeftX, topLeftY), (bottomRightX, bottomRightY), (30, 180, 90), 2)
        cv2.putText(image, "Unknown", (topLeftX, topLeftY), cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 180, 90), 2)

# Display the image.
cv2.imshow("jensen", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
