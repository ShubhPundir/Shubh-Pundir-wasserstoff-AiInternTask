from pathlib import Path
import fitz  # PyMuPDF
import docx
from docx.oxml.ns import qn
import pytesseract
from PIL import Image, ImageOps
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(file_path: str) -> list[tuple[int, str]]:
    """Extract text from PDF as a list of (page_num, text)."""
    doc = fitz.open(file_path)
    full_doc = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        full_doc.append((page_num, text))
    doc.close()
    return full_doc


def extract_text_from_docx(file_path: str) -> list[tuple[int, str]]:
    """Extract text from DOCX file, simulating pages based on manual page breaks."""
    doc = docx.Document(file_path)
    pages = []
    current_page = []
    page_num = 1

    for para in doc.paragraphs:
        current_page.append(para.text)

        # Check if this paragraph ends with a manual page break
        for run in para.runs:
            if any(
                child.tag == qn("w:br") and child.get(qn("w:type")) == "page"
                for child in run._element
            ):
                # Append current page and reset
                page_text = "\n".join(current_page).strip()
                if page_text:
                    pages.append((page_num, page_text))
                    page_num += 1
                    current_page = []

    # Add any remaining text as the last page
    remaining_text = "\n".join(current_page).strip()
    if remaining_text:
        pages.append((page_num, remaining_text))

    return pages


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


def extract_text_from_image(file_path: str) -> list[tuple[int, str]]:
    """Return single page image text as list with one (page_num, text)."""
    image = Image.open(file_path)
    processed_image = preprocess_image(image)
    text = pytesseract.image_to_string(processed_image)
    return [(1, text)]



def parse_document(file_path: str) -> list[tuple[int, str]]:
    """Return document as list of (page_num, text)."""
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
