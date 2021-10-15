from typing import List

from germansentiment import SentimentModel

class SentimentGuesser:
    def __init__(self) -> None:
        self.model = SentimentModel()
    
    def __call__(self, input_text: List[str]) -> List:
        result = self.model.predict_sentiment(input_text)
        return result
