from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import shutil
import os

from database import Base, engine, SessionLocal
from models import Pessoa

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pastas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cadastrar")
async def cadastrar(
    request: Request,
    nome: str = Form(...),
    cpf: str = Form(...),
    rg: str = Form(...),
    data_nascimento: str = Form(...),
    arquivo: UploadFile = File(...)
):
    file_path = os.path.join(UPLOAD_DIR, arquivo.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(arquivo.file, buffer)

    db = SessionLocal()
    pessoa = Pessoa(
        nome=nome,
        cpf=cpf,
        rg=rg,
        data_nascimento=data_nascimento,
        arquivo=arquivo.filename
    )
    db.add(pessoa)
    db.commit()
    db.refresh(pessoa)
    db.close()

    return RedirectResponse(url="/lista", status_code=303)

@app.get("/lista", response_class=HTMLResponse)
def listar(request: Request):
    db = SessionLocal()
    pessoas = db.query(Pessoa).all()
    return templates.TemplateResponse("listagem.html", {"request": request, "pessoas": pessoas})