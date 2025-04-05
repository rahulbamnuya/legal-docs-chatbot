from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import load_and_embed_docs, retrieve_chunks
from huggingface_hub import InferenceClient
from pathlib import Path
import shutil, os
from dotenv import load_dotenv

# Load env and token
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.1", token=HF_TOKEN)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = Path("law_docs")
UPLOAD_DIR.mkdir(exist_ok=True)

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    load_and_embed_docs()
    return templates.TemplateResponse("ask.html", {"request": request})

@app.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, question: str = Form(...)):
    context = "\n\n".join(retrieve_chunks(question))
    prompt = f"Answer the question using this context:\n\n{context}\n\nQuestion: {question}"
    response = client.text_generation(prompt=prompt, max_new_tokens=300, temperature=0.7)
    return templates.TemplateResponse("ask.html", {"request": request, "answer": response, "question": question})
