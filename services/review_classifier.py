from abc import ABC, abstractmethod

from transformers import pipeline


class ReviewClassifier(ABC):
    """
    Classe abstrata para classificação de avaliações
    """

    @abstractmethod
    def classify(self, review: str) -> str:
        """
        Classifica uma avaliação
        :param review:
        :return:
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

    def classify(self, review: str) -> str:
        """
        Classifica uma avaliação
        :param review:
        :return:
        """
        result = self.sentiment_analyzer(review)
        label = result[0]["label"]

        if label == "1 star":
            return "negative"

        if label == "2 stars":
            return "negative"

        if label == "3 stars":
            return "neutral"

        if label == "4 stars":
            return "positive"

        if label == "5 stars":
            return "positive"
