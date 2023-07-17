import cv2

# Open a video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    # Flip the frame horizontally using cv2.flip()
    frame = cv2.flip(frame, 1)

    # Apply the Canny edge detection algorithm to the frame
    edges = cv2.Canny(frame, 100, 200)

    # Display the original frame and the edges
    cv2.imshow("Frame", frame)
    cv2.imshow("edges", edges)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(5) & 0XFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

'''
Explanation:

1. Import the `cv2` module.
2. Open a video capture object using `cv2.VideoCapture(0)` to access the default camera.
3. Enter a `while` loop to continuously process frames from the video capture.
4. Use `cap.read()` to read a frame from the video capture. The return value `ret` indicates 
if a frame was successfully read, and `frame` contains the actual frame.
5. Flip the frame horizontally using `cv2.flip(frame, 1)` to obtain a mirror image.
6. Apply the Canny edge detection algorithm to the flipped frame using 
`cv2.Canny(frame, 100, 200)`. The parameters `100` and `200` specify the lower and upper 
thresholds for edge detection.
7. Display the original frame using `cv2.imshow("Frame", frame)`.
8. Display the edges using `cv2.imshow("edges", edges)`.
9. Use `cv2.waitKey(5)` to wait for a key press for 5 milliseconds. The bitwise AND operation `&` with `0XFF` and the comparison with `ord('q')` are used to check if the 'q' key was pressed to exit the loop.
10. Once the loop is terminated, release the video capture object using `cap.release()` 
and close all windows using `cv2.destroyAllWindows()`.

This code captures live video from the default camera, flips each frame horizontally, 
and applies the Canny edge detection algorithm to the frames. The original frames and the 
detected edges are displayed in separate windows. The program continues until the 'q' key 
is pressed.
'''