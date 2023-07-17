import cv2

# Open video capture object
cap = cv2.VideoCapture('media/frog.mp4')

while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Scaling Down the frame 0.5 times specifying a single scale factor
    downscale_factor = 0.5
    scaled_frame = cv2.resize(frame, None, fx=downscale_factor, fy=downscale_factor, interpolation=cv2.INTER_LINEAR)

    # Convert the frame to grayscale
    grayscale_frame = cv2.cvtColor(scaled_frame, cv2.COLOR_BGR2GRAY)

    # Convert the frame to RGB color space
    rgb_frame = cv2.cvtColor(scaled_frame, cv2.COLOR_BGR2RGB)

    # Break the loop if no frame is read
    if not ret:
        break

    # Display the frame in BGR format
    cv2.imshow("Video", scaled_frame)

    # Display the frame in grayscale format
    cv2.imshow("Video_GRAY", grayscale_frame)

    # Display the frame in RGB format
    cv2.imshow("Video_RGB", rgb_frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break

# Release the video capture object and destroy windows
cap.release()
cv2.destroyAllWindows()


'''
Explanation:
1. Import the `cv2` module.
2. Open the video capture object using `cv2.VideoCapture` with the video file path 'media/frog.mp4'.
3. Enter a loop to process each frame in the video.
4. Read the frame from the video capture object using `cap.read()`. The return value `ret` indicates if a frame is successfully read.
5. Scale down the frame by a factor of 0.5 using `cv2.resize` with `fx` and `fy` parameters. The downscaled frame is stored in `scaled_frame`.
6. Convert the downscaled frame to grayscale using `cv2.cvtColor` with `cv2.COLOR_BGR2GRAY` conversion flag. The grayscale frame is stored in `grayscale_frame`.
7. Convert the downscaled frame to RGB color space using `cv2.cvtColor` with `cv2.COLOR_BGR2RGB` conversion flag. The RGB frame is stored in `rgb_frame`.
8. Check if a frame is successfully read by checking the value of `ret`.
9. Display the downscaled frame in BGR format using `cv2.imshow` with the window name "Video".
10. Display the grayscale frame using `cv2.imshow` with the window name "Video_GRAY".
11. Display the RGB frame using `cv2.imshow` with the window name "Video_RGB".
12. Check for the 'q' key press to exit the loop using `cv2.waitKey`. The wait time is set to 15 milliseconds.
13. Release the video capture object using `cap.release()`.
14. Close all windows using `cv2.destroyAllWindows()`.

The code reads a video file, scales down each frame, and displays the original frame, grayscale frame, and RGB frame. The frames are processed in a loop until the user presses the 'q' key to exit.
'''
