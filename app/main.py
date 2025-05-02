from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.llm import ask_llm

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
def ask(prompt_req: PromptRequest):
    try:
        answer = ask_llm(prompt_req.prompt)
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "LLM API is running"}
