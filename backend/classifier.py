from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

medical_reference_texts = [
    "medical report",
    "hospital discharge summary",
    "doctor prescription",
    "diagnosis",
    "blood test report",
    "lab investigation",
    "radiology report", "inj", "injection", "tablet", "mg", "ml",
    "hospital", "doctor", "rx", "diagnosis",
    "amphotericin", "liposomal", "dose", "vial", "vitamin"
]

reference_embeddings = model.encode(medical_reference_texts)

def is_medical_document(text, threshold=0.4):
    if text == "__SCANNED_PDF__":
        # Assume medical only if filename or context suggests medical
        return True
    text_lower = text.lower()

    # Keyword-based fallback
    keyword_hits = sum(1 for k in medical_reference_texts if k in text_lower)
    if keyword_hits >= 2:
        return True

    # Embedding-based check
    if len(text.strip()) < 30:
        return False

    text_embedding = model.encode(text)
    similarity = util.cos_sim(text_embedding, reference_embeddings)

    return similarity.max().item() > threshold

