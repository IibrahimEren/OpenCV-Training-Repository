import cv2

# Open the video file for capturing frames
cap = cv2.VideoCapture("media/car.mp4")

# List to store the coordinates of circles
circles = []

# Mouse callback function to append the coordinates of clicked points to the circles list
def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))

# Create a named window to display the frame
cv2.namedWindow("Frame")

# Set the mouse callback function for the "Frame" window
cv2.setMouseCallback("Frame", mouse)

while True:
    # Read a frame from the video
    _, frame = cap.read()

    # Resize the frame to the desired size
    frame = cv2.resize(frame, (640, 480))

    # Draw circles on the frame based on the stored coordinates
    for center in circles:
        cv2.circle(frame, center, 20, (0, 100, 255), -1)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Wait for key events
    key = cv2.waitKey(1)

    # Break the loop if the 'Esc' key is pressed
    if key == 27:
        break

    # Clear the circles list if the 'r' key is pressed
    elif key == ord("r"):
        circles = []

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()

'''
Explain each functions: 

1. `cv2.VideoCapture("media/car.mp4")`: Creates a VideoCapture object to open and read the video file named "media/car.mp4".

2. `cv2.namedWindow("Frame")`: Creates a named window with the title "Frame" to display the video frame.

3. `cv2.setMouseCallback("Frame", mouse)`: Sets a mouse callback function named "mouse" for the "Frame" window. The callback function will be called when a mouse event occurs in the window.

4. `cv2.EVENT_LBUTTONDOWN`: Represents the left button down mouse event. It is used as a condition in the mouse callback function.

5. `circles.append((x, y))`: Appends the coordinates of the clicked point (x, y) to the `circles` list.

6. `cv2.circle(frame, center, 20, (0, 100, 255), -1)`: Draws a filled circle on the frame at the specified center coordinates. The circle has a radius of 20 pixels and the color is defined as (0, 100, 255) in BGR format.

7. `cv2.waitKey(1)`: Waits for a key event for the specified time (1 millisecond in this case). It returns the key code of the pressed key or -1 if no key is pressed.

8. `key == 27`: Checks if the pressed key's code is equal to 27, which corresponds to the 'Esc' key.

9. `key == ord("r")`: Checks if the pressed key's code is equal to the ASCII code of the 'r' key.

10. `cap.release()`: Releases the video capture object and frees up the resources.

11. `cv2.destroyAllWindows()`: Closes all open windows.
'''