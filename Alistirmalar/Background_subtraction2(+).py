import cv2
import numpy as np

# Open the video file for capturing frames
cap = cv2.VideoCapture('media/road.mp4')

# Create a background subtractor using MOG2 algorithm
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=100, detectShadows=True)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if ret == 0:
        break

    # Resize the frame to the desired size
    frame = cv2.resize(frame, (640, 480))

    # Apply background subtraction to the frame
    mask = subtractor.apply(frame)

    # Display the original frame and the resulting mask
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()

"""
explanations of the functions used:

1. `cv2.VideoCapture('media/road.mp4')`: Opens the video file specified by the path `'media/road.mp4'` and returns a 
`VideoCapture` object for capturing frames.

2. `cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=100, detectShadows=True)`: Creates a background 
subtractor object using the MOG2 (Mixture of Gaussians) algorithm. The `history` parameter determines the number of 
previous frames used for modeling the background, the `varThreshold` parameter sets the threshold value for determining
 whether a pixel belongs to the background or foreground, and the `detectShadows` parameter enables shadow detection.

3. `cap.read()`: Reads the next frame from the video capture object `cap`. It returns a boolean value (`ret`) 
indicating whether a frame was successfully read and the frame itself.

4. `cv2.resize(frame, (640, 480))`: Resizes the frame to the desired size of (640, 480) pixels.

5. `subtractor.apply(frame)`: Applies the background subtraction algorithm to the `frame` using the background 
subtractor object created earlier. It subtracts the background from the frame and returns a resulting mask.

6. `cv2.imshow("frame", frame)`: Displays the original `frame` in a window titled "frame".

7. `cv2.imshow("mask", mask)`: Displays the resulting `mask` (foreground) after background subtraction in a window 
titled "mask".

8. `cv2.waitKey(20) & 0xFF == ord('q')`: Waits for a key press event for 20 milliseconds. If the key pressed is 'q', 
the loop will be broken.

9. `cap.release()`: Releases the video capture object, closing the video file.

10. `cv2.destroyAllWindows()`: Closes all the windows created by `cv2.imshow()`.

These functions and methods are used to read frames from a video, apply background subtraction, and display the 
original frames and resulting masks in separate windows. The loop continues until the 'q' key is pressed or until 
there are no more frames in the video.

"""