import cv2
import numpy as np

# Open the video file for capturing
cap = cv2.VideoCapture('media/line.mp4')

# Loop through the frames of the video
while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    # Downscale the frame
    down = 0.3
    frame = cv2.resize(frame, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)
    # frame = cv2.resize(frame,(640,480))

    # Check if the frame was successfully read
    if ret == 0:
        break

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the yellow color range
    lower_yellow = np.array([18, 94, 140], np.uint8)  # [18,94,140], [20, 100, 100]
    upper_yellow = np.array([48, 255, 255], np.uint8)  # [48,255,255], [30, 255, 255]

    # Create a mask for the yellow color range
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Apply Canny edge detection to the masked image
    edges = cv2.Canny(mask, 75, 250)

    # Apply Hough line detection to detect lines in the edge image
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=20)

    # Check if any lines were detected
    if lines is None:
        continue

    # Draw the detected lines on the original frame
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the frame, mask, and edges
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("edges", edges)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

"""
Explanation of each line:

import cv2 - Imports the OpenCV library for image and video processing.
import numpy as np - Imports the NumPy library for numerical operations.
cap = cv2.VideoCapture('media/line.mp4') - Opens the video file named "line.mp4" for capturing frames.
while True: - Starts an infinite loop for processing each frame of the video.
ret, frame = cap.read() - Reads the next frame from the video. ret indicates whether the frame was successfully read or not.
down = 0.3 - Defines the scaling factor for downscaling the frame.
frame = cv2.resize(frame, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR) - Downscales the frame using the defined scaling factor.
if ret == 0: - Checks if the frame was successfully read. If not, breaks the loop.
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) - Converts the frame from BGR color space to HSV color space.
lower_yellow = np.array([18, 94, 140], np.uint8) - Defines the lower bounds of the yellow color range in HSV.
upper_yellow = np.array([48, 255, 255], np.uint8) - Defines the upper bounds of the yellow color range in HSV.
mask = cv2.inRange(hsv, lower_yellow, upper_yellow) - Creates a mask for the yellow color range in the HSV image.
edges = cv2.Canny(mask, 75, 250) - Applies the Canny edge detection algorithm to the masked image to detect edges.
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=20) - Applies the probabilistic Hough transform to detect lines in the edge image.
if lines is None: - Checks if any lines were detected. If not, continues to the next iteration of the loop.
for line in lines: - Iterates over the detected lines.
x1, y1, x2, y2 = line[0] - Retrieves the starting and ending points of the line.
cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) - Draws a line segment on the original frame using the starting and ending points.
cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1) - Draws a rectangle around the detected line on the original frame.
cv2.imshow("frame", frame) - Displays the frame in a window titled "frame".
cv2.imshow("mask", mask) - Displays the mask in a window titled "mask".
cv2.imshow("edges", edges) - Displays the edges in a window titled "edges".
if cv2.waitKey(20) & 0xFF == ord('q'): - Checks if the 'q' key is pressed. If so, breaks the loop.
cap.release() - Releases the video capture.
cv2.destroyAllWindows() - Closes all the windows.
"""