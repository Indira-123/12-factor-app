import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from app.config import MODEL_NAME

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    return tokenizer, model

def analyze_sentiment(text: str):
    tokenizer, model = load_model()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    sentiment = logits.argmax().item()
    return sentiment
