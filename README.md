# 🏥 Medical Document Verification System

A web-based application that verifies whether an uploaded document is a **medical-related document** or not.  
The system supports **images and PDFs (including scanned PDFs)** and uses **OCR and AI-assisted text analysis** to flag invalid or non-medical documents.

---

## 📌 Problem Statement

Patients or users may upload irrelevant files such as screenshots, random images, or non-medical documents.  
This system automatically:
- Extracts text from uploaded documents
- Analyzes the extracted content
- Flags documents as **VALID** or **FLAGGED**

---

## 🚀 Features

- 📂 Upload medical documents (Image / PDF)
- 🖱️ Drag & Drop upload support
- 🖼️ OCR for images and scanned PDFs
- 📄 Extracted text preview
- 🧠 AI-assisted medical document classification
- 🔄 Reset option to re-upload documents
- 🌐 React frontend with Flask backend

---

## 🧠 Workflow

1. User uploads a document through the UI  
2. Backend extracts text using OCR  
3. If PDF has no embedded text, pages are converted to images  
4. OCR is applied to extract text  
5. Text is analyzed to determine whether the document is medical or not  
6. Result is returned as **VALID** or **FLAGGED**

---

## 🛠️ Tech Stack

### Frontend
- React.js
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### OCR & Document Processing
- Tesseract OCR
- pdfplumber
- pdf2image
- Pillow (PIL)
- Poppler (for scanned PDFs)

### AI (Optional / Experimental)
- PyTorch
- Hugging Face Transformers
- DistilBERT (for text classification)

---

## 📁 Project Structure

```
project-root/
│
├── backend/
│ ├── app.py
│ ├── classifier.py
│ ├── uploads/
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── App.js
│ │ ├── App.css
│ │ └── api.js
│ └── package.json
│
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/medical-document-verification.git
cd medical-document-verification
```

### 2️⃣ Backend Setup (Flask)
Create Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate
```
Install Dependencies
```
pip install flask flask-cors pytesseract pdfplumber pdf2image pillow torch transformers
```

### 3️⃣ Install Tesseract OCR

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Add Tesseract installation path to Environment Variables (PATH)

#### Example:

`C:\Program Files\Tesseract-OCR\`

### 4️⃣ Install Poppler (For Scanned PDFs)

• Download Poppler for Windows

• Extract it

• Use the bin path in backend code

#### Example:

`C:\Jigisha\poppler\Library\bin`

### 5️⃣ Run Backend
```
cd backend
python app.py
```

Backend runs at:
```
http://127.0.0.1:5000
```
### 6️⃣ Frontend Setup (React)
```
cd frontend
npm install
npm start
```

Frontend runs at:
```
http://localhost:3000
```
## 📊 Sample Output

<img width="1422" height="772" alt="image" src="https://github.com/user-attachments/assets/8ba4611c-59e5-45cc-bd1a-3583d0b73660" />
<img width="964" height="1233" alt="image" src="https://github.com/user-attachments/assets/ad536002-bc9c-47ce-a44e-1dc37c76c592" />
<img width="949" height="1049" alt="image" src="https://github.com/user-attachments/assets/116a2b4e-eda5-46fc-8109-1a83a2569df3" />


## 🎓 Academic Relevance

This project demonstrates:

• OCR pipelines

• Scanned PDF handling

• Medical document verification

• AI-assisted decision making


## 👩‍💻 Author

Jigisha Mourya
AI / ML & GenAI Enthusiast

## 📄 License

This project is intended for educational and academic purposes only.


