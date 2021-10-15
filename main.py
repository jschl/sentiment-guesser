from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from sentiment_guesser import SentimentGuesser

class Text(BaseModel):
    text: List[str]

app = FastAPI()

sentiment_guesser = SentimentGuesser()

@app.post("/sentiment/")
async def guess_sentiment(item: Text):
    guessed_sentiment = sentiment_guesser(item.text)
    return guessed_sentiment
