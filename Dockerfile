FROM python:3.9

WORKDIR /code

ENV MODEL_NAME="distilbert-base-uncased-finetuned-sst-2-english"

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

RUN python -m scripts.download_model

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]