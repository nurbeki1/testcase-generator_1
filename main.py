from fastapi import FastAPI
from openai_client import generate_test_cases
from confluence_client import create_confluence_page

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/generate")
def generate(topic: str):
    md = generate_test_cases(topic)
    html = md.replace("\n", "<br>")

    page_url = create_confluence_page(f"Test Cases — {topic}", html)

    return {
        "status": "ok",
        "topic": topic,
        "confluence_page": page_url
    }
