# Sentiment Analysis API

A FastAPI server for sentiment analysis using Hugging Face transformers.

## Features

- Sentiment analysis (positive(2)/negative(0)/neutral(1)) for input text
- Uses pre-trained model
- FastAPI with automatic docs with Swagger UI

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/Indira-123/12-factor-app.git
   cd 12-factor-app
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file with model name

   ```bash
   echo "MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english" > .env
   ```

4. Download the model

   ```bash
   python -m scripts.download_model
   ```

5. Run the server

   ```bash
   uvicorn app.main:app --reload
   ```

   The server will start at `http://localhost:8000`
   Swagger UI served at `http://localhost:8000/docs`


