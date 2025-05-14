from transformers import AutoTokenizer, AutoModelForSequenceClassification
from app.config import MODEL_NAME

def download_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

    model.save_pretrained("./model")
    tokenizer.save_pretrained("./model")

if __name__ == "__main__":
    download_model()
