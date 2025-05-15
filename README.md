# Sentiment Analysis API

A FastAPI server for sentiment analysis using Hugging Face transformers.

## Features

- Sentiment analysis ( positive(2) / negative(0) / neutral(1) ) for input texts
- Uses pre-trained model
- FastAPI with automatic docs with Swagger UI


### 12 factors

 This codebase follows 11 of the 12 factors.

- Codebase

 Managed with Git, one codebase for one project

- Dependencies

Tracked in ```requirements.txt```

- Config 

Stored in ```app/config.py```

- Backing Services

 External resource (model files) in ```./model```

- Build, Release, Run

 Defined in ```.github/workflows/ci.yml```

- Processes

 App runs via FastAPI in ```src/main.py```

- Port Binding

 Docker maps host port `8000 `to container port `80`

- Concurrency

 Enabled with multiple workers(2) threads via Uvicorn

- Disposability

Docker containers are removed after run using `--rm`

- Logs

Handled by FastAPI’s default logging

- Admin Processes 

One-off tasks handled via `scripts/download_model.py`



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

5. Run the server locally

   ```bash
   uvicorn app.main:app --reload
   ```

   The server will start at `http://localhost:8000`

   Swagger UI served at `http://localhost:8000/docs`


### With Docker

1. Build image
    ```bash
   docker build .
   ```

2. Run container

    ```bash
   docker run --rm -it -p 8000:80 <imageid>
   ```

   The server will start at `http://localhost:8000`

   Swagger UI served at `http://localhost:8000/docs`

### Testing

1.  Run test with pytest

    ```bash
    pytest
    ```