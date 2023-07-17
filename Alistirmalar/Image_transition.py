import cv2


# Callback function for trackbar (used for displaying values)
def display_values(x):
    alpha = x / 1000  # Update the alpha value based on the trackbar position
    beta = 1 - alpha  # Calculate the corresponding beta value
    print(f"Alpha: {alpha:.2f}, Beta: {beta:.2f}")


# Read the input images
img1 = cv2.imread("media/puppy.jpg")
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.imread("media/bulldog.jpg")
img2 = cv2.resize(img2, (640, 480))

# Perform image blending using addWeighted() function
output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Define the window name for displaying images
window_name = "Image Blending"
cv2.namedWindow(window_name)

# Create a trackbar for adjusting the alpha value
cv2.createTrackbar("Alpha", window_name, 500, 1000, display_values)
# Set an initial position for the trackbar at 0.5 (corresponds to 500)

while True:
    # Display the blended image
    cv2.imshow(window_name, output)

    # Check if the ESC key is pressed
    if cv2.waitKey(1) == 27:
        break

    # Get the current position of the trackbar (alpha)
    alpha = cv2.getTrackbarPos("Alpha", window_name) / 1000

    # Calculate the beta value as (1 - alpha)
    beta = 1 - alpha

    # Perform image blending with the updated alpha and beta values
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)

# Close all windows
cv2.destroyAllWindows()



'''

```
def display_values(x):
    alpha = x / 1000
    beta = 1 - alpha
    print(f"Alpha: {alpha:.2f}, Beta: {beta:.2f}")
```
- This defines the callback function `display_values` that will be called when the trackbar position changes. 
It calculates the alpha and beta values based on the trackbar position and prints them.

```
img1 = cv2.imread("media/puppy.jpg")
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.imread("media/bulldog.jpg")
img2 = cv2.resize(img2, (640, 480))
```
- These lines read the input images `"media/puppy.jpg"` and `"media/bulldog.jpg"` using `cv2.imread()`. The images are 
then resized to a width of 640 pixels and a height of 480 pixels using `cv2.resize()`.

```
output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
```
- This line performs image blending using the `cv2.addWeighted()` function. It blends `img1` and `img2` with equal 
weights (0.5) and no gamma correction (0).

```
window_name = "Image Blending"
cv2.namedWindow(window_name)
```
- This assigns the window name `"Image Blending"` to a variable and creates a named window using `cv2.namedWindow()`.

```
cv2.createTrackbar("Alpha", window_name, 500, 1000, display_values)
```
- This line creates a trackbar named `"Alpha"` in the window specified by `window_name`. The trackbar ranges from 0 to
1000, with an initial position set to 500. The `display_values` function is set as the callback function for the trackbar.

```
while True:
    cv2.imshow(window_name, output)
    if cv2.waitKey(1) == 27:
        break
    alpha = cv2.getTrackbarPos("Alpha", window_name) / 1000
    beta = 1 - alpha
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
```
- These lines create an infinite loop for displaying the blended image and handling user input. It uses `cv2.imshow()` 
to show the `output` image in the window specified by `window_name`. It waits for a key event, and if the ESC key 
(key code 27) is pressed, the loop is terminated. Inside the loop, it retrieves the current trackbar position (alpha) 
using `cv2.getTrackbarPos()`, calculates the corresponding beta value, and performs image blending with the updated 
alpha and beta values.

```
cv2.destroyAllWindows()
```
- This line closes all open windows created by `cv2.namedWindow()` and releases any associated resources.

'''
