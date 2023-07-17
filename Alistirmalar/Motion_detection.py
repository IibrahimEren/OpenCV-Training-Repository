import cv2
import numpy as np

# This function does nothing. It is used to keep the trackbar open.
def nothing(x):
    pass

# Create a VideoCapture object and read the first two frames.
cap = cv2.VideoCapture('media/Shopping_Mall_Background.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Downs ample the frames by 40%.
down = 0.4
frame1 = cv2.resize(frame1, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)
frame2 = cv2.resize(frame2, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)

# Create a color for the contours.
color = (50, 30, 150)

# Create a window for the threshold trackbar.
cv2.namedWindow("threshold")
cv2.createTrackbar("threshold", "threshold", 30, 90, nothing)

## Create a background subtraction object.
# The `history` parameter specifies the number of frames to be used to learn the background model.
# The `varThreshold` parameter specifies the threshold for determining whether a pixel is foreground or background.
# The `detectShadows` parameter specifies whether to detect shadows.
fgbg = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=100, detectShadows=False
)

# Loop until the user presses `q`.
while cap.isOpened():

    # Calculate the difference between the two frames.
    diff = cv2.absdiff(frame1, frame2)

    # Apply the background subtraction method.
    fgmask = fgbg.apply(diff)

    # Get the threshold value from the trackbar.
    thresh = cv2.getTrackbarPos("threshold", "threshold")

    # Apply thresholding to the foreground mask.
    _, thresh = cv2.threshold(fgmask, thresh, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image.
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find the contours in the dilated image.
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the first frame.
    cv2.drawContours(frame1, contours, -1, color, 3)

    # Display the difference image, the thresholded image, the dilated image, and the frame with the contours.
    cv2.imshow("difference", diff)
    cv2.imshow("threshold", thresh)
    cv2.imshow("dilated", dilated)
    cv2.imshow("vid", frame1)

    # Update the first frame with the second frame.
    frame1 = frame2
    ret, frame2 = cap.read()
    frame2 = cv2.resize(frame2, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR_EXACT)

    # Check if the user pressed `q` to quit.
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Release the VideoCapture object and destroy all windows.
cap.release()
cv2.destroyAllWindows()
