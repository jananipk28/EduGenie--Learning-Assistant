from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import ask_question
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import create_learning_path


app = FastAPI(title="EduGenie")


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/ask")
async def ask(question: str = Form(...)):
    answer = ask_question(question)
    return {"answer": answer}


@app.post("/explain")
async def explain(topic: str = Form(...)):
    answer = explain_topic(topic)
    return {"answer": answer}


@app.post("/summarize")
async def summarize(text: str = Form(...)):
    answer = summarize_text(text)
    return {"answer": answer}


@app.post("/quiz")
async def quiz(topic: str = Form(...)):
    answer = generate_quiz(topic)
    return {"answer": answer}


@app.post("/learning-path")
async def learning_path(topic: str = Form(...)):
    answer = create_learning_path(topic)
    return {"answer": answer}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )