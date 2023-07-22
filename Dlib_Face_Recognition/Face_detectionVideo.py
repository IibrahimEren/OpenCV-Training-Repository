import face_recognition
import cv2

"""
This code finds faces in a video file and draws a rectangle around each one.
"""

path = 'media/face_video2.mp4'

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Define a color for the rectangle
color = (10, 60, 110)

# Loop over the frames in the video
while True:

    # Read a frame from the video
    ret, frame = cap.read()

    if ret == 0:
        break
    frame = cv2.flip(frame, 1)

    # Find the faces in the frame
    faceLocations = face_recognition.face_locations(frame)

    # Draw a rectangle around each face
    for (top, right, bottom, left) in faceLocations:
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

    # Display the image
    cv2.imshow("img", frame)

    # Check if the user pressed `q`
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture object
cap.release()

# Destroy all of the windows
cv2.destroyAllWindows()
