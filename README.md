# SentimentGuesser

Application for predicting sentiment of german input text.

## installation

```
pip install -r requirements.txt
python3 main.py
curl -X POST "http://localhost:8000/sentiment/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"text\": [\"ein super SentimentGuesser\"]}"
```