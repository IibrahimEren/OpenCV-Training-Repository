import cv2
import numpy as np

cap = cv2.VideoCapture('media/dog.mp4')  # Open the video capture

while True:
    ret, frame = cap.read()  # Read a frame from the video

    if ret == 0:  # If no frames are returned, break the loop
        break

    down = 0.4  # Scale factor for resizing the frame
    frame = cv2.resize(frame, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)  # Resize the frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space

    sensitivity = 15  # Sensitivity value for white color detection
    lower_white = np.array([0, 0, 255 - sensitivity])  # Lower threshold for white color in HSV
    upper_white = np.array([255, sensitivity, 255])  # Upper threshold for white color in HSV

    mask = cv2.inRange(hsv, lower_white, upper_white)  # Create a mask for white color in the frame
    res = cv2.bitwise_and(frame, frame, mask=mask)  # Apply the mask to the frame using bitwise AND operation

    cv2.imshow("frame", frame)  # Display the original frame
    cv2.imshow("mask", mask)  # Display the mask
    cv2.imshow("res", res)  # Display the result after applying the mask

    k = cv2.waitKey(5) & 0xFF  # Wait for a key press (5ms delay)
    if k == 27:  # If the key pressed is ESC (ASCII code 27), break the loop
        break

cv2.destroyAllWindows()  # Close all windows

'''
``` 
import cv2
import numpy as np

cap = cv2.VideoCapture('media/dog.mp4')
```

- Import the required libraries: `cv2` for OpenCV and `numpy` for array operations.
- Open the video capture using `cv2.VideoCapture` function, specifying the video file path.

``` 
while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    down = 0.4
    frame = cv2.resize(frame, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)
```

- Enter into a while loop to read frames from the video.
- Read a frame from the video using the `cap.read()` function. The returned values are stored in `ret` (indicating whether a frame was successfully read) and `frame` (the actual frame).
- Check if a frame was successfully read. If not (i.e., `ret` is 0), break the loop.
- Define a scale factor `down` to resize the frame.
- Resize the frame using `cv2.resize` function, specifying the frame, scale factor, and interpolation method.

``` 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    sensitivity = 15
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask=mask)
```

- Convert the resized frame from BGR color space to HSV color space using `cv2.cvtColor` function.
- Set the sensitivity value for white color detection. This value determines how strict the white color detection will be.
- Define the lower and upper thresholds for white color in HSV. These thresholds represent the range of HSV values for white color.
- Create a mask using `cv2.inRange` function, which checks if each pixel in the HSV image falls within the specified lower and upper thresholds. Pixels within the range are set to white (255), while pixels outside the range are set to black (0).
- Apply the mask to the original frame using `cv2.bitwise_and` function, performing a bitwise AND operation between the frame and the mask. This keeps only the white regions in the frame, while masking out the rest.

``` 
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break
```

- Display the original frame, mask, and the result after applying the mask using `cv2.imshow` function.
- Wait for a key press using `cv2.waitKey` function, specifying a delay of 5 milliseconds. The returned key value is stored in `k`.
- Check if the pressed key is ESC (ASCII code 27). If true, break the loop to exit the program.

``` 
cv2.destroyAllWindows()
```

- Close all windows using `cv2.destroyAllWindows` function to clean up resources and close the program properly.

This code captures a video, resizes each frame, converts it to HSV color space, detects white regions based on specified thresholds, and displays the original frame, mask, and the result after applying the mask in separate windows. The program exits when the ESC key is pressed.
'''