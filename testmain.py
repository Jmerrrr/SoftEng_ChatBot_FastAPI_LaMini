from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from model import qa_llm


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")


# @app.get('/')
# def read_form():
#     return 'hello world'


@app.get("/")
def form_post(request: Request):
    results = "What is Your Query"
    return templates.TemplateResponse('index.html', context={'request': request, 'results': results})


@app.post("/")
def form_post(request: Request, prompt: str = Form(...)):
    results = qa_llm(prompt)
    return templates.TemplateResponse('index.html', context={'request': request, 'results': results})