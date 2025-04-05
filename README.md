# Law Assistant AI 🤖⚖️

A FastAPI-based Generative AI web app that allows users to upload documents (PDF or TXT) and ask questions. The app uses Retrieval-Augmented Generation (RAG) and LLMs to generate accurate answers.

---

## 🚀 Demo

🎥 [Watch Demo Video](https://your-demo-link.com)

---

## ✨ Features

- Upload `.pdf` or `.txt` legal documents
- Ask natural language questions
- Get context-aware answers using Hugging Face LLM
- Clean UI with Jinja2 Templates
- Supports future PDF parsing extension

---

## 💡 Architecture

- **FastAPI**: Backend and routes
- **Jinja2**: Templating system for UI
- **Hugging Face Inference API**: Mistral 7B
- **Document Embedding**: FAISS for vector search
- **RAG Pipeline**: Fetch relevant chunks + LLM response

---

## 📦 Setup Instructions

```bash
git clone https://github.com/your-username/law-assistant-ai.git
cd law-assistant-ai
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate
pip install -r requirements.txt
