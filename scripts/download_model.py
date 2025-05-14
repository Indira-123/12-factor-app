from transformers import AutoTokenizer, AutoModelForSequenceClassification

def download_model():
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    model.save_pretrained("./model")
    tokenizer.save_pretrained("./model")

if __name__ == "__main__":
    download_model()
