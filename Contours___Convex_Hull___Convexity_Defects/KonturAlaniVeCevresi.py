import cv2

img = cv2.imread('media/triangle.png')  # Read the image

down = 0.4  # Scale factor for resizing the image
img = cv2.resize(img, None, fx=down, fy=down, interpolation=cv2.INTER_LINEAR)  # Resize the image

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # Convert the image to grayscale
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # Apply thresholding to obtain binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the binary image

cnt = contours[0]  # Get the first contour
area = cv2.contourArea(cnt)  # Calculate the area using contours
print("Area from contours: " + str(area))

M = cv2.moments(contours[0])  # Calculate moments of the contour
print("Area from moments: " + str(M['m00']))

perimeter = cv2.arcLength(cnt, True)  # Calculate the perimeter of the contour
print("Perimeter: " + str(perimeter))

cv2.imshow("original", img)  # Display the original image
cv2.imshow("gray", gray)  # Display the grayscale image
cv2.imshow("thresh", thresh)  # Display the thresholded image

cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all windows

'''
Explanation:
1. Read the image using `cv2.imread` function.
2. Define a scale factor `down` to resize the image.
3. Resize the image using `cv2.resize` function with the specified scale factor.
4. Convert the resized image to grayscale using `cv2.cvtColor` function.
5. Apply thresholding to the grayscale image using `cv2.threshold` function, creating a binary image.
6. Find contours in the binary image using `cv2.findContours` function.
7. Retrieve the first contour from the list of contours.
8. Calculate the area of the contour using `cv2.contourArea` function.
9. Print the area calculated from contours.
10. Calculate the moments of the contour using `cv2.moments` function.
11. Print the area calculated from moments.
12. Calculate the perimeter of the contour using `cv2.arcLength` function.
13. Print the perimeter.
14. Display the original image using `cv2.imshow` function.
15. Display the grayscale image.
16. Display the thresholded image.
17. Wait for a key press to close the windows.
18. Close all windows using `cv2.destroyAllWindows`.
'''