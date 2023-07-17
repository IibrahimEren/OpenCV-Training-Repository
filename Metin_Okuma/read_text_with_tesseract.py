# Import the necessary modules
from PIL import Image
import pytesseract

# Load the image
img = Image.open('media/metin.jpg')

# Set the language for OCR
lang = "eng"

# Extract the text from the image
text = pytesseract.image_to_string(img, lang=lang)

# Print the text
print(text)

# Explanation of the code:

# The `from PIL import Image` statement imports the `Image` module from the Python Imaging Library (PIL).
# The `import pytesseract` statement imports the `pytesseract` module, which is a Python wrapper for the Tesseract OCR engine.
# The `img = Image.open('media/metin.jpg')` statement loads the image `metin.jpg` into the `img` variable.
# The `lang = "eng"` statement sets the language for OCR to English.
# The `text = pytesseract.image_to_string(img, lang=lang)` statement extracts the text from the image `img` and sets it to the `text` variable.
# The `print(text)` statement prints the text in the `text` variable.