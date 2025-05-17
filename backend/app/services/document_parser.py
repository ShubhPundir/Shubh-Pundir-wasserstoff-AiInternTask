from pathlib import Path
import fitz  # PyMuPDF
import docx
import pytesseract
from PIL import Image, ImageFilter, ImageOps
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(file_path)
    full_text = []
    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text.append(f"--- Page {page_num + 1} ---\n{text}")
    doc.close()
    return "\n".join(full_text)


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX file using python-docx."""
    doc = docx.Document(file_path)
    full_text = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(full_text)


def preprocess_image(image: Image.Image) -> Image.Image:
    """Preprocess image before OCR."""
    # Convert to grayscale
    image = image.convert("L")

    # Increase contrast (optional)
    image = ImageOps.autocontrast(image)

    # Apply thresholding (binarization)
    threshold = 128
    image = image.point(lambda x: 255 if x > threshold else 0)

    # Resize image to make text more legible (optional)
    base_width = 1000
    w_percent = base_width / float(image.size[0])
    h_size = int((float(image.size[1]) * float(w_percent)))
    image = image.resize((base_width, h_size))

    return image


def extract_text_from_image(file_path: str) -> str:
    """Extract text from image files using Tesseract OCR."""
    image = Image.open(file_path)
    processed_image = preprocess_image(image)
    text = pytesseract.image_to_string(processed_image)
    return text


def parse_document(file_path: str) -> str:
    """Main function to detect type and parse document or image."""
    path = Path(file_path)
    ext = path.suffix.lower()

    if ext == ".pdf":
        return extract_text_from_pdf(str(path))
    elif ext == ".docx":
        return extract_text_from_docx(str(path))
    elif ext in {".png", ".jpg", ".jpeg"}:
        return extract_text_from_image(str(path))
    else:
        raise ValueError(f"Unsupported file format: {ext}")
