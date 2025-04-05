from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pathlib import Path
import fitz  # PyMuPDF for PDFs
import docx

model = SentenceTransformer('all-MiniLM-L6-v2')
texts = []
index = None

def extract_text(file_path):
    ext = file_path.suffix.lower()
    if ext == '.pdf':
        doc = fitz.open(file_path)
        return "\n".join([page.get_text() for page in doc])
    elif ext == '.docx':
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif ext == '.txt':
        return file_path.read_text(encoding="utf-8")
    else:
        return ""

def load_and_embed_docs(folder="law_docs"):
    global texts, index
    texts = []
    all_chunks = []

    for file in Path(folder).glob("*.*"):
        content = extract_text(file)
        chunks = [content[i:i+500] for i in range(0, len(content), 500)]
        texts.extend(chunks)
        all_chunks.extend(chunks)

    embeddings = model.encode(all_chunks)
    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))

def retrieve_chunks(query, k=3):
    q_embed = model.encode([query])
    D, I = index.search(np.array(q_embed), k)
    return [texts[i] for i in I[0]]
