import cv2

# Create a named window for displaying the live video
windowName = "Live"
cv2.namedWindow(windowName)

# Create a video capture object and open the default camera (index 0)
cap = cv2.VideoCapture(0)

# Print the current width and height of the video capture
print(f"Width: {cap.get(3)}\n"
      f"Height: {cap.get(4)}")

# Set the width and height of the video capture to 1280x720 pixels
cap.set(3, 1280)
cap.set(4, 720)

# Print the updated width and height of the video capture
print(f"Width<>: {cap.get(3)}\n"
      f"Height<>: {cap.get(4)}")

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if ret == 0:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Display the frame in the named window
    cv2.imshow(windowName, frame)

    # Check for the "Esc" key press to exit the loop
    if cv2.waitKey(1) == 27:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

'''
```
windowName = "Live"
cv2.namedWindow(windowName)
```
This line creates a named window with the title "Live" using the `cv2.namedWindow()` function. This window will be used 
to display the live video feed.

```
cap = cv2.VideoCapture(0)
```
This line creates a video capture object `cap` and opens the default camera (index 0) for capturing live video.

```
print(f"Width: {cap.get(3)}\n"
      f"Height: {cap.get(4)}")
```
These lines print the current width and height of the video capture using the `cap.get()` function. The width is obtained
using the index 3, and the height is obtained using the index 4.

```
cap.set(3,1280)
cap.set(4,720)
```
These lines set the width and height of the video capture to 1280x720 pixels using the `cap.set()` function. The index 3 
is used to set the width, and the index 4 is used to set the height.

```
print(f"Width<>: {cap.get(3)}\n"
      f"Height<>: {cap.get(4)}")
```
These lines print the updated width and height of the video capture to verify that the changes were applied successfully.

```
while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)
```
This is the main loop that continuously captures frames from the video capture object `cap`. The `cap.read()` function 
reads a frame from the video, and the return value `ret` indicates whether the frame was successfully read. If `ret` is 0, 
it means that there are no more frames to read, so the loop is terminated. The `cv2.flip()` function is used to horizontally 
flip the frame.

```
    cv2.imshow(windowName, frame)
```
This line displays the current frame in the named window "Live" using the `cv2.imshow()` function.

```
    if cv2.waitKey(1) == 27:
        break
```
This line waits for a key press for 1 millisecond. If the pressed key is the "Esc" key (represented by the value 27), 
the loop is terminated using the `break` statement.

```
cap.release()
cv2.destroyAllWindows()
```
These two lines release the video capture object `cap` and close all windows created by OpenCV using the 
`cap.release()` and `cv2.destroyAllWindows()` functions, respectively.
'''
