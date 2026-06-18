import fitz  # PyMuPDF

def read_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"[ERROR] Failed to read PDF {file_path}: {str(e)}"