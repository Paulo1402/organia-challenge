from abc import ABC, abstractmethod
from enum import Enum

from transformers import pipeline


class SentimentClassification(Enum):
    """
    Enum para classificação de sentimentos
    """

    POSITIVE = "Positivo"
    NEUTRAL = "Neutro"
    NEGATIVE = "Negativo"


class ReviewClassifier(ABC):
    """
    Classe abstrata para classificação de avaliações
    """

    @abstractmethod
    def classify(self, review: str) -> SentimentClassification:
        """
        Classifica uma avaliação
        :param review: Avaliação
        :return: Classificação
        """
        pass


class BertReviewClassifier(ReviewClassifier):
    """
    Classificador de avaliações usando BERT
    """

    def __init__(self):
        self.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment",
            device=0,
        )

    def classify(self, review: str) -> SentimentClassification:
        """
        Classifica uma avaliação
        :param review: Avaliação
        :return: Classificação
        """
        result = self.sentiment_analyzer(review)
        label = result[0]["label"]

        if label == "1 star":
            return SentimentClassification.NEGATIVE

        if label == "2 stars":
            return SentimentClassification.NEGATIVE

        if label == "3 stars":
            return SentimentClassification.NEUTRAL

        if label == "4 stars":
            return SentimentClassification.POSITIVE

        if label == "5 stars":
            return SentimentClassification.POSITIVE
