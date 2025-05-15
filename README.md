# Sentiment Analysis API

A FastAPI server for sentiment analysis using Hugging Face transformers.

## Features

- Sentiment analysis ( positive(2) / negative(0) / neutral(1) ) for input texts
- Uses pre-trained model
- FastAPI with automatic docs with Swagger UI
- Docker container support
- CI integration

### Classification Labels

- 0: Negative
- 1: Neutral
- 2: Positive

## 12-Factor App Compliance

This codebase follows 11 of the 12 factors.

1. **Codebase**  
   Managed with Git, one codebase for one project

2. **Dependencies**  
   Tracked in `requirements.txt`

3. **Config**  
   Stored in `app/config.py`

4. **Backing Services**  
   External resource (model files) in `./model`

5. **Build, Release, Run**  
   Defined in `.github/workflows/ci.yml`

6. **Processes**  
   Stateless app runs via FastAPI in `src/main.py`

7. **Port Binding**  
   Docker maps host port `8000 `to container port `80` with `-p 8000:80` option

8. **Concurrency**  
   Enabled with multiple workers(2) threads via Uvicorn

9. **Disposability**  
   Docker containers are removed after run using `--rm` option

10. **Logs**  
    Handled by FastAPI’s default logging

11. **Admin Processes**  
    One-off tasks handled via `scripts/download_model.py`

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Docker (optional)

### Manual Installation

1. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment

   ```bash
   echo "MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english" > .env
   ```

3. Download model

   ```bash
   python -m scripts.download_model
   ```

4. Run the server locally

   ```bash
   uvicorn app.main:app --reload
   ```

### With Docker

1. Build image

   ```bash
   docker build -t sentiment-api .
   ```

2. Run container

   ```bash
   docker run --rm -it -p 8000:80 sentiment-api
   ```

### Access:

- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

### Testing

Run test with pytest

```bash
pytest
```