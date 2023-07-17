import cv2
import numpy as np

# Open the video file for capturing frames
cap = cv2.VideoCapture('media/car.mp4')

# Define the desired size for the frames
size_value = (640, 480)

# Read the first frame and preprocess it
_, first_frame = cap.read()
first_frame = cv2.resize(first_frame, size_value)
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Resize the frame to the desired size
    frame = cv2.resize(frame, size_value)

    if ret == 0:
        break

    # Convert the current frame to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Compute the absolute difference between the first frame and the current frame
    diff = cv2.absdiff(first_gray, gray)

    # Apply a binary threshold to the difference image
    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Display the current frame, first frame, and difference image
    cv2.imshow("frame", frame)
    cv2.imshow("first_frame", first_frame)
    cv2.imshow("diff", diff)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
