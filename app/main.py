from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment_analyzer import analyze_sentiment

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/")
def sentiment_analysis(request: TextRequest):
    sentiment = analyze_sentiment(request.text)
    return {"sentiment": sentiment}
