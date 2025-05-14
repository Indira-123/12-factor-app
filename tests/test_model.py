from app.sentiment_analyzer import analyze_sentiment

def test_analyze_sentiment():
    result = analyze_sentiment("I love this!")
    assert result in [0, 1, 2]  # 0 = negative, 1 = neutral, 2 = positive
