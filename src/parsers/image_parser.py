from PIL import Image
import pytesseract


def read_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text