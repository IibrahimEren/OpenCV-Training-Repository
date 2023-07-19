import cv2
import numpy as np
from collections import deque

# Open the video capture object to read frames from the default camera (index 0)
cap = cv2.VideoCapture(0)

# Define the lower and upper blue color thresholds in HSV color space
lower_blue = np.array([100, 60, 60])
upper_blue = np.array([140, 255, 255])

# Create deques to store points for different colors (blue, green, red, yellow)
blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

# Initialize the index for each color
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# List of colors for drawing (blue, green, red, yellow)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]

# Initialize the color index to draw in blue initially
color_index = 0

# Create a white window for drawing (paint window)
paintWindow = np.zeros((471, 636, 3)) + 255

# Draw color selection rectangles on the paint window
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), colors[0], -1)
paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), colors[1], -1)
paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), colors[2], -1)
paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), colors[3], -1)

# Add text labels to the paint window
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(paintWindow, "CLEAR ALL", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

# Create a named window for displaying the paint window
cv2.namedWindow("Paint")

# Main loop to capture and process frames
while True:
    try:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert the frame from BGR to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Draw color selection rectangles on the original frame
        frame = cv2.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
        frame = cv2.rectangle(frame, (160, 1), (255, 65), colors[0], -1)
        frame = cv2.rectangle(frame, (275, 1), (370, 65), colors[1], -1)
        frame = cv2.rectangle(frame, (390, 1), (485, 65), colors[2], -1)
        frame = cv2.rectangle(frame, (505, 1), (600, 65), colors[3], -1)

        # Add text labels to the original frame
        cv2.putText(frame, "CLEAR ALL", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "BLUE", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "GREEN", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "RED", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "YELLOW", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        # Check if a frame is not captured properly
        if ret is False:
            break

        # Create a binary mask for blue color in the frame
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Perform morphological operations to remove noise from the mask
        mask = cv2.erode(mask, (5, 5), iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5, 5))
        mask = cv2.dilate(mask, (5, 5), iterations=1)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        center = None

        if len(contours) > 0:
            # Find the contour with the maximum area (largest blue object)
            max_contours = sorted(contours, key=cv2.contourArea, reverse=True)[0]
            ((x, y), radius) = cv2.minEnclosingCircle(max_contours)

            # Draw a circle around the detected blue object
            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 0), 3)

            # Calculate the center of the blue object
            M = cv2.moments(max_contours)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # Check if the blue object is within the color selection area
            if center[1] <= 65:
                if 40 <= center[0] <= 140:
                    # If the blue object is within the "CLEAR ALL" area, reset all points and paint window
                    blue_points = [deque(maxlen=600)]
                    green_points = [deque(maxlen=600)]
                    red_points = [deque(maxlen=600)]
                    yellow_points = [deque(maxlen=600)]

                    blue_index = 0
                    green_index = 0
                    red_index = 0
                    yellow_index = 0

                    # Clear the paint window
                    paintWindow[67:, :, :] = 255

                elif 160 <= center[0] <= 255:
                    # If the blue object is within the "BLUE" color selection area, set the color index to blue
                    color_index = 0

                elif 275 <= center[0] <= 370:
                    # If the blue object is within the "GREEN" color selection area, set the color index to green
                    color_index = 1

                elif 390 <= center[0] <= 485:
                    # If the blue object is within the "RED" color selection area, set the color index to red
                    color_index = 2

                elif 505 <= center[0] <= 600:
                    # If the blue object is within the "YELLOW" color selection area, set the color index to yellow
                    color_index = 3

            else:
                # If the blue object is outside the color selection area, store its position in the corresponding deque
                if color_index == 0:
                    blue_points[blue_index].appendleft(center)

                elif color_index == 1:
                    green_points[green_index].appendleft(center)

                elif color_index == 2:
                    red_points[red_index].appendleft(center)

                elif color_index == 3:
                    yellow_points[yellow_index].appendleft(center)

        else:
            # If no blue object is detected, add a new deque for each color and increment the corresponding index
            blue_points.append(deque(maxlen=512))
            blue_index += 1

            green_points.append(deque(maxlen=512))
            green_index += 1

            red_points.append(deque(maxlen=512))
            red_index += 1

            yellow_points.append(deque(maxlen=512))
            yellow_index += 1

        # Combine all the points for different colors
        points = [blue_points, green_points, red_points, yellow_points]

        # Draw lines connecting the stored points for each color on both the original frame and paint window
        for i in range(len(points)):
            for j in range(len(points[i])):
                for k in range(1, len(points[i][j])):
                    if points[i][j][k - 1] is None or points[i][j][k] is None:
                        continue
                    cv2.circle(frame, points[i][j][k - 1], 2, colors[i], 3)
                    cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                    cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

        # Display the original frame and paint window
        cv2.imshow("Frame", frame)
        cv2.imshow("Paint", paintWindow)

    except Exception as e:
        # If an exception occurs (e.g., when closing the window), ignore it and continue
        pass

    # Check if the 'q' key is pressed, and if so, break out of the loop
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
