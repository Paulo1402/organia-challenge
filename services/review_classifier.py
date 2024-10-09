from abc import ABC, abstractmethod

from transformers import pipeline


class ReviewClassifier(ABC):
    """
    Classe abstrata para classificação de avaliações
    """

    @abstractmethod
    def classify(self, review: str) -> int:
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

    def classify(self, review: str) -> int:
        """
        Classifica uma avaliação
        :param review:
        :return:
        """
        result = self.sentiment_analyzer(review)
        label = result[0]["label"]

        if label == "1 star":
            return 1

        if label == "2 stars":
            return 2

        if label == "3 stars":
            return 3

        if label == "4 stars":
            return 4

        if label == "5 stars":
            return 5
