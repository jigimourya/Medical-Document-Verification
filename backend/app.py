from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
from PIL import Image
from classifier import is_medical_document

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text(path):
    text = ""

    if path.endswith(".pdf"):
        # 1. Try text-based extraction
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        # 2. OCR fallback for scanned PDFs
        if len(text.strip()) < 30:
            images = convert_from_path(
                path,
                poppler_path=r"D:\Jigisha\poppler\poppler-25.12.0\Library\bin"
            )
            for img in images:
                text += pytesseract.image_to_string(img)

    else:
        image = Image.open(path)
        text = pytesseract.image_to_string(image)

    return text


@app.route("/verify-document", methods=["POST"])
def verify_document():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    text = extract_text(file_path)
    print("========== OCR / EXTRACTED TEXT ==========")
    print(text)
    print("========== END OF TEXT ===================")
    valid = is_medical_document(text)

    return jsonify({
        "filename": file.filename,
        "status": "VALID" if valid else "FLAGGED",
        "message": "Medical document verified" if valid else "Non-medical or irrelevant document",
        "extracted_text": text[:3000]
    })

if __name__ == "__main__":
    app.run(debug=True)
    
