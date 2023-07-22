# Import the face_recognition and PIL libraries
import face_recognition
from PIL import Image, ImageDraw

# Define the path to the image file
path = 'media/face.jpg'

# Load the image file
image = face_recognition.load_image_file(path)

# Find the facial landmarks in the image
landmarks = face_recognition.face_landmarks(image)

# Create a PIL.Image object from the image
PIL_Image = Image.fromarray(image)

# Create a PIL.ImageDraw object
d = ImageDraw.Draw(PIL_Image)

# Iterate over the facial landmarks
for landmark in landmarks:

    # Iterate over the features in each landmark
    for feature in landmark.keys():

        # Draw a line between the points of each feature
        d.line(landmark[feature], width=3)

# Show the image
PIL_Image.show()

