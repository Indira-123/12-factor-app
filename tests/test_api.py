from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sentiment_analysis():
    response = client.post("/analyze", json={"text": "I love this!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
