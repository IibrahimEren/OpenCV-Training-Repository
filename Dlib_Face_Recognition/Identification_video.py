import cv2
import face_recognition

# Load the image of Jensen for training.
path = 'media/jensen.png'
jensenImage = cv2.imread(path)
jensenImage_encoding = face_recognition.face_encodings(jensenImage)[0]
