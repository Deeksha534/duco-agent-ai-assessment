from PIL import Image
import pytesseract

def read_image(file_path):
    try:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    except Exception as e:
        return f"[ERROR] Failed to read image {file_path}: {str(e)}"